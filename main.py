import stream_adsb
from kafka import KafkaProducer

def main():

    while True:
        # Load ADSB data
        all_aircraft_states = stream_adsb.generate_OpenSky_data()
        # Get the icao24 ID of the first flight
        flight_id = str(all_aircraft_states[0].icao24)
        flight_id_bytes = bytes(flight_id, 'utf-8')
        print(flight_id_bytes)
        producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap:9092')
        producer.send('sample', flight_id_bytes)

    return None


if __name__ == "__main__" : main()