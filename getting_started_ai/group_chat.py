import os

from autogen import AssistantAgent, UserProxyAgent, ConversableAgent, GroupChat, GroupChatManager

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

kb_manager = ConversableAgent(
    name="kb_manager",
    llm_config=llm_config,
    system_message="""
    You answer in a polite way that the problem
    will be looked into, and resolved as soon as possible
    and that you will respond to the customer via email.

    Reply "TERMINATE" when you have no further input.
    """
)

specialist.description = "This agent works with the customer to resolve their issue."
surveyor.description = "This agent will ask questions to determine if the customer is satisfied with the support they received only when the conversation is over."
kb_manager.description = "This agent will take over when the user mentions that their request is urgent or important."

group_chat = GroupChat(
    agents=[specialist, surveyor, kb_manager],
    messages=[]
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)

user_proxy.initiate_chat(
    group_chat_manager,
    message="Hello, I need help!",
    summary_method="reflection_with_llm",
)
