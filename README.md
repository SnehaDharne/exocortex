# 🧠 Exocortex: Brain dump, but smarter
### Motivation : This project extends the concept of "exocortex" proposed in:

##  Yager, Kevin G. (2024). Towards a science exocortex. Digital Discovery, 3(10). https://doi.org/10.1039/D4DD00175K

Yager outlines a vision for augmenting scientific reasoning through AI-powered tools capable of structuring, critiquing, and accelerating research workflows. This repository serves as a proof of concept for that vision, operationalizing a system where a swarm of AI agents engage in deliberative reasoning. Specifically, every agent invoked in support of a hypothesis is paired with a counter-agent tasked with critically evaluating its claims, ensuring that conclusions arise through structured opposition rather than passive agreement.

This repo, is a step towards that idea. 
![Exocortex Diagram](assets/exocortex.png)

This prototype demonstrates the concept through a pipeline of reasoning agents. A **support agent** searches the literature for evidence in favor of a given hypothesis. An **oppose agent** then inverts the query to uncover contradictory or skeptical perspectives. Finally, a **synthesis agent** compares both outputs, identifies conflicts and research gaps, and proposes future directions or experiments to resolve ambiguity.

This deliberative pattern can be extended across the entire agentic swarm—for example:
- A data agent may construct both primary and inverse queries to identify bias in databases.
- An autonomous lab executor could test alternate procedures to ensure robustness in physical experimentation.

By embedding structured opposition into multi-agent workflows, this system moves towards the realization of a critical, reflective, and self-aware scientific exocortex.