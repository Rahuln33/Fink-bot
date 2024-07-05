import json
import openai

# Load Finkraft data from JSON file
with open('demo.json', 'r') as file:
    finkraft_data = json.load(file)

# Initialize OpenAI client
client = openai.AzureOpenAI(
    azure_endpoint="https://finkdataopenai.openai.azure.com/",
    api_key='d57b4f240c6f4c12bb8d316469e45f69',
    api_version="2024-02-15-preview"
)

def extract_information(data, query):
    """
    Recursively extract relevant information from nested data based on the user's query.
    """
    # Normalize the query
    query = query.lower()
    
    # Define a dictionary to hold matching information
    extracted_info = {}
    
    if isinstance(data, dict):
        for key, value in data.items():
            if query in key.lower():
                extracted_info[key] = value
            elif isinstance(value, (dict, list)):
                nested_info = extract_information(value, query)
                if nested_info:
                    extracted_info[key] = nested_info
    elif isinstance(data, list):
        for item in data:
            nested_info = extract_information(item, query)
            if nested_info:
                extracted_info.append(nested_info)
    
    return extracted_info

def query(user_input):
    # Extract relevant information from finkraft_data
    info = extract_information(finkraft_data, user_input)
    
    if info:
        # Format the extracted information
        response = json.dumps(info, indent=2)
        return response
    else:
        # Call OpenAI API using appropriate method if info not found in JSON
        completion = client.chat.completions.create(
            model="gpt-35-turbo",
            messages=[
                {"role": "system", "content": "I'm a fink. finkraft for all the details understand then. I only show user-related information."},
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