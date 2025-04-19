from crewai import Agent

def get_serverless_agent(llm):
    return Agent(
        role="Serverless Expert",
        goal="Analyze if serverless architecture is the best deployment strategy",
        backstory=(
            "You're an expert in serverless platforms like AWS Lambda, Google Cloud Functions, and Azure Functions. "
            "You understand cost, scalability, cold start latency, and operational simplicity."
        ),
        tools=[],
        llm=llm,
        verbose=True
    )
