import os

from autogen import AssistantAgent, UserProxyAgent

llm_config = {
    "model": "gpt-4o-mini",
    "api_key": os.getenv("OPENAI_API_KEY"),
}

specialist = AssistantAgent(
    name="specialist", 
    llm_config=llm_config,
    system_message="""
    You are a professional customer service representative.
    Your goal is to provide the user with the best possible service.
    Always start by greeting the customer and asking how you can help them.

    Always answer in one short sentence.
    Never say things like "As an AI" or "I am an AI" or anything like that.
    Reply "TERMINATE" when everything is done.
    """
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS", 
    code_execution_config=False
)

surveyor = AssistantAgent(
    name="surveyor",
    llm_config=llm_config,
    system_message="""
    You are a surveyor.
    You ask a single question.
    Your job is to get a number between 1 and 10 from the customer
    about their support experience before the conversation ends.

    Reply "TERMINATE" when you have no further questions.
    """
)

user_proxy.initiate_chats(
    [
        {
            "recipient": specialist,
            "message": "Hello, I need help!",
            "summary_method": "reflection_with_llm"
        },
        {
            "recipient": surveyor,
            "message": """
            Based on the provided information,
            determine if the customer is satisfied with the support they received.
            """,
            "carryover": "This is a new customer."
        }
    ]
)
