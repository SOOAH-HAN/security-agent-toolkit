from log_parse import parse_line
from log_classify import label_entries, count_groups


def show_request(item):
    """분류된 요청의 주소 · 방법 · 경로 · 상태 코드를 출력한다."""
    ip_address = item["ip"]
    method = item["method"]
    path = item["path"]
    status = item["status"]
    print(ip_address, method, path, status)


entries = []
with open("access_sample.log", encoding="utf-8") as log_file:
    for line in log_file:
        entry = parse_line(line)
        if entry is not None:
            entries.append(entry)

labeled = label_entries(entries)
counts = count_groups(labeled)
total = len(labeled)
normal_count = counts["정상"]
error_count = counts["오류"]
suspicious_count = counts["의심"]

print("--- 단계 1: 분류별 요청 수 - 전체", total, "개")
print("정상", normal_count, "· 오류", error_count, "· 의심", suspicious_count)
print("--- 단계 2: 의심으로 분류한 요청")
for item in labeled:
    if item["group"] == "의심":
        show_request(item)

print("--- 단계 3: 오류로 분류한 요청")
for item in labeled:
    if item["group"] == "오류":
        show_request(item)
