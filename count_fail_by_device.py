results = [
    {"device":"iPhone16","test_name":"Bluetooth","status":"FAIL"},
    {"device":"iPhone16","test_name":"Bluetooth","status":"PASS"},
    {"device":"iPhone16","test_name":"WiFi","status":"FAIL"},
    None,
    "invalid",
    {"status":"FAIL"},
    {"device":"","status":"FAIL"},
    {"device":123,"status":"FAIL"},
    {"device":"iPadPro","status":"FAIL"},
    {"device":"AppleWatch","status":"FAILED"},
]

def count_failures_by_device(results):
    device_failures = {}

    for test_results in results:
        if not isinstance(test_results, dict):
            continue

        if test_results.get("status") != "FAIL":
            continue

        device = test_results.get("device")

        if not isinstance(device, str) or not device:
            continue

        device_failures[device] = device_failures.get(device, 0) + 1
    return device_failures

output = count_failures_by_device(results)
print(output)