import requests
import time

def analyze_website_performance(url):
    try:
        start_time = time.time()
        
        response = requests.get(url)
        
        end_time = time.time()

        # Check if the website is up
        if response.status_code == 200:
            print(f"Website {url} is up. Response time: {end_time - start_time:.4f} seconds.")
        else:
            print(f"Website {url} returned a {response.status_code} status.")
    except requests.ConnectionError:
        print(f"Failed to connect to {url}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    url = input("Enter the URL to analyze: ")
    analyze_website_performance(url)
