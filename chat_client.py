import os
import requests
import socketio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Load API config from environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:3001/api/chat")
AUTH_URL = os.getenv("AUTH_URL", "http://localhost:3001/api/auth")
USER_URL = os.getenv("USER_URL", "http://localhost:3001/api/users")           
# Global variables
token = ""
user = None  

# Initialize Socket.io client
sio = socketio.Client()

def get_current_user_id():
    if user:
        return user.get("id")
    return None

# 1. Register user
def register_user(email, password, username):
    try:
        response = requests.post(
            f"{AUTH_URL}/register",
            json={"email": email, "password": password, "username": username},
        )
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

# 2. Login user
def login_user(email, password):
    global token, user
    try:
        response = requests.post(f"{AUTH_URL}/login", json={"email": email, "password": password})
        data = response.json()

        if "token" in data:
            token = data["token"]
            user = data.get("user", {})
            print("User logged in successfully:", user)
            return token
        else:
            print("Login failed:", data)
            return None
    except requests.exceptions.JSONDecodeError:
        print("Login error: Response is not valid JSON")
    except requests.RequestException as e:
        print("Login error:", e)


# 3. Connect to WebSocket
def connect_socket():
    global sio
    if not token:
        print("Error: Cannot connect WebSocket without authentication.")
        return

    try:
        headers = {"Authorization": f"Bearer {token}"}
        sio.connect(API_BASE_URL, headers=headers, auth={"userId": user.get("id")})

        @sio.event
        def connect():
            print("Socket connected")

        @sio.on("receive_message")
        def on_receive_message(msg):
            print("New room message:", msg)

        @sio.on("receive_private_message")
        def on_receive_private_message(msg):
            print("New private message:", msg)

        @sio.on("user_status_change")
        def on_user_status_change(status):
            print("User status changed:", status)

        @sio.event
        def disconnect():
            print("Socket disconnected")

    except Exception as e:
        print("WebSocket connection error:", e)


# 4. Get chat rooms
def get_rooms():
    if not token:
        print("Error: Authentication required.")
        return []

    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{API_BASE_URL}/rooms", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error fetching chat rooms:", e)
        return []


# 5. Send message to a chat room
def send_message(room_id, content):
    if not token:
        print("Error: Authentication required.")
        return

    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(
            f"{API_BASE_URL}/rooms/{room_id}/messages",
            json={"content": content},
            headers=headers
        )
        print("Message sent:", response.json())
    except requests.RequestException as e:
        print("Send message error:", e)


# 6. Send direct message
def send_direct_message(user_id, content):
    if not token:
        print("Error: Authentication required.")
        return

    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(
            f"{API_BASE_URL}/direct/{user_id}/messages",
            json={"content": content},
            headers=headers
        )
        print("Direct message sent:", response.json())
    except requests.RequestException as e:
        print("Send direct message error:", e)


# 7. Get room messages
def get_room_messages(room_id):
    if not token:
        print("Error: Authentication required.")
        return []

    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{API_BASE_URL}/rooms/{room_id}/messages", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error fetching room messages:", e)
        return []


# 8. Get direct messages
def get_direct_messages(user_id):
    if not token:
        print("Error: Authentication required.")
        return []

    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{API_BASE_URL}/direct/{user_id}/messages", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error fetching direct messages:", e)
        return []


# 9. Get users (excluding the logged-in user)
def get_users():
    if not token:
        print("Error: Authentication required.")
        return []

    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{USER_URL}", headers=headers)
        response.raise_for_status()
        users = response.json()

        # Filter out the logged-in user
        logged_in_user_id = user.get("id")
        filtered_users = [u for u in users if u.get("id") != logged_in_user_id]

        return filtered_users
    except requests.RequestException as e:
        print("Error fetching users:", e)
        return []
