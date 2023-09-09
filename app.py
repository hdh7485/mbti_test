from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# 예시 퀴즈 데이터
questions = [
    {
        'question': '헉 눈을 떠보니 10시!',
        'choices': ['괜찮아 재택근무 하면 되지', '허겁지겁 나갈 준비를 한다'],
        'answer': ['J', 'P']
    },
    {
        'question': '''하 오늘 좀 피곤하네. 일찍 퇴근해야겠다. \n
        띠링! rf-random에 내가 좋아하는 모임이?!\n
        참석하실 분은 이모지를 눌러주세요''',
        'choices': ['당연히 이모지 누른다', '응 아니야~ 모른 척 \'읽음\'만 누른다.'],
        'answer': ['E', 'I']
    },
    {
        'question': 'ㅇㅇ님과 논의해야 하는데, 슬랙으로 보내야겠다.',
        'choices': ['5-6줄의 대하드라마 작성 후 글자 서식도 보기 좋게 수정하여 전송', '일단 전송'],
        'answer': ['J', 'P']
    },
    {
        'question': '이모지를 찾는데 내가 원하는 이모지가 없다',
        'choices': ['아니 이게 없다고? 직접 만들어야지!', '귀찮아. 누군가 만들겠지'],
        'answer': ['E', 'I']
    },
    {
        'question': '두근두근 한 달 만에 돌아온 미식회!',
        'choices': ['가보고 싶었던 식당 바로 전송', '누군가 올려주길 존버'],
        'answer': ['E', 'I']
    },
    {
        'question': '어떤 종류의 정보 수집 방식을 선호하나요?',
        'choices': ['새로운 아이디어나 개념을 탐구하고 실험하는 것을 즐겨요', '구체적이고 실질적인 사실과 경험을 중요하게 생각해요'],
        'answer': ['N', 'S']
    },
    # 나머지 질문들 추가
]

current_question_index = 0
answers = []

@app.route('/')
def index():
    global current_question_index
    if current_question_index < len(questions):
        question_data = questions[current_question_index]
        return render_template('quiz.html', question_data=question_data)
    else:
        return redirect(url_for('result'))

@app.route('/next', methods=['POST'])
def next_question():
    global current_question_index, user_score, answers
    user_answer = request.form['answer']
    print(user_answer)
    answers.append(user_answer)

    # i = questions[current_question_index]['choices'].index(user_answer)
    # answers.append(questions[current_question_index]['answer'][i])
    
    # 정답 확인 및 점수 계산 (실제 데이터와 비교)
    # current_question = questions[current_question_index]
    #if user_answer == current_question['correct_answer']:
        #user_score += 1

    current_question_index += 1

    return redirect(url_for('index'))

@app.route('/result')
def result():
    global user_score, current_question_index, answers
    print(answers)
    mbti_str = str()

    i_num = answers.count('I')
    e_num = answers.count('E')
    if i_num > e_num:
        mbti_str = mbti_str + 'I'
    else:
        mbti_str = mbti_str + 'E'
        

    n_num = answers.count('N')
    s_num = answers.count('S')
    if n_num > s_num:
        mbti_str = mbti_str + 'N'
    else:
        mbti_str = mbti_str + 'S'

    f_num = answers.count('F')
    p_num = answers.count('T')
    if i_num > e_num:
        mbti_str = mbti_str + 'F'
    else:
        mbti_str = mbti_str + 'T'

    j_num = answers.count('J')
    p_num = answers.count('P')
    if i_num > e_num:
        mbti_str = mbti_str + 'J'

    else:
        mbti_str = mbti_str + 'P'

    
    print(mbti_str)

    rf_style = mbti_str
    current_question_index = 0
    return render_template('result.html', rf_style=rf_style)

if __name__ == '__main__':
    app.run(debug=True)

