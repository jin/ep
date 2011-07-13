#!/usr/bin/python2.7
# Requires python2.7+
# Module(s): pyserial

# Select USB port to read from
TTY = "/dev/ttyUSB0"

import sys
if sys.version_info[:2] < (2, 7):
    print "Error: Use Python 2.7 or greater"
    sys.exit()
else:
    import serial
    from serial.serialutil import SerialException
    import subprocess
    import shlex


def process_data(data):
    elements = data.split(",")
    elements.pop()
    d = {}
    d["Node"] = int(elements[0])
    d["Seq"] = int(elements[1])
    d["Batt"] = int(elements[2])
    d["Reading"] = int(elements[3])
    
    curl_post = '''curl -H "Content-Type: text/xml" -d "<?xml version='1.0' encoding='utf-8'?><node><reading>%d</reading></node>" http://localhost:8000/live/1/%d/''' % (d["Reading"], d["Node"])
    return curl_post 


def main():
    #try:
        #subprocess.call(["stty", "-F", TTY, "38400"])
        #print subprocess.check_output(["stty", "-F", TTY])
    #except subprocess.CalledProcessError:
        #print "Error: Cannot configure " + TTY + ", please check your selected device."
        #sys.exit()
    
    try:
        s = serial.Serial(TTY, 38400)
        print "Connected to " + TTY
    except SerialException:
        print "Cannot connect to " + TTY
        sys.exit()

    while True:
        try:
            data = s.readline()
            args = shlex.split(process_data(data))
            subprocess.Popen(args)

        except:
            break

    s.close()


if __name__ == "__main__":
    main()
