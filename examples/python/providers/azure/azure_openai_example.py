"""
Basic example of using Azure OpenAI with PraisonAI
"""

from praisonaiagents import Agent

# Initialize Agent with Azure OpenAI
agent = Agent(
    instructions="You are a helpful assistant",
    llm="azure/gpt-4",
)

# Example conversation
response = agent.start("Hello! Can you help me with a coding task?")

# Example with code generation
coding_task = """
Write a Python function that implements a binary search algorithm.
Include proper documentation and error handling.
"""

response = agent.start(coding_task)

# Example with analysis
analysis_task = """
Analyze the pros and cons of using microservices architecture 
for a large-scale e-commerce application.
"""

response = agent.start(analysis_task) 