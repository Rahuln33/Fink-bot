
# import json
# import openai

# # Load FinKraft data from JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)

# # Initialize OpenAI client
# client = openai.AzureOpenAI(
#     azure_endpoint="https://finkdataopenai.openai.azure.com/",
#     api_key='d57b4f240c6f4c12bb8d316469e45f69',
#     api_version="2024-02-15-preview"
# )

# def extract_information(query):
#     """
#     Extract relevant information from finkraft_data based on the user's query.
#     """
#     # Normalize the query
#     query = query.lower()
    
#     # Define a dictionary to hold matching information
#     extracted_info = {}
    
#     for key, value in finkraft_data.items():
#         if key.lower() in query:
#             extracted_info[key] = value
    
#     if extracted_info:
#         # Format the extracted information in a user-friendly manner
#         response = ""
#         for key, value in extracted_info.items():
#             response += f"{key}:\n{value}\n\n"
#         return response.strip()
#     else:
#         return None

# def query(user_input):
#     # Extract relevant information from finkraft_data
#     info = extract_information(user_input)
    
#     if info:
#         return info
#     else:
#         # Call OpenAI API using appropriate method if info not found in JSON
#         completion = client.chat.completions.create(
#             model="gpt-35-turbo",
#             messages=[
#                 {"role": "system", "content": "You are Fink, a chatbot for FinKraft AI. Provide detailed and user-friendly information to the users."},
#                 {"role": "user", "content": user_input}
#             ],
#             temperature=0.7,
#             max_tokens=150,
#             top_p=1.0,
#             frequency_penalty=0,
#             presence_penalty=0,
#             stop=None
#         )
#         bot_response = completion.choices[0].message.content
#         return bot_response

# def main():
#     print("Welcome! Chat with Fink (Press Ctrl+C to exit)")
#     try:
#         while True:
#             user_input = input("You: ")
#             bot_response = query(user_input)
#             print("Fink:", bot_response)
#     except KeyboardInterrupt:
#         print("\nChat ended.")

# if __name__ == "__main__":
#     main()



# import json
# import openai
# from fuzzywuzzy import fuzz

# # Load Finkraft data from JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)

# # Initialize OpenAI client
# client = openai.AzureOpenAI(
#     azure_endpoint="https://finkdataopenai.openai.azure.com/",
#     api_key='d57b4f240c6f4c12bb8d316469e45f69',
#     api_version="2024-02-15-preview"
# )

# def extract_information(data, query, threshold=80):
#     """
#     Recursively extract relevant information from nested data based on the user's query
#     with fuzzy matching.
#     """
#     # Normalize the query
#     query = query.lower()
    
#     # Define a list to hold matching values
#     extracted_values = []
    
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if fuzz.partial_ratio(query, key.lower()) >= threshold:
#                 if isinstance(value, (dict, list)):
#                     nested_values = extract_information(value, query, threshold)
#                     extracted_values.extend(nested_values)
#                 else:
#                     extracted_values.append(str(value))
#             elif isinstance(value, (dict, list)):
#                 nested_values = extract_information(value, query, threshold)
#                 extracted_values.extend(nested_values)
#     elif isinstance(data, list):
#         for item in data:
#             nested_values = extract_information(item, query, threshold)
#             extracted_values.extend(nested_values)
    
#     return extracted_values

# def query(user_input):
#     # Extract relevant information from finkraft_data
#     info = extract_information(finkraft_data, user_input)
    
#     if info:
#         # Format the extracted information
#         response = "\n".join(info)
#         return response
#     else:
#         # Call OpenAI API using appropriate method if info not found in JSON
#         completion = client.chat.completions.create(
#             model="gpt-35-turbo",
#             messages=[
#                 {"role": "system", "content": "I'm a fink. Finkraft for all the details understand then. I only show user-related information about finkraft."},
#                 {"role": "user", "content": user_input}
#             ],
#             temperature=0.7,
#             max_tokens=150,
#             top_p=1.0,
#             frequency_penalty=0,
#             presence_penalty=0,
#             stop=None
#         )
#         bot_response = completion.choices[0].message.content
#         return bot_response

# def main():
#     print("Welcome! Chat with the bot (Press Ctrl+C to exit)")
#     try:
#         while True:
#             user_input = input("You: ")
#             bot_response = query(user_input)
#             print("Bot:", bot_response)
#     except KeyboardInterrupt:
#         print("\nChat ended.")

