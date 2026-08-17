logs = [
    {"request_id": "r1", "service": "Auth", "timestamp": 100},
    {"request_id": "r2", "service": "Payments", "timestamp": 102},
    {"request_id": "r1", "service": "Gateway", "timestamp": 105},
    {"request_id": "r2", "service": "Database", "timestamp": 108},
    {"request_id": "r1", "service": "Database", "timestamp": 110},
]


def build_request_paths(ip_logs):
    # logs = []

    for record in ip_logs:
        if not isinstance(record, dict) or not record:
            continue

        request_id = record.get("request_id")
        service = record.get("service")
        ts = record.get("timestamp")

        if not isinstance(request_id, str) or not request_id:
            continue

        if not isinstance(service, str) or not service:
            continue

        if not isinstance(ts, (int, float)):
            continue

        # logs.append(record)

    # logs.sort(key=lambda log: (log["timestamp"], log["service"]))

    request_path = {}

    # for log in logs:
    #     request_id = log["request_id"]
    #     service = log["service"]

    if request_id not in request_path:
        request_path[request_id] = []

    request_path[request_id].append(service)

    return request_path

output_logs = build_request_paths(logs)
print(output_logs)