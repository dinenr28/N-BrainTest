import streamlit as st
import random

# ==========================================
# 1. GENERATOR BANK SOAL ACAK DENGAN LATEX EQUATION
# ==========================================
def buat_soal_sd():
    soal_list = []
    # 5 soal Pilihan Ganda secara acak
    for i in range(5):
        a = random.randint(10, 50)
        b = random.randint(5, 20)
        c = random.randint(2, 10)
        hasil = a + b * c
        soal_list.append({
            "id": f"sd-pg-{i}",
            "tipe": "pilihan_ganda",
            "pertanyaan": f"Berapakah hasil dari $ {a} + {b} \times {c} $ ?",
            "pilihan": [f"A. {hasil}", f"B. {hasil + 5}", f"C. {hasil - 10}", f"D. {hasil + 2}"],
            "kunci": "A",
            "pembahasan": f"Dahulukan perkalian: $ {b} \times {c} = {b*c} $. Lalu tambahkan dengan {a}: $ {a} + {b*c} = {hasil} $."
        })
    # 5 soal Essay secara acak
    for i in range(5):
        a = random.randint(50, 200)
        b = random.randint(2, 8)
        hasil = a // b
        soal_list.append({
            "id": f"sd-es-{i}",
            "tipe": "essay",
            "pertanyaan": f"Berapakah hasil pembagian bulat dari $ {a} \div {b} $ ?",
            "kunci": str(hasil),
            "pembahasan": f"Hasil dari $ {a} \div {b} $ adalah {hasil}."
        })
    return soal_list

def buat_soal_smp():
    soal_list = []
    # 5 soal Pilihan Ganda Aljabar
    for i in range(5):
        x = random.randint(2, 9)
        a = random.randint(2, 5)
        c = random.randint(10, 30)
        b = c - (a * x)
        opsi_a = x
        soal_list.append({
            "id": f"smp-pg-{i}",
            "tipe": "pilihan_ganda",
            "pertanyaan": f"Jika $ {a}x + ({b}) = {c} $, berapakah nilai dari variabel $ x $?",
            "pilihan": [f"A. {opsi_a}", f"B. {opsi_a + 2}", f"C. {opsi_a - 1}", f"D. {opsi_a + 3}"],
            "kunci": "A",
            "pembahasan": f"Pindah ruas: $ {a}x = {c} - ({b}) \rightarrow {a}x = {a*x} \rightarrow x = {x} $."
        })
    # 5 soal Essay Modulo
    for i in range(5):
        a = random.randint(30, 99)
        b = random.randint(4, 9)
        hasil = a % b
        soal_list.append({
            "id": f"smp-es-{i}",
            "tipe": "essay",
            "pertanyaan": f"Berapakah sisa pembagian dari ekspresi berikut: $ {a} \pmod{{ {b} }} $ ?",
            "kunci": str(hasil),
            "pembahasan": f"$ {a} $ dibagi $ {b} $ menghasilkan sisa $ {hasil} $."
        })
    return soal_list

