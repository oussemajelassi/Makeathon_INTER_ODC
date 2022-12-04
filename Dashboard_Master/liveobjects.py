
#
# Copyright (C) Orange
#
# This software is distributed under the terms and conditions of the 'MIT'
# license which can be found in the file 'LICENSE.md' in this package distribution

import time
import LiveObjects
import datetime

# Create LiveObjects
lo = LiveObjects.Connection()

MESSAGE_RATE = 10 # publishing update every 1 minute 
Daily_message_rate = 60 * 60 * 24 

# Main program
lo.connect()		                    # Connect to LiveObjects
last = uptime = time.time()
last_day = uptime = time.time()

RealTime = datetime.datetime.now()

Total_Corrupted = 20

while True:
    

    if (time.time()) >= last + MESSAGE_RATE:
        lo.add_to_payload("TotalFaultyProduct", 11)  # Add value to payload: name - value
        lo.send_data()                         # Sending data to cloud
        last = time.time()
        lo.loop() 			    			# Check for incoming messages and if connection is still active