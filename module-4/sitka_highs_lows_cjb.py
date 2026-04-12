import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt
plt.ion()

#Modified the file location to the exact location of hte file
filename = 'C:/Users/joeyb/OneDrive/Desktop/New folder/csd-325/module-4/sitka_weather_2018_simple.csv'
def plot_temps(choice):
    dates, temps = [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

    # Loop through each row in the CSV file
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date) #Condition logic for highs/lows
            if choice == 'highs':
                temps.append(int(row[5]))
            elif choice == 'lows':
                temps.append(int(row[6]))

#Adding dynamic color and titles

    fig, ax = plt.subplots()
    color = 'red' if choice == 'highs' else 'blue'
    ax.plot(dates, temps, c=color)

# Format plot.
    title = "Daily high temperatures - 2018" if choice == 'highs' else "Daily Low Temperatures - 2018"
    plt.title('', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()
    plt.pause(.001)

while True:
    print("\nMenu:")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")
    choice = input("Select an option: ").lower() #menu options
    if choice in ['1', 'highs']:
        plot_temps('highs')
    elif choice in ['2', 'lows']:
        plot_temps('lows')
    elif choice in ['3', 'exit']: #exit option
        print("Exiting program. Goodbye!")
        sys.exit() #input validation
    else:
        print("Invalid choice. Please try again.")
            
