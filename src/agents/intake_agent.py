from crewai import Agent

def create_routing_agent():
    return Agent(
        role='Intake Router',
        goal='Analyze incoming lead context from RAG and route to B2B or B2C workflows.',
        backstory='An expert triage analyst ensuring data segregation and immediate response priority.',
        verbose=True,
        allow_delegation=False
    )

def create_processing_agent():
    return Agent(
        role='Data Processor',
        goal='Extract key requirements from routed leads and update CRM schemas.',
        backstory='Meticulous data engineer specializing in unstructured-to-structured JSON parsing.',
        verbose=True
    )
