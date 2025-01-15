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
        super().__init__(tools=[], model=model)

    def recommend_player(self, position, strategy, draft_round, draft_position, isPPR):
        prompt = f"""
        You are an expert fantasy football advisor. Based on the following criteria, recommend a player to draft:
        - Position: {position}
        - Strategy: {strategy}
        - Round: {draft_round}
        - DraftPosition: {draft_position}
        - PPR: {isPPR}

        Provide a detailed explanation for your recommendation.
        """
        messages = [{"role": "user", "content": prompt}]
        response = self.model(messages)
        return response


# Example usage
agent = NFLDraftAdvisor(model=model)
position = "Running Back"
strategy = "I prefer a balanced team with a strong running game."
draft_round = "1"
draft_position = "1"
isPPR = True

print("Recommended Player:")
print(agent.recommend_player(position, strategy, draft_round, draft_position, isPPR))
