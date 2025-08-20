# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 01:51:40 2022

@author: yap21
"""

# sunpos.py
import math
execfile("fakegps.py")


def gmt_to_ist(gmt_time, timezone='Asia/Kolkata'):
    """
    Converts a given time in GMT format to IST format.

    Args:
        gmt_time (str): A string representing the time in the format 'HH:mm:ss'
        timezone (str): An optional parameter specifying the timezone to convert to. Defaults to 'Asia/Kolkata'.

    Returns:
        str: A string representing the time in the specified timezone in the format 'HH:mm:ss'
    """
  # Define a dictionary of timezone offsets in seconds
    timezone_offsets = {
        'GMT': 0,
        'Asia/Kolkata': 19800,  # GMT +5:30 (5.5 hours = 19800 sec)
        'US/Eastern': -18000,  # GMT -5:00
        # Add more timezone offsets as needed
    }

    # Split the input time string into hours, minutes, and seconds
    gmt_hours, gmt_minutes, gmt_seconds = map(int, gmt_time.split(':'))

    # Calculate the total number of seconds in the input time
    gmt_total_seconds = gmt_hours * 3600 + gmt_minutes * 60 + gmt_seconds

    # Calculate the time difference between GMT and the target timezone in seconds
    timezone_offset = timezone_offsets.get(timezone, 0)
  
    # Calculate the total number of seconds in the target timezone
    target_total_seconds = gmt_total_seconds + timezone_offset

    # Calculate the hours, minutes, and seconds in the target timezone
    target_hours, target_minutes = divmod(target_total_seconds, 3600)
    target_minutes, target_seconds = divmod(target_minutes, 60)

    # Format the resulting time as a string and return
    return f"{target_hours:02}:{target_minutes:02}:{target_seconds:02}"


# Convert a GMT time to IST
GPStime = gmt_to_ist(GPStime)



print("Latitude: "+latitude)
print("Latitude: "+latitude)
print("Longitude: "+longitude)
print("Satellites: " +satellites)
print("Time: "+GPStime)
parts = GPStime.split(":",2)

hour = parts[0]
#hour = int(hour)
minute =parts[1]
#minute = int(minute)
second = parts[2]
latitude = float(latitude)
longitude = float(longitude)

#print("h"+h)
#print("m"+m)
#print("s"+s)
print("----------------------")


        
        #print(buff) #debug
        #parts = buff.split(',')
#print("h"+h)
#print("m"+m)
#print("s"+s)

#from datetime import datetime
def sunpos(when, location, refraction):
# Extract the passed data
    year, month, day, hour, minute, second, timezone = when
    latitude, longitude = location
# Math typing shortcuts
    rad, deg = math.radians, math.degrees
    sin, cos, tan = math.sin, math.cos, math.tan
    asin, atan2 = math.asin, math.atan2
# Convert latitude and longitude to radians
    rlat = rad(latitude)
    rlon = rad(longitude)
    
# Decimal hour of the day at Greenwich
    greenwichtime = hour - timezone + minute / 60 + second / 3600
# Days from J2000, accurate from 1901 to 2099
    daynum = (
        367 * year
        - 7 * (year + (month + 9) // 12) // 4
        + 275 * month // 9
        + day
        - 730531.5
        + greenwichtime / 24
    )
# Mean longitude of the sun
    mean_long = daynum * 0.01720279239 + 4.894967873
# Mean anomaly of the Sun
    mean_anom = daynum * 0.01720197034 + 6.240040768
# Ecliptic longitude of the sun
    eclip_long = (
        mean_long
        + 0.03342305518 * sin(mean_anom)
        + 0.0003490658504 * sin(2 * mean_anom)
    )
# Obliquity of the ecliptic
    obliquity = 0.4090877234 - 0.000000006981317008 * daynum
# Right ascension of the sun
    rasc = atan2(cos(obliquity) * sin(eclip_long), cos(eclip_long))
# Declination of the sun
    decl = asin(sin(obliquity) * sin(eclip_long))
# Local sidereal time
    sidereal = 4.894961213 + 6.300388099 * daynum + rlon
# Hour angle of the sun
    hour_ang = sidereal - rasc
# Local elevation of the sun
    elevation = asin(sin(decl) * sin(rlat) + cos(decl) * cos(rlat) * cos(hour_ang))
# Local azimuth of the sun
    azimuth = atan2(
        -cos(decl) * cos(rlat) * sin(hour_ang),
        sin(decl) - sin(rlat) * sin(elevation),
    )
# Convert azimuth and elevation to degrees
    azimuth = into_range(deg(azimuth), 0, 360)
    elevation = into_range(deg(elevation), -180, 180)
# Refraction correction (optional)
    if refraction:
        targ = rad((elevation + (10.3 / (elevation + 5.11))))
        elevation += (1.02 / tan(targ)) / 60
# Return azimuth and elevation in degrees
    return (round(azimuth, 2), round(elevation, 2))
def into_range(x, range_min, range_max):
    shiftedx = x - range_min
    delta = range_max - range_min
    return (((shiftedx % delta) + delta) % delta) + range_min
if __name__ == "__main__":
# Close Encounters latitude, longitude
    location = (latitude, longitude)
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    #location = (23.0225, 72.5714)
# Fourth of July, 2022 at 11:20 am MDT (-6 hours)
    #when = (year,month,day,hour,minute,seconds,timezone)
    #when = (2023, 2, 24, 13, 50, 0, +5.5)
    when = (2023, 2, 24, hour, minute, second, 0)
    #when = (2023, 2, 22, h, m, s, +5.5)
   
# Get the Sun's apparent location in the sky
    azimuth, elevation = sunpos(when, location, True)
# Output the results
    print("\nWhen: ", when)
    print("Where: ", location)
    print("Azimuth: ", azimuth)
    print("Elevation: ", elevation)
    
# When:  (2022, 7, 4, 11, 20, 0, -6)
# Where:  (40.602778, -104.741667)
# Azimuth:  121.38
# Elevation:  61.91
