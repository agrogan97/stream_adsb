import stream_adsb
from kafka import KafkaProducer

def main():

    while True:
        all_aircraft_states = stream_adsb.generate_OpenSky_data()
        try:
            producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap:9092')
            producer.send('sample', all_aircraft_states)
            producer.send('sample', key=b'message-two', value=b'Message Sent')
            print("Success")
        except:
            print("Failure")

    return None


if __name__ == "__main__" : main()