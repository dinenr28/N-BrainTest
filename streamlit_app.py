import streamlit as st

# Import data soal secara modular dari folder database
from database.matematika import MATEMATIKA_DATA, PRE_POST_MATEMATIKA
from database.fisika import FISIKA_DATA, PRE_POST_FISIKA
from database.kimia import KIMIA_DATA, PRE_POST_KIMIA

# 1. KONFIGURASI TEMA WARNA AESTHETIC
TEMA = {
    "Retro Mint ✨": {"primary": "#85E3B2", "bg": "#F4F9F5", "text": "#2C3E35"},
    "Cyber Neon ⚡": {"primary": "#00F0FF", "bg": "#0D0E15", "text": "#FFFFFF"},
    "Pastel Sunset 🌅": {"primary": "#FFC6FF", "bg": "#FFF5F5", "text": "#4A3E4D"}
}

# Pilihan Warna Tema di Sidebar
st.sidebar.title("🎨 Custom Theme")
pilihan_tema = st.sidebar.selectbox("Pilih Warna Tampilan:", list(TEMA.keys()))
tema_aktif = TEMA[pilihan_tema]

# Inject CSS untuk Kustomisasi Warna Real-time
st.markdown(f"""
    <style>
    .stApp {{ background-color: {tema_aktif['bg']}; color: {tema_aktif['text']}; }}
    h1, h2, h3 {{ color: {tema_aktif['primary']} !important; }}
    </style>
""", unsafe_allow_html=True)

# 2. LOGIKA HITUNG RUMUS SKOR
def hitung_skor(daftar_soal, jawaban_user):
    if not daftar_soal: return 0
    benar = 0
    for soal in daftar_soal:
        ans = jawaban_user.get(soal['id'], "").strip().lower()
        kunci = soal['kunci_jawaban'].strip().lower()
        if soal['tipe'] == 'pilihan_ganda' and ans == kunci:
            benar += 1
        elif soal['tipe'] == 'essay' and (kunci in ans or ans in kunci):
            benar += 1
    return round((benar / len(daftar_soal)) * 100)

# 3. INTERACTION UI (PILIHAN PELAJARAN & JENJANG)
st.title("📚 Aplikasi Belajar Sains & Mat")

mapel = st.selectbox("Pilih Mata Pelajaran:", ["Matematika", "Fisika", "Kimia"])
jenjang_opsi = ["SD", "SMP", "SMA"] if mapel == "Matematika" else ["SMP", "SMA"]
jenjang = st.selectbox("Pilih Jenjang Sekolah:", jenjang_opsi)

# Load data sesuai pilihan user
if mapel == "Matematika":
    data_materi = MATEMATIKA_DATA.get(jenjang, [])
    tes_data = PRE_POST_MATEMATIKA
elif mapel == "Fisika":
    data_materi = FISIKA_DATA.get(jenjang, [])
    tes_data = PRE_POST_FISIKA
else:
    data_materi = KIMIA_DATA.get(jenjang, [])
    tes_data = PRE_POST_KIMIA

# 4. MENU BELAJAR & TES
menu = st.radio("Pilih Aktivitas:", ["Pre-Test", "Belajar Materi & Latihan", "Post-Test"], horizontal=True)

if menu == "Belajar Materi & Latihan":
    if not data_materi:
        st.info("Materi belum tersedia untuk jenjang ini.")
    else:
        # Pilih judul materi
        judul_materi = st.selectbox("Pilih Materi:", [m["judul"] for m in data_materi])
        materi_terpilih = next(m for m in data_materi if m["judul"] == str(judul_materi))
        
        # Tampilkan Konten Sebelum Soal
        st.subheader(f"📖 Materi: {materi_terpilih['judul']}")
        st.write(materi_terpilih["isi_konten"])
        
        # Tampilkan Soal Latihan
        st.subheader("✍️ Soal Latihan")
        jawaban_user = {}
        
        for soal in materi_terpilih["soal_latihan"]:
            st.write(soal["pertanyaan"])
            if soal["tipe"] == "pilihan_ganda":
                jawaban_user[soal["id"]] = st.radio("Pilih jawaban:", soal["pilihan"], key=soal["id"])[0]
            else:
                jawaban_user[soal["id"]] = st.text_input("Tulis jawaban kamu:", key=soal["id"])
        
        if st.button("Kirim Jawaban & Lihat Pembahasan"):
            skor = hitung_skor(materi_terpilih["soal_latihan"], jawaban_user)
            st.success(f"Skor kamu: {skor} / 100")
            
            st.subheader("💡 Pembahasan Soal:")
            for soal in materi_terpilih["soal_latihan"]:
                st.info(f"Soal: {soal['pertanyaan']}\n\n**Kunci:** {soal['kunci_jawaban']}\n\n**Pembahasan:** {soal['pembahasan']}")

else:
    # Handler Pre-test dan Post-test
    tipe_tes = "pre_test" if menu == "Pre-Test" else "post_test"
    soal_tes = tes_data[tipe_tes].get(jenjang, [])
    
    if not soal_tes:
        st.info(f"Soal {menu} belum tersedia untuk jenjang ini.")
    else:
        st.subheader(f"📝 {menu} - {mapel} {jenjang}")
        jawaban_user = {}
        for soal in soal_tes:
            st.write(soal["pertanyaan"])
            jawaban_user[soal["id"]] = st.radio("Pilih jawaban:", soal["pilihan"], key=soal["id"])[0]
            
        if st.button(f"Selesaikan {menu}"):
            skor = hitung_skor(soal_tes, jawaban_user)
            st.success(f"Hasil Akhir {menu}: {skor} / 100")
