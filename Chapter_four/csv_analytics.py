# ==================================
#          C S V
# ==================================

import csv

earthquake_records = [
    ["timestamp", "location", "magnitude", "depth_km"],
    ["2015-04-25 11:56", "Mars", 7.8, 15.0],
    ["2015-05-12 12:50", "Earth", 7.3, 15.0],
    ["2023-11-03 23:47", "Jupiter", 6.4, 12.0],
    ["2025-08-14 04:12", "Sun", 5.2, 10.0],
    ["2026-02-19 18:33", "Japan", 4.8, 11.5]
]

# ------------------------------------------------------------------------------
# STEP 1: WRITING TO A CSV FILE
# ------------------------------------------------------------------------------
print("--- Writing Tabular Data to Disk ---")

with open("seismic_activity.csv", "w") as csv_file:
    # Create a specialized writer object linked to our open file stream
    writer = csv.writer(csv_file)

    writer.writerows(earthquake_records)

print("Saved! 'nepal_seismic_log.csv' spreadsheet array generated successfully.\n")

# ------------------------------------------------------------------------------
# STEP 2: READING & ANALYZING THE CSV DATA
# ------------------------------------------------------------------------------

print("--- Reading & Parsing Columns ---")

total_magnitude = 0.0
record_count = 0

with open("seismic_activity.csv", "r") as csv_file:
    #create a reader stream mapping pointer
    reader = csv.reader(csv_file)

    # next(reader) pulls the very first row (the headers) out of the stream 
    # This leaves only raw numeric data elements inside the loop stream!
    headers = next(reader)
    print(f"Files columns detected: {headers}")

    print("Iterating through data matrix rows")
    for row in reader:
        # Every item in a row is read as a string by default!
        # To do math, we must explicitly convert strings to floats/integers
        location = row[1]
        magnitude = float(row[2])
        depth = float(row[3])

        print(f" -> Region: {location:<15} | Mag: {magnitude:<4} | Depth: {depth}km")

        total_magnitude += magnitude
        record_count += 1

# ------------------------------------------------------------------------------
# STEP 3: DATA INSIGHT REPORT SUMMARY
# ------------------------------------------------------------------------------
print("\n--- Analytical Compute Output ---")
if record_count > 0:
    average_mag = total_magnitude / record_count
    print(f"Total events processed:     {record_count}")
    print(f"Mean Historic Magnitude:    {average_mag:.2f}")