import serial
import sys
import time

def dump(serial_port, rate, filename="dump_data.csv"):
    try:
        print("[@] Opening serial connection.")
        ser = serial.Serial(serial_port, rate)
        print("[@] Serial connection established.")
        while True:
            try:
                data = ser.readline()
                with open(filename, "a+") as f:
                    data = hex(int(data,2))
                    tms = str(time.time())
                    f.write(tms + "," + data + "\r\n")
                    print("[@] Data from " + time.strftime('%d-%m-%Y %H:%M:%S', time.gmtime(float(tms)))) #debug
                    print(data) #debug
                f.close()
            except KeyboardInterrupt:
                ser.close()
                print("[@] Serial connection closed.")
                print("[@] Data saved in file " + filename)
                print("[@] Exiting program.")
                sys.exit(0)

    except serial.SerialException:
        print("[!] Could not open serial port. The port does not exsists or you have no premissions to open it (try run as root)")
        sys.exit(2)
    except serial.SerialTimeoutException:
        print("[!] Serial port timed out.")
        sys.exit(3)

if __name__ == "__main__":
    if( len(sys.argv) < 3):
        print("python3 dumper.py path baud_rate [filename]")
        sys.exit(1)
    try:
        dump(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        dump(sys.argv[1], sys.argv[2])

