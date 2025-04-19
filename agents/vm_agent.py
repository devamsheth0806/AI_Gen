from crewai import Agent

def get_vm_agent(llm):
    return Agent(
        role="Virtual Machine Expert",
        goal="Analyze if traditional virtual machines are the best deployment strategy",
        backstory=(
            "You're a cloud architect with deep expertise in VM provisioning on AWS EC2, Google Compute Engine, and Azure VMs. "
            "You can assess cost, control, and ease of use for VM-based deployments."
        ),
        tools=[],
        llm=llm,
        verbose=True
    )
