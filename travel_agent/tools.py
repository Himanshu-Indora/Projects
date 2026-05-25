"""Travel booking tools for flights, hotels, and transfers."""

from typing import List, Dict, Any
from langchain_core.tools import tool


# --- Flight Tools ---
@tool
def search_flights(
    origin: str, 
    destination: str, 
    departure_date: str, 
    return_date: str = None
) -> List[Dict[str, Any]]:
    """Searches for available flights based on origin, destination, and dates.
    Returns a list of flight options with details like price, airline, and times.
    
    Args:
        origin: Departure city
        destination: Arrival city
        departure_date: Departure date (YYYY-MM-DD format)
        return_date: Return date (YYYY-MM-DD format, optional)
        
    Returns:
        List of flight options with id, airline, price, and times
    """
    print(f"Searching flights from {origin} to {destination} on {departure_date} (return: {return_date})")
    # Mock implementation
    if "paris" in destination.lower() and "london" in origin.lower():
        return [
            {
                "id": "FL001", 
                "airline": "AirFrance", 
                "price": 150, 
                "departure_time": "10:00", 
                "arrival_time": "12:00",
                "duration": "2h"
            },
            {
                "id": "FL002", 
                "airline": "British Airways", 
                "price": 160, 
                "departure_time": "11:00", 
                "arrival_time": "13:00",
                "duration": "2h"
            },
        ]
    elif "new york" in destination.lower() and "los angeles" in origin.lower():
        return [
            {
                "id": "FL003",
                "airline": "United",
                "price": 280,
                "departure_time": "08:00",
                "arrival_time": "16:30",
                "duration": "5h 30m"
            },
            {
                "id": "FL004",
                "airline": "American Airlines",
                "price": 250,
                "departure_time": "14:00",
                "arrival_time": "22:00",
                "duration": "5h 30m"
            },
        ]
    return []


@tool
def book_flight(flight_id: str, user_details: Dict[str, Any]) -> Dict[str, Any]:
    """Books a specific flight using the flight ID and user details.
    Returns booking confirmation details.
    
    Args:
        flight_id: The flight ID to book
        user_details: Dictionary with user name and email
        
    Returns:
        Booking confirmation with booking_id and status
    """
    print(f"Booking flight {flight_id} for user {user_details.get('name', 'Unknown')}")
    # Mock implementation
    return {
        "booking_id": f"BKG-{flight_id}-XYZ", 
        "status": "confirmed", 
        "flight_id": flight_id,
        "passenger_name": user_details.get("name"),
        "confirmation_sent_to": user_details.get("email")
    }


# --- Hotel Tools ---
@tool
def search_hotels(
    location: str, 
    check_in_date: str, 
    check_out_date: str, 
    guests: int = 1
) -> List[Dict[str, Any]]:
    """Searches for available hotels in a given location for specified dates and number of guests.
    Returns a list of hotel options with details like name, price, and rating.
    
    Args:
        location: Hotel location/city
        check_in_date: Check-in date (YYYY-MM-DD format)
        check_out_date: Check-out date (YYYY-MM-DD format)
        guests: Number of guests
        
    Returns:
        List of hotel options with id, name, price per night, and rating
    """
    print(f"Searching hotels in {location} from {check_in_date} to {check_out_date} for {guests} guests")
    # Mock implementation
    if "paris" in location.lower():
        return [
            {
                "id": "HTL001", 
                "name": "Hotel Eiffel", 
                "price_per_night": 200, 
                "rating": 4.5,
                "rooms_available": 5
            },
            {
                "id": "HTL002", 
                "name": "Grand Hotel Paris", 
                "price_per_night": 350, 
                "rating": 5.0,
                "rooms_available": 3
            },
        ]
    elif "new york" in location.lower():
        return [
            {
                "id": "HTL003",
                "name": "Manhattan Plaza Hotel",
                "price_per_night": 280,
                "rating": 4.3,
                "rooms_available": 8
            },
            {
                "id": "HTL004",
                "name": "Times Square Luxury Hotel",
                "price_per_night": 450,
                "rating": 4.8,
                "rooms_available": 2
            },
        ]
    return []


@tool
def book_hotel(hotel_id: str, user_details: Dict[str, Any]) -> Dict[str, Any]:
    """Books a specific hotel using the hotel ID and user details.
    Returns booking confirmation details.
    
    Args:
        hotel_id: The hotel ID to book
        user_details: Dictionary with user name, email, and stay duration
        
    Returns:
        Booking confirmation with booking_id and status
    """
    print(f"Booking hotel {hotel_id} for user {user_details.get('name', 'Unknown')}")
    # Mock implementation
    return {
        "booking_id": f"BKG-{hotel_id}-ABC", 
        "status": "confirmed", 
        "hotel_id": hotel_id,
        "guest_name": user_details.get("name"),
        "confirmation_sent_to": user_details.get("email")
    }


# --- Transfer Tools ---
@tool
def search_transfers(
    pickup_location: str, 
    dropoff_location: str, 
    date: str, 
    time: str
) -> List[Dict[str, Any]]:
    """Searches for available transfers between two locations on a specific date and time.
    Returns a list of transfer options with details like vehicle type and price.
    
    Args:
        pickup_location: Pickup location
        dropoff_location: Dropoff location
        date: Transfer date (YYYY-MM-DD format)
        time: Transfer time (HH:MM format)
        
    Returns:
        List of transfer options with id, vehicle type, and price
    """
    print(f"Searching transfers from {pickup_location} to {dropoff_location} on {date} at {time}")
    # Mock implementation
    if "airport" in pickup_location.lower() and "hotel eiffel" in dropoff_location.lower():
        return [
            {
                "id": "TRF001", 
                "vehicle": "Sedan", 
                "price": 50,
                "duration": "25 mins"
            },
            {
                "id": "TRF002", 
                "vehicle": "Van", 
                "price": 80,
                "duration": "25 mins"
            },
        ]
    elif "airport" in pickup_location.lower() and "manhattan" in dropoff_location.lower():
        return [
            {
                "id": "TRF003",
                "vehicle": "Sedan",
                "price": 65,
                "duration": "45 mins"
            },
            {
                "id": "TRF004",
                "vehicle": "Luxury SUV",
                "price": 120,
                "duration": "45 mins"
            },
        ]
    return []


@tool
def book_transfer(transfer_id: str, user_details: Dict[str, Any]) -> Dict[str, Any]:
    """Books a specific transfer using the transfer ID and user details.
    Returns booking confirmation details.
    
    Args:
        transfer_id: The transfer ID to book
        user_details: Dictionary with user name and email
        
    Returns:
        Booking confirmation with booking_id and status
    """
    print(f"Booking transfer {transfer_id} for user {user_details.get('name', 'Unknown')}")
    # Mock implementation
    return {
        "booking_id": f"BKG-{transfer_id}-DEF", 
        "status": "confirmed", 
        "transfer_id": transfer_id,
        "passenger_name": user_details.get("name"),
        "confirmation_sent_to": user_details.get("email")
    }


# Export all tools
all_tools = [
    search_flights, 
    book_flight, 
    search_hotels, 
    book_hotel, 
    search_transfers, 
    book_transfer
]
