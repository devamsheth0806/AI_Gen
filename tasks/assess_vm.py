from crewai import Task
from utils.dataset_utils import filter_deployments

def assess_vm_task(agent, user_input):
    vm_options = filter_deployments(service_key='vm', user_input=user_input)
    option_text = "\n".join(
        [f"Cost: ${opt['price']}/hour, Product: {opt['product']}, Location: {opt['location']}, Meter Name: {opt['meterName']}" for opt in vm_options]
    )
    return Task(
        description=(
            f"You are the Virtual Machine Expert. Analyze the following VM deployment options:\n"
            f"{option_text}\n\n"
            f"Based on cost, performance, and complexity, recommend the most suitable VM deployment "
            f"option from the list, and explain why."
            f"Keep your options specific to requirements and the list"
        ),
        expected_output="Recommendation on VM deployment",
        agent=agent
    )
