# Geocode CSV
This script reads a CSV file containing city and municipality names, queries the Google Geolocation API to obtain the latitude and longitude for each city, and writes the results to a new CSV file.

## Prerequisites
* [Python 3.x](https://www.python.org/downloads/)
* [pip](https://pypi.org/project/pip/) or other package installer for python
* [Google Geolocation API key](https://developers.google.com/maps/documentation/geolocation/get-api-key)
## Installation
1. Clone the repository: For this step, you need [Git](https://git-scm.com/) installed.
    ```bash
    git clone https://github.com/marcusasplund/geocode.git
    ```

2. Install the required packages using the following command:

```bash
pip install -r requirements.txt
```
## Configuration
Before running the script, make sure to insert a valid [Google Geolocation API key](https://developers.google.com/maps/documentation/geolocation/get-api-key) in the api_key variable in the script:

```python
api_key = 'INSERT API KEY HERE'
```
If needed, modify the variables `city, municipality, country` so it fits your input data

## Usage
1. Prepare a CSV file named input.csv with the following columns:

* city
* municipality

## Example input:

```
city,municipality
Stockholm,Stockholm
Gothenburg,Gothenburg
Malmo,Malmo
```
2. Place the `input.csv` file in the same directory as the script.
3.Run the script using the following command:

```bash
python geocode_csv.py
```
4. The script will generate an output CSV file named output.csv in the same directory with the following columns:
* city
* municipality
* lat
* lng

## Example output:

```city,municipality,lat,lng
Stockholm,Stockholm,59.32932349999999,18.0685808
Gothenburg,Gothenburg,57.70887,11.97456
Malmo,Malmo,55.604981,13.003822
```
## Notes

* The script adds a random interval between 1-3 seconds between each API request to avoid hitting the rate limit.
* Make sure to not exceed the daily limits of the Google Geolocation API to avoid billing charges. Check the API documentation for more information on usage limits and billing.
