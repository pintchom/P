#internet-time-rtc-schedule-jobs-pico-w.py
import os, time, ssl, wifi, socketpool, adafruit_requests
import board
import rtc, circuitpython_schedule as schedule

clock = rtc.RTC()

wifi.radio.connect(os.getenv("WIFI_SSID"), os.getenv("WIFI_PASSWORD"))
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

url = "https://worldtimeapi.org/api/timezone/"
timezone = "America/New_York"
url = url+timezone

def get_time():
    print(f"Accessing url: {url}")
    response = requests.get(url)
    json = response.json()
    unixtime = json["unixtime"]
    raw_offset = json["raw_offset"]

    location_time = unixtime + raw_offset
    print(f"unixtime: {unixtime}, raw_offset: {raw_offset}, location_time: {location_time}")

    current_time = time.localtime(location_time)
    print(f"currentTime: {current_time}")

    printable_time = f"{current_time.tm_hour:d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"
    printable_date = f"{current_time.tm_mon:d}/{current_time.tm_mday:d}/{current_time.tm_year:02d}"
    print(f"printable_time: {printable_time}")
    print(f"printable_date: {printable_date}")

    clock.datetime = time.struct_time(current_time)

def job():
    print("A scheduled job just ran!")
    printable_time = f"{clock.datetime.tm_hour:d}:{clock.datetime.tm_min:02d}:{clock.datetime.tm_sec:02d}"
    print(f"printable_time: {printable_time}")

get_time()
schedule.every(5).seconds.do(job)
schedule.every().day.at("13:48").do(get_time)

while True:
    schedule.run_pending()
