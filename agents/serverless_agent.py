from crewai import Agent

def get_serverless_agent(llm):
    return Agent(
        role="Azure Functions Expert",
        goal="Analyze which Azure Functions configuration has the best deployment strategy",
        backstory=(
            "You're an expert in serverless platforms for Azure Functions. "
            "You understand cost, scalability, cold start latency, and operational simplicity."
        ),
        tools=[],
        llm=llm,
        verbose=True
    )
