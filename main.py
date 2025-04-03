import streamlit as st
import mysql.connector
from langchain_helper import get_few_shot_db_chain
import os
from dotenv import load_dotenv

load_dotenv()

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "srikar"),
        database=os.environ.get("DB_NAME", "project")
    )

# User authentication functions
def check_user_exists(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def create_user(name, email, phone, address):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (name, email, phone, address, created_at) VALUES (%s, %s, %s, %s, NOW())",
            (name, email, phone, address)
        )
        conn.commit()
        user_id = cursor.lastrowid
        return user_id
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

# Page configuration
st.set_page_config(page_title="E-Commerce Support", page_icon="🛒", layout="wide")
st.markdown("""
<style>
    .main-header {background-color: #2E7D32; padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;}
    .sub-header {border-bottom: 2px solid #2E7D32; padding-bottom: 10px; margin-bottom: 20px;}
    .response-area {background-color: #000000; padding: 20px; border-radius: 10px; border: 1px solid #ddd; box-shadow: 0 2px 5px rgba(0,0,0,0.1); font-size: 16px; line-height: 1.6;}
    .response-area ul {list-style-type: none; padding-left: 0;}
    .response-area li {margin-bottom: 10px;}
    .response-area strong {color: #2E7D32;}
    .stButton>button {background-color: #2E7D32; color: white; border-radius: 5px; padding: 10px 20px;}
    .login-form {background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-bottom: 20px;}
    .user-question {font-size: 16px; font-style: italic; color: #555; margin-bottom: 10px;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user' not in st.session_state:
    st.session_state['user'] = None
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'show_signup' not in st.session_state:
    st.session_state['show_signup'] = False

# Title
st.markdown("<h1 class='main-header'>E-Commerce Electronics Store Support 🛒</h1>", unsafe_allow_html=True)

# Login/Signup logic
if not st.session_state['logged_in']:
    if not st.session_state['show_signup']:
        # Login form
        st.markdown("<h2 class='sub-header'>Login</h2>", unsafe_allow_html=True)
        with st.form(key='login_form', clear_on_submit=True):
            email = st.text_input("Email Address")
            submit_button = st.form_submit_button(label='Login')

            if submit_button:
                if not email:
                    st.error("Please enter your email address")
                else:
                    user = check_user_exists(email)
                    if user:
                        st.session_state['logged_in'] = True
                        st.session_state['user'] = user
                        st.success(f"Welcome back, {user['name']}!")
                        st.rerun()
                    else:
                        st.error("Email not found. Please sign up.")
                        st.session_state['show_signup'] = True
                        st.rerun()

        if st.button("Don't have an account? Sign up"):
            st.session_state['show_signup'] = True
            st.rerun()
    else:
        # Signup form
        st.markdown("<h2 class='sub-header'>Create Account</h2>", unsafe_allow_html=True)
        with st.form(key='signup_form', clear_on_submit=True):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
            address = st.text_area("Shipping Address")
            submit_button = st.form_submit_button(label='Create Account')

            if submit_button:
                if not all([name, email, phone]):
                    st.error("Please fill all required fields")
                else:
                    existing_user = check_user_exists(email)
                    if existing_user:
                        st.error("Email already exists. Please login.")
                        st.session_state['show_signup'] = False
                        st.rerun()
                    else:
                        try:
                            user_id = create_user(name, email, phone, address)
                            st.session_state['logged_in'] = True
                            st.session_state['user'] = {
                                'user_id': user_id,
                                'name': name,
                                'email': email,
                                'phone': phone,
                                'address': address
                            }
                            st.success(f"Account created successfully! Welcome, {name}!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error creating account: {str(e)}")

        if st.button("Already have an account? Login"):
            st.session_state['show_signup'] = False
            st.rerun()
else:
    # User is logged in - show chatbot interface
    user = st.session_state['user']

    # Show user info in sidebar
    with st.sidebar:
        st.markdown(f"### Welcome, {user['name']}!")
        st.markdown(f"**Email:** {user['email']}")
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state['user'] = None
            st.rerun()


    @st.cache_resource
    def get_cached_chain():
        return get_few_shot_db_chain()

    chain = get_cached_chain()
    # Main chat interface
    st.markdown("<h2 class='sub-header'>Ask Us Anything</h2>", unsafe_allow_html=True)
    question = st.text_input("Ask a question:")

    if st.button("Submit") and question:
        # Display user question
        st.markdown(f"**Your question:** {question}")

        # Add spinner during processing
        with st.spinner("Processing your request..."):
            try:
                # chain = get_few_shot_db_chain()
                # Call the custom_chain function directly instead of .invoke()
                # sql_query = chain.invoke(question).replace("sql ", "").strip()
                # print("Generated SQL Query:", sql_query)
                # response = sql_query
                response = chain.invoke(question + f" (User email: {user['email']})")
                if isinstance(response, dict) and 'Answer' in response:#
                    answer = response['Answer']
                else:
                    # Fallback: If the response is a dictionary with 'result' (current behavior)
                    if isinstance(response, dict) and 'result' in response:
                        answer = response['result']
                    else:
                        answer = str(response)  # Fallback for unexpected response types#
                # Add to history
                st.session_state['history'].append({"question": question, "answer": answer})
                # Display response
                st.markdown("<h3 class='sub-header'>Response</h3>", unsafe_allow_html=True)
                formatted_answer = answer.replace("\n", "<br>").replace("- **", "<li><strong>").replace("**: ",
                                                                                                        "</strong>: ")
                st.markdown(f"<div class='response-area'>{formatted_answer}</div>", unsafe_allow_html=True)
                # st.markdown(f"<div class='response-area'>{response}</div>", unsafe_allow_html=True)##
            except Exception as e:
                st.error(f"Sorry, I encountered an error: {str(e)}")
                st.info("Please try rephrasing your question or contact customer support.")

    # Display conversation history
    if st.session_state['history']:
        st.markdown("<h3 class='sub-header'>Previous Conversations</h3>", unsafe_allow_html=True)
        for i, exchange in enumerate(reversed(st.session_state['history'])):
            with st.expander(f"Question: {exchange['question']}"):
                st.write(exchange['answer'])

