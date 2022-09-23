# def add_time(start, duration):

    

#     new_time = ""
#     return new_time

def convert_12_to_24(time: str) -> str:
    #  format must be "HOURS:MINS PERIOD(AM/PM)"
    
    # storing the important values
    # let's use 4:23 AM as an example
    SPLIT_AT = ":"
    hours = time.split(SPLIT_AT)[0] # "4"
    # the second part would be "23 AM" so we will split again
    mins = time.split(SPLIT_AT)[1].split(" ")[0] # "23"
    period = (time[-2:-1] + time[-1]).upper() # "AM"
    int(hours) + int(mins) # just to make sure it's entered in a correct format
    
    time_24 = ""
    
    # case 1, when it's AM (morning)
    if period == "AM":
        # Special case for 12 AM, it'll just add the hours time_24 = "HOURS"
        if hours == "12":
            time_24 += "00"
        else:
            time_24 += hours
    
    # case 2, when it's PM (night)
    elif period == "PM":
        # Special case for 12 PM, it'll be the same, 12
        if hours == "12":
            time_24 += hours
        else:
            time_24 += str(int(hours) + 12)
            
    time_24 += f":{mins}"
            
    return time_24
        
def convert_24_to_12(time: str) -> str:
    
    # storing the important values
    # let's use 16:20 as an example
    SPLIT_AT = ":"
    hours = time.split(SPLIT_AT)[0] # "16"
    mins = time.split(SPLIT_AT)[1] # "23"
    int(hours) + int(mins) # just to make sure it's entered in a correct format
    
    time_12 = ""
    
    # handling special case 00:MINS which is equal to 12 AM
    if hours == "00":
        time_12 += f"12:{mins} AM"
    # handling special case 12:MINS which is equal to 12 PM
    elif hours == "12":
        time_12 += f"12:{mins} PM"
    
    else:
        # case 1 it's AM (before 12)
        if int(hours) < 12:
            time_12 += f"{hours}:{mins} AM"
        # case 2 it's PM (after 12)
        elif int(hours) > 12:
            time_12 += f"{int(hours) - 12}:{mins} PM"
            
    return time_12
    
def calculate_time(time: str) -> str:
    # time must be in 24-hours format like this "HOURS:MINS"
    # time can be more than 24 hours
    pass

print(convert_24_to_12("11:59"))