# if __name__ == "__main__":
#     main()

##################

# import json
# import openai
# from fuzzywuzzy import fuzz

# # Load Finkraft data from JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)

# # Initialize OpenAI client
# client = openai.AzureOpenAI(
#     azure_endpoint="https://finkdataopenai.openai.azure.com/",
#     api_key='d57b4f240c6f4c12bb8d316469e45f69',
#     api_version="2024-02-15-preview"
# )

# def extract_information(data, query, threshold=80):
#     """
#     Recursively extract relevant information from nested data based on the user's query
#     with fuzzy matching.
#     """
#     # Normalize the query
#     query = query.lower()
    
#     # Define a list to hold matching values
#     extracted_values = []
    
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if fuzz.partial_ratio(query, key.lower()) >= threshold:
#                 if isinstance(value, (dict, list)):
#                     nested_values = extract_information(value, query, threshold)
#                     extracted_values.extend(nested_values)
#                 else:
#                     extracted_values.append(str(value))
#             elif isinstance(value, (dict, list)):
#                 nested_values = extract_information(value, query, threshold)
#                 extracted_values.extend(nested_values)
#     elif isinstance(data, list):
#         for item in data:
#             nested_values = extract_information(item, query, threshold)
#             extracted_values.extend(nested_values)
    
#     return extracted_values

# def is_related_to_finkraft(query):
#     """
#     Check if the query is related to FinKraft AI using fuzzy matching.
#     Adjust the threshold as needed for accuracy.
#     """
#     keywords = ["finkraft", "fink", "fink ai", "finkraft ai"]
#     query = query.lower()
    
#     for keyword in keywords:
#         if fuzz.partial_ratio(query, keyword) >= 90:  # Adjust threshold as needed
#             return True
#     return False

# def query(user_input):
#     # Check if the query is related to FinKraft AI
#     if not is_related_to_finkraft(user_input):
#         return "I'm a chatbot providing information about FinKraft AI. Please ask about FinKraft AI."

#     # Extract relevant information from finkraft_data
#     info = extract_information(finkraft_data, user_input)
    
#     if info:
#         # Format the extracted information
#         response = "\n".join(info)
#         return response
#     else:
#         # Call OpenAI API using appropriate method if info not found in JSON
#         completion = client.chat.completions.create(
#             model="gpt-35-turbo",
#             messages=[
#                 {"role": "system", "content": "I'm a chatbot providing information about FinKraft AI. Here is the FinKraft AI data."},
#                 {"role": "user", "content": user_input}
#             ],
#             temperature=0.7,
#             max_tokens=150,
#             top_p=1.0,
#             frequency_penalty=0,
#             presence_penalty=0,
#             stop=None
#         )
#         bot_response = completion.choices[0].message.content
#         return bot_response

# def main():
#     print("Welcome! Chat with the bot (Press Ctrl+C to exit)")
#     try:
#         while True:
#             user_input = input("You: ")
#             bot_response = query(user_input)
#             print("Bot:", bot_response)
#     except KeyboardInterrupt:
#         print("\nChat ended.")

# if __name__ == "__main__":
#     main()


# import json
# import openai
# from fuzzywuzzy import fuzz
# import mysql.connector
# from mysql.connector import errorcode

# # MySQL connection configuration
# mysql_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'rahul@333',  # Replace with your MySQL password
#     'database': 'fink',  # Replace with your database name
#     'raise_on_warnings': True
# }

# def create_table(cursor):
#     table_schema = (
#         "CREATE TABLE IF NOT EXISTS CHATGPT ("
#         "  id INT AUTO_INCREMENT PRIMARY KEY,"
#         "  user_input TEXT NOT NULL,"
#         "  bot_response TEXT NOT NULL"
#         ")"
#     )
#     try:
#         cursor.execute(table_schema)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("CHATGPT table already exists.")
#         else:
#             print(err.msg)

# # Load Finkraft data from JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)

# # Initialize OpenAI client
# client = openai.AzureOpenAI(
#     azure_endpoint="https://finkdataopenai.openai.azure.com/",
#     api_key='d57b4f240c6f4c12bb8d316469e45f69',
#     api_version="2024-02-15-preview"
# )

# def extract_information(data, query, threshold=80):
#     """
#     Recursively extract relevant information from nested data based on the user's query
#     with fuzzy matching.
#     """
#     # Normalize the query
#     query = query.lower()
    
