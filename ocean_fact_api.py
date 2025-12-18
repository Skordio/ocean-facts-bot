import requests, pprint, logging

def get_ocean_fact():
    logging.basicConfig(filename='ocean_fact_api.log', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s - %(levelname)s - %(message)s')
    error_bot_response = "Sorry, I couldn't find anything. Tell Skordio to go fix the API."
    error_log_msg = "Error fetching ocean fact."
    try:
        response = requests.get("https://oceanfacts.tropicbliss.net/api/random")
        if response.status_code == 200:
            logging.info("Successfully fetched ocean fact.")
            return response.json().get("fact", "No fact found.")
        else:
            logging.error(f"{error_log_msg} Status code: {response.status_code}")
            return error_bot_response
    except Exception as e:
        # log to file
        logging.error(f"{error_log_msg} Exception: {str(e)}")
        return error_bot_response


if __name__ == '__main__':
    print(get_ocean_fact())