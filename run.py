from crew import fetch_initial_crew, fetch_crew
import asyncio
from tasks.masumi_payment import pay

async def main():
    requirements = fetch_initial_crew().kickoff()
    result = fetch_crew(requirements).kickoff()
    print("\n✅ Recommendation:\n", result)

    selected_option = input("\n👉 Please choose one of the options (A, B, C) or type 'none' to cancel:\n").strip().lower()
    if selected_option in ['a', 'b', 'c']:
        await pay(result, selected_option)
    else:
        print("❌ No payment triggered. Exiting.")

if __name__ == "__main__":
    asyncio.run(main())
