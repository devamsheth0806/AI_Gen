from crewai import Task
from utils.dataset_utils import filter_deployments

def assess_k8s_task(agent, user_input):
    k8s_options = filter_deployments(service_key='kubernetes', user_input=user_input)
    
    option_text = "\n".join(
        [f"Cost: ${opt['price']}/hour, Product: {opt['product']}, Location: {opt['location']}, Meter Name: {opt['meterName']}" for opt in k8s_options]
    )
    return Task(
        description=(
            f"You are the Kubernetes Expert. Analyze the following Kubernetes deployment options:\n"
            f"{option_text}\n\n"
            f"Based on cost, performance, and complexity, recommend the most suitable Kubernetes deployment "
            f"option from the list, and explain why."
            f"Keep your options specific to requirements and the list"
        ),
        expected_output="Recommendation on Kubernetes deployment",
        agent=agent
    )
