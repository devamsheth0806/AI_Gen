from crewai import Agent

def get_vm_agent(llm):
    return Agent(
        role="Azure Virtual Machine Expert",
        goal="Analyze which Azure virtual machine configuration works best as deployment strategy",
        backstory=(
            "You're a cloud architect with deep expertise in VM provisioning on Azure VMs. "
            "You can assess cost, control, and ease of use for VM-based deployments."
        ),
        tools=[],
        llm=llm,
        verbose=True
    )
