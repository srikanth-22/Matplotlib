import datetime
import pytz

""" datetime.date"""
# d = datetime.date(2023,7,13)
# print(d)

tday = datetime.date.today()
# tdelta = datetime.timedelta(days=7)
# print(tday-tdelta)

# get no of days left fot bday
# bday = datetime.date(2023,8,23)
# till_bday = bday - tday
# print(till_bday)

"""datetime.time"""
# t = datetime.time(17,35,22,0)
# print(t)

"""datetime.datetime"""
# dt = datetime.datetime(2023,7,13,17,40,45,100000)
# print(dt)

# dt_tday = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_tday)
# print(dt_now)
# print(dt_utcnow)

""" Using pytz library"""
# dt = datetime.datetime(2023,7,13,17,57,44, )
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

# print(dt)
# print(dt_now)
# print(dt_utcnow)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)    #current UTC time with timezone aware
print(dt_utcnow)

# for tz in pytz.all_timezones:
#     print(tz)                 #all timezones
"""
Indian/Antananarivo           #indian time zones
Indian/Chagos
Indian/Christmas
Indian/Cocos
Indian/Comoro
Indian/Kerguelen
Indian/Mahe
Indian/Maldives
Indian/Mauritius
Indian/Mayotte
Indian/Reunion
"""

"""
youtube link: https://www.youtube.com/watch?v=eirjjyP2qcQ
"""