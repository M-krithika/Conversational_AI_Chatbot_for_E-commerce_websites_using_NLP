few_shots = [
    {'Question': "What is the status of my order with order ID 1023?",
     'SQLQuery': "SELECT status FROM orders WHERE order_id = 1023",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your order with ID 1023 is currently 'Shipped'. It is expected to be delivered soon."},

    {'Question': "Can I return my order with order ID 1050?",
     'SQLQuery': "SELECT return_status FROM returns WHERE order_id = 1050",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your return request for order 1050 is 'Pending'. You will receive an update shortly."},

    {'Question': "How many items are left in stock for the product 'Wireless Earbuds'?",
     'SQLQuery': "SELECT stock_quantity FROM products WHERE name = 'Wireless Earbuds'",
     'SQLResult': "Result of the SQL query",
     'Answer': "We currently have 45 units of 'Wireless Earbuds' in stock."},

    {'Question': "What is the estimated delivery date for my order 1105?",
     'SQLQuery': "SELECT estimated_delivery FROM orders WHERE order_id = 1105",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your order 1105 is expected to be delivered on 2025-03-01."},

    {'Question': "Can you provide details of my last order?",
     'SQLQuery': "SELECT order_id, total_amount, status, order_date FROM orders WHERE user_id = (SELECT user_id FROM users WHERE email = 'customer@example.com') ORDER BY order_date DESC LIMIT 1",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your last order (ID 1120) was placed on 2025-02-15. The total amount was $199.99, and the status is 'Delivered'."},

    {'Question': "How much will I be refunded for my returned order 1075?",
     'SQLQuery': "SELECT total_price FROM order_items WHERE order_id = 1075",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your refund amount for order 1075 will be $75.50 after processing."},

    {'Question': "What is the return policy for my order?",
     'SQLQuery': "SELECT return_status FROM returns WHERE order_id = 1085",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your order 1085 is eligible for return. Please initiate the process within 7 days of delivery."},

    {'Question': "How many products have I ordered so far?",
     'SQLQuery': "SELECT COUNT(order_id) FROM orders WHERE user_id = (SELECT user_id FROM users WHERE email = 'customer@example.com')",
     'SQLResult': "Result of the SQL query",
     'Answer': "You have placed a total of 5 orders with us."},

    {'Question': "Can I change my delivery address for order 1110?",
     'SQLQuery': "SELECT status FROM orders WHERE order_id = 1110",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your order 1110 is 'Shipped'. Unfortunately, the delivery address cannot be changed at this stage."},

    {'Question': "How do I cancel my order 1095?",
     'SQLQuery': "SELECT status FROM orders WHERE order_id = 1095",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your order 1095 is 'Pending'. You can cancel it by visiting the 'My Orders' section on our website."},
    {'Question': "What is the status of my order with order ID 12345?",
     'SQLQuery': "SELECT status FROM orders WHERE order_id = 12345",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your order with ID 12345 is currently 'Shipped' and will be delivered soon."},

    {'Question': "Can you tell me the estimated delivery date for my order 67890?",
     'SQLQuery': "SELECT estimated_delivery FROM orders WHERE order_id = 67890",
     'SQLResult': "Result of the SQL query",
     'Answer': "The estimated delivery date for your order 67890 is 2024-02-28."},

    {'Question': "I want to cancel my order with order ID 13579. Is it possible?",
     'SQLQuery': "SELECT status FROM orders WHERE order_id = 13579",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your order 13579 is still in 'Pending' status, so you can cancel it. Please visit your order page to proceed with cancellation."},

    {'Question': "How much did I pay for my order 24680?",
     'SQLQuery': "SELECT total_amount FROM orders WHERE order_id = 24680",
     'SQLResult': "Result of the SQL query",
     'Answer': "The total amount you paid for order 24680 is $120.50."},

    # Product-related queries
    {'Question': "Do you have the latest Apple iPhone in stock?",
     'SQLQuery': "SELECT stock_quantity FROM products WHERE name LIKE '%iPhone%' ORDER BY created_at DESC LIMIT 1",
     'SQLResult': "Result of the SQL query",
     'Answer': "Yes, we have the latest Apple iPhone in stock with 50 units available."},

    {'Question': "What is the price of the Samsung Galaxy S23?",
     'SQLQuery': "SELECT price FROM products WHERE name = 'Samsung Galaxy S23'",
     'SQLResult': "Result of the SQL query",
     'Answer': "The price of the Samsung Galaxy S23 is $899.99."},

    {'Question': "Can you show me the specifications of the Dell XPS 15 laptop?",
     'SQLQuery': "SELECT specifications FROM products WHERE name = 'Dell XPS 15'",
     'SQLResult': "Result of the SQL query",
     'Answer': "The Dell XPS 15 laptop has a 15.6-inch 4K display, Intel i9 processor, 32GB RAM, and 1TB SSD storage."},

    {'Question': "Are there any discounts available on Sony headphones?",
     'SQLQuery': "SELECT price, (price * (1 - (COALESCE(discounts.pct_discount,0)/100))) AS discounted_price FROM products LEFT JOIN discounts ON products.product_id = discounts.product_id WHERE name LIKE '%Sony Headphones%'",
     'SQLResult': "Result of the SQL query",
     'Answer': "Yes, the Sony headphones are available at a discounted price of $150.00 after a 10% discount."},

    # Return-related queries
    {'Question': "I want to return my order 98765. What is the status of my return request?",
     'SQLQuery': "SELECT return_status FROM returns WHERE order_id = 98765",
     'SQLResult': "Result of the SQL query",
     'Answer': "Your return request for order 98765 is currently 'Pending'. We will update you soon."},

    {'Question': "How do I initiate a return for my damaged product?",
     'SQLQuery': "N/A",
     'SQLResult': "N/A",
     'Answer': "You can initiate a return by visiting the 'My Orders' section and selecting 'Request Return' for the damaged product. Please ensure you upload a photo of the damaged item."},

    {'Question': "What is the return policy for electronics?",
     'SQLQuery': "SELECT answer FROM policies WHERE category = 'Returns'",
     'SQLResult': "Result of the SQL query",
     'Answer': "You can return any item within 30 days of purchase if it is unused and in original condition, provided the item is in its original condition with all accessories."},

    # General queries
    {'Question': "How can I contact customer support?",
     'SQLQuery': "SELECT answer FROM policies where category = 'Customer Support'",
     'SQLResult': "Result of the SQL query",
     'Answer': "You can contact our customer support via email at support@store.com or call us at +1-800-123-4567."},

    {'Question': "What payment methods do you accept?",
     'SQLQuery': "SELECT answer FROM policies WHERE category='payment'",
     'SQLResult': "Result of the SQL query",
     'Answer': "We accept credit/debit cards, UPIs, Cash On Delivery and bank transfers."},

    {'Question': "Do you offer same-day delivery?",
     'SQLQuery': "SELECT answer FROM policies WHERE category='delivery",
     'SQLResult': "Result of the SQL query",
     'Answer': "Yes, we offer same-day delivery for selected products and for select locations if the order is placed before 12 PM. Please check product availability during checkout."},
    {
        "Question": "What is the price of the iPhone 15?",
        "SQLQuery": "SELECT price FROM products WHERE name = 'iPhone 15';",
        "SQLResult": "79999",
        "Answer": "The price of the iPhone 15 is ₹79,999."
    },
    {
        "Question": "Do you have Dell XPS 15 in stock?",
        "SQLQuery": "SELECT stock_quantity FROM products WHERE name = 'Dell XPS 15';",
        "SQLResult": "20",
        "Answer": "Yes, we have 20 units of Dell XPS 15 in stock."
    },
    {
        "Question": "Which smartphones are available under ₹60,000?",
        "SQLQuery": "SELECT name, price FROM products WHERE category = 'Smartphones' AND price <= 60000;",
        "SQLResult": "[('Samsung Galaxy S23', 59999)]",
        "Answer": "Currently, the Samsung Galaxy S23 is available for ₹59,999."
    },
    {
        "Question": "What are the specifications of Sony WH-1000XM5?",
        "SQLQuery": "SELECT specifications FROM products WHERE name = 'Sony WH-1000XM5';",
        "SQLResult": "Black, Bluetooth 5.0",
        "Answer": "The Sony WH-1000XM5 has the following specifications: Black color, Bluetooth 5.0."
    },
    {
        "Question": "List all available laptops.",
        "SQLQuery": "SELECT name, price FROM products WHERE category = 'Laptops';",
        "SQLResult": "[('Dell XPS 15', 129999), ('MacBook Air M2', 119999)]",
        "Answer": "The available laptops are Dell XPS 15 (₹1,29,999) and MacBook Air M2 (₹1,19,999)."
    },
    {
        "Question": "Which earpods are available under ₹5,000?",
        "SQLQuery": "SELECT name, price FROM products WHERE category = 'Earpods' AND price <= 5000;",
        "SQLResult": "[('Realme Buds Air 3', 3999), ('Boat Airdopes 141', 2499)]",
        "Answer": "The available earpods under ₹5,000 are Realme Buds Air 3 (₹3,999) and Boat Airdopes 141 (₹2,499)."
    },
    {
        "Question": "What are the top-selling accessories?",
        "SQLQuery": "SELECT name, price FROM products WHERE category = 'Accessories' ORDER BY stock_quantity DESC LIMIT 3;",
        "SQLResult": "[('Sony WH-1000XM5', 34999), ('JBL Flip 6', 8999), ('Samsung 25W Charger', 1999)]",
        "Answer": "The top-selling accessories are Sony WH-1000XM5 (₹34,999), JBL Flip 6 (₹8,999), and Samsung 25W Charger (₹1,999)."
    },
    {
        "Question": "Do you have MacBook Air in stock?",
        "SQLQuery": "SELECT stock_quantity FROM products WHERE name LIKE 'MacBook Air%';",
        "SQLResult": "15",
        "Answer": "Yes, we have 15 units of MacBook Air in stock."
    },
    {
        "Question": "What is the cheapest smartphone available?",
        "SQLQuery": "SELECT name, price FROM products WHERE category = 'Smartphones' ORDER BY price ASC LIMIT 1;",
        "SQLResult": "[('Redmi Note 12', 13999)]",
        "Answer": "The cheapest smartphone available is Redmi Note 12 for ₹13,999."
    },
    {
        "Question": "Are there any discounts on laptops?",
        "SQLQuery": "SELECT name, price, discount FROM products WHERE category = 'Laptops' AND discount > 0;",
        "SQLResult": "[('HP Pavilion 15', 74999, 10), ('Asus ROG Strix', 99999, 5)]",
        "Answer": "Yes, discounts are available: HP Pavilion 15 has a 10% discount (₹74,999) and Asus ROG Strix has a 5% discount (₹99,999)."
    },
    {
        "Question": "What are the specifications of the iPhone 15?",
        "SQLQuery": "SELECT specifications FROM products WHERE name = 'iPhone 15';",
        "SQLResult": "[256GB, Black, 6.1-inch display]",
        "Answer": "The iPhone 15 comes with 256GB storage, Black color, and a 6.1-inch display."
    },
    {
        "Question": "Is the Samsung Galaxy S23 available in stock?",
        "SQLQuery": "SELECT stock_quantity FROM products WHERE name = 'Samsung Galaxy S23';",
        "SQLResult": "30",
        "Answer": "Yes, the Samsung Galaxy S23 is available in stock with 30 units remaining."
    },
    {
        "Question": "Do you offer discounts on laptops?",
        "SQLQuery": "SELECT discount FROM policies WHERE category = 'Laptops';",
        "SQLResult": "10% off on all laptops",
        "Answer": "Yes, we offer a 10% discount on all laptops."
    },
    {
        "Question": "What are the features of Sony WH-1000XM5 headphones?",
        "SQLQuery": "SELECT specifications FROM products WHERE name = 'Sony WH-1000XM5';",
        "SQLResult": "Black, Bluetooth 5.0, Noise-canceling",
        "Answer": "The Sony WH-1000XM5 headphones come in Black, support Bluetooth 5.0, and have noise-canceling features."
    },
]
