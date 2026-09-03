import json

import requests

# API endpoint URL for fetching player data
# localhost:8000/logs is the endpoint for the API that provides player data in JSON format
# Make a GET request to the API endpoint
#  # Check if the request was successful

# Parse the JSON response into a Python object
# see what fields exist

all_records = []  # Initialize an empty list to store all records
page = 1  # Initialize the page number for pagination
while True:
    # Fetch data for the current page
    response = requests.get(
        f"http://localhost:8000/logs?page={page}&page_size=50")
    response.raise_for_status()   # Check if the request was successful
    response_json = response.json()  # Parse the JSON response
    # Get the total number of pages from the response
    total_pages = response_json.get("total_pages", 1)
    data = response_json.get("data", [])  # Get the data for the current page
    print(f"Page {page} of {total_pages}")
    # Add the data from the current page to the all_records list
    all_records.extend(data)
    if page >= total_pages:  # Check if the current page is the last page
        break  # Exit the loop if all pages have been fetched
    page += 1  # Increment the page number to fetch the next page in the next iteration

valid_records = [p for p in all_records if p.get("soh_pct") is not None] # Filter out records with missing SOH values
soh_values = [p.get("soh_pct") for p in valid_records] # Extract SOH values from valid records
average_value = sum(soh_values) / len(soh_values) # Calculate the average SOH value
highest_player = max(valid_records, key=lambda p: p.get("soh_pct") or 0) # 
# Count total number of attack players
anomalies = [p for p in valid_records if p.get("soh_pct") > 100]
print(f"Anomalies found (SOH > 100%): {len(anomalies)}")
report = {
    "total_valid_records": len(valid_records),
    "average_soh": average_value,
    "highest_soh_vehicle": highest_player,
    "anomalies_count": len(anomalies),
    "anomalies": anomalies
}  # Output the results in JSON format
with open("report.json", "w") as f:
    # Write the report to a JSON file with indentation
    json.dump(report, f, indent=4)
# Print a message indicating that the report has been generated
print("Report generated and saved to report.json")
