from crew import fetch_initial_crew, fetch_crew, fetch_recommendation_crew
import asyncio
from tasks.masumi_payment import pay

recommendations = None
# Gather user input and return structured summary
async def get_recommendation_summary(requirement_text: str):
    initial_crew = fetch_initial_crew(requirement_text)
    requirements = initial_crew.kickoff()

    summary_crew = fetch_crew(requirements)
    summary = summary_crew.kickoff()

    return summary, requirements

# 🧠 Step 2: Get structured recommendation options (A, B, C)
async def get_top_options(summary, requirements):
    global recommendations
    recommendation_crew = fetch_recommendation_crew(summary, requirements)
    recommendations = recommendation_crew.kickoff()
    return recommendations.json

# 🧾 Step 3: Ask user for choice & trigger payment
async def implement_selected_option(selected_option):
    global recommendations
    print("\n✅ Recommendation Options:\n", recommendations)
    selected_option = selected_option.upper()
    if selected_option in ['A', 'B', 'C']:
        await pay(recommendations.json, selected_option)
    else:
        print("❌ No payment triggered. Exiting.")

# # 🔁 Main entry point (CLI mode)
# async def main():
#     requirement_text = input("🧑 Describe your deployment requirements:\n")
#     summary, requirements = await get_recommendation_summary(requirement_text)
#     recommendations = await get_top_options(summary, requirements)
#     await implement_selected_option(recommendations)

# if __name__ == "__main__":
#     asyncio.run(main())