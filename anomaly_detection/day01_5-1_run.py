from log_parse import parse_line


LOG_PATH = "access_sample.log"
entries = []
fail_count = 0
total = 0

with open(LOG_PATH, encoding="utf-8") as log_file:
    for line in log_file:
        total = total + 1
        entry = parse_line(line)
        if entry is None:
            fail_count = fail_count + 1
        else:
            entries.append(entry)

success_count = len(entries)
print("--- 단계 1: 로그 파일 읽기 - 전체", total, "줄")
print("읽기 성공", success_count, "줄 · 읽기 실패", fail_count, "줄")
print("--- 단계 2: 로그 첫 3줄을 읽은 결과")
print(entries[0])
print(entries[1])
print(entries[2])
print("--- 단계 3: 값이 덧붙은 요청 (경로에 ? 포함)")
for entry in entries:
    if "?" in entry["path"]:
        print(entry["ip"], entry["path"])
