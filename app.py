import streamlit as st
import math

def calculate_altitude(sea_level_pressure, current_pressure):
    return 44330 * (1 - (current_pressure / sea_level_pressure) ** (1/5.255))

st.title('해면고도 계산기')

sea_level_pressure = st.number_input('해면기압 (hPa)', min_value=900.0, max_value=1100.0, value=1013.25, step=0.01)
current_pressure = st.number_input('현재 위치의 기압 (hPa)', min_value=0.0, max_value=1100.0, value=1000.0, step=0.01)

if st.button('계산하기'):
    altitude = calculate_altitude(sea_level_pressure, current_pressure)
    st.success(f'현재 위치의 해면고도: {altitude:.2f} 미터')

st.write('참고: 이 계산은 대략적인 추정치이며, 실제 고도와 차이가 있을 수 있습니다.' made by 김우현)