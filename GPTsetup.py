import json

def get_api_details():
    print("Welcome to SAT-Tutor!")
    print("Please provide your OpenAI Chat-GPT API details.")

    api_key = input("API Key: ")
    model_name = input("Model Name: ")

    api_details = {
        "api_key": api_key,
        "model_name": model_name
    }

    return api_details

def save_api_details(api_details):
    with open("api_details.json", "w") as file:
        json.dump(api_details, file)

def main():
    api_details = get_api_details()
    save_api_details(api_details)

    print("API details saved successfully.")

if __name__ == "__main__":
    main()
