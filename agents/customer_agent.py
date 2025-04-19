from crewai import Agent

def get_customer_agent(llm):
    return Agent(
        role="Customer Agent",
        goal="Understand the developer's deployment requirements and coordinate with expert agents to choose the best deployment strategy.",
        backstory=(
            "You are the main interface between the developer and the cloud expert agents. "
            "Your job is to understand the user's needs, extract actionable constraints like budget, region, and performance, "
            "and then coordinate recommendations with Kubernetes, VM, and Serverless experts."
        ),
        tools=[],
        llm=llm,
        verbose=True
    )
