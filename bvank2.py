import winreg
import platform  # Import platform module for OS information

def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list

software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)

# Get operating system information
os_info = platform.uname()
operating_system = {
    'system': os_info.system,
    'release': os_info.release,
    'version': os_info.version,
    'machine': os_info.machine,
    'processor': os_info.processor
}

# Print operating system information
print("Operating System Information:")
for key, value in operating_system.items():
    print(f"{key.capitalize()}: {value}")

# Print installed software information
print("\nInstalled Software Information:")
for software in software_list:
    print('Name=%s, Version=%s, Publisher=%s' % (software['name'], software['version'], software['publisher']))

print('\nNumber of installed apps: %s' % len(software_list))
