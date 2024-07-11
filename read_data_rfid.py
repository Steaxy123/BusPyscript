from smbus2 import SMBus, i2c_msg
import time

bus = SMBus(1)
slave_address = 0x08  # Feste I2C-Slave-Adresse des Arduino


def read_rfid():
    try:
        # Sende Lesebefehl an den Arduino
        byte_data = [0x03]
        print(f"Sende Lesebefehl: {byte_data}")  # Debug-Ausgabe der gesendeten Daten
        write = i2c_msg.write(slave_address, byte_data)
        bus.i2c_rdwr(write)

        # Warten Sie eine Weile, um dem Arduino Zeit zu geben, die Daten zu lesen
        time.sleep(1)

        # Lesen Sie die Antwort vom Arduino
        read = i2c_msg.read(slave_address, 18)
        bus.i2c_rdwr(read)
        response = list(read)
        response_str = ''.join(chr(i) for i in response if i != 0)
        print(f"Gelesene Daten: {response_str}")

    except Exception as e:
        print(f"Fehler beim Lesen der RFID Daten: {e}")


if __name__ == "__main__":
    read_rfid()
