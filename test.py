input = [
    {"device": "iPhone16", "test_name": "CameraLaunch", "status": "FAIL"},
    {"device": "iPadPro", "test_name": "CameraLaunch", "status": "PASS"},
    None,
    {"device": "AppleWatch", "status": "FAIL"},
    {"device": "MacBook", "test_name": "", "status": "FAIL"},
    {"device": "AppleTV", "test_name": "WiFiConnect", "status": "FAIL"},
    "invalid record",
    {"device": "iPhone15", "test_name": 123, "status": "FAIL"},
    {"device": "iPadAir", "test_name": "WiFiConnect", "status": "FAILED"},
    {"device": "iPhone16", "test_name": "CameraLaunch", "status": "FAIL"},
]

def count_duplicates(results):

    dupe_values = {}

    for test_results in results:
        if not isinstance(test_results, dict):
            continue

        if test_results.get("status") != "FAIL":
            continue

        test_name = test_results.get("test_name")

        if not isinstance(test_name, str) or not test_name:
            continue

        dupe_values[test_name] = dupe_values.get(test_name, 0) + 1

    return dupe_values

output = count_duplicates(input)
print(output)