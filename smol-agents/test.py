from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
import os

model = LiteLLMModel(model_id="gemini/gemini-1.5-flash",
                     api_key=(geminiApiKey))

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("What are the next NFL playoff matchs?")