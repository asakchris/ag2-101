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

def should_escalate(sender):
    content = specialist.chat_messages
    messages = content[next(iter(content))]
    message_contents = [message["content"] for message in messages]
    all_messages = " ".join(message_contents)
    important_words = ["urgent", "important", "critical", "help", "support"]
    exists = any(word in all_messages.lower() for word in important_words)
    return exists

specialist.register_nested_chats(
    [
        {
            "recipient": kb_manager,
            "summary_method": "last_msg",
            "message": "Treat this urgently and respond in a professional manner.",
            "max_turns": 1,
        }
    ],
    trigger=lambda sender: sender is user_proxy and should_escalate(sender),
)

user_proxy.initiate_chats([
    {
        "recipient": specialist,
        "message": "Hello, I need help!",
    },
    {
        "recipient": surveyor,
        "message": "How was your experience with our support?",
    }
])
