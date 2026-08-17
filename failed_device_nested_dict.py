results = [
    {"device": "iPhone16", "test_name": "WiFi", "status": "FAIL", "duration": 2.0},
    {"device": "iPhone16", "test_name": "WiFi", "status": "FAIL", "duration": 4.0},
    {"device": "iPhone16", "test_name": "Bluetooth", "status": "FAIL", "duration": 3.0},
    {"device": "iPhone16", "test_name": "Bluetooth", "status": "PASS", "duration": 1.0},
    {"device": "iPadPro", "test_name": "WiFi", "status": "FAIL", "duration": 5.0},
    None,
    {"device": "iPadPro", "test_name": "", "status": "FAIL", "duration": 2.0},
]


# {
#     "iPhone16": {
#         "WiFi": 3.0,
#         "Bluetooth": 3.0
#     },
#     "iPadPro": {
#         "WiFi": 5.0
#     }
# }


def average_failed_duration_by_device_and_test(results):
    failure_counts = {}
    duration_totals = {}

    for record in results:
        if not isinstance(record, dict):
            continue

        if record.get("status") != "FAIL":
            continue

        device, test_name, duration = record.get("device"), record.get("test_name"), record.get("duration")

        if not isinstance(device, str) or not device:
            continue
        if not isinstance(test_name, str) or not test_name:
            continue
        if not isinstance(duration, (int, float)):
            continue

        if device not in duration_totals:
            duration_totals[device] = {}
            failure_counts[device] = {}

        duration_totals[device][test_name] = (duration_totals[device].get(test_name, 0) + duration)
        failure_counts[device][test_name] = (failure_counts[device].get(test_name, 0) + 1)

    averages = {}
    for device in duration_totals:
        averages[device] = {}
        for test_name in duration_totals[device]:
            averages[device][test_name] = (duration_totals[device][test_name] / failure_counts[device][test_name])

    return averages

failed_duration_averages = average_failed_duration_by_device_and_test(results)
print(failed_duration_averages)