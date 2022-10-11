def order(period, final_minutes, final_hour, e_12, var1, day,  var2='', var3=''):

    every_2 = [i for i in range(2,18)]
    every_48_48 = [i for i in range(48,10000,24)]
    every_48_72 = [i for i in range(72,10000,24)]
    #print(every_48_48)
    #print(every_48_72)

    pairs = list(zip(every_48_48, every_48_72))
    #print(pairs)

    every_day = list(zip(every_2, pairs))
    print(every_day)
    

    every_48_36 = [i for i in range(36,10000,24)]
    every_48_60 = [i for i in range(60,10000,24)]
    #print(every_48_36)
    #print(every_48_84)

    pairs_2 = list(zip(every_48_36, every_48_60))
    #print(pairs_2)

    every_day_2 = list(zip(every_2, pairs_2))
    print(every_day_2)

    if period == 'AM':
        
        if final_minutes < 60:
            dif_h = e_12 -12
            
            #print(e_12)
                
            # every day are numbers from 2-18 and range from 48,72 every 24 hours
            for i, j in every_day:
                if j[0] <= final_hour < j[1]:
                    if day:
                        return '{0}:{1:02d} {2}, {3} {4}{5}'.format(dif_h, final_minutes, var1, day, i , ' days later')
                    else: 
                        return '{0}:{1:02d} {2}, {3}{4}'.format(dif_h, final_minutes, var1, i, ' days later')
                else:
                    if day:
                        return '{0}:{1:02d} {2}, {3} {4}'.format(dif_h, final_minutes, var1, day, var2)
                    else: 
                        return '{0}:{1:02d} {2} {3}'.format(dif_h, final_minutes, var1, var2)
        
        elif 60 < final_minutes < 120:

            dif_m = final_minutes-60
            final_hour += 1
            dif_h = e_12 -12 
            #print(dif_m)
                
            for i, j in every_day:
                if j[0] <= final_hour < j[1]:    
                    if day:
                        return '{0}:{1:02d} {2}, {3} {4}{5}'.format(dif_h, dif_m, var1, day, i , ' days later')
                    else: 
                        return '{0}:{1:02d} {2}, {3}{4}'.format(dif_h, dif_m, var1, i, ' days later')
                else:
                    if day:
                        return '{0}:{1:02d} {2}, {3} {4}'.format(dif_h, dif_m, var1, day, var2)
                    else:
                        return '{0}:{1:02d} {2} {3}'.format(dif_h, dif_m, var1, var2)
    elif period == 'PM':
        
        if final_minutes < 60:
            #final_hour += 1
            dif_h = e_12 -12
            #print(final_hour)
            # every day 2  are numbers from 2-18 and range from 36,60 every 24 hours
            for i, j in every_day_2:
                if j[0] <= final_hour < j[1]:
                    if day:
                        return '{0}:{1:02d} {2}, {3} {4}{5}'.format(dif_h, final_minutes, var1, day, i , ' days later')
                    else: 
                        return '{0}:{1:02d} {2}, {3}{4}'.format(dif_h, final_minutes, var1, i, ' days later')
                else:
                    if day:
                        return '{0}:{1:02d} {2}, {3} {4}'.format(dif_h, final_minutes, var1, day, var2)
                    else: 
                        return '{0}:{1:02d} {2}{3}'.format(dif_h, final_minutes, var1, var2)
        
        elif 60 < final_minutes < 120:
            dif_m = final_minutes - 60
            final_hour += 1
            dif_h = e_12 -12
            #print(final_hour)
                
            for i, j in every_day_2:
                if j[0] <= final_hour < j[1]:    
                    if day:
                        return '{0}:{1:02d} {2}, {3} {4}{5}'.format(dif_h, dif_m, var1, day, i , ' days later')
                    else: 
                        return '{0}:{1:02d} {2}, {3}{4}'.format(dif_h, dif_m, var1, i, ' days later')
                else:
                    if day:
                        return '{0}:{1:02d} {2}, {3} {4}'.format(dif_h, dif_m, var1, day, var2)
                    else:
                        return '{0}:{1:02d} {2} {3}'.format(dif_h, dif_m, var1, var2)

