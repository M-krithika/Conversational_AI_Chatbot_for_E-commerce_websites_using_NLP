from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain.prompts.prompt import PromptTemplate


from few_shots import few_shots

import os
from dotenv import load_dotenv

load_dotenv()



def get_few_shot_db_chain():
    db_user = "root"
    db_password = "Database@123"
    db_host = "localhost"
    db_name = "project"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                              sample_rows_in_table_info=3)
    # llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)
    llm = GoogleGenerativeAI(model="gemini-2.5-pro-exp-03-25", google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.2)

    # embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-large-en')
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    # vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)
    # persist_directory = "chroma_db"  # Directory to store the vector store
    persist_directory = "chroma_db"  # Directory to store the vector store
    try:
        # Initialize Chroma with persistence and explicit tenant configuration
        vectorstore = Chroma(
            collection_name="few_shots",
            embedding_function=embeddings,
            persist_directory=persist_directory
        )
        # Add the texts to the vector store (this will create the collection if it doesn't exist)
        vectorstore.add_texts(texts=to_vectorize, metadatas=few_shots)
        vectorstore.persist()
    except Exception as e:
        raise e
    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )

    mysql_prompt = """You are an e-commerce electronics store expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".
     
     Note:
    - Always format the response in a customer-friendly manner
    - Use natural language that sounds like a helpful customer service representative
    - Refer to the the Few Shots example
    - Generate syntactically Correct SQL Query
    - CRITICAL: ONLY generate the pure SQL query text
    - DO NOT INCLUDE THE WORD 'sql' BEFORE OR WITHIN THE SQL QUERY
    - DONT GIVE RAW SQL QUERY AS RESPONSE TO USER. GENERATE RESPONSE IN NATURAL LANGUAGE
    
    RESPONSE GENERATION CRITICAL INSTRUCTIONS:
    1. AFTER obtaining the SQL query result, ALWAYS TRANSFORM THE RAW DATA INTO A WARM, HELPFULL CUSTOMER SERVICE RESPONSE
    2. If no order is found:
        - Provide a sympathetic message
        - Suggest contacting customer support
        - Offer alternative assistance
    3. If order is found:
        - Clearly state the current order status
        - Include relevant details like estimated delivery date
        - Use a friendly, reassuring tone
    4. NEVER RETURN THE SQL QUERY TO THE USER
    5. Speak as a helpful customer service representative would

     For order status queries:
    - If an order is not found, inform the customer politely and suggest contacting customer support
    - Show the estimated delivery date if the order is in transit
    - If the order is delivered, show the delivery date
    - If there are any issues, provide relevant details
    Use the following format:

    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here

    No pre-amble.
    """

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer", ],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],
    )
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
    return chain
