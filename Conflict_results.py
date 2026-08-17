results = [
    {"device": "iPhone16", "test_name": "WiFi", "status": "PASS"},
    {"device": "iPhone16", "test_name": "WiFi", "status": "FAIL"},
    {"device": "iPhone16", "test_name": "Bluetooth", "status": "PASS"},
    {"device": "iPadPro", "test_name": "WiFi", "status": "PASS"},
    None,
    {"device": "", "test_name": "Battery", "status": "FAIL"},
]

def conflict_results(results):
    seen_results={}

    for record in results:
        if not isinstance(record, dict):
            continue

        device, test_name, status = record.get("device"), record.get("test_name"), record.get("status")

        if not isinstance(device, str) or not isinstance(test_name, str) or not isinstance(status, str):
            continue

        if status not in ("PASS", "FAIL"):
            continue

        if device not in seen_results:
            seen_results[device] = {}

        if test_name not in seen_results[device]:
            seen_results[device][test_name] = status
        elif seen_results[device][test_name] != status:
            return {"Conflict Found": True, "Device": device, "Test Name": test_name, "Status 1": seen_results[device][test_name], "Status 2": status}

    return {
        "Conflict Found": False
    }

find_conflict = conflict_results(results)
print(find_conflict)
        
