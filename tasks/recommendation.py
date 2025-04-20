from crewai import Task
from models.recommedation_output import RecommendationOutput
def recommend_task(agent, summary, user_input):
    return Task(
        description=(
            f"You are the Customer Agent.\n"
            f"The developer has the following requirements:\n{user_input}\n\n"
            f"You've received expert agent recommendations and summary: \n{summary}.\n\n"
            f"Your job is to identify the top 3 best options based on cost, location, and suitability. " 
            "Present those options in capital letters like A, B and C, to the developer clearly with their price. Choose specific options\n"
            f"Ask the user to choose ONE option or say 'none'.\n\n"
            "The price for each resource is in per hour. Compute its value for full month cos, that is multiply the price with 24 * 30.\n "
            f"Provide output as a JSON object, options as keys and values as JSON with technical details in description and monthly cost.\n"
            "Keep monthly cost in float. Do NOT wrap your output in Markdown or code blocks. Return raw JSON in single line only. \n"
            "Follow JSON format and no extra text: {'A': {'description':'...', 'monthly_cost': }}"
        ),
        expected_output="List of top 3 recommended options and a user prompt to select one or decline.",
        agent=agent,
        output_json=RecommendationOutput
    )
