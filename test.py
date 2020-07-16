import datetime
import time

dict = {}

dict["test"] = datetime.datetime.now()
dict["test2"]["lol"] = datetime.datetime.now()
print(dict)

time.sleep(5)

dict["test2"]["lol"] = datetime.datetime.now()


print(-(dict["test"]-dict["test2"]).total_seconds())