#     # Define a list to hold matching values
#     extracted_values = []
    
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if fuzz.partial_ratio(query, key.lower()) >= threshold:
#                 if isinstance(value, (dict, list)):
#                     nested_values = extract_information(value, query, threshold)
#                     extracted_values.extend(nested_values)
#                 else:
#                     extracted_values.append(str(value))
#             elif isinstance(value, (dict, list)):
#                 nested_values = extract_information(value, query, threshold)
#                 extracted_values.extend(nested_values)
#     elif isinstance(data, list):
#         for item in data:
#             nested_values = extract_information(item, query, threshold)
#             extracted_values.extend(nested_values)
    
#     return extracted_values

# def is_related_to_finkraft(query):
#     """
#     Check if the query is related to FinKraft AI using fuzzy matching.
#     Adjust the threshold as needed for accuracy.
#     """
#     keywords = ["finkraft", "fink", "fink ai", "finkraft ai"]
#     query = query.lower()
    
#     for keyword in keywords:
#         if fuzz.partial_ratio(query, keyword) >= 90:  # Adjust threshold as needed
#             return True
#     return False

# def query(user_input, cursor, conn):
#     # Check if the query is related to FinKraft AI
#     if not is_related_to_finkraft(user_input):
#         return "I'm a chatbot providing information about FinKraft AI. Please ask about FinKraft AI."

#     # Extract relevant information from finkraft_data
#     info = extract_information(finkraft_data, user_input)
    
#     if info:
#         # Format the extracted information
#         response = "\n".join(info)
#     else:
#         # Call OpenAI API using appropriate method if info not found in JSON
#         completion = client.chat.completions.create(
#             model="gpt-35-turbo",
#             messages=[
#                 {"role": "system", "content": "I'm a chatbot providing information about FinKraft AI. Here is the FinKraft AI data."},
#                 {"role": "user", "content": user_input}
#             ],
#             temperature=0.7,
#             max_tokens=150,
#             top_p=1.0,
#             frequency_penalty=0,
#             presence_penalty=0,
#             stop=None
#         )
#         response = completion.choices[0].message.content
    
#     # Store conversation in the MySQL database
#     insert_query = (
#         "INSERT INTO CHATGPT (user_input, bot_response)"
#         "VALUES (%s, %s)"
#     )
#     insert_data = (user_input, response)
#     cursor.execute(insert_query, insert_data)
#     conn.commit()  # Commit the transaction

#     return response

# def main():
#     try:
#         # Connect to MySQL
#         conn = mysql.connector.connect(**mysql_config)
#         cursor = conn.cursor()

#         # Create table if not exists
#         create_table(cursor)

#         print("Welcome! Chat with the bot (Press Ctrl+C to exit)")
#         while True:
#             user_input = input("You: ")
#             bot_response = query(user_input, cursor, conn)
#             print("Bot:", bot_response)

#     except mysql.connector.Error as err:
#         print(f"MySQL error: {err}")

#     except KeyboardInterrupt:
#         print("\nChat ended.")

#     finally:
#         # Close cursor and connection
#         if 'cursor' in locals() and cursor:
#             cursor.close()
#         if 'conn' in locals() and conn:
#             conn.close()

# if __name__ == "__main__":
#     main()


#######################
# from flask import Flask, request, jsonify
# from flask_cors import CORS  # Import CORS
# import json
# import openai
# from fuzzywuzzy import fuzz
# import mysql.connector
# from mysql.connector import errorcode

# app = Flask(__name__)
# CORS(app)  # Enable CORS

# # MySQL connection configuration
# mysql_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'rahul@333',
#     'database': 'fink',
#     'raise_on_warnings': True
# }

# def create_table(cursor):
#     table_schema = (
#         "CREATE TABLE IF NOT EXISTS CHATGPT ("
#         "  id INT AUTO_INCREMENT PRIMARY KEY,"
#         "  user_input TEXT NOT NULL,"
#         "  bot_response TEXT NOT NULL"
#         ")"
#     )
#     try:
#         cursor.execute(table_schema)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("CHATGPT table already exists.")
#         else:
#             print(err.msg)

# # Load Finkraft data from JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)

# # Initialize OpenAI client
# client = openai.AzureOpenAI(
#     azure_endpoint="https://finkdataopenai.openai.azure.com/",
#     api_key='d57b4f240c6f4c12bb8d316469e45f69',
#     api_version="2024-02-15-preview"
# )

