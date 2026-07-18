import streamlit as st
import random

# ==========================================
# 1. GENERATOR BANK SOAL ACAK (MENGHASILKAN RIBUAN KOMBINASI)
# ==========================================
def buat_soal_sd():
    soal_list = []
    # Generate 5 soal Pilihan Ganda secara acak
    for i in range(5):
        a = random.randint(10, 50)
        b = random.randint(5, 20)
        c = random.randint(2, 10)
        hasil = a + b * c
        soal_list.append({
            "id": f"sd-pg-{i}",
            "tipe": "pilihan_ganda",
            "pertanyaan": f"Berapakah hasil dari {a} + {b} x {c} ?",
            "pilihan": [f"A. {hasil}", f"B. {hasil + 5}", f"C. {hasil - 10}", f"D. {hasil + 2}"],
            "kunci": "A",
            "pembahasan": f"Dahulukan perkalian: {b} x {c} = {b*c}. Lalu tambahkan dengan {a}: {a} + {b*c} = {hasil}."
        })
    # Generate 5 soal Essay secara acak
    for i in range(5):
        a = random.randint(50, 200)
        b = random.randint(2, 8)
        hasil = a // b
        soal_list.append({
            "id": f"sd-es-{i}",
            "tipe": "essay",
            "pertanyaan": f"Berapakah hasil pembagian bulat dari {a} dibagi {b} ?",
            "kunci": str(hasil),
            "pembahasan": f"Hasil dari {a} : {b} adalah {hasil}."
        })
    return soal_list

def buat_soal_smp():
    soal_list = []
    # Generate 5 soal Pilihan Ganda Aljabar
    for i in range(5):
        x = random.randint(2, 9)
        a = random.randint(2, 5)
        c = random.randint(10, 30)
        b = c - (a * x)
        opsi_a = x
        soal_list.append({
            "id": f"smp-pg-{i}",
            "tipe": "pilihan_ganda",
            "pertanyaan": f"Jika {a}x + ({b}) = {c}, berapakah nilai x?",
            "pilihan": [f"A. {opsi_a}", f"B. {opsi_a + 2}", f"C. {opsi_a - 1}", f"D. {opsi_a + 3}"],
            "kunci": "A",
            "pembahasan": f"Pindah ruas: {a}x = {c} - ({b}) -> {a}x = {a*x} -> x = {x}."
        })
    # Generate 5 soal Essay Modulo / Teori Bilangan
    for i in range(5):
        a = random.randint(30, 99)
        b = random.randint(4, 9)
        hasil = a % b
        soal_list.append({
            "id": f"smp-es-{i}",
            "tipe": "essay",
            "pertanyaan": f"Berapakah sisa pembagian (modulo) dari {a} mod {b} ?",
            "kunci": str(hasil),
            "pembahasan": f"{a} dibagi {b} adalah {a//b} sisa {hasil}."
        })
    return soal_list

def buat_soal_sma():
    soal_list = []
    # Generate 5 soal Pilihan Ganda Integral
    for i in range(5):
        n = random.randint(2, 4)
        a = n + 1
        b_atas = random.randint(2, 3)
        b_bawah = 1
        hasil = (b_atas**a) - (b_bawah**a)
        soal_list.append({
            "id": f"sma-pg-{i}",
            "tipe": "pilihan_ganda",
            "pertanyaan": f"Berapakah hasil integral tentu ∫ (dari {b_bawah} sampai {b_atas}) {a}x^{n} dx ?",
            "pilihan": [f"A. {hasil}", f"B. {hasil + 4}", f"C. {hasil - 2}", f"D. {hasil * 2}"],
            "kunci": "A",
            "pembahasan": f"Antiturunan dari {a}x^{n} adalah x^{a}. Substitusi batas: ({b_atas}^{a}) - ({b_bawah}^{a}) = {hasil}."
        })
    # Generate 5 soal Essay Turunan
    for i in range(5):
        pangkat = random.randint(3, 6)
        koef = random.randint(2, 5)
        x_val = 2
        turunan_koef = koef * pangkat
        turunan_pangkat = pangkat - 1
        hasil = turunan_koef * (x_val**turunan_pangkat)
        soal_list.append({
            "id": f"sma-es-{i}",
            "tipe": "essay",
            "pertanyaan": f"Jika f(x) = {koef}x^{pangkat}, berapakah nilai dari turunan pertama f'(2) ?",
            "kunci": str(hasil),
            "pembahasan": f"f'(x) = {turunan_koef}x^{turunan_pangkat}. Substitusi x=2: {turunan_koef} x ({x_val}^{turunan_pangkat}) = {hasil}."
        })
    return soal_list

