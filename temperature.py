#Analyses temperature data collected from multiple weather stations in Australia:

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

# Load data
for year in range(1987, 2005):
    file_path = f'temperature_data/stations_group_{year}.csv'
    try:
        with open(file_path) as f:
            reader = csv.reader(f)
            header = next(reader)  # Skip header
            years[year] = {row[0]: list(map(float, row[4:])) for row in reader}
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to process {file_path}: {e}")

# Combine data by station across all years
for year, data in years.items():
    for station, temps in data.items():
        if station not in stations:
            stations[station] = []
        stations[station].extend(temps)

# Calculate average temperature for each month across all years
monthly_averages = [0] * 12
try:
    for station_temps in stations.values():
        for i in range(12):
            monthly_averages[i] += station_temps[i]
    monthly_averages = [round(total / len(stations), 2) for total in monthly_averages]
except Exception as e:
    print(f"[ERROR] Failed to calculate monthly averages: {e}")

# Save monthly averages to file
try:
    with open('average_temp.txt', 'w') as f:
        f.write("Monthly Average Temperatures:\n")
        f.write("\n".join([f"Month {i + 1}: {avg}" for i, avg in enumerate(monthly_averages)]))
except Exception as e:
    print(f"[ERROR] Failed to write average_temp.txt: {e}")

# Calculate average temperatures for each season
seasons = {
    "Summer": [11, 0, 1],
    "Autumn": [2, 3, 4],
    "Winter": [5, 6, 7],
    "Spring": [8, 9, 10]
}
season_averages = {}
try:
    for season, months in seasons.items():
        season_averages[season] = round(
            sum(monthly_averages[m] for m in months) / len(months), 2
        )
    with open('average_temp.txt', 'a') as f:
        f.write("\n\nSeasonal Average Temperatures:\n")
        for season, avg in season_averages.items():
            f.write(f"{season}: {avg}\n")
except Exception as e:
    print(f"[ERROR] Failed to calculate or write seasonal averages: {e}")

# Find station with the largest temperature range
try:
    largest_range_station = max(
        stations.items(), key=lambda x: max(x[1]) - min(x[1])
    )
    largest_range = round(max(largest_range_station[1]) - min(largest_range_station[1]), 2)

    with open('largest_temp_range_station.txt', 'w') as f:
        f.write(f"Station with Largest Temperature Range:\n")
        f.write(f"{largest_range_station[0]}: {largest_range}\n")
except Exception as e:
    print(f"[ERROR] Failed to compute or write largest temperature range: {e}")

# Find the warmest and coolest stations
try:
    station_averages = {
        station: sum(temps) / len(temps) for station, temps in stations.items()
    }
    warmest_station = max(station_averages.items(), key=lambda x: x[1])
    coolest_station = min(station_averages.items(), key=lambda x: x[1])

    with open('warmest_and_coolest_station.txt', 'w') as f:
        f.write("Warmest Station:\n")
        f.write(f"{warmest_station[0]}: {round(warmest_station[1], 2)}\n\n")
        f.write("Coolest Station:\n")
        f.write(f"{coolest_station[0]}: {round(coolest_station[1], 2)}\n")
except Exception as e:
    print(f"[ERROR] Failed to determine or write warmest/coolest stations: {e}")