# def extract_information(data, query, threshold=80):
#     query = query.lower()
#     extracted_values = []
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if fuzz.partial_ratio(query, key.lower()) >= threshold:
#                 if isinstance(value, (dict, list)):
#                     nested_values = extract_information(value, query, threshold)
#                     extracted_values.extend(nested_values)
#                 else:
#                     extracted_values.append(str(value))
#             elif isinstance(value, (dict, list)):
#                 nested_values = extract_information(value, query, threshold)
#                 extracted_values.extend(nested_values)
#     elif isinstance(data, list):
#         for item in data:
#             nested_values = extract_information(item, query, threshold)
#             extracted_values.extend(nested_values)
#     return extracted_values

# def is_related_to_finkraft(query):
#     keywords = ["finkraft", "fink", "fink ai", "finkraft ai"]
#     query = query.lower()
#     for keyword in keywords:
#         if fuzz.partial_ratio(query, keyword) >= 90:
#             return True
#     return False

# def query(user_input, cursor, conn):
#     if not is_related_to_finkraft(user_input):
#         return "I'm a chatbot providing information about FinKraft AI. Please ask about FinKraft AI."

#     info = extract_information(finkraft_data, user_input)
#     if info:
#         response = "\n".join(info)
#     else:
#         completion = client.chat.completions.create(
#             model="gpt-35-turbo",
#             messages=[
#                 {"role": "system", "content": "I'm a chatbot providing information about FinKraft AI. Here is the FinKraft AI data."},
#                 {"role": "user", "content": user_input}
#             ],
#             temperature=0.7,
#             max_tokens=150,
#             top_p=1.0,
#             frequency_penalty=0,
#             presence_penalty=0,
#             stop=None
#         )
#         response = completion.choices[0].message.content

#     insert_query = "INSERT INTO CHATGPT (user_input, bot_response) VALUES (%s, %s)"
#     insert_data = (user_input, response)
#     cursor.execute(insert_query, insert_data)
#     conn.commit()
#     return response

# @app.route('/api/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get('message')
#     try:
#         conn = mysql.connector.connect(**mysql_config)
#         cursor = conn.cursor()
#         create_table(cursor)
#         bot_response = query(user_input, cursor, conn)
#     except mysql.connector.Error as err:
#         print(f"MySQL error: {err}")
#         return jsonify({'response': 'Database error.'}), 500
#     finally:
#         if 'cursor' in locals() and cursor:
#             cursor.close()
#         if 'conn' in locals() and conn:
#             conn.close()
#     return jsonify({'response': bot_response})

# if __name__ == '__main__':
#     app.run(debug=True)

#Today  start

# from flask import Flask, request, jsonify
# from mysql.connector import errorcode

# from flask_cors import CORS
# import mysql.connector
# import openai
# import json

# app = Flask(__name__)
# CORS(app)

# # MySQL connection configuration
# mysql_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'rahul@333',
#     'database': 'fink',
#     'raise_on_warnings': True
# }

# # Initialize OpenAI client
# client = openai.AzureOpenAI(
#     azure_endpoint="https://finkdataopenai.openai.azure.com/",
#     api_key='d57b4f240c6f4c12bb8d316469e45f69',
#     api_version="2024-02-15-preview"
# )

# # Load FinKraft data from JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)

# def extract_information(query):
#     query = query.lower()
#     extracted_info = {}
#     for key, value in finkraft_data.items():
#         if key.lower() in query:
#             extracted_info[key] = value
#     if extracted_info:
#         response = ""
#         for key, value in extracted_info.items():
#             response += f"{key}:\n{value}\n\n"
#         return response.strip()
#     else:
#         return None

# def create_table(cursor):
#     table_schema = (
#         "CREATE TABLE IF NOT EXISTS CHATGPT ("
#         "  id INT AUTO_INCREMENT PRIMARY KEY,"
#         "  email_id VARCHAR(255),"
#         "  user_input TEXT NOT NULL,"
#         "  bot_response TEXT NOT NULL"
#         ")"
#     )
#     try:
#         cursor.execute(table_schema)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("CHATGPT table already exists.")
#         else:
#             print(err.msg)

# @app.route('/api/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_input = data.get('message')
#     email_id = data.get('email')  # Assuming email is passed in the request

#     conn = None
#     cursor = None
#     try:
#         conn = mysql.connector.connect(**mysql_config)
#         cursor = conn.cursor()

