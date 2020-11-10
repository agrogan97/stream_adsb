from opensky_api import OpenSkyApi
import json

'''
Module Summary:
    - Uses the OpenSky API to stream ADSB data and feeds this to a Kafka producer
Inputs:
    - None
Outputs:
    - None

Author:
    - Alex Grogan
Team:
    - 
Date:
    - 10/11/2020
'''

def generate_OpenSky_data():
    '''
    Summary:
        - Get a list of the statevectors for all the current aircraft on OpenSky
    Inputs:
        - None
    Returns:
        - all_aircraft_states
    '''

    # Instantiate the OpenSky API class
    api = OpenSkyApi()

    states_instance = api.get_states() # <-- would contain bbox to define area

    all_aircraft_states = states_instance.states

    return all_aircraft_states

def format_opensky_for_consumer(all_aircraft_states):
    '''
    Summary:
        - Take in the opensky state vectors and format them into strings, and then bytecode
    Inputs:
        - all_aircraft_states :: exact output from generate_OpenSky_data()
    Returns:
        - 
    '''

    '''
    Want a dict of form {'flight_ID' : {'lat' : lat, 'long' : long } , ... }
    '''

    my_dict = {}

    for flight in all_aircraft_states:
        my_dict[str(flight.icao24)] = { 'lat' : flight.latitude, 'lon' : flight.longitude }

    return my_dict

    

def main():

    all_aircraft_states = generate_OpenSky_data()
    format_opensky_for_consumer(all_aircraft_states)
    # print("Data loaded")

    # for my_flight in all_aircraft_states:
        # print("Name: %s | Origin: %s | Lat/Long: (%.4f, %.4f) |" % (my_flight.icao24, my_flight.origin_country, my_flight.latitude, my_flight.longitude) )

    return None


if __name__ == "__main__" : main()
