from datetime import datetime

# Unix timestamp of our current local time (GMT +02:00)
unix_timestamp = int((datetime.now() - datetime(1970, 1, 1)).total_seconds())

# From my current time zone to UTC there's a difference of minus 2 hours(= 7200s)
unix_timestamp_utc = unix_timestamp - 7200

# From UTC to KTC there's a difference of plus 9 hours(= 32400s)
unix_timestamp_korea = unix_timestamp_utc + 32400

print("Unix Time Stamp of current local time: ", unix_timestamp)
print("UTC Unix Time Stamp: ", unix_timestamp_utc)
print("Korean Unix Time Stamp: ", unix_timestamp_korea)