#         # Drop the existing table (if exists) and create a new one with the correct schema
#         cursor.execute("DROP TABLE IF EXISTS CHATGPT")
#         create_table(cursor)
        
#         info = extract_information(user_input)
        
#         if info:
#             bot_response = info
#         else:
#             completion = client.chat.completions.create(
#                 model="gpt-35-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are Fink, a chatbot for FinKraft AI. Provide detailed and user-friendly information to the users."},
#                     {"role": "user", "content": user_input}
#                 ],
#                 temperature=0.7,
#                 max_tokens=150,
#                 top_p=1.0,
#                 frequency_penalty=0,
#                 presence_penalty=0,
#                 stop=None
#             )
#             bot_response = completion.choices[0].message.content
        
#         insert_query = "INSERT INTO CHATGPT (email_id, user_input, bot_response) VALUES (%s, %s, %s)"
#         insert_data = (email_id, user_input, bot_response)
#         print(insert_data)
#         cursor.execute(insert_query, insert_data)
#         conn.commit()
        
#         return jsonify({'response': bot_response})
#     except mysql.connector.Error as err:
#         print(f"MySQL error: {err}")
#         return jsonify({'response': 'Database error.'}), 500
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# if __name__ == '__main__':
#     app.run(debug=True)


###################

# from flask import Flask, request, jsonify
# from mysql.connector import errorcode
# from flask_cors import CORS
# import mysql.connector
# import openai
# import json
# app = Flask(__name__)
# CORS(app)
# # MySQL connection configuration
# mysql_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'rahul@333',
#     'database': 'fink',
#     'raise_on_warnings': True
# }
# # Initialize OpenAI client
# client = openai.AzureOpenAI(
#     azure_endpoint="https://finkdataopenai.openai.azure.com/",
#     api_key='d57b4f240c6f4c12bb8d316469e45f69',
#     api_version="2024-02-15-preview"
# )
# # Load FinKraft data from JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)
# def extract_information(query):
#     query = query.lower()
#     extracted_info = {}
#     for key, value in finkraft_data.items():
#         if key.lower() in query:
#             extracted_info[key] = value
#     if extracted_info:
#         response = ""
#         for key, value in extracted_info.items():
#             response += f"{key}:\n{value}\n\n"
#         return response.strip()
#     else:
#         return None
# def create_table(cursor):
#     table_schema = (
#         "CREATE TABLE IF NOT EXISTS CHATGPT ("
#         "  id INT AUTO_INCREMENT PRIMARY KEY,"
#         "  email_id VARCHAR(255),"
#         "  user_input TEXT NOT NULL,"
#         "  bot_response TEXT NOT NULL"
#         ")"
#     )
#     try:
#         cursor.execute(table_schema)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("CHATGPT table already exists.")
#         else:
#             print(err.msg)
# @app.route('/api/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_input = data.get('message')
#     email_id = data.get('email')  # Assuming email is passed in the request
#     conn = None
#     cursor = None
#     try:
#         conn = mysql.connector.connect(**mysql_config)
#         cursor = conn.cursor()
#         # Drop the existing table (if exists) and create a new one with the correct schema
#         cursor.execute("DROP TABLE IF EXISTS CHATGPT")
#         create_table(cursor)
#         info = extract_information(user_input)
#         if info:
#             bot_response = info
#         else:
#             completion = client.chat.completions.create(
#                 model="gpt-35-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are Fink, a chatbot for FinKraft AI. Provide detailed and user-friendly information to the users."},
#                     {"role": "user", "content": user_input}
#                 ],
#                 temperature=0.7,
#                 max_tokens=150,
#                 top_p=1.0,
#                 frequency_penalty=0,
#                 presence_penalty=0,
#                 stop=None
#             )
#             bot_response = completion.choices[0].message.content
#         insert_query = "INSERT INTO CHATGPT (email_id, user_input, bot_response) VALUES (%s, %s, %s)"
#         insert_data = (email_id, user_input, bot_response)
#         print(insert_data)
#         cursor.execute(insert_query, insert_data)
#         conn.commit()
#         return jsonify({'response': bot_response})
#     except mysql.connector.Error as err:
#         print(f"MySQL error: {err}")
#         return jsonify({'response': 'Database error.'}), 500
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()
# if __name__ == '__main__':
#     app.run(debug=True)


############today
############today
# import json
# import openai
# from fuzzywuzzy import fuzz

# # Load Finkraft data from JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)

