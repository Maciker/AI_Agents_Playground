from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = LiteLLMModel(model_id="gemini/gemini-1.5-flash",
                     api_key=(api_key))

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("Give the probabilities for each team alive on the NFL to win the Superbowl?")