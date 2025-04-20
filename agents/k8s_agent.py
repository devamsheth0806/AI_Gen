from crewai import Agent

def get_k8s_agent(llm):
    return Agent(
        role="Azure Kubernetes Expert",
        goal="Analyze which Azure Kubernetes service configuration has the best deployment strategy",
        backstory="You're a senior DevOps engineer specializing in Azure K8s clusters on cloud platforms.",
        tools=[],
        llm=llm,
        verbose=True
    )
