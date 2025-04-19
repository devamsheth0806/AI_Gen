from crewai import Task

def gather_user_requirements_task(agent, developer_input):
    return Task(
        description=(
            f"You received the following user message about their deployment needs:\n\n"
            f"\"{developer_input}\"\n\n"
            "Extract the following structured fields as a Python dictionary:\n"
            "- max_budget (float, in USD per hour)\n"
            "- location (string)\n"
            "- performance_preference (string: low, medium, high)\n"
            "- app_type (string)\n\n"
            "⚠️ Respond with ONLY a valid **Python dictionary**. Do NOT use Markdown (no triple backticks).\n"
            "⚠️ If the budget is specified as per day/week/month, evaluate it to per hour as a decimal float.\n"
            "⚠️ Do NOT return math expressions like 3.60/24 — just return 0.15.\n"
            "⚠️ No comments, no explanation, no extra text."
        ),
        expected_output="A valid Python dictionary with keys: max_budget, location, performance_preference, app_type.",
        agent=agent
    )
