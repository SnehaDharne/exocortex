from crewai import Task
from Tools.embed_papers import embed_papers
from Tools.publication_tool import fetch_publications
from Agents.research_agent import support_agent, oppose_agent, insight_agent

support_task = Task(
    description="""
    You support the hypothesis in the user's question.
    Step 1: Rewrite {topic} into a search query that finds **supportive** literature published before the given date.
    Step 2: Use fetch_publications to find relevant papers.
    Step 3: Embed the abstracts.
    Step 4: Summarize the **evidence** supporting the claim. Cite papers directly.
    """,
    agent=support_agent,
    expected_output="summarization of the evidence supporting the claim, cited papers",
    input_keys=["topic"],
    expected_output_key = "support_view",
    tools=[fetch_publications, embed_papers]
)
oppose_task = Task(
    description="""
    You are skeptical of the hypothesis. Your goal is to find literature that **contradicts or questions** the claim in {topic}.
    Step 1: Rewrite the query to explore **counter-evidence**.
    Step 2: Use fetch_publications to find those papers.
    Step 3: Embed the abstracts.
    Step 4: Summarize your counter-argument using citations.
    """,
    agent=oppose_agent,
    expected_output="summarization of the evidence opposing the claim, cited papers",
    input_keys=["topic"],
    expected_output_key = "oppose_view",
    tools=[fetch_publications, embed_papers]
)

deliberation_task = Task(
    description="""
    Analyze the outputs from support_view and oppose_view.
    Highlight where the evidence **conflicts**, where it **aligns**, and what remains **uncertain**.
    If both views rely on different datasets, benchmarks, or assumptions — surface that.
    Conclude with a **conflict insight** and suggest next experiment.
    """,
    agent=insight_agent,
    expected_output = "summarization of output from both agents, highlighting conflicts and gap for research",
    input_keys=["support_view", "oppose_view"]
)
