
import json

LOG = [
'{"time": "02:10", "user": "seoyeon", "device": "NB-7741", "decision": "거부", "reason": "미등록 기기"}',
'{"time": "02:13", "user": "seoyeon", "device": "NB-0417", "decision": "허용", "reason": "-"}',
'{"time": "08:55", "user": "junho", "device": "NB-0522", "decision": "허용", "reason": "-"}',
'{"time": "09:02", "user": "dami", "device": "NB-0333", "decision": "거부", "reason": "퇴사 계정"}',
'{"time": "09:03", "user": "dami", "device": "NB-0333", "decision": "거부", "reason": "퇴사 계정"}',
'{"time": "09:20", "user": "gaeun", "device": "NB-0188", "decision": "허용", "reason": "-"}',
'{"time": "09:41", "user": "junho", "device": "NB-0522", "decision": "거부", "reason": "MFA 안 함"}',
'{"time": "09:44", "user": "junho", "device": "NB-0522", "decision": "허용", "reason": "-"}',
'{"time": "10:30", "user": "dami", "device": "NB-0333", "decision": "거부", "reason": "퇴사 계정"}',
'{"time": "11:15", "user": "gaeun", "device": "NB-0188", "decision": "허용", "reason": "-"}',
'{"time": "11:50", "user": "seoyeon", "device": "NB-0417", "decision": "허용", "reason": "-"}',
'{"time": "13:05", "user": "junho", "device": "NB-0522", "decision": "허용", "reason": "-"}',
'{"time": "14:00", "user": "jiho", "device": "NB-0610", "decision": "거부", "reason": "해외 접속"}',
'{"time": "14:40", "user": "jiho", "device": "NB-0610", "decision": "허용", "reason": "-"}',
'{"time": "15:20", "user": "seoyeon", "device": "NB-7741", "decision": "거부", "reason": "미등록 기기"}',
'{"time": "15:48", "user": "gaeun", "device": "NB-0188", "decision": "허용", "reason": "-"}',
'{"time": "16:05", "user": "dami", "device": "NB-0333", "decision": "거부", "reason": "퇴사 계정"}',
'{"time": "16:30", "user": "junho", "device": "NB-0522", "decision": "허용", "reason": "-"}',
'{"time": "17:10", "user": "jiho", "device": "NB-0610", "decision": "허용", "reason": "-"}',
'{"time": "17:55", "user": "gaeun", "device": "NB-0188", "decision": "허용", "reason": "-"}',
]

def to_min(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)

last = {}
deny_reasons = {}

for text in LOG:
    line = json.loads(text)  # ① JSON 글자를 딕셔너리로 변환
    user = line["user"]
    now = to_min(line["time"])

    # ② 같은 계정의 거부 직후 허용 여부 확인
    if (
        user in last
        and last[user][0] == "거부"
        and line["decision"] == "허용"
        and now - last[user][1] <= 10
    ):
        print("[거부 후 허용]", user, line["time"], line["device"])

    # ③ 계정별 마지막 결정과 시각 저장
    last[user] = (line["decision"], now)

    if line["decision"] == "거부":
        deny_reasons[line["reason"]] = deny_reasons.get(line["reason"], 0) + 1

# ④ 거부 이유별 막대그래프 출력
for reason in deny_reasons:
    count = deny_reasons[reason]
    print(reason, "#" * count, count)

