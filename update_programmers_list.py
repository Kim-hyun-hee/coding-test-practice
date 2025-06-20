import os
import subprocess
from datetime import datetime

BASE_DIR = "프로그래머스"
README_PATH = "README.md"

START_TAG = "<!-- START_AUTOGEN -->"
END_TAG = "<!-- END_AUTOGEN -->"

# ✅ git log 를 통해 .cs 파일의 최초 커밋 날짜 가져오기
def get_git_commit_date(filepath):
    try:
        result = subprocess.run(
            ["git", "log", "--reverse", "--format=%ad", "--date=short", "--", filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip().splitlines()[0]
    except (subprocess.CalledProcessError, IndexError):
        print(f"❌ git log 실패 또는 기록 없음: {filepath}")
        return "날짜 없음"

# ✅ 프로그래머스 문제 목록 추출
def extract_programmers_problems():
    entries = {}

    for level_folder in sorted(os.listdir(BASE_DIR)):
        level_path = os.path.join(BASE_DIR, level_folder)
        if not os.path.isdir(level_path) or not level_folder[0].isdigit():
            continue

        level_name = f"Level {level_folder}"
        entries.setdefault(level_name, [])

        for problem_folder in sorted(os.listdir(level_path)):
            problem_path = os.path.join(level_path, problem_folder)
            if not os.path.isdir(problem_path):
                continue

            problem_name = problem_folder.split(". ", 1)[1] if ". " in problem_folder else problem_folder
            rel_path = os.path.join(BASE_DIR, level_folder, problem_folder, "README.md").replace("\\", "/")

            commit_dates = []

            for file in os.listdir(problem_path):
                if file.endswith(".cs"):
                    # Git 기준 상대 경로로 설정
                    relative_path = os.path.join(BASE_DIR, level_folder, problem_folder, file).replace("\\", "/")
                    commit_date = get_git_commit_date(relative_path)
                    print(f"📄 검사 중: {relative_path} → commit_date = {commit_date}")
                    if commit_date != "날짜 없음":
                        commit_dates.append(commit_date)

            if commit_dates:
                modified_time = min(commit_dates)
            else:
                modified_time = "날짜 없음"

            entries[level_name].append((problem_name, rel_path, modified_time))

    return entries

# ✅ README에 들어갈 문자열 구성
def build_problem_list(entries):
    lines = []
    for level in sorted(entries.keys()):
        lines.append(f"## {level}")
        for name, path, date in sorted(entries[level], key=lambda x: x[2], reverse=True):
            lines.append(f"- [{name}]({path}) <sub>{date}</sub>")
        lines.append("")  # 줄바꿈
    return "\n".join(lines)

# ✅ README 갱신
def update_readme(entries):
    if not os.path.exists(README_PATH):
        print("❌ README.md 파일이 존재하지 않습니다.")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if START_TAG not in content or END_TAG not in content:
        print("❌ START/END 태그가 README.md에 없습니다.")
        return

    before = content.split(START_TAG)[0]
    after = content.split(END_TAG)[1]
    middle = build_problem_list(entries)

    new_content = f"{before}{START_TAG}\n{middle}\n{END_TAG}{after}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ README.md 자동 업데이트 완료!")

# ✅ 실행
if __name__ == "__main__":
    data = extract_programmers_problems()
    update_readme(data)
