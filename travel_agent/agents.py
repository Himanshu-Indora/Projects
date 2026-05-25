"""Multi-agent orchestration for travel booking system."""

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage
from typing import Any

from tools import (
    search_flights,
    book_flight,
    search_hotels,
    book_hotel,
    search_transfers,
    book_transfer,
    all_tools
)


class TravelAgentSystem:
    """Main travel agent system with supervisor and sub-agents."""
    
    def __init__(self, openai_api_key: str = None):
        """Initialize the travel agent system.
        
        Args:
            openai_api_key: OpenAI API key (uses env variable if not provided)
        """
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self._initialize_agents()
    
    def _initialize_agents(self):
        """Initialize all sub-agents."""
        
        # Flight Agent
        flight_tools_info = [search_flights, book_flight]
        self.flight_agent = create_react_agent(
            llm=self.llm,
            tools=flight_tools_info,
            state_modifier=(
                "You are an expert flight booking agent. Use the provided tools to search and book flights. "
                "Always ask for all necessary details (origin, destination, departure date, return date if applicable) before searching. "
                "Present options clearly with prices, times, and airlines. "
                "Confirm booking details with the user before finalizing any booking."
            )
        )
        
        # Hotel Agent
        hotel_tools_info = [search_hotels, book_hotel]
        self.hotel_agent = create_react_agent(
            llm=self.llm,
            tools=hotel_tools_info,
            state_modifier=(
                "You are an expert hotel booking agent. Use the provided tools to search and book hotels. "
                "Always ask for all necessary details (location, check-in date, check-out date, number of guests) before searching. "
                "Present options clearly with prices, ratings, and amenities. "
                "Confirm booking details with the user before finalizing any booking."
            )
        )
        
        # Transfer Agent
        transfer_tools_info = [search_transfers, book_transfer]
        self.transfer_agent = create_react_agent(
            llm=self.llm,
            tools=transfer_tools_info,
            state_modifier=(
                "You are an expert transfer booking agent. Use the provided tools to search and book transfers. "
                "Always ask for all necessary details (pickup location, dropoff location, date, time) before searching. "
                "Present options clearly with vehicle types, prices, and durations. "
                "Confirm booking details with the user before finalizing any booking."
            )
        )
    
    def route_to_agent(self, user_message: str) -> str:
        """Route user message to appropriate agent.
        
        Args:
            user_message: The user's request
            
        Returns:
            Agent type: 'flight', 'hotel', 'transfer', or 'supervisor'
        """
        message_lower = user_message.lower()
        
        # Simple routing logic based on keywords
        if any(word in message_lower for word in ['flight', 'plane', 'airline', 'booking']):
            return 'flight'
        elif any(word in message_lower for word in ['hotel', 'accommodation', 'lodging', 'stay']):
            return 'hotel'
        elif any(word in message_lower for word in ['transfer', 'transport', 'taxi', 'pickup']):
            return 'transfer'
        else:
            return 'supervisor'
    
    def get_supervisor_response(self, messages: list) -> dict:
        """Get response from supervisor agent.
        
        Args:
            messages: Conversation history
            
        Returns:
            Agent response
        """
        supervisor_prompt = (
            "You are a helpful travel assistant supervisor. Your goal is to assist users with their travel plans. "
            "You can help book flights, hotels, and transfers. "
            "First, understand the user's overall intent and travel needs. "
            "Ask clarifying questions if needed to gather all necessary information. "
            "Guide the user through their booking journey step by step. "
            "Be friendly, helpful, and professional."
        )
        
        # Create a simple supervisor response
        state = {"messages": messages}
        response = self.llm.invoke(
            state["messages"] + [HumanMessage(content=supervisor_prompt)]
        )
        return {"response": response.content}
    
    def process_message(self, user_message: str, conversation_history: list = None) -> dict:
        """Process a user message and route to appropriate agent.
        
        Args:
            user_message: User's message
            conversation_history: Previous messages in conversation
            
        Returns:
            Dictionary with agent response and routing information
        """
        if conversation_history is None:
            conversation_history = []
        
        # Add user message to history
        messages = conversation_history + [HumanMessage(content=user_message)]
        
        # Route to appropriate agent
        agent_type = self.route_to_agent(user_message)
        
        try:
            if agent_type == 'flight':
                state = {"messages": messages}
                response = self.flight_agent.invoke(state)
                final_message = response["messages"][-1].content if response["messages"] else "No response"
            elif agent_type == 'hotel':
                state = {"messages": messages}
                response = self.hotel_agent.invoke(state)
                final_message = response["messages"][-1].content if response["messages"] else "No response"
            elif agent_type == 'transfer':
                state = {"messages": messages}
                response = self.transfer_agent.invoke(state)
                final_message = response["messages"][-1].content if response["messages"] else "No response"
            else:  # supervisor
                response = self.get_supervisor_response(messages)
                final_message = response["response"]
            
            return {
                "response": final_message,
                "agent_type": agent_type,
                "status": "success"
            }
        except Exception as e:
            return {
                "response": f"Sorry, an error occurred: {str(e)}",
                "agent_type": agent_type,
                "status": "error",
                "error": str(e)
            }


def create_travel_agent() -> TravelAgentSystem:
    """Factory function to create and return a travel agent system.
    
    Returns:
        Initialized TravelAgentSystem instance
    """
    return TravelAgentSystem()
