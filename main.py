from crew import exo_crew
from datetime import datetime

now = datetime.today()
def run(query):
    print('running for query', query)
    result = exo_crew.kickoff(inputs = {"topic": query})
    
    support_file = f'Outputs/support_{now}.txt'
    oppose_file = f'Outputs/oppose_{now}.txt'
    synthesis_file = f'Outputs/synthesis_{now}.txt'
    with open(support_file, "w") as f:
        f.write(result.tasks_output[0].raw)

    with open(oppose_file, "w") as f:
        f.write(result.tasks_output[1].raw)

    with open(synthesis_file, "w") as f:
        f.write(result.tasks_output[2].raw)
            
if __name__ == "__main__":
    run('Do transformer-based architectures outperform CNNs for vision tasks? 16-08-2025')
    
    
#sample queries to run : 1. Do foundation models show emergent reasoning?,
#                        2. Are smaller LLMs (7B and below) viable alternatives with efficient fine-tuning like QLoRA?
#                        3. Do transformer-based architectures outperform CNNs for vision tasks?