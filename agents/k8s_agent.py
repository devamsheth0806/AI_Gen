from crewai import Agent

def get_k8s_agent(llm):
    return Agent(
        role="Kubernetes Expert",
        goal="Analyze if Kubernetes is the best deployment strategy",
        backstory="You're a senior DevOps engineer specializing in K8s clusters on cloud platforms.",
        tools=[],
        llm=llm,
        verbose=True
    )
