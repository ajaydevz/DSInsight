from datetime import *
import pytz

india_time = pytz.timezone('asia/kolkata')
datetime_india = datetime.now(india_time)

print("indian time:",datetime_india.strftime("%H:%M:%S"))

