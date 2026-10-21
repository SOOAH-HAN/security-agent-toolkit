from rbac import check_permission, ROLES, USERS
from access_log import LOG

allowed = 0
denied = 0
counts = {}
used = {}

# ← 1부: 기록을 하나씩 다시 판정하며 건수와 쓴 권한 모으기
for log_id, time, user, resource, action in LOG:
    ok, reason = check_permission(user, resource, action)

    if ok:
        allowed += 1

        key = user + " 허용"
        counts[key] = counts.get(key, 0) + 1

        role = USERS[user]["role"]
        if role not in used:
            used[role] = []
        used[role].append(f"{resource}:{action}")

    else:
        denied += 1

        print("[거부]", log_id, time, user, resource, action, "-", reason)

        key = user + " 거부"
        counts[key] = counts.get(key, 0) + 1
        
print("허용", allowed, "거부", denied)
print(counts)

# ← 2부: 쓰이지 않은 권한 출력하기
for role, perms in ROLES.items():
    for perm in perms:
        if perm not in used.get(role, []):
            print("쓰이지 않음", role, perm)