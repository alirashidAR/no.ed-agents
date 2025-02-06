import json
from google import genai
from pydantic import BaseModel, TypeAdapter


class Roles(BaseModel):
  role : str

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
        config={
            'response_mime_type': 'application/json',
            'response_schema': list[Roles],
        },
    )

    return response.text

