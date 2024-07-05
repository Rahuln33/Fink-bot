
###########2
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

#         # Ensure the table exists
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

##################
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
#         "  session_id VARCHAR(255),"
#         "  email VARCHAR(255),"
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

# def get_conversation_history(cursor, session_id):
#     query = "SELECT user_input, bot_response FROM CHATGPT WHERE session_id = %s"
#     cursor.execute(query, (session_id,))
#     history = cursor.fetchall()
#     conversation = []
#     for user_input, bot_response in history:
#         conversation.append({"role": "user", "content": user_input})
#         conversation.append({"role": "assistant", "content": bot_response})
#     return conversation

# @app.route('/api/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_input = data.get('message')
#     email = data.get('email')  # Assuming email is passed in the request
#     session_id = data.get('session_id')  # Assuming session_id is passed in the request

#     conn = None
#     cursor = None
#     try:
#         conn = mysql.connector.connect(**mysql_config)
#         cursor = conn.cursor()

#         # Ensure the table exists
#         create_table(cursor)
        
#         info = extract_information(user_input)
        
#         if info:
#             bot_response = info
#         else:
#             # Get the conversation history for the session
#             conversation_history = get_conversation_history(cursor, session_id)
#             conversation_history.append({"role": "user", "content": user_input})
            
#             completion = client.chat.completions.create(
#                 model="gpt-35-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are Fink, a chatbot for FinKraft AI. Provide detailed and user-friendly information to the users."},
#                 ] + conversation_history,
#                 temperature=0.7,
#                 max_tokens=150,
#                 top_p=1.0,
#                 frequency_penalty=0,
#                 presence_penalty=0,
#                 stop=None
#             )
#             bot_response = completion.choices[0].message.content
        
#         insert_query = "INSERT INTO CHATGPT (session_id, email, user_input, bot_response) VALUES (%s, %s, %s, %s)"
#         insert_data = (session_id, email_id, user_input, bot_response)
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

#########
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import errorcode
import openai
import json

app = Flask(__name__)
CORS(app)

# MySQL connection configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'rahul@333',
    'database': 'fink',
    'raise_on_warnings': True
}

# Initialize OpenAI client
client = openai.AzureOpenAI(
    azure_endpoint="https://finkdataopenai.openai.azure.com/",
    api_key='d57b4f240c6f4c12bb8d316469e45f69',
    api_version="2024-02-15-preview"
)

# Load FinKraft data from JSON file
with open('finkraft_data.json', 'r') as file:
    finkraft_data = json.load(file)

def extract_information(query):
    query = query.lower()
    extracted_info = {}
    for key, value in finkraft_data.items():
        if key.lower() in query:
            extracted_info[key] = value
    if extracted_info:
        response = ""
        for key, value in extracted_info.items():
            response += f"{key}:\n{value}\n\n"
        return response.strip()
    else:
        return None

def create_table(cursor):
    table_schema = (
        "CREATE TABLE IF NOT EXISTS CHATGPT ("
        "  id INT AUTO_INCREMENT PRIMARY KEY,"
        "  session_id VARCHAR(255),"
        "  email_id VARCHAR(255),"
        "  user_input TEXT,"
        "  bot_response TEXT"
        ")"
    )
    try:
        cursor.execute(table_schema)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("CHATGPT table already exists.")
        else:
            print(err.msg)

def get_conversation_history(cursor, session_id):
    query = "SELECT user_input, bot_response FROM CHATGPT WHERE session_id = %s"
    cursor.execute(query, (session_id,))
    history = cursor.fetchall()
    conversation = []
    for user_input, bot_response in history:
        conversation.append({"role": "user", "content": user_input})
        conversation.append({"role": "assistant", "content": bot_response})
    return conversation

def get_or_create_session_id(cursor, email_id):
    cursor.execute("SELECT session_id FROM CHATGPT WHERE email_id = %s LIMIT 1", (email_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        cursor.execute("SELECT MAX(session_id) FROM CHATGPT")
        max_session_id = cursor.fetchone()[0]
        if max_session_id:
            new_session_id = int(max_session_id) + 1
        else:
            new_session_id = 10001
        return str(new_session_id)

@app.route('/api/start_session', methods=['POST'])
def start_session():
    data = request.json
    email = data.get('email')
    print("Received email:", email)

    if not email:
        print("Email is missing")
        return jsonify({'error': 'Email is required'}), 400

    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        create_table(cursor)  # Ensure the table is created before inserting data

        # Generate or retrieve a session ID
        session_id = get_or_create_session_id(cursor, email)
        print("Generated session ID:", session_id)

        # Insert the email into the database with default values for user_input and bot_response
        insert_query = "INSERT INTO CHATGPT (session_id, email_id, user_input, bot_response) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (session_id, email, '', ''))
        conn.commit()
        print("Inserted email with session ID:", insert_query)

        return jsonify({'session_id': session_id}), 200
    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")
        return jsonify({'error': 'Database error'}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')
    email = data.get('email')
    session_id = data.get('session_id')
    print("Received email:", email)
    print("Session ID:", session_id)
    print("User input:", user_input)

    if not user_input or not email or not session_id:
        return jsonify({'response': 'Invalid input parameters.'}), 400

    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        create_table(cursor)

        info = extract_information(user_input)
        
        if info:
            bot_response = info
        else:
            # Get the conversation history for the session
            conversation_history = get_conversation_history(cursor, session_id)
            conversation_history.append({"role": "user", "content": user_input})
            
            completion = client.chat.completions.create(
                model="gpt-35-turbo",
                messages=[
                    {"role": "system", "content": "You are Fink, a chatbot for FinKraft AI. Provide detailed and user-friendly information to the users."},
                ] + conversation_history,
                temperature=0.7,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None
            )
            bot_response = completion.choices[0].message.content
        
        insert_query = "INSERT INTO CHATGPT (session_id, email_id, user_input, bot_response) VALUES (%s, %s, %s, %s)"
        print("Insert query:", insert_query)
        insert_data = (session_id, email, user_input, bot_response)
        print("Insert data:", insert_data)
        cursor.execute(insert_query, insert_data)
        conn.commit()
        
        return jsonify({'response': bot_response})
    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")
        return jsonify({'response': 'Database error.'}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
