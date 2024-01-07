# Trello Board Member Fetcher

This Python script fetches member information from a specified Trello board. It retrieves all `idMembers` for users in the Trello board, labeling them with their usernames. 

This project was done for my own personal project to send messages onto Telegram to the people assigned to my Trello boards through the use of Trello's API as well as Telegram's Bot feature, hosted on CloudFlare Workers (for free!).

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.
- You have a Trello account and have obtained your API key and token.
- You have the ID of the Trello board you want to work with.

## Installation

To install the required packages, run the following command:

```bash
pip install requests python-dotenv
```

## Configuration

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Navigate to the repository folder:**

   ```bash
   cd your-repository
   ```

3. **Set up the environment variables:**

   Create a `.env` file in the root directory of the project and add the following content:

   ```env
   TRELLO_API_KEY=your_api_key
   TRELLO_API_TOKEN=your_api_token
   TRELLO_BOARD_ID=your_board_id
   ```

   Replace `your_api_key`, `your_api_token`, and `your_board_id` with your actual Trello API key, token, and board ID.

4. **Installing required packages:**

   Run the code below in your IDE's terminal to install the required packages to make this program run properly:

   ```env
   pip install -r requirements. txt
   ```

## Usage

To run the script, use the following command:

```bash
python retrieve_idMembers_Trello.py
```

The script will output the usernames and member IDs of users assigned to cards on the specified Trello board.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under [MIT License](LICENSE).

## Contact

If you have any questions or feedback, please create a new issue on GitHub and I'll see if I can help you with your issue.
