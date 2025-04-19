from crewai import Task
from utils.dataset_utils import deployment_options

def assess_vm_task(agent):
    vm_options = deployment_options["vm"]
    option_text = "\n".join(
        [f"Cost: ${opt['price']}/hour.\n"
            f"Product: {opt['product']}.\n"
            f"Location: {opt['vm']['location']}.\n"
            f"Meter Name: {opt['meter name']}.\n"
         for opt in vm_options]
    )
    return Task(
        description=(
            f"You are the Virtual Machine Expert. Analyze the following VM deployment options:\n\n"
            f"{option_text}\n\n"
            f"Based on cost, performance, and complexity, recommend the most suitable VM deployment "
            f"option from the list, and explain why."
        ),
        expected_output="Recommendation on VM deployment",
        agent=agent
    )
