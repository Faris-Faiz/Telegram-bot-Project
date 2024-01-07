from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

# Trello API Credentials
api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')

def get_board_cards(board_id, api_key, api_token):
    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    query = {
        'key': api_key,
        'token': api_token
    }
    response = requests.get(url, params=query)
    return response.json()

def get_member_username(member_id, api_key, api_token):
    url = f"https://api.trello.com/1/members/{member_id}"
    query = {
        'key': api_key,
        'token': api_token
    }
    response = requests.get(url, params=query)
    return response.json().get('username', '')

def main():
    cards = get_board_cards(board_id, api_key, api_token)
    member_ids = set()

    # Collect all unique member IDs from cards
    for card in cards:
        member_ids.update(card['idMembers'])

    # Get usernames for each member ID
    member_usernames = {member_id: get_member_username(member_id, api_key, api_token) for member_id in member_ids}

    # Display member IDs with their corresponding usernames
    for member_id, username in member_usernames.items():
        print(f"Username: {username}, Member ID: {member_id}")

if __name__ == "__main__":
    main()