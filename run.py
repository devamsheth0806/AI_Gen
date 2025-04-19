from crew import fetch_initial_crew, crew

if __name__ == "__main__":
    requirements = fetch_initial_crew().kickoff()
    result = fetch_crew(requirements).kickoff()
    print("\n✅ Final Recommendation:\n", result)
