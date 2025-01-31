import streamlit as st
from datetime import datetime

st.title("🌟 Welcome to My Blog 🌟")
st.markdown("---")

st.subheader("📸 My Profile")
st.image("jolina.jpg", caption="Jolina M. Aniscal", width=500,)  

st.markdown("""
<style>
.profile-card {
    background-color: #e8f5e9; 
    padding: 20px; 
    border-radius: 10px; 
    border: 2px solid #388e3c;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
}
</style>
<div class="profile-card">
    <h4>👤 Name: Jolina M. Aniscal</h4>
    <p>🎂 Age: 18</p>
    <p>📅 Birthday: January 12, 2006</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📖 About Me")
about_me = """
Hi, I am a student who loves studying, watching movies, playing sports (especially table tennis), 
and eating all the time. My favorite color is green. 🌿
"""
st.markdown(f"""
<div style="background-color: #e0f7fa; padding: 20px; border-radius: 10px; border: 2px solid #00796b;">
    <p style="color: #004d40;">{about_me}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
sections = ["🏆 Achievements"]
choice = st.radio("Navigate to:", sections)

if choice == "🏆 Achievements":
    st.subheader("📜 Certificates and Achievements")

    with st.expander("Add Certificates"):
        new_certificate = st.text_input("Certificate Name")
        if st.button("Add Certificate"):
            if 'certificates' not in st.session_state:
                st.session_state['certificates'] = []
            if new_certificate:
                st.session_state['certificates'].append(new_certificate)
                st.success("Certificate added!")
            else:
                st.error("Please enter a certificate name.")

    st.markdown("### 🎖️ Certificates")
    if 'certificates' in st.session_state and st.session_state['certificates']:
        for i, cert in enumerate(st.session_state['certificates']):
            st.write(f"{i + 1}. {cert}")
            if st.button(f"Delete {cert}", key=f"del_cert_{i}"):
                st.session_state['certificates'].pop(i)
                st.success(f"Deleted {cert}")
                st.experimental_rerun()
    else:
        st.write("No certificates added yet.")

    with st.expander("Add Educational Attainment"):
        new_education = st.text_input("Educational Attainment")
        if st.button("Add Educational Attainment"):
            if 'education' not in st.session_state:
                st.session_state['education'] = []
            if new_education:
                st.session_state['education'].append(new_education)
                st.success("Educational attainment added!")
            else:
                st.error("Please enter educational attainment.")

    st.markdown("### 🎓 Educational Attainment")
    if 'education' in st.session_state and st.session_state['education']:
        for i, edu in enumerate(st.session_state['education']):
            st.write(f"{i + 1}. {edu}")
            if st.button(f"Delete {edu}", key=f"del_edu_{i}"):
                st.session_state['education'].pop(i)
                st.success(f"Deleted {edu}")
                st.experimental_rerun()
    else:
        st.write("No educational attainment added yet.")

