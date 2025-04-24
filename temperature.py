import csv

# Dictionary of temperature data for each station
years = {}
stations = {}

# Load data
for year in range(1987, 2005):
    with open(f'temperature_data/stations_group_{year}.csv') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header
        years[year] = {row[0]: list(map(float, row[4:])) for row in reader}

# Combine data by station across all years
for year, data in years.items():
    for station, temps in data.items():
        if station not in stations:
            stations[station] = []
        stations[station].extend(temps)

#  Calculate average temperature for each month across all years
monthly_averages = [0] * 12
for station_temps in stations.values():
    for i in range(12):
        monthly_averages[i] += station_temps[i]
monthly_averages = [round(total / len(stations), 2) for total in monthly_averages]

# Save monthly averages to file
with open('average_temp.txt', 'w') as f:
    f.write("Monthly Average Temperatures:\n")
    f.write("\n".join([f"Month {i + 1}: {avg}" for i, avg in enumerate(monthly_averages)]))

#  Calculate average temperatures for each season
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
with open('average_temp.txt', 'a') as f:
    f.write("\n\nSeasonal Average Temperatures:\n")
    for season, avg in season_averages.items():
        f.write(f"{season}: {avg}\n")

#  Find station with the largest temperature range
largest_range_station = max(
    stations.items(), key=lambda x: max(x[1]) - min(x[1])
)
largest_range = round(max(largest_range_station[1]) - min(largest_range_station[1]), 2)

# Save largest range station to file
with open('largest_temp_range_station.txt', 'w') as f:
    f.write(f"Station with Largest Temperature Range:\n")
    f.write(f"{largest_range_station[0]}: {largest_range}\n")

# 4. Find the warmest and coolest stations
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
