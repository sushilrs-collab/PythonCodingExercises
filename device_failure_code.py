def device_with_most_failures(results):
    failure_counts = {}
    max_device = None
    max_count = 0

    for record in results:
        if not isinstance(record, dict):
            continue

        device = record.get("device")
        status = record.get("status")

        if not isinstance(device, str) or not device:
            continue
        if not isinstance(status, str) or status != "FAIL":
            continue

        failure_counts[device] = failure_counts.get(device, 0) + 1

        if failure_counts[device] > max_count:
            max_count = failure_counts[device]
            max_device = device

    return max_device, max_count



results = [
    {"device":"iPhone16","status":"FAIL"},
    {"device":"iPhone16","status":"FAIL"},
    {"device":"iPhone16","status":"PASS"},
    {"device":"iPadPro","status":"FAIL"},
    {"device":"iPadPro","status":"FAIL"},
    {"device":"AppleWatch","status":"PASS"},
    {"device":"AppleWatch","status":"FAIL"},
]

most_failed_device = device_with_most_failures(results)
print(f"The device with the most failures is: {most_failed_device[0]} with {most_failed_device[1]} failures.")