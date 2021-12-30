# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of 
# years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# format_duration(62)    # returns "1 minute and 2 seconds"
# format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.

# Detailed rules

# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, 
# separated by a space. The unit of time is used in plural if the integer is greater than 1.

# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be 
# written in English.

# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year 
# and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. 
# Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

def format_duration(seconds):
    if seconds == 0:
        return 'now'
    
    years = seconds//31536000
    days = (seconds%31536000)//86400
    hours = ((seconds%31536000)%86400)//3600
    minutes = (((seconds%31536000)%86400)%3600)//60
    seconds = (((seconds%31536000)%86400)%3600)%60
    
    answer = ''
    answer += f'{(str(years) + " years ") if years != 0 else ""}'
    answer += f'{(str(days) + " days ") if days != 0 else ""}'
    answer += f'{(str(hours) + " hours ") if hours != 0 else ""}'
    answer += f'{(str(minutes) + " minutes ") if minutes != 0 else ""}'
    answer += f'{(str(seconds) + " seconds ") if seconds != 0 else ""}'
    print(answer)
    
    to_filter = answer.split(' ')
    
    result = ''
    met_years = False
    met_days = False
    met_hours = False
    met_minutes = False
    for i in range(0, len(to_filter)):
        if to_filter[i] == 'years':
            met_years = True
            if years == 1:
                result += '1 year'
            else:
                result += f'{years} years'
        elif to_filter[i] == 'days':
            met_days = True
            if days == 1:
                if met_years:
                    result += ', 1 day'
                else:
                    result += '1 day'
            else:
                if met_years:
                    result += f', {days} days'
                else:
                    result += f'{days} days'
        elif to_filter[i] == 'hours':
            met_hours = True
            if hours == 1:
                if met_years or met_days:
                    result += ', 1 hour'
                else:
                    result += '1 hour'
            else:
                if met_years or met_days:
                    result += f', {hours} hours'
                else:
                    result += f'{hours} hours'
        elif to_filter[i] == 'minutes':
            met_minutes = True
            if minutes == 1:
                if met_years or met_days or met_hours:
                    result += ', 1 minute'
                else:
                    result += '1 minute'
            else:
                if met_years or met_days or met_hours:
                    result += f', {minutes} minutes'
                else:
                    result += f'{minutes} minutes'
        elif to_filter[i] == 'seconds':
            if seconds == 1:
                if met_years or met_days or met_hours or met_minutes:
                    result += ' and 1 second'
                else:
                    result += '1 second'
            else:
                if met_years or met_days or met_hours or met_minutes:
                    result += f' and {seconds} seconds'
                else:
                    result += f'{seconds} seconds'
    
    # now check if there is at least 1 'and'
    met_and = False
    for word in result.split(' '):
        if word == 'and':
            met_and = True
    
    if not met_and and len(result.split(' ')) > 2:
        filtered_result = ''
        result = result.split(' ')
        fixed = False
        for i in range(0, len(result)):
            if i == len(result)-3:
                size = len(result[i])
                filtered_result += result[i][0:size-1]
                filtered_result += f' and '
                fixed = True
                continue
            if fixed and i == len(result) - 1:
                filtered_result += result[i]
                break
            filtered_result += (result[i] + ' ')
        
        return filtered_result
                       
    return result
