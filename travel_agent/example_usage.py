"""
Example usage scenarios for the travel agent system.

Run this script to see the travel agent in action without using the interactive CLI.
"""

import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from agents import create_travel_agent


# Load environment variables
load_dotenv()


def example_flight_booking():
    """Example: Flight booking scenario."""
    print("\n" + "="*70)
    print("EXAMPLE 1: Flight Booking")
    print("="*70 + "\n")
    
    agent = create_travel_agent()
    conversation = []
    
    # Scenario: User wants to book a flight
    user_message = "I want to book a flight from London to Paris next week."
    print(f"User: {user_message}")
    
    result = agent.process_message(user_message, conversation)
    print(f"Agent: {result['response']}\n")
    conversation.append(HumanMessage(content=user_message))
    
    # Follow-up: Provide dates
    user_message = "I'll be traveling on June 10th and returning June 17th."
    print(f"User: {user_message}")
    
    result = agent.process_message(user_message, conversation)
    print(f"Agent: {result['response']}\n")
    conversation.append(HumanMessage(content=user_message))
    
    # Follow-up: Select flight
    user_message = "I'll take the AirFrance flight FL001 for £150. My name is John Doe."
    print(f"User: {user_message}")
    
    result = agent.process_message(user_message, conversation)
    print(f"Agent: {result['response']}\n")


def example_hotel_booking():
    """Example: Hotel booking scenario."""
    print("\n" + "="*70)
    print("EXAMPLE 2: Hotel Booking")
    print("="*70 + "\n")
    
    agent = create_travel_agent()
    conversation = []
    
    # Scenario: User wants to book a hotel
    user_message = "I need a hotel in Paris for my trip."
    print(f"User: {user_message}")
    
    result = agent.process_message(user_message, conversation)
    print(f"Agent: {result['response']}\n")
    conversation.append(HumanMessage(content=user_message))
    
    # Follow-up: Provide hotel details
    user_message = "Check-in on June 10th, check-out on June 13th for 2 guests."
    print(f"User: {user_message}")
    
    result = agent.process_message(user_message, conversation)
    print(f"Agent: {result['response']}\n")
    conversation.append(HumanMessage(content=user_message))


def example_transfer_booking():
    """Example: Transfer booking scenario."""
    print("\n" + "="*70)
    print("EXAMPLE 3: Transfer Booking")
    print("="*70 + "\n")
    
    agent = create_travel_agent()
    conversation = []
    
    # Scenario: User wants to arrange a transfer
    user_message = "I need a transfer from Paris airport to Hotel Eiffel."
    print(f"User: {user_message}")
    
    result = agent.process_message(user_message, conversation)
    print(f"Agent: {result['response']}\n")
    conversation.append(HumanMessage(content=user_message))
    
    # Follow-up: Provide transfer details
    user_message = "June 10th at 2 PM for 2 passengers."
    print(f"User: {user_message}")
    
    result = agent.process_message(user_message, conversation)
    print(f"Agent: {result['response']}\n")
    conversation.append(HumanMessage(content=user_message))


def example_comprehensive_trip():
    """Example: Comprehensive trip planning scenario."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Comprehensive Trip Planning")
    print("="*70 + "\n")
    
    agent = create_travel_agent()
    conversation = []
    
    # Start with overall trip intent
    user_message = "I'm planning a trip to New York from Los Angeles for a week in June."
    print(f"User: {user_message}")
    
    result = agent.process_message(user_message, conversation)
    print(f"Agent: {result['response']}\n")
    print(f"[Routed to: {result['agent_type']}]\n")
    conversation.append(HumanMessage(content=user_message))
    
    # Request flight details
    user_message = "Can you help me find flights? I want to depart June 10th and return June 17th."
    print(f"User: {user_message}")
    
    result = agent.process_message(user_message, conversation)
    print(f"Agent: {result['response']}\n")
    print(f"[Routed to: {result['agent_type']}]\n")
    conversation.append(HumanMessage(content=user_message))


def run_all_examples():
    """Run all example scenarios."""
    print("\n")
    print("#"*70)
    print("# AI TRAVEL ASSISTANT - EXAMPLE USAGE SCENARIOS")
    print("#"*70)
    
    try:
        example_flight_booking()
        example_hotel_booking()
        example_transfer_booking()
        example_comprehensive_trip()
        
        print("\n" + "="*70)
        print("All examples completed successfully!")
        print("="*70 + "\n")
        print("To use the interactive CLI, run: python main.py")
        
    except Exception as e:
        print(f"\nError running examples: {str(e)}")
        print("Make sure OPENAI_API_KEY is set in your .env file")


if __name__ == "__main__":
    # Verify OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it in your .env file before running this script.")
        exit(1)
    
    run_all_examples()
