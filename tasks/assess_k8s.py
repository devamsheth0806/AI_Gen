from crewai import Task
from utils.cost_dataset import deployment_options

def assess_k8s_task(agent):
    return Task(
        description=(
            f"Assess Kubernetes as a deployment strategy.\n"
            f"Cost: ${deployment_options['kubernetes']['cost_per_month']}/month.\n"
            f"Performance: {deployment_options['kubernetes']['performance']}.\n"
            f"Complexity: {deployment_options['kubernetes']['complexity']}.\n"
            f"Summarize its suitability and tradeoffs."
        ),
        expected_output="Recommendation on Kubernetes deployment",
        agent=agent
    )
