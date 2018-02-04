import datetime

def greeting_on_time():
    instruction = "Type in text to get Shakespeare quotes!"
    time_rn = datetime.datetime.now()
    hour_rn = time_rn.hour
    if hour_rn >= 4 and hour_rn <= 11:
        return "Good dawning to thee, friend. " + instruction
    elif hour_rn > 11 and hour_rn <= 15:
        return "Good day at once. " + instruction
    else:
        return "Good dog-you-den all! " + instruction
