import csv

print("Smart Biomedical Monitoring System")
print("--------------------------------")

with open("readings.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Heart Rate:", row["heart_rate"], "BPM")
        print("Temperature:", row["temperature"], "°C")
        print("SpO2:", row["spo2"], "%")
        print("--------------------------")
