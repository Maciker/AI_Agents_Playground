from smolagents import CodeAgent, LiteLLMModel
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = LiteLLMModel(model_id="gemini/gemini-1.5-flash",
                     api_key=api_key)


# Define the agent
class NFLDraftAdvisor(CodeAgent):
    def __init__(self, model):
        super().__init__(model=model)

    def recommend_player(self, position, strategy):
        prompt = f"""
        You are an expert fantasy football advisor. Based on the following criteria, recommend a player to draft:
        - Position: {position}
        - Strategy: {strategy}

        Provide a detailed explanation for your recommendation.
        """
        response = self.model.generate(prompt)
        return response


# Example usage
agent = NFLDraftAdvisor(model=model)
position = "Running Back"
strategy = "I prefer a balanced team with a strong running game."

print("Recommended Player:")
print(agent.recommend_player(position, strategy))
