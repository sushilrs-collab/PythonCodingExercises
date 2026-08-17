results = [
    {"device": "iPhone16", "status": "FAIL"},
    {"device": "iPhone16", "status": "FAIL"},
    {"device": "iPadPro", "status": "FAIL"},
    {"device": "AppleWatch", "status": "FAIL"},
    {"device": "AppleWatch", "status": "FAIL"},
    {"device": "AppleWatch", "status": "FAIL"},
    {"device": "ApplePro", "status": "FAIL"},
    {"device": "Applepro", "status": "FAIL"}
]

def top_three_failures(results):
    failed_devices = {}

    for record in results:
        if not isinstance(record, dict):
            continue
        device = record.get("device")
        status = record.get("status")

        if not isinstance(device, str) or not device:
            continue
        if not isinstance(status, str) or status not in ["PASS", "FAIL"]:
            continue
        if status == "FAIL":
            failed_devices[device]= failed_devices.get(device, 0) + 1

    sorted_devices = sorted(failed_devices.items(), key=lambda item: item[1], reverse=True)

    print(sorted_devices)  # Debugging line to check the sorted devices
    
    # Sort devices by failure count and return the top three
    return sorted_devices[:3]

top_failures = top_three_failures(results)
print(top_failures)