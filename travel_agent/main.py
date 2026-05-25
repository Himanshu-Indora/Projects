"""Main entry point for the travel agent system with interactive CLI."""

import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from agents import create_travel_agent


# Load environment variables
load_dotenv()

# Verify OpenAI API key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it before running this script.")


def main():
    """Main function to run the travel agent interactive CLI."""
    
    print("\n" + "="*70)
    print("Welcome to the AI Travel Assistant!")
    print("="*70)
    print("\nI can help you with:")
    print("  • Searching and booking flights")
    print("  • Finding and booking hotels")
    print("  • Arranging transfers")
    print("\nType 'quit' or 'exit' to end the conversation.")
    print("="*70 + "\n")
    
    # Initialize the travel agent system
    travel_agent = create_travel_agent()
    conversation_history = []
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            print("\nTravel Assistant: Thank you for using the AI Travel Assistant! Have a great trip!")
            break
        
        # Skip empty inputs
        if not user_input:
            print("Travel Assistant: Please enter a message or ask for help with your travel plans.\n")
            continue
        
        # Process the message
        print("\nTravel Assistant: ", end="", flush=True)
        result = travel_agent.process_message(user_input, conversation_history)
        
        # Display response
        print(result["response"])
        print()
        
        # Update conversation history
        conversation_history.append(HumanMessage(content=user_input))
        conversation_history.append(HumanMessage(content=result["response"]))
        
        # Optional: Display routing information in debug mode
        # print(f"[Debug] Routed to: {result['agent_type']}\n")


if __name__ == "__main__":
    main()
