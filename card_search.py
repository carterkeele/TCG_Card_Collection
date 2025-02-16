import requests

def fetch_card_data(card_name):
    formatted_name = card_name.lower()

    api_url = f'https://api.lorcana-api.com/cards/fetch?strict={formatted_name}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        card_data = response.json()

        if card_data:
            return card_data
        else:
            print("No Data Found")
            return None
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


card = fetch_card_data("Elsa - Snow Queen")

if card:
    print(card)


    
