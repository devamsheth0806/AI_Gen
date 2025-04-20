from crewai import Task

def gather_user_requirements_task(agent, developer_input):
    return Task(
        description=(
            f"User input:\n\"{developer_input}\"\n\n"
            "Extract all relevant deployment requirements as a **strict JSON object**.\n"
            "Output format:\n"
            "{\n"
            "  \"max_budget\": 0.27,\n"
            "  \"location\": \"us-west\",\n"
            "  \"performance_preference\": \"high\",\n"
            "  \"app_type\": \"web\",\n"
            "  \"custom_scaling\": true,\n"
            "  ... other relevant keys\n"
            "}\n\n"
            "✅ Rules:\n"
            "- Return **only JSON**, no extra text\n"
            "- Keep numbers in decimal or integer form (no strings)\n"
            "- Use `true`/`false` for booleans\n"
            "- Omit keys that aren’t relevant\n"
            "Do NOT wrap your output in Markdown or code blocks. Return raw JSON in single line only."
        ),
        expected_output="Dynamic JSON of all relevant extracted keys",
        agent=agent
    )