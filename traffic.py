from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import os

#ijiejf

def getPilots():
    pilots = 0
    url = 'https://api2.simaware.ca/api/livedata/live.json'
    response = requests.get(url)
    for aircraft in response.json():
        pilots += 1
    return pilots

def writeEntry(pilots):
    header = ['timestamp', 'pilots']
    original = []
    with open('data.csv', "r") as current:
        reader = csv.DictReader(current, delimiter=',')
        for row in reader:
            original.append(row)
    print(original)

    with open("temp.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        new = original
        new.append({
            'timestamp': str(datetime.now()),
            'pilots': pilots
        })
        print(new)
        for row in new:
            writer.writerow(row)
    
    try:
        os.remove("data.csv")
        os.rename("temp.csv", "data.csv")
    except FileNotFoundError as e:
        print(e)

def run():
    print("Scraping Vatsim stats...")
    pilots = getPilots()
    print("Pilots online:", pilots)
    writeEntry(pilots)
    print("CSV updated at", datetime.now())

if __name__ == "__main__":
    run()
