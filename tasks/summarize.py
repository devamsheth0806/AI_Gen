from crewai import Task

def summarize_task(agent, user_input):
    return Task(
        description=(
            f"You are the Customer Agent.\n"
            f"The developer provided the following deployment requirements on Azure:\n"
            f"{user_input}\n\n"
            f"Three expert agents (Kubernetes, VM, Serverless) have returned their recommended options "
            f"based on these constraints.\n"
            f"Your job is to read all their outputs, compare them carefully based on price, location, and suitability, "
            f"and provide a final recommendation.\n\n"
            f"Your final output should:\n"
            f"1. Summarize each expert’s recommendation (1–2 lines each).\n"
            f"2. Compare the pros and cons.\n"
            f"3. Recommend ONE option as the final deployment strategy.\n"
            f"4. Justify your decision based on the user's input.\n"
            f"5. Specify all technical details along with price as list"
        ),
        expected_output="Final deployment recommendation with comparison.",
        agent=agent
    )
