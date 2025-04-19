__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from crewai import Crew
from agents.customer_agent import get_customer_agent
from agents.k8s_agent import get_k8s_agent
from agents.vm_agent import get_vm_agent
from agents.serverless_agent import get_serverless_agent

from tasks.assess_k8s import assess_k8s_task
from tasks.assess_vm import assess_vm_task
from tasks.assess_serverless import assess_serverless_task
from tasks.gather_requirements import gather_user_requirements_task
from tasks.summarize import summarize_task
from dotenv import load_dotenv
import os
import ast

from langchain_openai import ChatOpenAI

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4")  

customer = get_customer_agent(llm)

k8s = get_k8s_agent(llm)
vm = get_vm_agent(llm)
serverless = get_serverless_agent(llm)


def fetch_initial_crew():    
    # Step 1: Simulate developer input
    developer_input = input("🧑 Describe your deployment requirements:\n")

    # Step 2: Run the gather requirements task
    gather_task = gather_user_requirements_task(customer, developer_input)

    return Crew(agents=[customer], tasks=[gather_task])

def fetch_crew(requirements):
    try:
        cleaned = requirements.raw.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.strip("`").replace("python", "").strip()
        user_input = ast.literal_eval(cleaned)
    except Exception as e:
        print("❌ Could not parse structured input from agent.")
        print("⚠️ Agent returned:", requirements.raw)
        raise e

    return Crew(
        agents=[k8s, vm, serverless, customer],
        tasks=[
            assess_k8s_task(k8s, user_input),
            assess_vm_task(vm, user_input),
            assess_serverless_task(serverless, user_input),
            summarize_task(customer, user_input)
        ]
    )