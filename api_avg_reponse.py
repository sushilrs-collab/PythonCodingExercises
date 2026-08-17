logs = [
    {"api": "/login", "response_time": 120},
    {"api": "/search", "response_time": 650},
    {"api": "/login", "response_time": 180},
    {"api": "/checkout", "response_time": 500},
    {"api": "/search", "response_time": 1000},
    {"api": "/checkout", "response_time": 300},
]

def largest_api_average(input_logs):
    api_total = {}
    api_count = {}

    for log in input_logs:
        if not isinstance(log, dict) or not log:
            continue

        api_name = log.get("api")
        response_time = log.get("response_time")

        if not isinstance(api_name, str) or not api_name:
            continue

        if (not isinstance(response_time, (int, float)) or isinstance(response_time, bool) or response_time < 0):
            continue

        if api_name not in api_total:
            api_total[api_name] = response_time
        else:
            api_total[api_name] = api_total[api_name] + response_time
        

        api_count[api_name] = api_count.get(api_name, 0) + 1

    average = {}

    for api_name in api_total:
        average[api_name] = api_total[api_name] / api_count[api_name]

    slowest_api = None
    highest_average = 0

    for api_name in average:
        if average[api_name] > highest_average:
            highest_average = average[api_name]
            slowest_api = api_name

    return slowest_api, highest_average


slowest_api, highest_average = largest_api_average(logs)
print(f"The API with slowest response time is : {slowest_api} average time taken is : {highest_average}")