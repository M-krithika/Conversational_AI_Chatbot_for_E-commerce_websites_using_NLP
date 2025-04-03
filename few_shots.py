few_shots = [
    {
        "Question": "I want to place an order for an iPhone 15 with quantity 1 (User email: sreeja123@gmail.com)",
        "SQLQuery": "INSERT INTO orders (user_id, total_amount, order_date, status, estimated_delivery, updated_at, payment) VALUES ((SELECT user_id FROM users WHERE email='sreeja123@gmail.com'), (SELECT price * 1 FROM products WHERE name='iPhone 15'), NOW(), 'Pending', DATE_ADD(CURDATE(), INTERVAL 10 DAY), NOW(), 'COD'); SELECT LAST_INSERT_ID(); INSERT INTO order_items (order_id, product_id, quantity, unit_price, total_price) VALUES (LAST_INSERT_ID(), (SELECT product_id FROM products WHERE name='iPhone 15'), 1, (SELECT price FROM products WHERE name='iPhone 15'), (SELECT price * 1 FROM products WHERE name='iPhone 15'))",
        "SQLResult": "[(4,)]",
        "Answer": "Perfect! I've created order #4 for you. You've ordered 1 iPhone 15, and the total amount is $999.99. The estimated delivery date is in 10 days, and your order status is currently 'Pending'. Your payment method is COD. You'll receive an email confirmation soon."
    },
    {
        'Question': "What is the status of my order (User email: srikar123@gmail.com)",
        'SQLQuery': "select status from orders o, users u where u.user_id=o.user_id and u.email='srikar123@gmail.com'",
        'SQLResult': "Delivered",
        'Answer': "Your order with ID 1023 is currently 'Delivered'."},

    {
        'Question': "Can I return my order with order ID 1050?",
        'SQLQuery': "SELECT return_status FROM returns WHERE order_id = 1050",
        'SQLResult': "Result of the SQL query",
        'Answer': "Your return request for order 1050 is 'Pending'. You will receive an update shortly."},

    {
        'Question': "How many items are left in stock for the product 'Wireless Earbuds'?",
        'SQLQuery': "SELECT stock_quantity FROM products WHERE name = 'Wireless Earbuds'",
        'SQLResult': "Result of the SQL query",
        'Answer': "We currently have 45 units of 'Wireless Earbuds' in stock."},

    {
        'Question': "What is the estimated delivery date for my order 1105?",
        'SQLQuery': "SELECT estimated_delivery FROM orders WHERE order_id = 1105",
        'SQLResult': "Result of the SQL query",
        'Answer': "Your order 1105 is expected to be delivered on 2025-03-01."},

    {
        'Question': "Can you provide details of my last order?",
        'SQLQuery': "SELECT order_id, total_amount, status, order_date FROM orders WHERE user_id = (SELECT user_id FROM users WHERE email = 'customer@example.com') ORDER BY order_date DESC LIMIT 1",
        'SQLResult': "Result of the SQL query",
        'Answer': "Your last order (ID 1120) was placed on 2025-02-15. The total amount was $199.99, and the status is 'Delivered'."},
    {
        'Question': "How much will I be refunded for my returned order 1075?",
        'SQLQuery': "SELECT total_price FROM order_items WHERE order_id = 1075",
        'SQLResult': "Result of the SQL query",
        'Answer': "Your refund amount for order 1075 will be $75.50 after processing."},

    {
        'Question': "What is the return policy for my order?",
        'SQLQuery': "SELECT return_status FROM returns WHERE order_id = 1085",
        'SQLResult': "Result of the SQL query",
        'Answer': "Your order 1085 is eligible for return. Please initiate the process within 7 days of delivery."},

    {
        'Question': "How many products have I ordered so far?",
        'SQLQuery': "SELECT COUNT(order_id) FROM orders WHERE user_id = (SELECT user_id FROM users WHERE email = 'customer@example.com')",
        'SQLResult': "Result of the SQL query",
        'Answer': "You have placed a total of 5 orders with us."},

    {
        'Question': "Can I change my delivery address for order 1110?",
        'SQLQuery': "SELECT status FROM orders WHERE order_id = 1110",
        'SQLResult': "Result of the SQL query",
        'Answer': "Your order 1110 is 'Shipped'. Unfortunately, the delivery address cannot be changed at this stage."},
    {
        'Question': "How do I cancel my order 1095? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `status`, `order_date`, `total_amount` FROM orders WHERE `order_id` = 1095 AND `user_id` = (SELECT `user_id` FROM users WHERE `email` = 'sreeja123@gmail.com')",
        'SQLResult': "[('Pending', '2025-03-20', 99999.00)]",
        'Answer': "Let me check your order 1095:\n- Order 1095: Placed on 2025-03-20, with a total amount of 99999.00 INR. The current status is 'Pending'.\nSince it’s still in 'Pending' status, you can cancel it. Please visit the 'My Orders' section on our website to proceed with the cancellation. If you need further assistance, feel free to reach out!"
    },
    {
        'Question': "What is the status of my order with order ID 12345? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `status`, `order_date`, `estimated_delivery` FROM orders WHERE `order_id` = 12345 AND `user_id` = (SELECT `user_id` FROM users WHERE `email` = 'john.doe@gmail.com')",
        'SQLResult': "[('Shipped', '2025-03-15', '2025-03-25')]",
        'Answer': "Here’s the status of your order 12345:\n- Order 12345: Placed on 2025-03-15, with an estimated delivery date of 2025-03-25. The current status is 'Shipped'.\nYour order is on its way and should arrive soon! You can track it in the 'My Orders' section. Let me know if you need further assistance!"
    },
    {
        'Question': "Can you tell me the estimated delivery date for my order 67890? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `status`, `order_date`, `estimated_delivery` FROM orders WHERE `order_id` = 67890 AND `user_id` = (SELECT `user_id` FROM users WHERE `email` = 'sreeja123@gmail.com')",
        'SQLResult': "[('Processing', '2025-03-18', '2025-03-28')]",
        'Answer': "Here are the details for your order 67890:\n- Order 67890: Placed on 2025-03-18, with an estimated delivery date of 2025-03-28. The current status is 'Processing'.\nYour order is being prepared and will be shipped soon. You can track its progress in the 'My Orders' section. Let me know if you have any other questions!"
    },
    {
        'Question': "I want to cancel my order with order ID 13579. Is it possible? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `status`, `order_date`, `total_amount` FROM orders WHERE `order_id` = 13579 AND `user_id` = (SELECT `user_id` FROM users WHERE `email` = 'john.doe@gmail.com')",
        'SQLResult': "[('Pending', '2025-03-19', 34999.00)]",
        'Answer': "Let me check your order 13579:\n- Order 13579: Placed on 2025-03-19, with a total amount of 34999.00 INR. The current status is 'Pending'.\nGood news! Since it’s still in 'Pending' status, you can cancel it. Please visit the 'My Orders' section on our website to proceed with the cancellation. If you need help, feel free to contact customer support!"
    },
    {
        'Question': "How much did I pay for my order 24680? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `status`, `order_date`, `total_amount` FROM orders WHERE `order_id` = 24680 AND `user_id` = (SELECT `user_id` FROM users WHERE `email` = 'sreeja123@gmail.com')",
        'SQLResult': "[('Delivered', '2025-03-10', 12050.00)]",
        'Answer': "Here are the details for your order 24680:\n- Order 24680: Placed on 2025-03-10, with a total amount of 12050.00 INR. The current status is 'Delivered'.\nIt looks like your order has already been delivered. If you have any concerns, please contact customer support, and we’ll be happy to assist!"
    },
    {
        'Question': "Do you have the Apple iPhone? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` LIKE '%iPhone%' ORDER BY `created_at` DESC LIMIT 1",
        'SQLResult': "[('iPhone 15', '256GB, Black, 6.1-inch display', 99999.00)]",
        'Answer': "Yes, we have the Apple iPhone in stock! Here’s what we have:\n- iPhone 15: Priced at 99999.00 INR, it comes with 256GB storage, Black color, and a 6.1-inch display.\nWould you like to proceed with this iPhone?"
    },
    {
        'Question': "What is the price of the Samsung Galaxy S23? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` = 'Samsung Galaxy S23'",
        'SQLResult': "[('Samsung Galaxy S23', '256GB, Green, 6.2-inch display', 89999.00)]",
        'Answer': "Here are the details for the Samsung Galaxy S23:\n- Samsung Galaxy S23: Priced at 89999.00 INR, it comes with 256GB storage, Green color, and a 6.2-inch display.\nWould you like to add this flagship phone to your cart?"
    },
    {
        'Question': "Can you show me the specifications of the Dell XPS 15 laptop? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` = 'Dell XPS 15'",
        'SQLResult': "[('Dell XPS 15', 'Intel i7, 16GB RAM, 512GB SSD', 149999.00)]",
        'Answer': "Here are the specifications for the Dell XPS 15 laptop:\n- Dell XPS 15: Priced at 149999.00 INR, it comes with an Intel i7 processor, 16GB RAM, and a 512GB SSD.\nIt’s a powerful choice for professionals. Would you like to know more or proceed with this laptop?"
    },
    {
        'Question': "Are there any discounts available on Sony headphones? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` LIKE '%Sony WH-1000XM5%'",
        'SQLResult': "[('Sony WH-1000XM5', 'Black, Bluetooth 5.0', 34999.00)]",
        'Answer': "I checked for Sony headphones, and here’s what we have:\n- Sony WH-1000XM5: Priced at 34999.00 INR, these noise-canceling wireless headphones come in Black with Bluetooth 5.0 connectivity.\nUnfortunately, there are no discounts available at the moment, but they’re a fantastic choice for premium audio. Would you like to proceed?"
    },
    {
        'Question': "Do you have Gaming laptops? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT p.`name`, p.`specifications`, p.`price`, IFNULL(d.`discount_percentage`, 0) AS discount_percentage, d.`description` FROM products p LEFT JOIN discounts d ON p.`product_id` = d.`product_id` AND d.`start_date` <= '2025-03-27' AND d.`end_date` >= '2025-03-27' WHERE p.`category` = 'Gaming Laptops' ORDER BY p.`created_at` DESC LIMIT 5",
        'SQLResult': "[('HP Omen 16', 'AMD Ryzen 9, RTX 4070, 16GB RAM, 1TB SSD, 16.1-inch 144Hz', 139999.00, 0, NULL), ('Asus ROG Strix G16', 'Intel i9, RTX 4060, 16GB RAM, 1TB SSD, 16-inch 165Hz', 124999.00, 0, NULL), ('Lenovo Legion 5 Pro', 'AMD Ryzen 7, RTX 3070, 16GB RAM, 1TB SSD', 132999.00, 0, NULL)]",
        'Answer': "Yes, we have some fantastic gaming laptops for you:\n- HP Omen 16: Priced at 139999.00 INR, it comes with an AMD Ryzen 9, RTX 4070, 16GB RAM, 1TB SSD, and a 16.1-inch 144Hz display.\n- Asus ROG Strix G16: Priced at 124999.00 INR, it features an Intel i9, RTX 4060, 16GB RAM, 1TB SSD, and a 16-inch 165Hz display.\n- Lenovo Legion 5 Pro: Priced at 132999.00 INR, it includes an AMD Ryzen 7, RTX 3070, 16GB RAM, and a 1TB SSD.\nThere are no active discounts on these gaming laptops at the moment. These laptops are perfect for an immersive gaming experience! Which one catches your eye?"
    },
    {
        'Question': "Can you show me budget smartphones under 25000 INR? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `price`, `specifications` FROM products WHERE `category` = 'Smartphones' AND `price` <= 25000 ORDER BY `price` ASC LIMIT 3",
        'SQLResult': "[('Infinix Note 50X 5G', 19999.00, '128GB, Mystic Black, 6.8-inch IPS LCD, Dimensity 6080'), ('Vivo T4 5G', 27999.00, '128GB, Starry Night, 6.5-inch AMOLED, Dimensity 6020')]",
        'Answer': "Here are some budget smartphones under 25000 INR:\n- Infinix Note 50X 5G: Priced at 19999.00 INR, it comes with 128GB, Mystic Black, 6.8-inch IPS LCD, Dimensity 6080.\n- Vivo T4 5G: Priced at 27999.00 INR, it comes with 128GB, Starry Night, 6.5-inch AMOLED, Dimensity 6020.\nLet me know if you'd like more options!"
    },
    {
        'Question': "What are the best TVs for a cinematic experience? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `name`, `price`, `specifications` FROM products WHERE `category` = 'TVs' AND `specifications` LIKE '%Dolby Vision%' OR `specifications` LIKE '%OLED%' ORDER BY `price` DESC LIMIT 3",
        'SQLResult': "[('Samsung 65-inch QN90C Neo QLED', 249999.00, '65-inch, 4K, 144Hz, HDR10+, Tizen OS'), ('Sony Bravia 55-inch XR A80L', 179999.00, '55-inch, 4K OLED, 120Hz, Dolby Vision, Google TV'), ('Sony Bravia XR A80K 65-inch', 159999.00, '65-inch, XR Processor, Acoustic Surface Audio')]",
        'Answer': "For a cinematic experience, I recommend these top TVs with features like Dolby Vision or OLED:\n- Samsung 65-inch QN90C Neo QLED: Priced at 249999.00 INR, it offers 65-inch, 4K, 144Hz, HDR10+, Tizen OS.\n- Sony Bravia 55-inch XR A80L: Priced at 179999.00 INR, it comes with 55-inch, 4K OLED, 120Hz, Dolby Vision, Google TV.\n- Sony Bravia XR A80K 65-inch: Priced at 159999.00 INR, it features 65-inch, XR Processor, Acoustic Surface Audio.\nThese TVs will give you an amazing viewing experience!"
    },
    {
        'Question': "Can you compare the MacBook Pro 14 and Samsung Galaxy Book5 Pro? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `price`, `specifications` FROM products WHERE `name` IN ('MacBook Pro 14', 'Samsung Galaxy Book5 Pro')",
        'SQLResult': "[('MacBook Pro 14', 164999.00, 'M3 Pro, 16GB RAM, 1TB SSD, Silver'), ('Samsung Galaxy Book5 Pro', 139999.00, 'Intel Core Ultra 7, 16GB RAM, 1TB SSD, 16-inch AMOLED, Windows 11')]",
        'Answer': "Let’s compare the MacBook Pro 14 and Samsung Galaxy Book5 Pro for you:\n- MacBook Pro 14: Priced at 164999.00 INR, it comes with an M3 Pro chip, 16GB RAM, 1TB SSD, and a Silver finish. It’s great for Apple ecosystem users and creative professionals.\n- Samsung Galaxy Book5 Pro: Priced at 139999.00 INR, it features an Intel Core Ultra 7, 16GB RAM, 1TB SSD, and a 16-inch AMOLED display, running Windows 11. It’s ideal for those who prefer Windows and a stunning AMOLED screen.\nBoth are powerful, but the MacBook is better for macOS users, while the Galaxy Book offers a larger AMOLED display at a lower price."
    },
    {
        'Question': "Do you have any wearables for fitness tracking under 15000 INR? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `name`, `price`, `specifications` FROM products WHERE `category` = 'Wearables' AND `price` <= 15000 AND `specifications` LIKE '%Heart Rate%' ORDER BY `price` ASC LIMIT 3",
        'SQLResult': "[('Fitbit Charge 6', 12999.00, 'GPS, 7-day battery life, Water-resistant'), ('Mi Band 8', 3999.00, '1.62-inch AMOLED, SpO2, 14-day battery life, Black')]",
        'Answer': "Yes, we have some great wearables for fitness tracking under 15000 INR:\n- Mi Band 8: Priced at 3999.00 INR, it features a 1.62-inch AMOLED display, SpO2, heart rate monitoring, and a 14-day battery life, in Black.\n- Fitbit Charge 6: Priced at 12999.00 INR, it comes with GPS, heart rate monitoring, a 7-day battery life, and is water-resistant.\nThese are perfect for tracking your fitness goals!"
    },
    {
        'Question': "What are the latest cameras for professional photography? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `price`, `specifications` FROM products WHERE `category` = 'Cameras' AND `specifications` LIKE '%4K%' OR `specifications` LIKE '%8K%' ORDER BY `created_at` DESC LIMIT 3",
        'SQLResult': "[('Fujifilm X100VI', 159999.00, '40MP APS-C, 23mm f/2 lens, Hybrid Viewfinder, Silver'), ('Insta360 X4', 54999.00, '8K video, 72MP photos, FlowState stabilization'), ('Sony Alpha A7 IV', 214999.00, '33MP, 4K video, 5-axis stabilization')]",
        'Answer': "Here are the latest cameras for professional photography with 4K or 8K capabilities:\n- Fujifilm X100VI: Priced at 159999.00 INR, it features a 40MP APS-C sensor, 23mm f/2 lens, Hybrid Viewfinder, in Silver.\n- Insta360 X4: Priced at 54999.00 INR, it offers 8K video, 72MP photos, and FlowState stabilization, great for 360-degree shots.\n- Sony Alpha A7 IV: Priced at 214999.00 INR, it comes with a 33MP sensor, 4K video, and 5-axis stabilization.\nThese cameras are excellent for professional photography!"
    },
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
    {
        'Question': "How can I contact customer support? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `answer` FROM policies WHERE `category` = 'Customer Support'",
        'SQLResult': "['You can contact our customer support via email at support@store.com or call us at +91-800-123-4567.']",
        'Answer': "Here’s how you can reach our customer support:\n- You can contact our customer support via email at support@store.com or call us at +91-800-123-4567.\nWe’re here to assist you with any queries or issues. How can I help you today?"
    },
    {
        'Question': "What payment methods do you accept? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `answer` FROM policies WHERE `category` = 'payment'",
        'SQLResult': "['We accept credit/debit cards, UPIs, Cash On Delivery, and bank transfers.']",
        'Answer': "Here are the payment methods we accept:\n- We accept credit/debit cards, UPIs, Cash On Delivery, and bank transfers.\nYou can choose the most convenient option during checkout. Let me know if you have any questions about payments!"
    },
    {
        'Question': "Do you offer same-day delivery? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `answer` FROM policies WHERE `category` = 'delivery'",
        'SQLResult': "['Yes, we offer same-day delivery for selected products and for select locations if the order is placed before 12 PM. Please check product availability during checkout.']",
        'Answer': "Here’s our policy on same-day delivery:\n- Yes, we offer same-day delivery for selected products and for select locations if the order is placed before 12 PM. Please check product availability during checkout.\nWould you like to explore products eligible for same-day delivery?"
    },
    # Modified product-related queries
    {
        'Question': "What is the price of the iPhone 15? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` = 'iPhone 15'",
        'SQLResult': "[('iPhone 15', '256GB, Black, 6.1-inch display', 99999.00)]",
        'Answer': "Here are the details for the iPhone 15:\n- iPhone 15: Priced at 99999.00 INR, it comes with 256GB storage, Black color, and a 6.1-inch display.\nWould you like to add this iPhone to your cart?"
    },
    {
        'Question': "Do you have Dell XPS 15 in stock? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` = 'Dell XPS 15'",
        'SQLResult': "[('Dell XPS 15', 'Intel i7, 16GB RAM, 512GB SSD', 149999.00)]",
        'Answer': "Yes, we have the Dell XPS 15 in stock! Here are the details:\n- Dell XPS 15: Priced at 149999.00 INR, it comes with an Intel i7 processor, 16GB RAM, and a 512GB SSD.\nWe have 20 units available. Would you like to proceed with this laptop?"
    },
    {
        'Question': "Which smartphones are available under ₹60,000? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `category` = 'Smartphones' AND `price` <= 60000 ORDER BY `price` ASC LIMIT 5",
        'SQLResult': "[('Infinix Note 50X 5G', '128GB, Mystic Black, 6.8-inch IPS LCD, Dimensity 6080', 19999.00), ('Vivo T4 5G', '128GB, Starry Night, 6.5-inch AMOLED, Dimensity 6020', 27999.00), ('Realme GT 3', '256GB, Pulse White, Snapdragon 8+ Gen 1', 46999.00), ('Meizu 22', '256GB, Ocean Blue, 6.55-inch AMOLED, Snapdragon 7 Gen 2', 45999.00), ('Motorola Edge 60 Fusion', '256GB, Lunar Grey, 6.67-inch OLED, Snapdragon 7+ Gen 3', 54999.00)]",
        'Answer': "Here are the smartphones available under ₹60,000:\n- Infinix Note 50X 5G: Priced at 19999.00 INR, it comes with 128GB, Mystic Black, 6.8-inch IPS LCD, Dimensity 6080.\n- Vivo T4 5G: Priced at 27999.00 INR, it comes with 128GB, Starry Night, 6.5-inch AMOLED, Dimensity 6020.\n- Realme GT 3: Priced at 46999.00 INR, it comes with 256GB, Pulse White, Snapdragon 8+ Gen 1.\n- Meizu 22: Priced at 45999.00 INR, it comes with 256GB, Ocean Blue, 6.55-inch AMOLED, Snapdragon 7 Gen 2.\n- Motorola Edge 60 Fusion: Priced at 54999.00 INR, it comes with 256GB, Lunar Grey, 6.67-inch OLED, Snapdragon 7+ Gen 3.\nWhich one would you like to explore further?"
    },
    {
        'Question': "What are the specifications of Sony WH-1000XM5? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` = 'Sony WH-1000XM5'",
        'SQLResult': "[('Sony WH-1000XM5', 'Black, Bluetooth 5.0', 34999.00)]",
        'Answer': "Here are the specifications for the Sony WH-1000XM5:\n- Sony WH-1000XM5: Priced at 34999.00 INR, these headphones come in Black with Bluetooth 5.0 connectivity.\nThey’re a great choice for premium audio. Would you like to add them to your cart?"
    },
    {
        'Question': "List all available laptops. (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `category` = 'Laptops' ORDER BY `price` ASC",
        'SQLResult': "[('Acer Aspire 5', 'Intel i5, 8GB RAM, 512GB SSD, 15.6-inch FHD display', 54999.00), ('Lenovo IdeaPad Slim 3', 'Intel i5, 16GB RAM, 512GB SSD, 15.6-inch FHD, Arctic Grey', 64999.00), ('Acer TravelLite 2025', 'Intel Core i5 13th Gen, 16GB RAM, 512GB SSD, 15.6-inch FHD, Windows 11', 79999.00), ('ASUS Zenbook A14 (2025)', 'Snapdragon X Elite, 16GB RAM, 512GB SSD, 14-inch OLED, Windows 11', 99999.00), ('HP Spectre x360', 'Intel i7, 16GB RAM, 512GB SSD, 13.5-inch OLED', 114999.00), ('HP EliteBook Ultra G1i', 'Intel Core Ultra 5, 16GB RAM, 512GB SSD, 14-inch FHD, Windows 11 Pro', 119999.00), ('Dell XPS 15', 'Intel i7, 16GB RAM, 512GB SSD', 149999.00), ('Lenovo ThinkBook Plus Gen 6', 'Intel Core Ultra 7, 32GB RAM, 1TB SSD, 14-inch Rollable OLED, Windows 11', 159999.00), ('MacBook Pro 14', 'M3 Pro, 16GB RAM, 1TB SSD, Silver', 164999.00), ('Samsung Galaxy Book5 Pro', 'Intel Core Ultra 7, 16GB RAM, 1TB SSD, 16-inch AMOLED, Windows 11', 139999.00)]",
        'Answer': "Here are all the laptops currently available:\n- Acer Aspire 5: Priced at 54999.00 INR, it comes with an Intel i5, 8GB RAM, 512GB SSD, 15.6-inch FHD display.\n- Lenovo IdeaPad Slim 3: Priced at 64999.00 INR, it comes with an Intel i5, 16GB RAM, 512GB SSD, 15.6-inch FHD, Arctic Grey.\n- Acer TravelLite 2025: Priced at 79999.00 INR, it comes with an Intel Core i5 13th Gen, 16GB RAM, 512GB SSD, 15.6-inch FHD, Windows 11.\n- ASUS Zenbook A14 (2025): Priced at 99999.00 INR, it comes with a Snapdragon X Elite, 16GB RAM, 512GB SSD, 14-inch OLED, Windows 11.\n- HP Spectre x360: Priced at 114999.00 INR, it comes with an Intel i7, 16GB RAM, 512GB SSD, 13.5-inch OLED.\n- HP EliteBook Ultra G1i: Priced at 119999.00 INR, it comes with an Intel Core Ultra 5, 16GB RAM, 512GB SSD, 14-inch FHD, Windows 11 Pro.\n- Dell XPS 15: Priced at 149999.00 INR, it comes with an Intel i7, 16GB RAM, 512GB SSD.\n- Lenovo ThinkBook Plus Gen 6: Priced at 159999.00 INR, it comes with an Intel Core Ultra 7, 32GB RAM, 1TB SSD, 14-inch Rollable OLED, Windows 11.\n- MacBook Pro 14: Priced at 164999.00 INR, it comes with an M3 Pro, 16GB RAM, 1TB SSD, Silver.\n- Samsung Galaxy Book5 Pro: Priced at 139999.00 INR, it comes with an Intel Core Ultra 7, 16GB RAM, 1TB SSD, 16-inch AMOLED, Windows 11.\nWhich laptop would you like to explore further?"
    },
    {
        'Question': "Which earpods are available under ₹5,000? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `category` = 'Accessories' AND `name` LIKE '%Earbuds%' AND `price` <= 5000 ORDER BY `price` ASC",
        'SQLResult': "[('Boat Airdopes 141', 'Bluetooth 5.1, 42-hour playtime, IPX5, Black', 1499.00)]",
        'Answer': "Here are the earbuds available under ₹5,000:\n- Boat Airdopes 141: Priced at 1499.00 INR, they come with Bluetooth 5.1, 42-hour playtime, IPX5 rating, in Black.\nThese are a great budget option for wireless audio! Would you like to add them to your cart?"
    },
    {
        'Question': "What are the top-selling accessories? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `category` = 'Accessories' ORDER BY `stock_quantity` DESC LIMIT 3",
        'SQLResult': "[('Boat Airdopes 141', 'Bluetooth 5.1, 42-hour playtime, IPX5, Black', 1499.00), ('Anker PowerCore 10000', '10000mAh, USB-C, 20W PD, Black', 2999.00), ('Bose QuietComfort Earbuds II', 'Black, Bluetooth 5.3, 24-hour battery life', 19999.00)]",
        'Answer': "Here are our top-selling accessories based on stock movement:\n- Boat Airdopes 141: Priced at 1499.00 INR, they come with Bluetooth 5.1, 42-hour playtime, IPX5 rating, in Black.\n- Anker PowerCore 10000: Priced at 2999.00 INR, it’s a compact portable charger with 10000mAh, USB-C, 20W PD, in Black.\n- Bose QuietComfort Earbuds II: Priced at 19999.00 INR, they come in Black with Bluetooth 5.3 and a 24-hour battery life.\nThese accessories are popular among our customers! Which one would you like to explore?"
    },
    {
        'Question': "Do you have MacBook Air in stock? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` LIKE '%MacBook Air%'",
        'SQLResult': "[]",
        'Answer': "I’m sorry, we currently don’t have any MacBook Air models in stock. However, we do have the MacBook Pro 14, which might interest you:\n- MacBook Pro 14: Priced at 164999.00 INR, it comes with an M3 Pro chip, 16GB RAM, 1TB SSD, in Silver.\nWould you like to explore this option or check for other laptops?"
    },
    {
        'Question': "What is the cheapest smartphone available? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `category` = 'Smartphones' ORDER BY `price` ASC LIMIT 1",
        'SQLResult': "[('Infinix Note 50X 5G', '128GB, Mystic Black, 6.8-inch IPS LCD, Dimensity 6080', 19999.00)]",
        'Answer': "Here’s the cheapest smartphone we have available:\n- Infinix Note 50X 5G: Priced at 19999.00 INR, it comes with 128GB, Mystic Black, 6.8-inch IPS LCD, Dimensity 6080.\nIt’s a great budget option with 5G support! Would you like to add it to your cart?"
    },
    {
        'Question': "Are there any discounts on laptops? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT p.`name`, d.`discount_percentage`, d.`description` FROM products p JOIN discounts d ON p.`product_id` = d.`product_id` WHERE p.`category` = 'Laptops' AND d.`start_date` <= '2025-03-27' AND d.`end_date` >= '2025-03-27'",
        'SQLResult': "[('Dell XPS 15', 15.00, 'March Madness Discount on Dell XPS 15')]",
        'Answer': "Yes, there are discounts on laptops! Here’s what’s available:\n- Dell XPS 15: 15% off as part of the March Madness Discount, valid until March 31, 2025.\nWould you like to explore this laptop or check other options?"
    },
    {
        'Question': "What are the specifications of the iPhone 15? (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` = 'iPhone 15'",
        'SQLResult': "[('iPhone 15', '256GB, Black, 6.1-inch display', 99999.00)]",
        'Answer': "Here are the specifications for the iPhone 15:\n- iPhone 15: Priced at 99999.00 INR, it comes with 256GB storage, Black color, and a 6.1-inch display.\nIt’s a fantastic choice for an Apple smartphone! Would you like to proceed with this iPhone?"
    },
    {
        'Question': "Is the Samsung Galaxy S23 available in stock? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` = 'Samsung Galaxy S23'",
        'SQLResult': "[('Samsung Galaxy S23', '256GB, Green, 6.2-inch display', 89999.00)]",
        'Answer': "Yes, the Samsung Galaxy S23 is available in stock! Here are the details:\n- Samsung Galaxy S23: Priced at 89999.00 INR, it comes with 256GB storage, Green color, and a 6.2-inch display.\nWe have 30 units available. Would you like to add this smartphone to your cart?"
    },
    {
        'Question': "Are there any discounts on laptops? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT p.`name`, d.`discount_percentage`, d.`description` FROM products p JOIN discounts d ON p.`product_id` = d.`product_id` WHERE p.`category` = 'Laptops' AND d.`start_date` <= '2025-03-27' AND d.`end_date` >= '2025-03-27'",
        'SQLResult': "[('Dell XPS 15', 15.00, 'March Madness Discount on Dell XPS 15')]",
        'Answer': "Yes, there are discounts on laptops! Here’s what’s available:\n- Dell XPS 15: 15% off as part of the March Madness Discount, valid until March 31, 2025.\nWould you like to explore this laptop or check other options?"
    },
    {
        'Question': "What are the features of Sony WH-1000XM5 headphones? (User email: john.doe@gmail.com)",
        'SQLQuery': "SELECT `name`, `specifications`, `price` FROM products WHERE `name` = 'Sony WH-1000XM5'",
        'SQLResult': "[('Sony WH-1000XM5', 'Black, Bluetooth 5.0', 34999.00)]",
        'Answer': "Here are the features of the Sony WH-1000XM5 headphones:\n- Sony WH-1000XM5: Priced at 34999.00 INR, they come in Black with Bluetooth 5.0 connectivity.\nThey’re a premium choice for wireless audio! Would you like to add them to your cart?"
    },
    {
        'Question': "Show me mobiles under 20000 (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT p.`name`, p.`specifications`, p.`price`, IFNULL(d.`discount_percentage`, 0) AS discount_percentage, d.`description` FROM products p LEFT JOIN discounts d ON p.`product_id` = d.`product_id` AND d.`start_date` <= '2025-04-02' AND d.`end_date` >= '2025-04-02' WHERE p.`category` = 'Smartphones' AND p.`price` <= 20000 ORDER BY p.`price` ASC LIMIT 5",
        'SQLResult': "[('Infinix Note 50X 5G', '128GB, Mystic Black, 6.8-inch IPS LCD, Dimensity 6080', 19999.00, 0, NULL)]",
        'Answer': "Here are the mobiles available under ₹20,000:\n- Infinix Note 50X 5G: Priced at 19999.00 INR, it comes with 128GB storage, Mystic Black color, a 6.8-inch IPS LCD display, and a Dimensity 6080 processor.\n\nIf you’re open to a slightly higher budget, the Vivo T4 5G is available at 27999.00 INR with 128GB storage, Starry Night color, a 6.5-inch AMOLED display, and a Dimensity 6020 processor.\nWhich one would you like to explore further?"
    },
    {
        'Question': "Show me laptops under 60000 (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT p.`name`, p.`specifications`, p.`price`, IFNULL(d.`discount_percentage`, 0) AS discount_percentage, d.`description` FROM products p LEFT JOIN discounts d ON p.`product_id` = d.`product_id` AND d.`start_date` <= '2025-04-02' AND d.`end_date` >= '2025-04-02' WHERE p.`category` = 'Laptops' AND p.`price` <= 60000 ORDER BY p.`price` ASC LIMIT 5",
        'SQLResult': "[('Acer Aspire 5', 'Intel i5, 8GB RAM, 512GB SSD, 15.6-inch FHD display', 54999.00, 0, NULL)]",
        'Answer': "Here are the laptops available under ₹60,000:\n- Acer Aspire 5: Priced at 54999.00 INR, it comes with an Intel i5 processor, 8GB RAM, a 512GB SSD, and a 15.6-inch FHD display.\n\nIf you’re open to a slightly higher budget, the Lenovo IdeaPad Slim 3 is available at 64999.00 INR with an Intel i5 processor, 16GB RAM, a 512GB SSD, and a 15.6-inch FHD display in Arctic Grey.\nWhich one would you like to explore further?"
    },
    {
        'Question': "Show me mid-range mobiles (User email: sreeja123@gmail.com)",
        'SQLQuery': "SELECT p.`name`, p.`specifications`, p.`price`, IFNULL(d.`discount_percentage`, 0) AS discount_percentage, d.`description` FROM products p LEFT JOIN discounts d ON p.`product_id` = d.`product_id` AND d.`start_date` <= '2025-04-02' AND d.`end_date` >= '2025-04-02' WHERE p.`category` = 'Smartphones' AND p.`price` BETWEEN 15000 AND 25000 ORDER BY p.`price` ASC LIMIT 5",
        'SQLResult': "[('Vivo T4 5G', '128GB, Starry Night, 6.5-inch AMOLED, Dimensity 6020', 27999.00, 0, NULL), ('Realme Narzo 80 Pro', '128GB, Blaze Orange, 6.6-inch AMOLED, Dimensity 7050', 29999.00, 0, NULL), ('Poco X7 Pro', '128GB, Yellow, 6.67-inch AMOLED, Snapdragon 7+ Gen 2', 32999.00, 0, NULL), ('Redmi Note 14 Pro+', '256GB, Moonlight White, 6.67-inch AMOLED, Dimensity 7300', 34999.00, 0, NULL), ('iQOO Neo 9 Pro', '256GB, Cosmic Blue, 6.78-inch AMOLED, Snapdragon 8 Gen 2', 39999.00, 0, NULL)]",
        'Answer': "Here are some mid-range mobiles (₹15,000 to ₹25,000):\n- Vivo T4 5G: Priced at 27999.00 INR, it comes with 128GB storage, Starry Night color, a 6.5-inch AMOLED display, and a Dimensity 6020 processor.\n- Realme Narzo 80 Pro: Priced at 29999.00 INR, it comes with 128GB storage, Blaze Orange color, a 6.6-inch AMOLED display, and a Dimensity 7050 processor.\n- Poco X7 Pro: Priced at 32999.00 INR, it comes with 128GB storage, Yellow color, a 6.67-inch AMOLED display, and a Snapdragon 7+ Gen 2 processor.\n- Redmi Note 14 Pro+: Priced at 34999.00 INR, it comes with 256GB storage, Moonlight White color, a 6.67-inch AMOLED display, and a Dimensity 7300 processor.\n- iQOO Neo 9 Pro: Priced at 39999.00 INR, it comes with 256GB storage, Cosmic Blue color, a 6.78-inch AMOLED display, and a Snapdragon 8 Gen 2 processor.\nWhich one would you like to explore further?"
    },
    {
        "Question": "I want to place an order for an iPhone 15 (User email: david@example.com)",
        "SQLQuery": "SELECT p.product_id, p.name, p.price, p.stock_quantity, u.user_id, u.name, u.address FROM products p, users u WHERE p.name = 'iPhone 15' AND p.stock_quantity > 0 AND u.email = 'david@example.com';",
        "SQLResult": "1, iPhone 15, 999.99, 50, 8, David Lee, 789 Oak St, Chicago, IL",
        "Answer": "I see you're interested in the iPhone 15, which is available in stock for $999.99. I can use your stored shipping address:\n\n789 Oak St, Chicago, IL\n\nPlease confirm product, product quantity to place order."
    },
    {
        'Question': "Yes, proceed with the order for iphone 15 and quantity is 1 (User email: david@example.com)",
        'SQLQuery': "INSERT INTO orders (user_id, total_amount, order_date, status, estimated_delivery, updated_at) VALUES ((select user_id from users where email='david@example.com'), (select price from products where name='iphone 15'), NOW(), 'Pending', DATE_ADD(CURDATE(), INTERVAL 10 DAY), NOW()); SELECT LAST_INSERT_ID();",
        'SQLResult': "4",
        'Answer': "Perfect! I've created order #4 for you. The total amount is $999.99, and the estimated delivery date is in 10 days. Your order status is currently 'Pending'. I'll add the iPhone 15 to your order now and available payment option is COD. Please confirm payment option"},
    {
        'Question': " Yes confirm my order with payment option is COD.",
        'SQLQuery': "insert into order_items(order_id, product_id, quantity, unit_price, total_price)values((select LAST_INSERT_ID()),(select product_id from products where name='iphone 15'),1,(select price from products where name='iphone 15'),(select price from products where name='iphone 15')*1); SELECT LAST_INSERT_ID();",
        'SQLResult':'1 row affected',
        'Answer': "Your order has been confirmed with the payment option as COD. The iPhone 15 has been added to your order #4, and the total amount remains $999.99. Your order status is now 'Processing'. You'll receive an email confirmation soon."
    },
    {
        'Question': "I want to order a Galaxy S24 Ultra (User email: sarah@example.com)",
        'SQLQuery': "SELECT p.product_id, p.name, p.price, p.stock_quantity, u.user_id, u.name, u.address FROM products p, users u WHERE p.name = 'Galaxy S24 Ultra' AND p.stock_quantity > 0 AND u.email = 'sarah@example.com';",
        'SQLResult': "3, Galaxy S24 Ultra, 1199.99, 30, 5, Sarah Johnson, 456 Pine Ave, New York, NY",
        'Answer': "I see you're interested in the Galaxy S24 Ultra, which is available in stock for $1,199.99. Since you're already logged in, I can use your stored shipping address:\n\n456 Pine Ave, New York, NY\n\nWould you like to proceed with placing this order?"
    },

    {
        'Question': "I'd like to add Sony WH-1000XM5 headphones to my order (User email: david@example.com)",
        'SQLQuery': "SELECT o.order_id FROM orders o JOIN users u ON o.user_id = u.user_id WHERE u.email = 'david@example.com' AND o.status = 'Pending' ORDER BY o.order_date DESC LIMIT 1; SELECT product_id, name, price, stock_quantity FROM products WHERE name = 'Sony WH-1000XM5' AND stock_quantity > 0;",
        'SQLResult': "4; 4, Sony WH-1000XM5, 349.99, 100",
        'Answer': "The Sony WH-1000XM5 headphones are available for $349.99. I can add them to your pending order #4. Would you like me to proceed?"
    },

    {
        'Question': "Yes, add them to my order (User email: david@example.com)",
        'SQLQuery': "INSERT INTO order_items (order_id, product_id, quantity, unit_price, total_price) VALUES (4, 4, 1, 349.99, 349.99); UPDATE orders SET total_amount = total_amount + 349.99 WHERE order_id = 4; UPDATE products SET stock_quantity = stock_quantity - 1 WHERE product_id = 4;",
        'SQLResult': "1 row affected",
        'Answer': "I've added the Sony WH-1000XM5 headphones to your order #4. Your new order total is $1,349.98. Is there anything else you'd like to add?"},

        {'Question': "Are there any discounts available for my order? (User email: david@example.com)",
         'SQLQuery': "SELECT o.order_id FROM orders o JOIN users u ON o.user_id = u.user_id WHERE u.email = 'david@example.com' AND o.status = 'Pending' ORDER BY o.order_date DESC LIMIT 1; SELECT oi.product_id, p.name FROM order_items oi JOIN products p ON oi.product_id = p.product_id WHERE oi.order_id = 4; SELECT d.discount_id, d.product_id, p.name, d.discount_percentage FROM discounts d JOIN products p ON d.product_id = p.product_id WHERE CURDATE() BETWEEN d.start_date AND d.end_date AND d.product_id IN (1, 4);",
         'SQLResult': "4; 1, iPhone 15; 4, Sony WH-1000XM5; 1, 1, iPhone 15, 10.00",
         'Answer': "Good news! There's currently a 10% discount available for the iPhone 15 as part of our Spring Sale. This will reduce your iPhone price from $999.99 to $899.99, saving you $100. Would you like me to apply this discount to your order?"},

        {'Question': "Please complete my order (User email: david@example.com)",
         'SQLQuery': "UPDATE orders SET status = 'Processing', updated_at = NOW() WHERE order_id = (SELECT order_id FROM (SELECT o.order_id FROM orders o JOIN users u ON o.user_id = u.user_id WHERE u.email = 'david@example.com' AND o.status = 'Pending' ORDER BY o.order_date DESC LIMIT 1) as temp)",
         'SQLResult': "1 row affected",
         'Answer': "Thank you for your order! Your order has been placed successfully and is now being processed. The total amount is $1,349.98. Your estimated delivery date is in 10 days. You'll receive a confirmation email shortly with your order details. Is there anything else I can help you with today?"},

        {'Question': "What's the status of my last order? (User email: david@example.com)",
         'SQLQuery': "SELECT o.order_id, o.status, o.estimated_delivery, o.total_amount, o.order_date FROM orders o JOIN users u ON o.user_id = u.user_id WHERE u.email = 'david@example.com' ORDER BY o.order_date DESC LIMIT 1",
         'SQLResult': "4, Processing, 2025-03-27, 1349.98, 2025-03-17",
         'Answer': "Your most recent order (#4) is currently in 'Processing' status. It was placed today and has an estimated delivery date of March 27, 2025. The total amount for this order is $1,349.98. Is there anything specific you'd like to know about this order?"
        }
]
