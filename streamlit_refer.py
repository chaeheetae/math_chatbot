import streamlit as st
import random

# 수학 문제 생성 함수
def generate_math_problem():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)
    
    # 나누기 문제일 경우 소수점 제거
    if operation == '/':
        num1 = num1 * num2
    
    problem = f"{num1} {operation} {num2}"
    return problem, eval(problem)
    
# Streamlit 앱 구성
st.title("수학 문제 제공 챗봇")
st.write("새로운 수학 문제를 받고 답을 입력해보세요!")

# 새 문제 생성 버튼
if st.button("새 문제 생성"):
    problem, answer = generate_math_problem()
    st.session_state['problem'] = problem
    st.session_state['answer'] = answer

# 문제와 답 입력 폼
if 'problem' in st.session_state:
    st.write(f"문제: {st.session_state['problem']}")
    user_answer = st.text_input("답을 입력하세요:")

    if st.button("답 확인"):
        if user_answer:
            if float(user_answer) == st.session_state['answer']:
                st.success("정답입니다!")
            else:
                st.error("오답입니다. 다시 시도하세요.")
        else:
            st.warning("답을 입력하세요.")
