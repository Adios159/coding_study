scores = [
    {'id': '001', 'name': 'Alice', 'kor': 95, 'eng': 88, 'math': 75},
    {'id': '002', 'name': 'Bob', 'kor': 70, 'eng': 92, 'math': 85},
    {'id': '003', 'name': 'Charlie', 'kor': 85, 'eng': 80, 'math': 98},
    {'id': '004', 'name': 'David', 'kor': 90, 'eng': 95, 'math': 90},
    {'id': '005', 'name': 'Eve', 'kor': 65, 'eng': 70, 'math': 72}
]

print(">> 학생별 평균 점수")
for student in scores:
    avg = (student['kor'] + student['eng'] + student['math']) / 3
    student['avg'] = round(avg, 2)
    print(f"{student['id']}/{student['name']}: {student['avg']:.2f}")

subjects = ['kor', 'eng', 'math']
subject_names = {'kor': '국어', 'eng': '영어', 'math': '수학'}

print("\n>> 과목별 최고 점수")
for subject in subjects:
    top_student = max(scores, key=lambda x: x[subject])
    print(f"{subject_names[subject]}: {top_student['id']}/{top_student['name']}")

