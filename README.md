# geocode with google geocoding api

A small python script that takes a csv, queries [google geocoding api](https://developers.google.com/maps/documentation/geocoding/overview) and writes a new csv with lat, lng if found.
The sleep is for throttling the requests to prevent temporary shut down.
Feel free to adjust the input and output columns to your needs. In my case, i only had a list with city names and municipalitys. You could of course use any address format. Note that country Sweden is hard coded.
