from crewai import Task

def gather_user_requirements_task(agent, raw_input):
    return Task(
        description=(
            f"You received the following user message about their deployment needs:\n\n"
            f"\"{raw_input}\"\n\n"
            f"Extract key requirements as structured keywords such as: max_budget, location, performance_preference, app_type."
        ),
        expected_output="A Python-style dictionary containing extracted constraints.",
        agent=agent
    )