# 바꿀 단어 설정
old_word = "호호"
new_word = "후후"

# 사용자로부터 파일 경로 입력받기
# 예: C:\\Users\\사용자이름\\Desktop\\메모.txt
file_path = input("/content/drive/MyDrive/translation_final.json")

try:
    # 1. 파일을 읽기 모드로 열기
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"'{file_path}' 파일을 성공적으로 읽었습니다.")

    # 2. 내용 안에서 단어 바꾸기
    # "키로비그는", "키로비그를" 같은 단어도 이 한 줄로 모두 처리됩니다.
    changed_content = content.replace(old_word, new_word)

    # 3. 파일을 쓰기 모드로 열어 변경된 내용 덮어쓰기
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(changed_content)

    print(f"파일 내의 모든 '{old_word}'를 '{new_word}'로 성공적으로 변경했습니다.")

except FileNotFoundError:
    print(f"오류: '{file_path}' 파일을 찾을 수 없습니다. 경로를 다시 확인해주세요.")
except Exception as e:
    print(f"오류가 발생했습니다: {e}")
