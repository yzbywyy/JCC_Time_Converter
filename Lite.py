# 这是汪越洋开发的危机联动计时工具，版权所有，仅供获得授权者使用。

import datetime
import time


def init():
    print("这是BIMUN2023的危机联动系统两委员会时间轴换算工具，仅供得到开发者允许的用户使用！")
    print("每一次输入完成后请按“Enter”键。")
    timeList = list(map(str, input(
        "请输入会议开始的会议次元GMT +0时间，依次为年、月、日、时、分，相互之间空一格：").split()))
    # 范例：“1956 10 24 14 0”
    time_str = timeStr(timeList)
    ratio = int(input("请输入时间轴换算比例："))
    return [ratio, time_str]


def timeStr(timeList):
    time_str = timeList[0]
    for i in timeList[1:3]:
        time_str = time_str + "/" + i
    time_str = time_str + " " + timeList[3] + ":" + timeList[4] + ":00"
    return time_str
    # 将列表[Y,M,D,h,m]转换为字符串“Y/M/D h:m:00”。


def timeStamp(deal_time):
    dateTime_p = datetime.datetime.strptime(deal_time, '%Y/%m/%d %H:%M:%S')
    metTime = dateTime_p - datetime.datetime(1970, 1, 1)
    date_tample = metTime.days * 24 * 3600 + metTime.seconds
    return date_tample
    # 读取时间，转换成时间戳形式。这样写是为了兼容1970年1月1日之前的时间。


def timeConvert(deal_timeStamp, difference):
    output_timeStamp = deal_timeStamp + difference * 3600
    return output_timeStamp
    # 换算时差，由于时间戳是距离1970年1月1日0时的秒数，所以每差一小时需差3600秒。理论上兼容半时区，即difference可为0.5的倍数，但是未经测试。


def timeOut(deal_timeStamp):
    timeStr = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=deal_timeStamp)
    return timeStr
    # 转换为字符串方便输出。


area = {'-4': '美国东海岸', '+0': '格林尼治', '+1': '巴黎/布达佩斯', '+2': '开罗/特拉维夫', '+3': '莫斯科'}
# 这里可以自定义需要计量的时间。
Space = {'-4': '      ', '+0': '        ', '+1': '   ', '+2': '   ', '+3': '          '}
# 为显示美观起见，留出空格，可自行处理，也可增加函数计算空格数量。
time_und_ratio = init()
global ratio
ratio = time_und_ratio[0]
timeGMT = time_und_ratio[1]
time_stamp = timeStamp(timeGMT)
# 初始化计时。

while True:
    timeNow = time.time()
    # 读取现在的北京时间。
    timePast = timeNow
    timeGone = timeNow - timePast
    while timeGone < 60:
        time.sleep(0.1)
        timePast = time.time()
        timeGone = timePast - timeNow
        # 这里计算时间是否经过一分钟，如果没有就休眠0.1秒再确认。
    time_stamp += 60 * ratio
    # 如果经过一分钟，给计时的时间戳加上60乘时间轴比例。
    print("\n")
    print(time.strftime("当前现实次元北京时间：            GMT +8 %Y-%m-%d %X\n", time.localtime()))
    # 空格同上。
    for difference in ['-4', '+0', '+1', '+2', '+3']:
        # 时差可自行修改。
        diff = int(difference)
        timeOutput = timeOut(timeConvert(time_stamp, diff))
        location = area[difference]
        # 读取地名。
        space = Space[difference]
        # 同上。
        print("当前会议次元%s时间：%sGMT %s %s" % (location, space, difference, timeOutput))
    print("\n")
    # 输出结果。
