from crewai import Task
from utils.dataset_utils import deployment_options

def assess_k8s_task(agent):
    k8s_options = deployment_options["kubernetes"]
    option_text = "\n".join(
        [f"Cost: ${opt['price']}/hour, Product: {opt['product']}, Location: {opt['location']}, Meter Name: {opt['meterName']}" for opt in k8s_options]
    )
    return Task(
        description=(
            f"You are the Kubernetes Expert. Analyze the following Kubernetes deployment options:\n\n"
            f"{option_text}\n\n"
            f"Based on cost, performance, and complexity, recommend the most suitable Kubernetes deployment "
            f"option from the list, and explain why."
        ),
        expected_output="Recommendation on Kubernetes deployment",
        agent=agent
    )
