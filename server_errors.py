logs = [
    {"service": "payments", "endpoint": "/charge", "status_code": 500},
    {"service": "payments", "endpoint": "/charge", "status_code": 503},
    {"service": "payments", "endpoint": "/refund", "status_code": 200},
    {"service": "authentication", "endpoint": "/login", "status_code": 401},
    {"service": "authentication", "endpoint": "/login", "status_code": 500},
    {"service": "catalog", "endpoint": "/products", "status_code": 404},
    None,
    {"service": "", "endpoint": "/health", "status_code": 500},
]

def count_server_errors(logs):
    error_counts = {}

    for log in logs:
        if not isinstance(log, dict):
            continue

        service = log.get("service")
        endpoint = log.get("endpoint")
        status = log.get("status_code")

        if not isinstance(service, str) or not service:
            continue

        if not isinstance(endpoint, str) or not endpoint:
            continue

        if not isinstance(status, int) or not status:
            continue

    
        if service not in error_counts:
            error_counts[service] = {}

        if endpoint not in error_counts[service]:
            error_counts[service][endpoint] = 0

        if 500 <= status <= 599:
            error_counts[service][endpoint] += 1

    return error_counts

endpoint_service_server_error = count_server_errors(logs)
print(endpoint_service_server_error)
