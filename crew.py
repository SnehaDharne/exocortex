from crewai import Agent, Task, Crew
from Tools.publication_tool import fetch_publications
from Agents.research_agent import *
from Tasks.research_task import *


agents = [support_agent, oppose_agent, insight_agent]
tasks = [support_task, oppose_task, deliberation_task]

exo_crew = Crew(
    agents=agents,
    tasks=tasks,
    verbose=True
)
