from smbus import SMBus
import time

bus = SMBus(1)
slave_address = 0x08

def read_rfid():
    try:
        data = bus.read_i2c_block_data(slave_address, 0, 16)
        uid = ''.join(chr(i) for i in data if i != 0)
        if uid != "NO_TAG":
            print(f"RFID Tag UID: {uid}")
        else:
            print("Kein RFID Tag erkannt")
    except Exception as e:
        print(f"Fehler beim Lesen der RFID Daten: {e}")

def main():
    while True:
        read_rfid()
        time.sleep(1)

if __name__ == "__main__":
    main()
