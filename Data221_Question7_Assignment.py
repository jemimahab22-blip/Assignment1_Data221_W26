def time_conversion(seconds):
    if not isinstance(seconds, int):
        return "Must be an integer"
    if seconds < 0 or seconds >= 24*3600:
        return "Seconds must be between 0 and 86399"

    hours_since_midnight= seconds//3600
    minutes_since_midnight= (seconds%60)//60
    seconds_since_midnight= seconds%60

    am_pm="AM" if hours_since_midnight <12 else "PM"#determining if the hour is AM or PM
    #returning a formatted string
    return f"{hours_since_midnight:02}:{minutes_since_midnight:02}:{seconds_since_midnight:02} {am_pm}"
print(time_conversion(0))
print(time_conversion(23193479))
print(time_conversion(81398))
print(time_conversion(-1))