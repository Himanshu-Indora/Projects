````markdown
# AI Travel Assistant - Multi-Agent System

A sophisticated multi-agent AI travel assistant built with LangGraph and OpenAI's GPT-4o. This system orchestrates multiple specialized agents to help users book flights, hotels, and arrange transfers.

## Features

- **Multi-Agent Architecture**: Supervisor pattern with specialized sub-agents for flights, hotels, and transfers
- **Intelligent Routing**: Automatically routes user requests to the appropriate agent
- **Interactive CLI**: User-friendly command-line interface for booking travel services
- **Mock Tools**: Simulated booking tools that can be easily replaced with real APIs
- **Conversation Memory**: Maintains conversation history for context-aware interactions

## Project Structure

```
travel_agent/
├── tools.py          # Tool definitions for flights, hotels, and transfers
├── agents.py         # Agent initialization and multi-agent orchestration
├── main.py           # CLI interface and main entry point
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variables template
└── README.md         # This file
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- OpenAI API key (get one from [OpenAI](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository or navigate to the project directory**:
   ```bash
   cd travel_agent
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_actual_api_key_here
     ```

### Running the Application

Start the interactive travel assistant:

```bash
python main.py
```

You'll be greeted with a welcome message and can start booking your travel!

## Usage Examples

### Flight Booking
```
You: I want to book a flight from London to Paris next week.

Travel Assistant: I'd be happy to help you book a flight from London to Paris! 
To search for the best options, I need a few details:

1. Departure date (in YYYY-MM-DD format)
2. Return date (if you need a round trip)
3. Any airline preferences?

You: Departing on 2025-06-10 and returning on 2025-06-17, no airline preference.

Travel Assistant: [Shows available flights with options to select]
```

### Hotel Booking
```
You: I need a hotel in Paris for 3 nights for 2 people.

Travel Assistant: Great! To find the perfect hotel in Paris, I need:

1. Check-in date (YYYY-MM-DD format)
2. Check-out date (YYYY-MM-DD format)
3. Any specific amenities or preferences?

You: Check-in on 2025-06-10 and check-out on 2025-06-13.

Travel Assistant: [Shows available hotels with pricing and ratings]
```

### Transfer Booking
```
You: I need a transfer from Paris airport to my hotel.

Travel Assistant: I can arrange that for you! Please provide:

1. Hotel name or address
2. Pickup date and time
3. Number of passengers

You: Hotel Eiffel, 2025-06-10 at 14:00, 2 passengers

Travel Assistant: [Shows available transfer options]
```

## Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface (CLI)                      │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│            Main Agent (Supervisor/Concierge)                │
│  - Routes user requests to appropriate sub-agents           │
│  - Maintains conversation context                           │
│  - Orchestrates multi-step bookings                         │
└─┬──────────────────────┬──────────────────────┬─────────────┘
  │                      │                      │
  ▼                      ▼                      ▼
┌─────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│  Flight Agent   │ │   Hotel Agent    │ │ Transfer Agent   │
├─────────────────┤ ├──────────────────┤ ├──────────────────┤
│ • search_flights│ │ • search_hotels  │ │ • search_transfers
│ • book_flight   │ │ • book_hotel     │ │ • book_transfer  │
└─────────────────┘ └──────────────────┘ └──────────────────┘
        │                   │                      │
        ▼                   ▼                      ▼
    ┌────────────────────────────────────────────────────┐
    │           Tools / External APIs                     │
    │  (Mock implementation - integrate real APIs here)   │
    └────────────────────────────────────────────────────┘
```

## Agent Descriptions

### Supervisor Agent
- Acts as the main conversational interface
- Understands user intent and requirements
- Delegates specific tasks to specialized agents
- Maintains conversation flow and context
- Aggregates results and presents options

### Flight Agent
- Handles all flight-related queries and bookings
- Collects necessary details: origin, destination, dates
- Searches available flights
- Facilitates flight selections and bookings

### Hotel Agent
- Manages hotel search and reservation
- Gathers: location, check-in/out dates, number of guests
- Searches for available hotels
- Processes hotel bookings

### Transfer Agent
- Arranges ground transportation
- Collects: pickup/dropoff locations, date, time
- Searches transfer options
- Completes transfer bookings

## Extending the System

### Adding Real API Integration

Replace the mock implementations in `tools.py` with actual API calls:

```python
@tool
def search_flights(origin: str, destination: str, departure_date: str, return_date: str = None):
    """Connect to real flight API (e.g., Amadeus, Skyscanner)"""
    # Example with Amadeus API
    api_response = amadeus.shopping.flight_offers_search.get(
        originLocationCode=origin,
        destinationLocationCode=destination,
        departureDate=departure_date,
        ...
    )
    return format_flight_results(api_response)
```

### Adding New Agent Types

To add a new agent (e.g., Restaurant Booking Agent):

1. **Create new tools** in `tools.py`
2. **Initialize the agent** in `agents.py`
3. **Update routing logic** in `route_to_agent()` method
4. **Add documentation** in this README

### Persistent Storage

Enhance conversation memory by integrating a database:

```python
from langgraph.checkpoint.sqlite import SqliteSaver

checkpointer = SqliteSaver("travel_agent_memory.db")
# Use checkpointer in agent compilation
```

## Configuration

### LLM Model Selection

The system uses `gpt-4o` by default. You can change it in `agents.py`:

```python
self.llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.7)
```

### Temperature Settings

- **Temperature 0**: Deterministic, best for structured booking queries
- **Temperature 0.5-0.7**: Balanced, good for conversational interactions
- **Temperature 1.0**: Creative, suitable for travel recommendations

## Troubleshooting

### "OPENAI_API_KEY environment variable is not set"
- Make sure your `.env` file exists and contains your API key
- Run `source venv/bin/activate` (on Windows: `venv\Scripts\activate`)

### "Module not found" errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're in the correct virtual environment

### API Rate Limiting
- OpenAI has rate limits on API calls
- Add retry logic or implement request throttling if needed

### Tool Execution Errors
- Check that tool parameters match the expected format
- Review the mock implementation for expected input/output

## Performance Tips

1. **Caching**: Cache frequently searched flights/hotels to reduce API calls
2. **Parallel Processing**: Process multiple sub-agent tasks concurrently
3. **Async Operations**: Use async/await for long-running operations
4. **Batch Requests**: Group multiple searches into single API calls

## Roadmap

- [ ] Integration with real travel APIs (Amadeus, Expedia, etc.)
- [ ] Database persistence for user profiles and booking history
- [ ] Payment processing integration
- [ ] Web UI with React/Next.js
- [ ] Mobile app support
- [ ] Multi-language support
- [ ] Travel recommendations engine
- [ ] Dynamic pricing and deals
- [ ] Group booking features

## Dependencies

- `langchain-openai`: OpenAI integration for LangChain
- `langgraph`: Graph-based agent orchestration
- `python-dotenv`: Environment variable management
- `requests`: HTTP client for API calls

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## Support

For issues or questions:
- Check the Troubleshooting section
- Review [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- Check [OpenAI API Documentation](https://platform.openai.com/docs)

## References

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [A Complete Guide to Multi-Agent Systems in LangGraph](https://pub.towardsai.net/a-complete-guide-to-multi-agent-systems-in-langgraph-network-to-supervisor-and-hierarchical-models-a0c319cff24b)

---

**Happy travels! 🌍✈️🏨**
````
