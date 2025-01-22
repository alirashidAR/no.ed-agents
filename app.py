from smolagents import CodeAgent, HfApiModel
from huggingface_hub import login
import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

if HUGGINGFACE_TOKEN is None:
    raise ValueError("HUGGINGFACE_TOKEN is not set in the environment variables.")

login(HUGGINGFACE_TOKEN)

model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"

model = HfApiModel(model_id=model_id)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Add two numbers",
)