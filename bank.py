import wmi

def get_firmware_info():
    c = wmi.WMI()
    firmware_info = []

    for firmware in c.Win32_Firmware():
        firmware_info.append({
            'Name': firmware.Name,
            'Description': firmware.Description,
            'Version': firmware.Version,
            'Manufacturer': firmware.Manufacturer,
        })

    return firmware_info

def get_driver_info():
    c = wmi.WMI()
    driver_info = []

    for driver in c.Win32_PnPSignedDriver():
        driver_info.append({
            'Name': driver.Description,
            'DeviceID': driver.DeviceID,
            'Manufacturer': driver.Manufacturer,
            'DriverVersion': driver.DriverVersion,
            'DriverDate': driver.DriverDate,
        })

    return driver_info

# Get firmware information
firmware_info = get_firmware_info()

print("Firmware Information:")
for firmware in firmware_info:
    print(f"Name: {firmware['Name']}, Description: {firmware['Description']}, Version: {firmware['Version']}")

# Get driver information
driver_info = get_driver_info()

print("\nDriver Information:")
for driver in driver_info:
    print(f"Name: {driver['Name']}, DeviceID: {driver['DeviceID']}, Manufacturer: {driver['Manufacturer']}, Driver Version: {driver['DriverVersion']}, Driver Date: {driver['DriverDate']}")
