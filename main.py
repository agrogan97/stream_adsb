import stream_adsb
from kafka import KafkaProducer

def main():

    while True:
        # Load ADSB data
        all_aircraft_states = stream_adsb.generate_OpenSky_data()
        # Get the icao24 ID of the first flight
        flight_id = all_aircraft_states[0].icao24
        print(flight_id)
        producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap:9092')
        producer.send('sample', flight_id)
        # producer.send('sample', key=b'message-two', value=b'Message Sent')
        # print("Success")

    return None


if __name__ == "__main__" : main()