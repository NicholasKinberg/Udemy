# Problem statement: Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        minutes, seconds = divmod(seconds, 60) # divmod(dividend, divider) command divides first argument by second argument to return (x, y), x = whole number quotient, y = remainder
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        years, days = divmod(days, 365)
        # this solution works better than previously designed solution because we can use one variable for hours instead of hours and hoursRemaining, which would've doubled the complexity of the program
        result = [] # results array in which to append results
        if years > 0:
            result.append(str(years) + " year" + ("s" if years > 1 else "")) # nested if-else statement in return statement to consider pluralism
        if days > 0:
            result.append(str(days) + " day" + ("s" if days > 1 else ""))
        if hours > 0:
            result.append(str(hours) + " hour" + ("s" if hours > 1 else ""))
        if minutes > 0:
            result.append(str(minutes) + " minute" + ("s" if minutes > 1 else ""))
        if seconds > 0:
            result.append(str(seconds) + " second" + ("s" if seconds > 1 else ""))
        if len(result) > 1:
            return ", ".join(result[:-1]) + " and " + result[-1] # comma joiner that begins with last element in list appends an " and " to finish by iterating backwards through array
        else:
            return result[0] # if length of result is one, just return that
################################################################################
times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now" # just another way of expressing "if seconds == 0:"

    chunks = []
    for name, secs in times:
        qty = seconds // secs # qty is 5-part variable where seconds is divided by each element in times array
        if qty:
            if qty > 1:
                name += "s" # adds an s if plural, nothing if otherwise
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs # seconds becomes a remainder variable

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0] # same logic as first solution, iterating backwards on an array but returning only one element if chunks (results) array is length one
################################################################################
def format_duration(seconds):
    if seconds == 0: return "now"
    units = ( (31536000, "year"  ), 
              (   86400, "day"   ),
              (    3600, "hour"  ),
              (      60, "minute"),
              (       1, "second") )
    ts, t = [], seconds
    for unit in units:
        u, t = divmod(t, unit[0])
        ts += ["{} {}{}".format(u, unit[1], "s" if u>1 else "")] if u != 0 else []
    return ", ".join([str(d)for d in ts[:-1]]) + (" and " if len(ts)>1 else "") + ts[-1]
################################################################################
def f(n, unit):
    return [', ', '{} {}{}'.format(n, unit, 's' if n > 1 else '')]

def format_duration(seconds):
    if not seconds: return 'now'

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    fs = []
    if years: fs.extend(f(years, 'year'))
    if days: fs.extend(f(days, 'day'))
    if hours: fs.extend(f(hours, 'hour'))
    if minutes: fs.extend(f(minutes, 'minute'))
    if seconds: fs.extend(f(seconds, 'second'))

    fs[-2] = ' and '
    fs.pop(0)
    return ''.join(fs)
################################################################################
def format_duration(s):
    dt = []
    for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'), (s+1, 'year')]:
        s, m = divmod(s, b)
        if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
    return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'
################################################################################
def format_duration(seconds):
    if seconds == 0: return 'now'
    y, seconds = divmod(seconds, 60 * 60 * 24 * 365 )
    d, seconds = divmod(seconds, 60 * 60 * 24 )
    h, seconds = divmod(seconds, 60 * 60 )
    m, seconds = divmod(seconds, 60 )
    s = seconds
    time_list = [str(x) + ' ' + y + ('s' if x > 1 else '') for x, y in zip([y,d,h,m,s], ['year','day','hour','minute','second']) if x > 0]
    return ', '.join(time_list[:-2] + [' and '.join(time_list[-2:])])
################################################################################
from datetime import timedelta
def format_duration(sec):
    timy = timedelta(seconds = sec)
    times = [timy.days//365, timy.days%365, timy.seconds//3600, timy.seconds//60 - (timy.seconds//3600)*60, timy.seconds%60]
    name = ["year", "day", "hour", "minute", "second"]
    res = []
    for x in range(0, 5):
        if times[x]:
            res.append(str(times[x]) + " " + name[x])
            if times[x] > 1:
                res[-1] += "s"
    return {
        0 : "now",
        1 : "{}",
        2 : "{} and {}",
        3 : "{}, {} and {}",
        4 : "{}, {}, {} and {}",
        5 : "{}, {}, {}, {} and {}"
      }[len(res)].format(*res)
################################################################################
from collections import OrderedDict

def format_duration(seconds):
    if(seconds == 0): return 'now'
    
    time = OrderedDict()
    
    time['years'] = seconds // 31536000
    time['days'] = seconds // 86400 % 365
    time['hours'] = seconds // 3600 % 24
    time['minutes'] = seconds // 60 % 60
    time['seconds'] = seconds % 60
    
    output = []
    
    for key in time:
        if(time[key] > 1):
            output.append(str(time[key]) + ' ' + key)
        elif (time[key] == 1):
            output.append(str(time[key]) + ' ' + key[:-1])
            
    print(output)
            
    return ", ".join(output[:-2] + [" and ".join(output[-2:])])