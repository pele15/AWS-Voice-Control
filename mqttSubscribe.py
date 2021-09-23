from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
from pydub import AudioSegment
from pydub.playback import play
import sys
import configparser
import threading


topics = configparser.ConfigParser()
topics.read('topics.ini')

io.init_logging(getattr(io.LogLevel, io.LogLevel.NoLogs.name), 'stderr')
received_all_event = threading.Event()

# callback for connection intrreupt
def on_connection_interrupted(connection, error, **kwargs):
    print("Connection interrupted. error: {}".format(error))

# Callback when an interrupted connection is re-established.
def on_connection_resumed(connection, return_code, session_present, **kwargs):
    print("Connection resumed. return_code: {} session_present: {}".format(return_code, session_present))

    if return_code == mqtt.ConnectReturnCode.ACCEPTED and not session_present:
        print("Session did not persist. Resubscribing to existing topics...")
        resubscribe_future, _ = connection.resubscribe_existing_topics()

        # Cannot synchronously wait for resubscribe result because we're on the connection's event-loop thread,
        # evaluate result with a callback instead.
        resubscribe_future.add_done_callback(on_resubscribe_complete)


def on_resubscribe_complete(resubscribe_future):
        resubscribe_results = resubscribe_future.result()
        print("Resubscribe results: {}".format(resubscribe_results))

        for topic, qos in resubscribe_results['topics']:
            if qos is None:
                sys.exit("Server rejected resubscribe to topic: {}".format(topic))

def on_message_recieved(topic, payload, dup=None, qos=None, retian=None, **kwargs):
    print("Received message from topic '{}': {}".format(topic, payload))
    print("payload = ", payload)
    audio = AudioSegment.from_wav("sounds/hell-key/hello.wav")
    play(audio)

def main():
    # Spin up resources
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

    config = configparser.ConfigParser()
    config.read('config.ini')
    print(config['AWS']['endpoint'])
    mqtt_conn = mqtt_connection_builder.mtls_from_path(
        endpoint =  config['AWS']['endpoint'],
        port = int(config['AWS']['port']),
        cert_filepath = config['AWS']['cert_filepath'],
        pri_key_filepath = config['AWS']['pri_key_filepath'],
        client_bootstrap = client_bootstrap,
        ca_filepath = config['AWS']['ca_filepath'],
        on_connection_interrupted = on_connection_interrupted,
        on_connection_resumed = on_connection_resumed,
        client_id = config['AWS']['client_id'],
        clean_session = False,
        keep_alive_secs = 30,
        http_proxy_options = None
    )

    connection = mqtt_conn.connect()
    connection.result() # waits until connection is established
    print("connection established!")

    subscribe_event, packet_id = mqtt_conn.subscribe(
        topic = topics['TOPICS']['topic'],
        qos= mqtt.QoS.AT_LEAST_ONCE,
        callback=on_message_recieved
    )
    result = subscribe_event.result()
    received_all_event.wait()

main()