from smbus import SMBus

bus = SMBus(1)
slave_address = 0x08

def write_rfid(data):
    try:
        byte_data = [ord(c) for c in data]
        bus.write_i2c_block_data(slave_address, 0, byte_data)
        print(f"Daten gesendet: {data}")
    except Exception as e:
        print(f"Fehler beim Schreiben der RFID Daten: {e}")

if __name__ == "__main__":
    data_to_write = "HELLO RFID"
    write_rfid(data_to_write)
