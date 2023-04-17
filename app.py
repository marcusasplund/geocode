"""
geocode_csv.py

This script reads a CSV file containing city and municipality names, queries the Google Geolocation API to get
latitude and longitude for each city, and writes the results to a new CSV file.

Before running the script, make sure to insert a valid Google Geolocation API key in the `api_key` variable.
"""

import csv
import requests
import random
import time

# Input CSV file
input_file = 'input.csv'

# Output CSV file
output_file = 'output.csv'

# Google Geolocation API Key
api_key = 'INSERT API KEY HERE'


def read_input_csv(file_path):
    """
    Read input CSV file and return a list of rows.

    :param file_path: str, path to the input CSV file
    :return: list, a list of dictionaries representing rows in the CSV file
    """
    try:
        with open(file_path, 'r') as input_csv:
            reader = csv.DictReader(input_csv)
            data = [row for row in reader]
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        exit()

    return data


def write_output_csv(file_path, fieldnames, data):
    """
    Write the output CSV file.

    :param file_path: str, path to the output CSV file
    :param fieldnames: list, the fieldnames for the CSV file header
    :param data: list, a list of dictionaries containing the data to write
    """
    try:
        with open(file_path, 'w', newline='') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
            writer.writeheader()

            for row in data:
                writer.writerow(row)
    except Exception as e:
        print(f"Error: {e}")


def get_lat_lng(city, municipality, api_key):
    """
    Query the Google Geolocation API and return latitude and longitude for the given city and municipality.

    :param city: str, the city name
    :param municipality: str, the municipality name
    :param api_key: str, the Google Geolocation API key
    :return: tuple, (latitude, longitude) as floats, or (0, 0) if not found
    """
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city, municipality},Sweden&key={api_key}'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: API returned error code {response.status_code}")
        return 0, 0
    response = response.json()

    if 'error_message' in response:
        print(f"Error: {response['error_message']}")
        return 0, 0

    if 'results' in response and len(response['results']) > 0:
        if 'geometry' in response['results'][0] and 'location' in response['results'][0]['geometry']:
            lat = response['results'][0]['geometry']['location']['lat']
            lng = response['results'][0]['geometry']['location']['lng']
        else:
            print(f"Error: No location data found for {city}")
            lat = 0
            lng = 0
    else:
        print(f"Error: No results found for {city}")
        lat = 0
        lng = 0

    return lat, lng


def main():
    input_data = read_input_csv(input_file)
    output_data = []

    for row in input_data:
        city = row['city']
        municipality = row['municipality']
        lat, lng = get_lat_lng(city, municipality, api_key)
        # Add the latitude and longitude to the row data
        row['lat'] = lat
        row['lng'] = lng
        output_data.append(row)

        # Add random interval between 1-3 seconds
        sleep_time = random.uniform(1, 3)
        time.sleep(sleep_time)

    # Write the output CSV file
    fieldnames = ['city', 'municipality', 'lat', 'lng']
    write_output_csv(output_file, fieldnames, output_data)


if __name__ == '__main__':
    main()
