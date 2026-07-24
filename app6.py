import random 
num=0
import streamlit as st
num1=random.randint(1,100)
num2=random.randint(1,100)
sign=random.choice(['+','-','*','/'])
if sign =='+':
  sc=num1+num2
if sign =='-':
 sc=num1-num2
if sign =='*':
 sc=num1*num2
if sign =='/':
 sc=num1/num2
st.write(num1,sign,num2)
number=st.number_input("ادخل اجابتك")
if st.button("تاكيد الاجابه "):
 if number==sc:
  st.write("انت عبقري ")
  num=+1
else:
 st.write("انت غبي ")
 num=0