def buat_soal_sma():
    soal_list = []
    # 5 soal Pilihan Ganda Integral Tentu
    for i in range(5):
        n = random.randint(2, 3)
        a = n + 1
        b_atas = random.randint(2, 3)
        b_bawah = 1
        hasil = (b_atas**a) - (b_bawah**a)
        soal_list.append({
            "id": f"sma-pg-{i}",
            "tipe": "pilihan_ganda",
            "pertanyaan": f"Tentukan hasil nilai akhir dari integral tentu berikut: $$ \int_{{{b_bawah}}}^{{{b_atas}}} {a}x^{{{n}}} \, dx $$",
            "pilihan": [f"A. {hasil}", f"B. {hasil + 4}", f"C. {hasil - 2}", f"D. {hasil * 2}"],
            "kunci": "A",
            "pembahasan": f"Antiturunan dari $ {a}x^{{{n}}} $ adalah $ x^{{{a}}} $. Masukkan batas atas dan bawah: $ ({b_atas}^{{{a}}}) - ({b_bawah}^{{{a}}}) = {hasil} $."
        })
    # 5 soal Essay Turunan Fungsi
    for i in range(5):
        pangkat = random.randint(3, 5)
        koef = random.randint(2, 4)
        x_val = 2
        turunan_koef = koef * pangkat
        turunan_pangkat = pangkat - 1
        hasil = turunan_koef * (x_val**turunan_pangkat)
        soal_list.append({
            "id": f"sma-es-{i}",
            "tipe": "essay",
            "pertanyaan": f"Diketahui fungsi $ f(x) = {koef}x^{{{pangkat}}} $. Berapakah nilai dari turunan pertama $ f'(2) $ ?",
            "kunci": str(hasil),
            "pembahasan": f"Rumus turunan $ f'(x) = {turunan_koef}x^{{{turunan_pangkat}}} $. Substitusi nilai $ x=2 \rightarrow {turunan_koef} \times ({x_val}^{{{turunan_pangkat}}}) = {hasil} $."
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
    ["🏠 Menu Utama", "✍ *Mulai Ujian (10 Soal Acak)*", "🧮 Kalkulator Ilmiah"]
)

# --- MENU UTAMA ---
if menu_utama == "🏠 Menu Utama":
    st.title("🧠 N-BrainTest Dashboard (Equation Edition)")
    st.markdown("Aplikasi bank soal matematika otomatis dengan penulisan notasi matematika yang presisi menggunakan standar LaTeX.")
    st.session_state.soal_sesi = None 

# --- LATIHAN SOAL (10 SOAL PER SESI) ---
elif menu_utama == "✍ *Mulai Ujian (10 Soal Acak)*":
    st.title("📝 Ujian Kuantitatif & Logika Matematika")
    jenjang = st.selectbox("Pilih Jenjang Sekolah:", ["SD", "SMP", "SMA"])
    
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
    
    st.info(f"Memuat 10 soal acak tingkat {jenjang}. Selamat mengerjakan!")
    st.write("---")
    
    for i, soal in enumerate(daftar_soal):
        st.markdown(f"### Soal {i+1}:")
        st.markdown(soal['pertanyaan'])
        if soal["tipe"] == "pilihan_ganda":
            jawaban_user[soal["id"]] = st.radio("Pilih Opsi:", soal["pilihan"], key=soal["id"])
        else:
            jawaban_user[soal["id"]] = st.text_input("Tulis jawaban berupa angka saja:", key=soal["id"])
            
    if st.button("Kirim Lembar Ujian"):
        benar = 0
        for soal in daftar_soal:
            ans = jawaban_user.get(soal['id'], "").strip().upper()
            # Cek jawaban berdasarkan pilihan ganda atau esai
            user_choice = ans[0] if soal['tipe'] == 'pilihan_ganda' and ans else ans
            if user_choice == soal['kunci']:
                benar += 1
                
        skor = round((benar / len(daftar_soal)) * 100)
        st.success(f"🎯 Hasil Evaluasi Akhir Sesi: {skor} / 100 ({benar} dari 10 Soal Benar)")
        
        st.subheader("💡 Pembahasan Lengkap Sesi Ini:")
        for i, soal in enumerate(daftar_soal):
            st.markdown(f"**Pembahasan Soal {i+1}:**")
            st.markdown(soal['pembahasan'])

# --- KALKULATOR ILMIAH ---
elif menu_utama == "🧮 Kalkulator Ilmiah":
    st.title("⚡ Kalkulator Modulo & Kalkulus")
    
    st.write("Rumus Integral Tentu Standar:")
    st.latex(r"\int x^n \, dx = \frac{1}{n+1} x^{n+1} + C")
    
    a = st.number_input("Koefisien Bilangan Utama:", value=10)
    b = st.number_input("Pembagi / Batas Atas:", value=3)
    if st.button("Hitung Sisa Bagi (Modulo)"):
        st.success(f"Hasil: {a % b}")
