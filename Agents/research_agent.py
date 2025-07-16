from crewai import Agent, LLM
from Tools.embed_papers import embed_papers
from Tools.publication_tool import fetch_publications
import os
from dotenv import load_dotenv

load_dotenv()

llm1 = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0,
    api_key= os.getenv("GEMINI_API_KEY"),
    
)

support_agent = Agent(
    role="Supporting Researcher",
    goal="Argue in support of the hypothesis using high-quality research literature.",
    backstory="You believe the hypothesis is valid and you're looking for scholarly work that supports it. Your job is to build the best possible cited case for it.",
    tools=[fetch_publications, embed_papers],
    verbose=True,
    llm=llm1
)
oppose_agent = Agent(
    role="Skeptical Researcher",
    goal="Challenge the hypothesis using credible papers that show limitations, counterexamples, or alternative explanations.",
    backstory="You are an academic contrarian. You believe all claims should be questioned and are looking to poke holes in the given hypothesis.",
    tools=[fetch_publications, embed_papers],
    verbose=True,
    llm=llm1
)
insight_agent = Agent(
    role="Research Synthesizer",
    goal="Compare opposing viewpoints and surface contradictions, gaps, or unexplored dimensions.",
    backstory="You synthesize insights by reading through competing claims and identifying where the truth breaks down or has yet to be found.",
    tools=[],
    verbose=True,
    llm=llm1
)

