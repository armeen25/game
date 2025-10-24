import streamlit as st

st.header("💬 แสดงความคิดเห็นเกี่ยวกับประโยชน์ของการเล่นเกม")

st.write("กรอกความคิดเห็นของคุณเกี่ยวกับประโยชน์ของการเล่นเกมด้านล่างนี้:")

name = st.text_input("ชื่อของคุณ:")
benefit = st.text_area("คุณคิดว่าการเล่นเกมให้ประโยชน์อย่างไร?")

if st.button("ส่งความคิดเห็น"):
    if name and benefit:
        st.success(f"ขอบคุณ {name}! 🙌")
        st.write("ความคิดเห็นของคุณ:")
        st.info(benefit)
    else:
        st.warning("กรุณากรอกชื่อและความคิดเห็นก่อนส่ง")

st.divider()

st.caption("💭 ความคิดเห็นจากผู้เล่นช่วยให้เราเข้าใจมุมมองที่หลากหลายมากขึ้น!")
