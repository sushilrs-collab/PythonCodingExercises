results = [
    {"device":"iPhone16","status":"FAIL","duration":2.4},
    {"device":"iPhone16","status":"PASS","duration":1.8},
    {"device":"iPhone16","status":"FAIL","duration":3.1},
    {"device":"iPadPro","status":"FAIL","duration":4.0},
    {"device":"iPadPro","status":"FAIL","duration":2.0},
    {"device":"AppleWatch","status":"PASS","duration":1.1},
]

def average_failed_duration_by_device(results):

    duration_totals = {}
    failure_counts = {}

    for record in results:
        if not isinstance(record, dict):
            continue

        if record.get("status") != "FAIL":
            continue

        device = record.get("device")
        duration = record.get("duration")

        if not isinstance(device, str) or not device:
            continue

        if not isinstance(duration , (int, float)):
            continue

        failure_counts[device] = failure_counts.get(device, 0) + 1
        duration_totals[device] = duration_totals.get(device, 0) + duration

    averages = {}

    for device in duration_totals:
        averages[device] = duration_totals[device] / failure_counts[device]

    return averages

failed_duration_averages = average_failed_duration_by_device(results)
print(failed_duration_averages)