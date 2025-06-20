import os
from datetime import datetime

BASE_DIR = "프로그래머스" 
README_PATH = "README.md"

START_TAG = "<!-- START_AUTOGEN -->"
END_TAG = "<!-- END_AUTOGEN -->"

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
            rel_path = os.path.join("프로그래머스", level_folder, problem_folder, "README.md").replace("\\", "/")
            file_dates = []
            for file in os.listdir(problem_path):
                if file.endswith(".cs"):
                    full_path = os.path.join(problem_path, file)
                    file_dates.append(os.path.getmtime(full_path))
            
            if file_dates:
                timestamp = min(file_dates)  # 가장 오래된 C# 파일 기준
                modified_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
            else:
                modified_time = "날짜 없음"

            entries[level_name].append((problem_name, rel_path, modified_time))

    return entries

def build_problem_list(entries):
    lines = []
    for level in sorted(entries.keys()):
        lines.append(f"## {level}")
        for name, path, date in sorted(entries[level], key=lambda x: x[2], reverse=True):
            lines.append(f"- [{name}]({path}) <sub>{date}</sub>")
        lines.append("")  # 줄바꿈
    return "\n".join(lines)

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

if __name__ == "__main__":
    data = extract_programmers_problems()
    update_readme(data)
