from crewai import Task

def gather_user_requirements_task(agent, raw_input):
    return Task(
        description=(
            f"You received the following user message about their deployment needs:\n\n"
            f"\"{raw_input}\"\n\n"
            f"Extract key requirements as structured keywords including but not limited to: max_budget, location, performance_preference, app_type"
            f"Keep numeric values in numeric format, don't convert them to string."
            f"If budget is anything apart from per hour, evaluate the budget to per hour in decimals. Do not keep fraction or equation form."
            f"Do not include special characters."
            f"Do not change the keywords mentioned above."
        ),
        expected_output="A Python-style dictionary containing extracted constraints.",
        agent=agent
    )