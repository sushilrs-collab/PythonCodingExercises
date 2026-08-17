results = [
    {"test": "Search", "status": "FAIL"},
    {"test": "Login", "status": "PASS"},
    {"test": "Login", "status": "PASS"},
    {"test": "Search", "status": "PASS"},
]

def flaky_test(input_logs):
    test_status = {}
    flaky_results = []

    for record in input_logs:
        if not isinstance(record, dict):
            continue

        test = record.get("test")
        status = record.get("status")

        if not isinstance(test, str) or not test:
            continue
        if not isinstance(status, str) or not ("PASS", "FAIL") or not status:
            continue


        if test not in test_status:
            test_status[test] = set()

        test_status[test].add(status)

    for test, status in test_status.items():
        if len(status) == 2:
            flaky_results.append(test)

    return flaky_results


flaky_tests_results = flaky_test(results)
print(flaky_tests_results)