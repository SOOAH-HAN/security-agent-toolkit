import llm_client                                             # 오전에 만든 llm_client.py 를 불러온다
import notifier                                               # 3교시에 만든 notifier.py 를 불러온다
import report_generator                                       # 오후에 만든 report_generator.py 를 불러온다

# 1. 문제 5-3 의 assert 세 줄을 옮기세요 (sample · two 도 함께)
ssert report_generator.make_lines(sample) == "- [HIGH] E01 로그인 실패 4회\n", "make_lines 결과가 다르다"
assert report_generator.make_lines([]) == "", "빈 리스트는 빈 문자열이어야 한다"
assert report_generator.make_lines(two).count("\n") == 2, "한 건에 한 줄이어야 한다"
# 2. 문제 5-4 의 assert 세 줄을 옮기세요 (config 도 함께)
assert notifier.needs_approval("high", config) == True
assert notifier.needs_approval("low", config) == False
assert notifier.needs_approval("critical", config) == True
# 3. 문제 5-5 의 assert 세 줄을 옮기세요 (fenced 도 함께)
assert llm_client.parse_llm_json(fenced) == {"tool": "lock_account"}
assert llm_client.parse_llm_json("그럴듯한 문장입니다") is None
assert llm_client.parse_llm_json("") is None

print("[테스트 통과] 9건 모두")                                       # 여기까지 오면 아홉 줄이 모두 참이었다
