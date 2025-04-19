from crewai import Task

def summarize_task(agent):
    return Task(
        description=(
            "As the Customer Agent, you have received deployment assessments from Kubernetes, VM, and Serverless experts.\n"
            "Compare their recommendations based on cost, performance, and complexity.\n"
            "Choose the most appropriate deployment strategy for a general web application.\n"
            "Include the reason why it was selected over the others."
        ),
        expected_output="Final recommendation for deployment with comparison and justification.",
        agent=agent
    )
