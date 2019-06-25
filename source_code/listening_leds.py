import zmq
from matrix_io.proto.malos.v1 import driver_pb2,io_pb2

# connect to matrix socket
socket = zmq.Context().socket(zmq.PUSH)
socket.connect("tcp://127.0.0.1:20021")

def listening_leds():
    driver_config_proto = driver_pb2.DriverConfig()
    everloop_image = []
    for i in range(0, 35):
        led_value = io_pb2.LedValue()
        # set red brightness to 100
        led_value.blue = 20
        # append that led configuration to led container
        everloop_image.append(led_value)
    # put the image into driver
    driver_config_proto.image.led.extend(everloop_image)
    # send the configuration to the driver
    socket.send(driver_config_proto.SerializeToString())
    return None


if __name__ == "__main__":
    listening_leds()