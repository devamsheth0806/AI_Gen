from crewai import Crew
from agents.customer_agent import get_customer_agent
from agents.k8s_expert import get_k8s_agent
from agents.vm_expert import get_vm_agent
from agents.serverless_expert import get_serverless_agent

from tasks.assess_k8s import assess_k8s_task
from tasks.assess_vm import assess_vm_task
from tasks.assess_serverless import assess_serverless_task
from tasks.summarize_recommendation import summarize_task

from openai import OpenAI
llm = OpenAI(model="gpt-4")  # or use Gemini's wrapper

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
