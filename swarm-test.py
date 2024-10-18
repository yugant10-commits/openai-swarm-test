import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

from swarm import Swarm, Agent

client = Swarm()

def transfer_to_agent_b():
    return agent_b

def perform_addition(number1:int, number2: int)->int:
    print("inside perform addition")
    print(f"number 1 inpute:{number1}")
    print(f"number 2 inpute:{number2}")
    return number1*number2


english_agent = Agent(
    name="English Agent",
    instructions="You only speak English.",
)

spanish_agent = Agent(
    name="Spanish Agent",
    instructions="You only speak Spanish.",
)

cat_agent = Agent(
    name="Cat Agent",
    instructions="You answer any question about cats and all your answers must end in 'meow, meow, meow' .",
)

def transfer_to_cats_agent():
    """Transfer spanish speaking users immediately."""
    return spanish_agent

def transfer_to_spanish_agent():
    """Transfer any queires about cats immediately."""
    print("inside cats agent")
    return cat_agent

english_agent.functions.append(transfer_to_spanish_agent)
english_agent.functions.append(transfer_to_cats_agent)
english_agent.functions.append(perform_addition)


messages = [{"role": "user", "content": "subtract 2 from 1"}]
response = client.run(agent=english_agent, messages=messages)

print(response.messages[-1]["content"])
