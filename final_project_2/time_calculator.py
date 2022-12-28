def add_time(time, sum, day=None):
    hour_minute, am_pm = time.split(" ")
    hour, minutes = hour_minute.split(":")
    hour = int(hour)
    minutes = int(minutes)
    sum_hour, sum_minutes = sum.split(":")
    sum_hour = int(sum_hour)
    sum_minutes = int(sum_minutes)


    final_hour = hour + sum_hour
    final_minute = minutes + sum_minutes

    if final_minute >= 60:
        hours = final_minute // 60
        final_minute -= hours * 60
        final_hour += hours

    if final_hour >= 24:
        days = final_hour // 24
        final_hour_1 = final_hour - (days * 24)
        if final_hour_1 > 12:
            final_hour_1 -= 12
        

    if 12 < final_hour < 24 and final_minute > 0:
        final_hour_1 = final_hour - 12
    
    if final_hour <= 12:
        final_hour_1 = final_hour
    
    if am_pm == "AM":
        select_am_pm = final_hour // 24
    elif am_pm == "PM":
        select_am_pm = (final_hour // 12)
        if final_hour % 24 != 0:
            select_am_pm += 1

    if am_pm == "AM":
        if final_hour >= 24:
            hour_pm = [even for even in range(100) if even % 2 == 0]
            hour_pm = [prime for prime in range(100) if prime % 2 != 0]
            
            if select_am_pm in hour_am:
                am_pm_output = "AM"
            elif select_am_pm in hour_pm:
                am_pm_output = "PM"
        
        elif final_hour < 12:
            am_pm_output = "AM"
        
        else:
            am_pm_output = "PM"
        
    elif am_pm == "PM":
        if final_hour >= 36 and final_minute > 0:
            # print(f'--{final_hour}--')
            hour_am = [even for even in range(100) if even % 2 == 0]
            hour_pm = [prime for prime in range(100) if prime % 2 != 0]
            # print(hour_am, hour_pm)
            # print(f'--{final_hour}--')
            # print(f'__{select_am_pm}__')
            if select_am_pm in hour_am:
                am_pm_output = "AM"
            elif select_am_pm in hour_pm:
                am_pm_output = "PM"

        elif final_hour < 12:
            am_pm_output = "PM"
        
        elif 12 <= final_hour < 24:
            am_pm_output = "AM"
        
        elif 24 <= final_hour < 36 and final_minute == 0:
            am_pm_output = "PM"
        

    result = f"{final_hour_1}:{final_minute:02d} {am_pm_output}"

    if am_pm == "AM":
            days = final_hour // 24
    elif am_pm == "PM":
            days = (final_hour / 24) + 1

    if not day: 
        if am_pm == "AM":
            if days < 1:
                return result
            if days >= 1 and days < 2:
                return f"{result} (next day)"
            if days >= 2:
                return f"{result} ({int(days)} days later)"

        if am_pm == "PM":
            if days < 1.5:
                return result
            if days >= 1.5 and days < 2.5:
                return f"{result} (next day)"
            if days >= 2.5:
                return f"{result} ({int(days)} days later)"

    if day:
        # print(f'--{final_hour}--')
        day = day.lower().capitalize()
        weekdays = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        day_index = weekdays.index(day)
        target_index = (day_index + int(days)) % len(weekdays)
        final_day = weekdays[target_index]

        if am_pm == "AM":
            if final_hour < 24:
                return f"{result}, {day}"

            if final_hour >= 24 and final_hour < 48:
                return f"{result}, {final_day} (next day)"

            if final_hour >= 48:
                return f"{result}, {final_day} ({int(days)} days later)"

        if am_pm == "PM":
            if final_hour < 12:
                return f"{result}, {day}"

            if final_hour >= 12 and final_hour < 36:
                return f"{result}, {final_day} (next day)"

            if final_hour >= 36:
                return f"{result}, {final_day} ({int(days)} days later)"
        
if __name__ == "__main__":

    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))
