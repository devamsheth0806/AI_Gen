from crew import fetch_initial_crew, fetch_crew, fetch_recommendation_crew
import asyncio
from tasks.masumi_payment import pay

async def main():
    requirements = fetch_initial_crew().kickoff()
    summary = fetch_crew(requirements).kickoff()
    recommendations = fetch_recommendation_crew(summary, requirements).kickoff()
    print("\n✅ Recommendation:\n", recommendations)

    selected_option = input("\n👉 Please choose one of the options (A, B, C) or type 'none' to cancel:\n").strip().lower()
    if selected_option.upper() in ['A', 'B', 'C']:
        await pay(recommendations.json(), selected_option)
    else:
        print("❌ No payment triggered. Exiting.")

if __name__ == "__main__":
    asyncio.run(main())

