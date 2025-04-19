from crewai import Task

def summarize_task(agent, user_input):
    return Task(
        description=(
            f"You are the Customer Agent.\n"
            f"The developer has the following requirements:\n{user_input}\n\n"
            f"You've received expert agent recommendations (Kubernetes, VM, Serverless).\n\n"
            f"Your job is to:\n"
            f"1. Summarize each agent's recommendation briefly (1–2 lines each).\n"
            f"2. Identify the 2–3 best options based on cost, location, and suitability.\n"
            f"3. Present those options to the developer clearly with their price.\n"
            f"4. Ask the user to choose ONE option or say 'none'.\n\n"
            f"💡 Use this format in your output:\n"
            f"---\n"
            f"💬 Summary:\n"
            f"- Kubernetes Agent: ...\n"
            f"- VM Agent: ...\n"
            f"- Serverless Agent: ...\n\n"
            f"✅ Recommended Options:\n"
            f"Option A: <description> | Monthly Price: $X\n"
            f"Option B: <description> | Monthly Price: $Y\n"
            f"Option C: <description> | Monthly Price: $Z (optional)\n\n"
        ),
        expected_output="List of 2-3 recommended options and a user prompt to select one or decline.",
        agent=agent
    )
