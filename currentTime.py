# Python program to get current time in Indian subcontinent
from datetime import *
import pytz


tz_INDIA = pytz.timezone('Asia/Kolkata')
datetime_INDIA = datetime.now(tz_INDIA)
print("INDIAN time:", datetime_INDIA.strftime("%H:%M:%S"))
