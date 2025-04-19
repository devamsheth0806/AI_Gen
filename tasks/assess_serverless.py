from crewai import Task
from utils.dataset_utils import deployment_options

def assess_serverless_task(agent):
    return Task(
        description=(
            f"Assess Serverless as a deployment strategy.\n"
            f"Cost: ${deployment_options['serverless']['cost_per_month']}/month.\n"
            f"Performance: {deployment_options['serverless']['performance']}.\n"
            f"Complexity: {deployment_options['serverless']['complexity']}.\n"
            f"Summarize its suitability and tradeoffs."
        ),
        expected_output="Recommendation on Serverless deployment",
        agent=agent
    )
