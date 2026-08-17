jobs = [
    {"pipeline": "mobile-release", "stage": "build", "duration": 120, "result": "SUCCESS"},
    {"pipeline": "mobile-release", "stage": "test", "duration": 300, "result": "FAILED"},
    {"pipeline": "mobile-release", "stage": "test", "duration": 420, "result": "FAILED"},
    {"pipeline": "backend-deploy", "stage": "build", "duration": 180, "result": "FAILED"},
    {"pipeline": "backend-deploy", "stage": "deploy", "duration": 240, "result": "SUCCESS"},
    {"pipeline": "backend-deploy", "stage": "build", "duration": 220, "result": "FAILED"},
    {"pipeline": "data-processing", "stage": "test", "duration": "invalid", "result": "FAILED"},
    None,
    {"pipeline": "", "stage": "deploy", "duration": 100, "result": "FAILED"},
]

def average_duration(jobs):
    duration_totals = {}
    failure_count = {}

    for job in jobs:
        if not isinstance(job, dict):
            continue

        pipeline, pi_stage, duration, result = job.get("pipeline"), job.get("stage"), job.get("duration"), job.get("result")

        if not isinstance(pipeline, str) or not pipeline:
            continue

        if not isinstance(pi_stage, str) or not pi_stage:
            continue

        if not isinstance(duration, (int, float)) or duration < 0:
            continue

        if result != "FAILED":
            continue

        if not pipeline in duration_totals:
            duration_totals[pipeline] = {}

        if not pi_stage in duration_totals[pipeline]:
            duration_totals[pipeline][pi_stage] = 0
        duration_totals[pipeline][pi_stage] += duration

        if not pipeline in failure_count:
            failure_count[pipeline] = {}

        if not pi_stage in failure_count[pipeline]:
            failure_count[pipeline][pi_stage] = 0
        failure_count[pipeline][pi_stage] += 1

    average_duration = {}
    for pipeline, stages in duration_totals.items():
        average_duration[pipeline] = {}
        for pi_stage, total_duration in stages.items():
            average_duration[pipeline][pi_stage] = (
                total_duration / failure_count[pipeline][pi_stage]
            )

    return average_duration

failed_duration_ci = average_duration(jobs)
print(failed_duration_ci)
        
