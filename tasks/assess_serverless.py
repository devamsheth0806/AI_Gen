from crewai import Task
from utils.dataset_utils import deployment_options

def assess_serverless_task(agent):

    serverless_options = deployment_options["serverless"]
    option_text = "\n".join(
        [f"Cost: ${opt['price']}/hour.\n"
            f"Product: {opt['product']}.\n"
            f"Location: {opt['location']}.\n"
            f"Meter Name: {opt['meter name']}.\n"
         for opt in serverless_options]
    )

    return Task(
        description=(
            f"You are the Serverless Expert. Analyze the following serverless deployment options:\n\n"
            f"{option_text}\n\n"
            f"Based on cost, performance, and complexity, recommend the most suitable serverless deployment "
            f"option from the list, and explain why."
        ),
        expected_output="Recommendation on Serverless deployment",
        agent=agent
    )
