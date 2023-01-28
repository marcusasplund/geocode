import csv
import requests
import random
import time

# Input CSV file
input_file = 'input.csv'

# Output CSV file
output_file = 'output.csv'

# Google Geolocation API Key
api_key = 'YOUR_API_KEY'

try:
    # Read input CSV file
    with open(input_file, 'r') as input_csv:
        reader = csv.DictReader(input_csv)
        data = [row for row in reader]
except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
    exit()

try:
    # Write output CSV file
    with open(output_file, 'w', newline='') as output_csv:
        fieldnames = ['city', 'municipality', 'lat', 'lng']
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            city = row['city']
            municipality = row['municipality']

            # Query Google Geolocation API
            url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={api_key}'
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Error: API returned error code {response.status_code}")
                continue
            response = response.json()

            if 'error_message' in response:
                print(f"Error: {response['error_message']}")
                continue

            # Extract lat and lng from API response
            lat = response['results'][0]['geometry']['location']['lat']
            lng = response['results'][0]['geometry']['location']['lng']

            # Write to output CSV file
            writer.writerow({'city': city, 'municipality': municipality, 'lat': lat, 'lng': lng})

            # Add random interval between 1-3 seconds
            sleep_time = random.uniform(1, 3)
            time.sleep(sleep_time)

except Exception as e:
    print(f"Error: {e}")

