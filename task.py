# List of Dictionaries for multiple aircraft
aircraft_data = [
    {
        "Aircraft Name": "Flight A123",
        "Latitude": 37.7749,
        "Longitude": -122.4194,
        "Speed": 500,
        "Heading": 90,
        "Altitude": 35000,
        "Status": "In Flight"
    },
    {
        "Aircraft Name": "Flight B456",
        "Latitude": 40.7128,
        "Longitude": -74.0060,
        "Speed": 450,
        "Heading": 180,
        "Altitude": 30000,
        "Status": "Landed"
    },
    {
        "Aircraft Name": "Flight C789",
        "Latitude": 51.5074,
        "Longitude": -0.1278,
        "Speed": 550,
        "Heading": 270,
        "Altitude": 38000,
        "Status": "Delayed"
    }
]

# Define function
def display_flight_data(flight_list, status_filter=None):
    for aircraft in flight_list:
        # Apply the status filter if provided
        if status_filter and aircraft["Status"] != status_filter:
            continue
        print(f"Aircraft Name: {aircraft['Aircraft Name']}")
        print(f"Latitude: {aircraft['Latitude']}")
        print(f"Longitude: {aircraft['Longitude']}")
        print(f"Speed: {aircraft['Speed']} knots")
        print(f"Heading: {aircraft['Heading']}°")
        print(f"Altitude: {aircraft['Altitude']} ft")
        print(f"Status: {aircraft['Status']}")
        print("="*40)

# Display all aircraft data
print("Displaying all aircraft data:")
display_flight_data(aircraft_data)

# Display only "In Flight" aircraft data
print("Displaying only 'In Flight' aircraft data:")
display_flight_data(aircraft_data, status_filter="In Flight")

# Allow user to add new aircraft
def add_aircraft():
    name = input("Enter the Aircraft Name: ")
    latitude = float(input("Enter Latitude: "))
    longitude = float(input("Enter Longitude: "))
    speed = int(input("Enter Speed (knots): "))
    heading = int(input("Enter Heading (°): "))
    altitude = int(input("Enter Altitude (ft): "))
    status = input("Enter Status (In Flight, Landed, Delayed): ")

    new_aircraft = {
        "Aircraft Name": name,
        "Latitude": latitude,
        "Longitude": longitude,
        "Speed": speed,
        "Heading": heading,
        "Altitude": altitude,
        "Status": status
    }
    aircraft_data.append(new_aircraft)
    print("New aircraft added successfully.")

# Allow user to update the status of an aircraft
def update_status():
    name = input("Enter the Aircraft Name to update: ")
    new_status = input("Enter new status (In Flight, Landed, Delayed): ")

    for aircraft in aircraft_data:
        if aircraft["Aircraft Name"] == name:
            aircraft["Status"] = new_status
            print(f"Status of {name} updated to {new_status}.")
            return
    print("Aircraft not found.")

# Allowing user to add a new aircraft and update the status
add_aircraft()
update_status()


# Display the updated aircraft data
print("Displaying updated aircraft data:")
display_flight_data(aircraft_data)