def order_12_48(final_hour, final_minutes, every_12, am_pm, day, n_d=''):

    if final_minutes < 60:

        final_hour -= every_12
        

        if day:
            return '{0}:{1:02d} {2}, {3} {4}'.format(final_hour, final_minutes, am_pm , day, n_d)
        else:
            return '{0}:{1:02d} {2} {3}'.format(final_hour, final_minutes, am_pm, n_d)

    elif 60 <= final_minutes < 120:

        dif_m = final_minutes - 60
        final_hour += 1
        final_hour -= every_12
        

        if final_hour >= 12:
            if day:
                return '{0}:{1:02d} {2}, {3} {4}'.format(final_hour, dif_m, am_pm ,day, n_d)
            else:
                return '{0}:{1:02d} {2}'.format(final_hour, dif_m, am_pm, n_d)
        else:
            if day:
                return '{0}:{1:02d} {2}, {3} {4}'.format(final_hour, dif_m, am_pm ,day, n_d)
            else:
                return '{0}:{1:02d} {2} {3}'.format(final_hour, dif_m, am_pm, n_d)


def order_12(final_minutes, day, final_hour, var1, var2):

    if final_minutes < 60:
        if day:
            return '{0}:{1:02d} {2}, {3}'.format(final_hour, final_minutes, var1 , day)
        else:
            return '{0}:{1:02d} {2} {3}'.format(final_hour, final_minutes, var1)


    elif 60 <= final_minutes < 120:
        dif_m = final_minutes - 60
        final_hour += 1
        # change the am, pm to pm, am if total hours after adding 1 because of total min 
        # trespass 60, we do thi to udpate the time format
        if final_hour >= 12:
            if day:
                return '{0}:{1:02d} {2}, {3}'.format(final_hour,dif_m,var2 ,day)
            else:
                return '{0}:{1:02d} {2}'.format(final_hour,dif_m, var2)
        else:
            if day:
                return '{0}:{1:02d} {2}, {3}'.format(final_hour,dif_m,var1 ,day)
            else:
                return '{0}:{1:02d} {2}'.format(final_hour,dif_m, var1)

def add_time(start, end, day= ''):

    start_1 = start.split(' ')
    period = start_1[1]
    hour, minutes = start_1[0].split(':')
    
    hour_2, minutes_2 = end.split(':')
    
    final_hour = int(hour) + int(hour_2)
    final_minutes = int(minutes) + int(minutes_2)
    
    day = day.lower().capitalize()

    #days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    every_12 = [i for i in range(12,4993,12)]
    #print(every_12)
    #print(len(every_12))

    every_am = []
    for i in range(208):
        i = 'AM'
        every_am.append(i)
    every_pm = []
    for i in range(208):
        i = 'PM'
        every_pm.append(i)

    every_am_pm = [sub[item] for item in range(208) for sub in [every_am, every_pm]]
    #print(every_am_pm)
    every_pm_am = [sub[item] for item in range(208) for sub in [every_pm, every_am]]
    #print(every_pm_am)

    every_12_12 = [i for i in range(12,10000,12)]
    every_12_24 = [i for i in range(24,10000,12)]
    
    pairs_3 = list(zip(every_12_12, every_12_24))
   # print(len(pairs_3))

    every_day_3= list(zip(pairs_3, every_am_pm))
    #print(every_day_3)
    # print(len(every_day_3))

    every_day_4 = list(zip(pairs_3, every_pm_am))

    n_days = final_hour // 24
    n_hour = n_days * 24 
    e_12 = final_hour - n_hour


    if period == 'AM':
        
        
        if final_hour < 12:
            return order_12(final_minutes, day, final_hour, 'AM', 'PM')
                
        elif 12 <= final_hour < 24:
            return order_12_48(final_hour, final_minutes,  every_12[0], 'PM', day)
                

        elif 24 <= final_hour < 36:
            return order_12_48(final_hour, final_minutes, every_12[1], 'AM', day, n_d='(next day)')
                
        elif 36 <= final_hour < 48: 
            return order_12_48(final_hour, final_minutes, every_12[2], 'PM', day, '(next day)')

        # else:
        #     for m, n in every_day_3:
        #         if m[0] >= 48:
        #             if m[0] <= final_hour < m[1]:
        #                 return order(period, final_minutes, final_hour, e_12, n, day,var2=n_days, var3='days later')



    elif period == 'PM':
        if final_hour < 12:
                return order_12(final_minutes, day, final_hour, 'PM', 'AM')
                
        elif 12 <= final_hour < 24:
            return order_12_48(final_hour, final_minutes,  every_12[0], 'AM', day,' (next day)')
                
        elif 24 <= final_hour < 36:

            return order_12_48(final_hour, final_minutes, every_12[1], 'PM', day,' (next day)')
        
        # else:
        #     for m, n in every_day_3:
        #         if m[0] >= 48:
        #             if m[0] <= final_hour < m[1]:
        #                 return order(period, final_minutes, final_hour,  n, day, var3='days later')

if __name__ == '__main__':

    #print(add_time("3:50 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    #print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "14:30"))
    #print(add_time("11:43 PM", "24:20", "tueSday"))
    #print(add_time("6:30 AM", "205:12", 'tuesday'))