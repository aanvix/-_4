
import json
def task() -> float:
    name_file = "input.json"
    with open(name_file) as a:
        json_values = json.load(a)

    _sum_ = sum([item["score"] * item["weight"] for item in json_values])
    return round(_sum_, 3)

print(task())