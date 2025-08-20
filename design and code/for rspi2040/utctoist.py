

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
ist_time = gmt_to_ist('12:00:00')
print(ist_time)  