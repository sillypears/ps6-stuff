import csv
from pprint import pprint
import datetime as dt
import pytz
import json
import sys

class PS6(object):
    def __init__(self, day:int, time:int, dat:dt.date, entry:int, entry_unit:str, clw:str, sculpt:str, quant:int, price:int, link:str, goldbag:bool) :
        self.day = day
        self.entry_time = time
        self.date = dat
        self.entry_window = entry
        self.entry_unit = entry_unit
        self.sculpt = sculpt
        self.colorway = clw
        self.quantity = quant
        self.price = price
        self.link = link
        self.goldbag = True if goldbag == "TRUE" else False

    def to_json(self):
        return {
            'day': self.day,
            'entry_time': self.entry_time,
            'entry_unit': self.entry_unit,
            'date_day': self.date.astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d'),
            'date_time_iso': self.date.isoformat(),
            'entry_window': self.entry_window,
            'sculpt': self.sculpt,
            'colorway': self.colorway,
            'quantity': self.quantity,
            'price': self.price,
            'link': self.link,
            'goldbag': self.goldbag
        }

def main():
    PS6Caps = []
    tz = pytz.timezone('US/Pacific')

    with open (sys.argv[1], 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for x in reader:
            try:
                if x['Time (PST)'] != '':
                    temp = PS6(
                        day=int(x['Day']), 
                        time=x['Time (PST)'], 
                        dat=tz.localize(dt.datetime(year=int(x['Date'].split('/')[2]), month=int(x['Date'].split('/')[0]), day=int(x['Date'].split('/')[1]), hour=int(x['Time (PST)']) )).astimezone(pytz.timezone('UTC')),
                        entry=int(x['Entry Window'].replace('m','')),
                        entry_unit="minute" if x['Entry Window'].partition('m')[1] == 'm' else "second",
                        sculpt=x['Sculpts'], 
                        clw=x['Colorway'],
                        quant=int(x['Quantity']),
                        price=int(x['Price']),
                        link=x['Link'],
                        goldbag=x['Gold Bag']
                    )
                    PS6Caps.append(temp)
            except:
                pass
    with open('ps6.json', 'w+') as f:
        json.dump([x.to_json() for x in PS6Caps], f, indent=4)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
