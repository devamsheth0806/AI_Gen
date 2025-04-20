from crewai import Task

def summarize_task(agent, user_input):
    return Task(
        description=(
            f"You are the Customer Agent.\n"
            f"The developer has the following requirements:\n{user_input}\n\n"
            f"You've received expert agent recommendations (Kubernetes, VM, Serverless).\n\n"
            f"Your job is to summarize each agent's recommendation briefly (1 to 2 lines each) and identify the 2 to 3 best options based on cost, location, and suitability."
            "Maintain the technical information and name of resources as required."
        ),
        expected_output="Summarize the results from the expert agents",
        agent=agent
    )
