import streamlit as st
import math

# ==========================================
# 1. DATABASE MATERI & SOAL SUPER LENGKAP
# ==========================================
DATABASE_MATEMATIKA = {
    "SD": {
        "Perhitungan Dasar": {
            "materi": "Perhitungan dasar meliputi penjumlahan, pengurangan, perkalian, dan pembagian. Ingat aturan kabataku (kali, bagi, tambah, kurang) untuk menentukan prioritas hitung.",
            "soal": [
                {"id": "sd-dasar-1", "tipe": "pilihan_ganda", "pertanyaan": "Hasil dari 25 + 15 x 4 - 30 adalah...", "pilihan": ["A. 130", "B. 55", "C. 70", "D. 95"], "kunci": "B", "pembahasan": "Kerjakan perkalian dulu: 15 x 4 = 60. Lalu: 25 + 60 - 30 = 55."},
                {"id": "sd-dasar-2", "tipe": "essay", "pertanyaan": "Berapakah hasil dari 125 : 5 + 8?", "kunci": "33", "pembahasan": "125 : 5 = 25. Kemudian 25 + 8 = 33."}
            ]
        },
        "Pecahan & Desimal": {
            "materi": "Mengubah pecahan menjadi desimal atau persen mempermudah perhitungan operasi campuran cerita.",
            "soal": [
                {"id": "sd-pecahan-1", "tipe": "pilihan_ganda", "pertanyaan": "Ibu memiliki 2,5 kg gula. Digunakan 40% untuk kue. Sisa gula ibu...", "pilihan": ["A. 1,5 kg", "B. 1,0 kg", "C. 2,1 kg", "D. 0,5 kg"], "kunci": "A", "pembahasan": "Dipakai = 40% x 2,5 = 1 kg. Sisa = 2,5 - 1 = 1,5 kg."}
            ]
        }
    },
    "SMP": {
        "Aljabar Dasar": {
            "materi": "Aljabar menyederhanakan ekspresi dengan huruf (variabel). Pindah ruas akan mengubah tanda operasi (+ menjadi -, x menjadi :).",
            "soal": [
                {"id": "smp-aljabar-1", "tipe": "pilihan_ganda", "pertanyaan": "Jika 3x - 7 = 8, berapakah nilai x?", "pilihan": ["A. 3", "B. 5", "C. 2", "D. 6"], "kunci": "B", "pembahasan": "3x = 8 + 7 -> 3x = 15 -> x = 5."}
            ]
        },
        "Persamaan Kuadrat": {
            "materi": "Persamaan kuadrat berbentuk ax² + bx + c = 0. Akar-akarnya bisa dicari dengan rumus abc atau pemfaktoran.",
            "soal": [
                {"id": "smp-kuadrat-1", "tipe": "pilihan_ganda", "pertanyaan": "Akar penyelesaian dari x² - 5x + 6 = 0 adalah...", "pilihan": ["A. {1, 6}", "B. {-2, -3}", "C. {2, 3}", "D. {1, 5}"], "kunci": "C", "pembahasan": "(x - 2)(x - 3) = 0. Maka x = 2 atau x = 3."}
            ]
        }
    },
    "SMA": {
        "Logika & Algoritma": {
            "materi": "Algoritma matematika sering dinyatakan dalam barisan pembagian, deret logika, modulo, atau pseudocode berulang.",
            "soal": [
                {"id": "sma-algo-1", "tipe": "pilihan_ganda", "pertanyaan": "Berapakah hasil dari 47 modulo 6?", "pilihan": ["A. 5", "B. 2", "C. 1", "D. 4"], "kunci": "A", "pembahasan": "47 dibagi 6 adalah 7 dengan sisa 5. Maka 47 mod 6 = 5."}
            ]
        },
        "Integral & Kalkulus": {
            "materi": "Integral Tentu menghitung luas daerah di bawah kurva fungsi: ∫ xⁿ dx = (1 / n+1) xⁿ⁺¹ + C.",
            "soal": [
                {"id": "sma-integral-1", "tipe": "pilihan_ganda", "pertanyaan": "Hasil dari ∫ (dari 1 sampai 3) 3x² dx adalah...", "pilihan": ["A. 26", "B. 27", "C. 28", "D. 24"], "kunci": "A", "pembahasan": "Integralnya [x³] batas 1 ke 3. = 3³ - 1³ = 27 - 1 = 26."}
            ]
        }
    }
}

# ==========================================
# 2. SISTEM NAVIGASI DASHBOARD (SIDEBAR)
# ==========================================
st.sidebar.title("🎛️ Dashboard Menu")
menu_utama = st.sidebar.radio(
    "Pilih Menu:", 
    ["🏠 Menu Utama", "📖 Pelajaran & Materi", "✍️ Latihan Soal (Kuis)", "🧮 Kalkulator Ilmiah"]
)

def hitung_skor(daftar_soal, jawaban_user):
    benar = 0
    for soal in daftar_soal:
        ans = jawaban_user.get(soal['id'], "").strip().upper()
        if soal['tipe'] == 'pilihan_ganda' and ans == soal['kunci']:
            benar += 1
        elif soal['tipe'] == 'essay' and ans.lower() == soal['kunci'].lower():
            benar += 1
    return round((benar / len(daftar_soal)) * 100) if daftar_soal else 0

