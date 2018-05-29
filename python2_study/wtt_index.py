import time

print time.localtime()

def getNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def getHourBeginString(timeStr=''):
    if timeStr != '':
        tstr = timeStr[0:13] + ':00:00'
    else:
        tstr = getNowTime()[0:13] + ':00:00'
    return tstr


def getHourBeginInt(timeStr = ''):
    tint = int(time.mktime(time.strptime(getHourBeginString(timeStr), '%Y-%m-%d %H:%M:%S')))
    return tint


print getNowTime()

print time.localtime(time.time())

print getHourBeginInt()

print int(time.time())
