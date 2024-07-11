from smbus import SMBus

bus = SMBus(1)
slave_address = 0x08  # Feste I2C-Slave-Adresse des Arduino

def write_rfid(block_addr, data):
    try:
        byte_data = [0x02, block_addr] + [ord(c) for c in data.ljust(16, '\0')]
        bus.write_i2c_block_data(slave_address, 0, byte_data)
        print(f"Daten gesendet: {data}")
    except Exception as e:
        print(f"Fehler beim Schreiben der RFID Daten: {e}")

if __name__ == "__main__":
    block_addr = 4  # Beispiel-Blockadresse zum Schreiben
    data_to_write = "HELLO RFID"
    write_rfid(block_addr, data_to_write)
