import requests, pprint, logging

def get_ocean_fact():
    # Initialize logging
    logging.basicConfig(filename='api.log', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s - %(levelname)s - %(message)s')
    error_bot_response = "Sorry, I couldn't find anything. Tell Skordio to go fix the API."

    # Get stuff from server
    try:
        response = requests.get("https://oceanfacts.tropicbliss.net/api/random")
        if response.status_code == 200:
            logging.info("Successfully fetched ocean fact.")
            return response.json().get("fact", "No fact found.")
        else:
            logging.error(f"HTTP error fetching ocean fact. Status code: {response.status_code}\nResponse text: {response.text}")
            return error_bot_response
    except Exception as e:
        # log to file
        logging.error(f"Error fetching ocean fact. Exception: {str(e)}")
        return error_bot_response


if __name__ == '__main__':
    print(get_ocean_fact())