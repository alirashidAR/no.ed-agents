import json
from google import genai

def get_recommended_roles(api_key, tags):
    prompt = f'''List 4 roles that align with 
    the following interests: {tags} 

    Return with the following format:
    ["role1", "role2", "role3", "role4"]
    
    Send just the list of roles as a response and NOTHING else.
    '''
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
    )

    response_text = response.text.strip()

    try:
        # Convert JSON string to a Python list if already in JSON format
        roles_list = json.loads(response_text)
    except json.JSONDecodeError:
        # Fallback: If it's not a proper JSON string, try evaluating safely
        import ast
        roles_list = ast.literal_eval(response_text)

    return json.dumps(roles_list)  # Convert to JSON string
