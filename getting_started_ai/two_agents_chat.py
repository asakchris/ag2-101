import os

from autogen import AssistantAgent, UserProxyAgent

llm_config = {
    "model": "gpt-4o-mini",
    "api_key": os.getenv("OPENAI_API_KEY"),
}

specialist = AssistantAgent(
    name="specialist", 
    llm_config=llm_config
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS", 
    code_execution_config=False
)

user_proxy.initiate_chat(
    specialist, 
    message="Hello, I need help!"
)