# # Initialize OpenAI client
# client = openai.AzureOpenAI(
#     azure_endpoint="https://finkdataopenai.openai.azure.com/",
#     api_key='d57b4f240c6f4c12bb8d316469e45f69',
#     api_version="2024-02-15-preview"
# )

# def extract_information(data, query, threshold=80):
#     """
#     Recursively extract relevant information from nested data based on the user's query
#     with fuzzy matching.
#     """
#     # Normalize the query
#     query = query.lower()
    
#     # Define a list to hold matching values
#     extracted_values = []
    
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if fuzz.partial_ratio(query, key.lower()) >= threshold:
#                 if isinstance(value, (dict, list)):
#                     nested_values = extract_information(value, query, threshold)
#                     extracted_values.extend(nested_values)
#                 else:
#                     extracted_values.append(str(value))
#             elif isinstance(value, (dict, list)):
#                 nested_values = extract_information(value, query, threshold)
#                 extracted_values.extend(nested_values)
#     elif isinstance(data, list):
#         for item in data:
#             nested_values = extract_information(item, query, threshold)
#             extracted_values.extend(nested_values)
    
#     return extracted_values

# def query(user_input):
#     # Extract relevant information from finkraft_data
#     info = extract_information(finkraft_data, user_input)
    
#     if info:
#         # Format the extracted information
#         response = "\n".join(info)
#         return response
#     else:
#         # Call OpenAI API using appropriate method if info not found in JSON
#         completion = client.chat.completions.create(
#             model="gpt-35-turbo",
#             messages=[
#                 {"role": "system", "content": "I'm a fink. Finkraft for all the details understand then. I only show user-related information about finkraft."},
#                 {"role": "user", "content": user_input}
#             ],
#             temperature=0.7,
#             max_tokens=150,
#             top_p=1.0,
#             frequency_penalty=0,
#             presence_penalty=0,
#             stop=None
#         )
#         bot_response = completion.choices[0].message.content
#         return bot_response

# def main():
#     print("Welcome! Chat with the bot (Press Ctrl+C to exit)")
#     try:
#         while True:
#             user_input = input("You: ")
#             bot_response = query(user_input)
#             print("Bot:", bot_response)
#     except KeyboardInterrupt:
#         print("\nChat ended.")

# if __name__ == "__main__":
#     main()

############
import json
import openai
from fuzzywuzzy import fuzz

# Load Finkraft data from JSON file
with open('finkraft_data.json', 'r') as file:
    finkraft_data = json.load(file)

# Initialize OpenAI client
client = openai.AzureOpenAI(
    azure_endpoint="https://finkdataopenai.openai.azure.com/",
    api_key='d57b4f240c6f4c12bb8d316469e45f69',
    api_version="2024-02-15-preview"
)

def extract_information(data, query, threshold=80):
    """
    Recursively extract relevant information from nested data based on the user's query
    with fuzzy matching.
    """
    # Normalize the query
    query = query.lower()
    
    # Define a list to hold matching values
    extracted_values = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            if fuzz.partial_ratio(query, key.lower()) >= threshold:
                if isinstance(value, (dict, list)):
                    nested_values = extract_information(value, query, threshold)
                    extracted_values.extend(nested_values)
                else:
                    extracted_values.append(str(value))
            elif isinstance(value, (dict, list)):
                nested_values = extract_information(value, query, threshold)
                extracted_values.extend(nested_values)
    elif isinstance(data, list):
        for item in data:
            nested_values = extract_information(item, query, threshold)
            extracted_values.extend(nested_values)
    
    return extracted_values

def query(user_input):
    # Extract relevant information from finkraft_data
    info = extract_information(finkraft_data, user_input)
    
    if info:
        # Format the extracted information
        response = "\n".join(info)
        return response
    else:
        # Call OpenAI API using appropriate method if info not found in JSON
        completion = client.chat.completions.create(
            model="gpt-35-turbo",
            messages=[
                {"role": "system", "content": "I'm a fink. Finkraft for all the details understand then. I only show user-related information about finkraft."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        bot_response = completion.choices[0].message.content
        return bot_response

def main():
    print("Welcome! Chat with the bot (Press Ctrl+C to exit)")
    try:
        while True:
            user_input = input("You: ")
            bot_response = query(user_input)
            print("Bot:", bot_response)
    except KeyboardInterrupt:
        print("\nChat ended.")

if __name__ == "__main__":
    main()
