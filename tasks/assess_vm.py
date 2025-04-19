from crewai import Task
from utils.dataset_utils import deployment_options

def assess_vm_task(agent):
    return Task(
        description=(
            f"Assess Virtual Machines (VMs) as a deployment strategy.\n"
            f"Cost: ${deployment_options['vm']['cost_per_month']}/month.\n"
            f"Performance: {deployment_options['vm']['performance']}.\n"
            f"Complexity: {deployment_options['vm']['complexity']}.\n"
            f"Summarize its suitability and tradeoffs."
        ),
        expected_output="Recommendation on VM deployment",
        agent=agent
    )
