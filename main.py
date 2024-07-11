from smbus import SMBus
import time
import logging

# Initialisiere den I2C-Bus
bus = SMBus(1)
slave = 0x8

# Konfiguriere das Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_i2c():
    try:
        data = bus.read_i2c_block_data(slave, 0, 4)
        if len(data) >= 2:
            i2c_values = [chr(data[0]), chr(data[1])]
            return i2c_values
        else:
            logging.error("Unerwartetes Datenformat vom I2C-Bus.")
            return None
    except IOError:
        logging.error("Verbindung zum Bus fehlgeschlagen")
        return None
    except Exception as e:
        logging.error(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return None

def main():
    while True:
        bus_data = read_i2c()
        if bus_data is not None:
            line = bus_data[0]
            try:
                weight = float(bus_data[1])
                logging.info(f"Bus Line {line} weighs {weight:.2f}")
            except ValueError:
                logging.error("Fehler bei der Umwandlung der Gewichtsdaten.")
        time.sleep(1)

if __name__ == "__main__":
    main()
