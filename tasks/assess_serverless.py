from crewai import Task
from utils.dataset_utils import filter_deployments

def assess_serverless_task(agent, user_input):
    serverless_options = options = filter_deployments(service_key='serverless', user_input=user_input)
    option_text = "\n".join(
        [f"Cost: ${opt['price']}/hour, Product: {opt['product']}, Location: {opt['location']}, Meter Name: {opt['meterName']}" for opt in serverless_options]
    )

    return Task(
        description=(
            f"You are the Serverless Expert. Analyze the following serverless deployment options:\n\n"
            f"{option_text}\n\n"
            f"Based on cost, performance, and complexity, recommend the most suitable serverless deployment "
            f"option from the list, and explain why."
            f"Keep your options specific to requirements and the list"
        ),
        expected_output="Recommendation on Serverless deployment",
        agent=agent
    )
