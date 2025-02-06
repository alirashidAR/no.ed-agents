from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    HfApiModel,
    ManagedAgent,
    DuckDuckGoSearchTool,
    LiteLLMModel,
)
from markdownify import markdownify
from requests.exceptions import RequestException
from smolagents import tool
from dotenv import load_dotenv
from tools.web import visit_webpage, get_links_from_markdown
from tools.coursera import get_coursera_courses_names
import os

load_dotenv()

model= LiteLLMModel(
    model_id='gemini/gemini-1.5-flash',
    api_key=os.getenv("GOOGLE_GEN_AI")
)

# model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"
# model_web = HfApiModel(model_id)



web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), visit_webpage, get_links_from_markdown,get_coursera_courses_names],
    model=model,
)

managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="search",
    description="Runs web searches for you. Give it your query as an argument.",
)

manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[managed_web_agent],
    additional_authorized_imports=["time", "numpy", "pandas","json","requests"],
)

## Rough Draft of the resume( The  parsed resume will be passed to the function)
# Resume ={
#     "skills": ["Python", "Machine Learning", "Data Science"],
#     "experience": "3 years",
#     "education": "Bachelor's degree in Computer Science",
#     "tech_stack": ["Python", "TensorFlow", "Scikit-learn"],
# }

answer_format = [
    {
        "answer": {
            "id": 1,
            "topic": "Python",
            "subtopics": ["Data Types", "Control Structures", "Functions", "Classes"],
            "duration": "3-4 weeks",
            "courses_courses": ["coursera_course_link1", "coursera_course_link2"],
            "projects_to_do": ["A data analysis project", "A simple web application"],
            "outcome_of_learning_30_words": "You will be able to write clean and efficient code in Python and understand the basics of programming.",
        }
    }
]


async def create_roadmap(resume:str, role:str):
    answer= manager_agent.run(f'''For this {resume} create a roadmap to become a {role} , MAKE SURE NOT TO ADD topics that the user had already covered IN THE Resume.Research about the current trends on the web and then create the roadmap from web.Find relevant coursera coureses too for the sub topics with current links.Have 6 topics.Follow the following format for the answer {answer_format}. Just make sure to add the links to the courses and add relevant courses and return only the answer in the required format''')
    print(answer)

    return answer