# Learning AutoGen 2 (AG2)

This repository contains learning materials and examples for AutoGen 2, focusing on multi-agent conversations and automated workflows using Large Language Models (LLMs).

## What is AutoGen 2?

AutoGen 2 is a framework that enables the development of LLM applications using multiple conversable agents. It allows for:
- Multi-agent conversations
- Sequential chat workflows
- Automated task completion
- Customizable agent behaviors

## Project Structure

This project includes examples demonstrating various AutoGen 2 features:

### Lesson 2: Sequential Chats and Customer Onboarding
- Demonstrates how to create multiple agents with specific roles
- Shows how to orchestrate sequential conversations
- Implements a practical customer onboarding workflow

## Prerequisites

- Python 3.8+
- OpenAI API key
- Basic understanding of LLMs and Python
- Pipenv (Install with `pip install pipenv`)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd ag2-learning
```

2. Install and activate dependencies using Pipenv:
```bash
# Install dependencies from Pipfile
pipenv install

# Activate the virtual environment
pipenv shell
```

3. Configure environment:
   - Create a `.env` file in the project root
   - Copy `.env.sample` to `.env` in the project root:
   ```bash
   cp .env.sample .env
   ```
   - Add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```
   - Copy `OAI_CONFIG_LIST.sample` to `OAI_CONFIG_LIST`:
   ```bash
   cp OAI_CONFIG_LIST.sample OAI_CONFIG_LIST
   ```
   - Update both files with your actual API keys

   Note: The `.env` and `OAI_CONFIG_LIST` files are git-ignored to protect your API keys.

## Key Concepts Covered

1. **Agent Creation**
   - ConversableAgent configuration
   - System message definition
   - Agent behavior customization

2. **Chat Management**
   - Sequential chat orchestration
   - Message history handling
   - Chat summarization

3. **Agent Types**
   - Information gathering agents
   - Topic preference agents
   - Customer engagement agents
   - Proxy agents

4. **Advanced Features**
   - Chat reflection and summarization
   - Context management
   - Cost tracking

## Running the Examples

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Navigate to the lesson notebooks:
   - `L2_Sequential_Chats_and_Customer_Onboarding.ipynb`

3. Follow the notebook cells and comments to understand each concept

## Best Practices

- Always use descriptive agent names (alphanumeric, underscores, hyphens only)
- Configure appropriate system messages for each agent
- Set reasonable conversation limits using `max_turns`
- Use chat summarization for complex workflows
- Monitor costs using the built-in tracking

## Common Issues and Solutions

1. Agent Name Format
   - Use only alphanumeric characters, underscores, and hyphens
   - Avoid spaces and special characters

2. API Key Configuration
   - Ensure `.env` file is properly configured
   - Check API key permissions and quotas

3. Conversation Management
   - Use `clear_history` appropriately
   - Monitor conversation length
   - Implement proper termination conditions

## Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Python dotenv Documentation](https://pypi.org/project/python-dotenv/)

## Contributing

Feel free to:
- Submit issues for bugs or suggestions
- Create pull requests with improvements
- Share your learning experiences

## License

[Add your license information here]
