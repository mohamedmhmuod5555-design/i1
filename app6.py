import random
import streamlit as st

# عنوان اللعبة
st.title("أهلا بك في لعبه الذكاء التابعه ل محمد احمد رياض")

# 1. حفظ البيانات في ذاكرة المتصفح لمنع تغير الأرقام والنقاط تلقائياً
if "num" not in st.session_state:
    st.session_state.num = 0
if "num1" not in st.session_state:
    st.session_state.num1 = random.randint(1, 100)
if "num2" not in st.session_state:
    st.session_state.num2 = random.randint(1, 100)
if "sign" not in st.session_state:
    st.session_state.sign = random.choice(["+", "-", "*", "/"])

# 2. استدعاء الأرقام المحفوظة حالياً لعرضها وحسابها
num1 = st.session_state.num1
num2 = st.session_state.num2
sign = st.session_state.sign

# 3. حساب الإجابة الصحيحة بناءً على العملية الحالية
if sign == "+":
    sc = num1 + num2
elif sign == "-":
    sc = num1 - num2
elif sign == "*":
    sc = num1 * num2
elif sign == "/":
    sc = round(num1 / num2, 2)  # تقريب القسمة لكسر عشري مبسط

# 4. عرض السؤال للمستخدم
st.write(f"### السؤال هو: {num1} {sign} {num2}")

# 5. استقبال إجابة المستخدم
number = st.number_input("ادخل اجابتك", value=0.0)

# 6. زر تأكيد الإجابة وطباعة النتيجة فوراً بشكل ملون وبدون مشاكل
if st.button("تأكيد الاجابه"):
    if number == sc:
        st.success("انت عبقري! إجابة صحيحة")
        st.session_state.num += 1
    else:
        st.error(f"إجابة خاطئة، الإجابة الصحيحة هي: {sc}")
        st.session_state.num = 0

# 7. زر لتوليد سؤال جديد وتحديث الشاشة
if st.button("السؤال التالي"):
    st.session_state.num1 = random.randint(1, 100)
    st.session_state.num2 = random.randint(1, 100)
    st.session_state.sign = random.choice(["+", "-", "*", "/"])
    st.rerun()  # أمر لإعادة تحديث الشاشة لعرض السؤال الجديد فوراً

# 8. عرض النقاط الحالية للمستخدم
st.write(f"### نقاطك تكون: {st.session_state.num}")
