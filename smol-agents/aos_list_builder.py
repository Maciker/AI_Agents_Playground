from smolagents import CodeAgent, LiteLLMModel
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = LiteLLMModel(model_id="gemini/gemini-1.5-flash",
                     api_key=api_key)


# Define the agent
class AoSListBuilder(CodeAgent):
    def __init__(self, model):
        super().__init__(tools=[], model=model)

    def build_army_list(self, faction, playstyle, points_limit, enemy_faction):
        prompt = f"""
        You are an expert Warhammer Age of Sigmar player. Create a competitive army list with the following criteria:
        - Faction: {faction}
        - Playstyle: {playstyle}
        - Points Limit: {points_limit}
        - EnemyFaction: {enemy_faction}

        Provide a detailed breakdown of the units, their roles, and how they synergize with the chosen playstyle.
        """
        messages = [{"role": "user", "content": prompt}]
        response = self.model(messages)
        return response


# Example usage
agent = AoSListBuilder(model=model)
faction = "Stormcast Eternals"
playstyle = "Aggressive, with a focus on fast-moving units and heavy hitters."
points_limit = 2000
enemy_faction = "Slave to darkness"

print("Army List:")
print(agent.build_army_list(faction, playstyle, points_limit, enemy_faction))
