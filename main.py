import stream_adsb
from kafka import KafkaProducer
import random
import json

def main():

    while True:
        # Load ADSB data
        all_aircraft_states = stream_adsb.generate_OpenSky_data()
        flight_dict = stream_adsb.format_opensky_for_consumer(all_aircraft_states)

        # Encode into bytecode
        encoded_dict = json.dumps(flight_dict).encode('utf-8')

        # Get the icao24 ID of the first flight
        flight_id = str(all_aircraft_states[random.randint(0, 4)].icao24)
        # flight_id_bytes = bytes(flight_id, 'utf-8')
        # print(flight_id_bytes)
        producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap:9092')
        producer.send('adsb-data', encoded_dict)

    return None


if __name__ == "__main__" : main()