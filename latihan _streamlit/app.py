import streamlit as st

dasboard = st.Page("./fitur/dasboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
        "Menu Utama" : [dasboard],
        "Transaksi" : [nabung],

    }
)

if 'total_semua' not in st.session_state:
    st.session_state ['total_semua'] = []
    
pg.run()