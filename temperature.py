#analyses temperature data collected from multiple weather stations in Australia
    # Group CAS/DAN 05
    # Group Members
    # Bipana Tripathee [SID: s388875] 
    # Elijah Balanon Cantoria [SID: s358778] 
    # Sakshi Sakshi [SID: s386993] 
    # Shreeya Regmi [SID: s390356] 

import csv

# Dictionary of temperature data for each station
years = {}
stations = {}

# Function for loading data with error handling
def load_data(year):
    try:
        with open(f'temperature_data/stations_group_{year}.csv') as f:
            reader = csv.reader(f)
            header = next(reader)  # Skip header
            return {row[0]: list(map(float, row[4:])) for row in reader}
    except FileNotFoundError:
        print(f"Error: The file for year {year} does not exist.")
        return {}
    except ValueError:
        print(f"Error: Invalid data format in file for year {year}.")
        return {}

# Input and validation for year range
def get_years():
    while True:
        try:
            start_year = int(input("Enter start year (between 1987 and 2004): "))
            end_year = int(input("Enter end year (between 1987 and 2004): "))
            if 1987 <= start_year <= 2004 and 1987 <= end_year <= 2004 and start_year <= end_year:
                return range(start_year, end_year + 1)
            else:
                print("Invalid input. Please enter years between 1987 and 2004.")
        except ValueError:
            print("Invalid input. Please enter valid integers for years.")

# Ask user for year range
years_range = get_years()

# Load data for the specified year range
for year in years_range:
    data = load_data(year)
    if data:
        years[year] = data

# Combine data by station across all years
for year, data in years.items():
    for station, temps in data.items():
        if station not in stations:
            stations[station] = []
        stations[station].extend(temps)

# Calculate average temperature for each month across all years
monthly_averages = [0] * 12
for station_temps in stations.values():
    for i in range(12):
        monthly_averages[i] += station_temps[i]
monthly_averages = [round(total / len(stations), 2) for total in monthly_averages]

# Save monthly averages to file
try:
    with open('average_temp.txt', 'w') as f:
        f.write("Monthly Average Temperatures:\n")
        f.write("\n".join([f"Month {i + 1}: {avg}" for i, avg in enumerate(monthly_averages)]))
except IOError:
    print("Error writing to 'average_temp.txt'.")

# Calculate average temperatures for each season
seasons = {
    "Summer": [11, 0, 1],  # Dec, Jan, Feb
    "Autumn": [2, 3, 4],   # Mar, Apr, May
    "Winter": [5, 6, 7],   # Jun, Jul, Aug
    "Spring": [8, 9, 10]   # Sep, Oct, Nov
}
season_averages = {}
for season, months in seasons.items():
    season_averages[season] = round(
        sum(monthly_averages[m] for m in months) / len(months), 2
    )

# Save seasonal averages to file
try:
    with open('average_temp.txt', 'a') as f:
        f.write("\n\nSeasonal Average Temperatures:\n")
        for season, avg in season_averages.items():
            f.write(f"{season}: {avg}\n")
except IOError:
    print("Error appending to 'average_temp.txt'.")

# Find station with the largest temperature range
try:
    largest_range_station = max(
        stations.items(), key=lambda x: max(x[1]) - min(x[1])
    )
    largest_range = round(max(largest_range_station[1]) - min(largest_range_station[1]), 2)

    # Save largest range station to file
    with open('largest_temp_range_station.txt', 'w') as f:
        f.write(f"Station with Largest Temperature Range:\n")
        f.write(f"{largest_range_station[0]}: {largest_range}\n")
except ValueError:
    print("Error calculating the largest temperature range.")

# Find the warmest and coolest stations
try:
    station_averages = {
        station: sum(temps) / len(temps) for station, temps in stations.items()
    }
    warmest_station = max(station_averages.items(), key=lambda x: x[1])
    coolest_station = min(station_averages.items(), key=lambda x: x[1])

    # Save warmest and coolest stations to file
    with open('warmest_and_coolest_station.txt', 'w') as f:
        f.write("Warmest Station:\n")
        f.write(f"{warmest_station[0]}: {round(warmest_station[1], 2)}\n\n")
        f.write("Coolest Station:\n")
        f.write(f"{coolest_station[0]}: {round(coolest_station[1], 2)}\n")
except ValueError:
    print("Error calculating warmest and coolest stations.")