# ==========================================
# 3. KONTEN PER MENU
# ==========================================

# --- MENU UTAMA ---
if menu_utama == "🏠 Menu Utama":
    st.title("🧠 N-BrainTest Dashboard")
    st.markdown("Selamat datang di platform belajar matematika komprehensif. Pilih fitur belajar di sidebar samping!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📖 **Materi Lengkap**\nBelajar teori dari perhitungan dasar hingga integral.")
    with col2:
        st.success("✍️ **Soal Ujian**\nUji kemampuan logika dan hitungan kuantitatif kamu.")
    with col3:
        st.warning("🧮 **Kalkulator**\nAlat bantu hitung cepat rumus matematika.")

# --- PELAJARAN & MATERI ---
elif menu_utama == "📖 Pelajaran & Materi":
    st.title("📚 Ruang Belajar Teori")
    jenjang = st.selectbox("Pilih Jenjang Sekolah:", ["SD", "SMP", "SMA"])
    
    materi_opsi = list(DATABASE_MATEMATIKA[jenjang].keys())
    topik = st.selectbox("Pilih Topik Pembahasan:", materi_opsi)
    
    isi_materi = DATABASE_MATEMATIKA[jenjang][topik]["materi"]
    st.subheader(f"📌 Materi: {topik} ({jenjang})")
    st.info(isi_materi)

# --- LATIHAN SOAL (KUIS) ---
elif menu_utama == "✍️ Latihan Soal (Kuis)":
    st.title("📝 Ujian & Latihan Soal HOTS")
    jenjang = st.selectbox("Pilih Jenjang Soal:", ["SD", "SMP", "SMA"])
    
    materi_opsi = list(DATABASE_MATEMATIKA[jenjang].keys())
    topik = st.selectbox("Pilih Topik Soal:", materi_opsi)
    
    daftar_soal = DATABASE_MATEMATIKA[jenjang][topik]["soal"]
    jawaban_user = {}
    
    st.write("---")
    for i, soal in enumerate(daftar_soal):
        st.write(f"**Soal {i+1}: {soal['pertanyaan']}**")
        if soal["tipe"] == "pilihan_ganda":
            jawaban_user[soal["id"]] = st.radio("Pilih Opsi:", soal["pilihan"], key=soal["id"])[0]
        else:
            jawaban_user[soal["id"]] = st.text_input("Tulis jawaban angka/kata:", key=soal["id"])
            
    if st.button("Kirim Lembar Jawaban"):
        skor = hitung_skor(daftar_soal, jawaban_user)
        st.success(f"🎯 Skor Evaluasi Kamu: {skor} / 100")
        
        st.subheader("💡 Lembar Pembahasan:")
        for soal in daftar_soal:
            st.markdown(f"- **Kunci:** `{soal['kunci']}` | **Solusi:** {soal['pembahasan']}")

# --- KALKULATOR ILMIAH ---
elif menu_utama == "🧮 Kalkulator Ilmiah":
    st.title("⚡ Kalkulator Super Pintar")
    
    tipe_kalkulator = st.selectbox("Pilih Jenis Perhitungan:", ["Hitungan Dasar", "Kalkulus (Integral/Turunan)", "Algoritma & Modulo"])
    
    if tipe_kalkulator == "Hitungan Dasar":
        col1, col2 = st.columns(2)
        num1 = col1.number_input("Angka Pertama", value=0.0)
        num2 = col2.number_input("Angka Kedua", value=0.0)
        operasi = st.selectbox("Operasi Matematika:", ["+", "-", "x", "/"])
        
        if st.button("Hitung Sekarang"):
            if operasi == "+": hasil = num1 + num2
            elif operasi == "-": hasil = num1 - num2
            elif operasi == "x": hasil = num1 * num2
            elif operasi == "/": hasil = num1 / num2 if num2 != 0 else "Error: Pembagian dengan 0"
            st.metric("Hasil", str(hasil))
            
    elif tipe_kalkulator == "Kalkulus (Integral/Turunan)":
        st.write("Membantu memproyeksikan integral tentu sederhana $f(x) = ax^n$")
        a = st.number_input("Koefisien (a)", value=1.0)
        n = st.number_input("Pangkat (n)", value=2.0)
        
        if st.button("Hitung Rumus Antiturunan"):
            if n == -1:
                st.code(f"Hasil integral: {a} ln|x| + C")
            else:
                st.code(f"Hasil integral: {a/(n+1)} x^{int(n+1)} + C")
                
    elif tipe_kalkulator == "Algoritma & Modulo":
        st.write("Menghitung sisa bagi algoritma pembagian bilangan bulat.")
        angka = st.number_input("Bilangan yang dibagi (Dividend)", value=10, step=1)
        pembagi = st.number_input("Bilangan pembagi (Divisor)", value=3, step=1)
        
        if st.button("Jalankan Fungsi Modulo"):
            if pembagi == 0:
                st.error("Pembagi tidak boleh 0!")
            else:
                sisa = angka % pembagi
                st.success(f"Hasil Akhir: {angka} mod {pembagi} = {sisa}")