# ==========================================
# 2. SISTEM STATE SESSION & NAVIGASI DASHBOARD
# ==========================================
if "soal_sesi" not in st.session_state:
    st.session_state.soal_sesi = None
if "jenjang_sebelumnya" not in st.session_state:
    st.session_state.jenjang_sebelumnya = ""

st.sidebar.title("🎛️ Dashboard Menu")
menu_utama = st.sidebar.radio(
    "Pilih Menu:", 
    ["🏠 Menu Utama", "✍️ Mulai Ujian (10 Soal Acak)", "🧮 Kalkulator Ilmiah"]
)

# --- MENU UTAMA ---
if menu_utama == "🏠 Menu Utama":
    st.title("🧠 N-BrainTest Dashboard (Infinite Question Mode)")
    st.markdown("Aplikasi ini dikonfigurasi dengan **Bank Soal Generator Otomatis**. Anda bisa mendapatkan ribuan variasi soal berbeda, namun dibatasi hanya **10 soal pilihan terbaik** di setiap sesi ujian.")
    st.session_state.soal_sesi = None  # Reset kuis saat kembali ke menu utama

# --- LATIHAN SOAL (10 SOAL PER SESI) ---
elif menu_utama == "✍️ Mulai Ujian (10 Soal Acak)":
    st.title("📝 Ujian Kuantitatif & Logika Matematika")
    jenjang = st.selectbox("Pilih Jenjang Sekolah:", ["SD", "SMP", "SMA"])
    
    # Tombol buat generate 10 soal baru berulang-ulang tanpa batas
    if st.button("🔄 Generate 10 Soal Baru") or st.session_state.soal_sesi is None or st.session_state.jenjang_sebelumnya != jenjang:
        st.session_state.jenjang_sebelumnya = jenjang
        if jenjang == "SD":
            st.session_state.soal_sesi = buat_soal_sd()
        elif jenjang == "SMP":
            st.session_state.soal_sesi = buat_soal_smp()
        else:
            st.session_state.soal_sesi = buat_soal_sma()
            
    daftar_soal = st.session_state.soal_sesi
    jawaban_user = {}
    
    st.info(f"Berhasil memuat 10 soal acak untuk tingkatan {jenjang}. Selamat mengerjakan!")
    st.write("---")
    
    for i, soal in enumerate(daftar_soal):
        st.write(f"**Soal {i+1}: {soal['pertanyaan']}**")
        if soal["tipe"] == "pilihan_ganda":
            jawaban_user[soal["id"]] = st.radio("Pilih Opsi:", soal["pilihan"], key=soal["id"])[0]
        else:
            jawaban_user[soal["id"]] = st.text_input("Tulis jawaban berupa angka saja:", key=soal["id"])
            
    if st.button("Kirim Lembar Ujian"):
        benar = 0
        for soal in daftar_soal:
            ans = jawaban_user.get(soal['id'], "").strip().upper()
            if soal['tipe'] == 'pilihan_ganda' and ans == soal['kunci']:
                benar += 1
            elif soal['tipe'] == 'essay' and ans == soal['kunci']:
                benar += 1
                
        skor = round((benar / len(daftar_soal)) * 100)
        st.success(f"🎯 Hasil Evaluasi Akhir Sesi: {skor} / 100 ({benar} dari 10 Soal Benar)")
        
        st.subheader("💡 Pembahasan Lengkap Sesi Ini:")
        for i, soal in enumerate(daftar_soal):
            st.markdown(f"**Soal {i+1}:** {soal['pembahasan']}")

# --- KALKULATOR ILMIAH ---
elif menu_utama == "🧮 Kalkulator Ilmiah":
    st.title("⚡ Kalkulator Modulo & Kalkulus")
    angka = st.number_input("Bilangan Pertama / Dividend", value=10)
    pembagi = st.number_input("Bilangan Kedua / Divisor", value=3)
    if st.button("Hitung Modulo"):
        st.success(f"Hasil Sisa Bagi: {angka % pembagi}")
