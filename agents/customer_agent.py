from crewai import Agent

def get_customer_agent(llm):
    return Agent(
        role="Customer Agent",
        goal="Help the developer find the most cost-effective and suitable deployment strategy",
        backstory=(
            "You are a helpful DevOps assistant who interacts directly with the developer. "
            "You collect recommendations from the Kubernetes, VM, and Serverless agents, compare them, "
            "and present the best deployment strategy with reasoning."
        ),
        tools=[],
        llm=llm,
        verbose=True
    )
