import glob
import os
from datetime import date, timedelta

from scrap import start_scrap


csv_files = glob.glob('../csv/*.csv')
csv_dates = [
    date.fromisoformat(csv_file[-14:-4])
    for csv_file in csv_files
    ]
csv_last_date = max(csv_dates)

days_before_new_scrap = 2

if date.today() > csv_last_date + timedelta(days=days_before_new_scrap):
    print("new scrap running\n..........")
    #start_scrap()
    print("\nupdating the model\n..........")
    #do notebook02
    print("\nmodel evaluation\n..........")
    #do notebook03
    print("\nupdate complete\n")
else:
    print("using current data\n")