results = [
    {"device": "iPhone16", "test_name": "WiFi", "status": "PASS"},
    {"device": "iPhone16", "test_name": "Bluetooth", "status": "PASS"},
    {"device": "iPadPro", "test_name": "WiFi", "status": "FAIL"},
    {"device": "iPadPro", "test_name": "WiFi", "status": "PASS"},
    {"device": "AppleWatch", "test_name": "Battery", "status": "PASS"},
]

def device_test_status(results):
    device_status_list = {}

    for record in results:
        if not isinstance(record, dict):
            continue

        device = record.get("device")
        status = record.get("status")

        if not isinstance(device, str) or not device:
            continue
        if status not in ["PASS", "FAIL"]:
            continue

        if device not in device_status_list:
            device_status_list[device] = status == "PASS"
        elif status == "FAIL":
            device_status_list[device] = False

    return device_status_list

test_results = device_test_status(results)
print(test_results)