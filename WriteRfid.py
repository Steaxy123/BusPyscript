from smbus2 import SMBus, i2c_msg
import time

bus = SMBus(1)
slave_address = 0x08  # Feste I2C-Slave-Adresse des Arduino


def write_rfid(block_addr, data):
    try:
        # Befehl (0x02) und Blockadresse an den Anfang der Nachricht setzen
        byte_data = [0x02, block_addr] + [ord(c) for c in data.ljust(16, '\0')]
        print(f"Sende Daten: {byte_data}")  # Debug-Ausgabe der gesendeten Daten

        # Sende Daten an den Arduino
        write = i2c_msg.write(slave_address, byte_data)
        bus.i2c_rdwr(write)
        print(f"Daten gesendet: {data}")

        # Warten Sie eine Weile, um dem Arduino Zeit zu geben, den Tag zu erkennen und zu schreiben
        time.sleep(1)

        # Lesen Sie die Antwort vom Arduino
        read = i2c_msg.read(slave_address, 16)
        bus.i2c_rdwr(read)
        response = list(read)
        response_str = ''.join(chr(i) for i in response if i != 0)
        print(f"Antwort vom Arduino: {response_str}")

    except Exception as e:
        print(f"Fehler beim Schreiben der RFID Daten: {e}")


if __name__ == "__main__":
    block_addr = 4  # Beispiel-Blockadresse zum Schreiben
    data_to_write = "HELLO RFID"
    write_rfid(block_addr, data_to_write)
