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
from tasks.summarize import summarize_task
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")




llm = ChatOpenAI(model="gpt-4")  

customer = get_customer_agent(llm)
k8s = get_k8s_agent(llm)
vm = get_vm_agent(llm)
serverless = get_serverless_agent(llm)

crew = Crew(
    agents=[k8s, vm, serverless, customer],
    tasks=[
        assess_k8s_task(k8s),
        assess_vm_task(vm),
        assess_serverless_task(serverless),
        summarize_task(customer)
    ]
)
