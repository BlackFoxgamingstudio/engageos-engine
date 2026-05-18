import os
from crewai import Crew, Process
from agents.intake_agent import create_routing_agent, create_processing_agent

def main():
    print("Initializing EngageOS 5-Stage Customer Pipeline...")
    
    # Initialize agents
    router = create_routing_agent()
    processor = create_processing_agent()
    
    # Define tasks (stubs for demonstration)
    # ... task definitions ...
    
    # Form the crew
    intake_crew = Crew(
        agents=[router, processor],
        tasks=[],
        process=Process.sequential
    )
    
    print("Crew ready. Awaiting intake events.")

if __name__ == "__main__":
    main()
