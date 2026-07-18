import streamlit as st
import random
import math

# CONFIG Halaman
st.set_page_config(page_title="N-BrainTest Premium", layout="wide")

# ==========================================
# 1. DATABASE RUMUS & MATERI (MENU PELAJARAN)
# ==========================================
RUMUS_MATEMATIKA = {
    "SD": {
        "Perhitungan Dasar & Pecahan": r"""
        * **Kabataku**: Prioritas hitung adalah Kali ($\times$), Bagi ($\div$), Tambah ($+$), Kurang ($-$).
        * **Pecahan**: $\frac{\text{Pembilang}}{\text{Penyebut}}$. Menyamakan penyebut menggunakan KPK.
        """,
        "KPK & FPB": r"""
        * **KPK (Kelipatan Persekutuan Terkecil)**: Ambil semua faktor prima dengan pangkat terbesar.
        * **FPB (Faktor Persekutuan Terbesar)**: Ambil faktor prima yang sama dengan pangkat terkecil.
        """,
        "Luas & Volume (Dasar)": r"""
        * **Persegi**: $L = s \times s$
        * **Persegi Panjang**: $L = p \times l$
        * **Kubus**: $V = s^3$
        * **Balok**: $V = p \times l \times t$
        """
    },
    "SMP": {
        "Aljabar & Persamaan Linear": r"""
        * **Mencari nilai $x$**: Pindah ruas membalik tanda operasi ($+$ menjadi $-$, $\times$ menjadi $\div$).
        * **SPLDV (Dua Variabel)**: Bentuk umum $ax + by = c$. Diselesaikan dengan metode **Substitusi** (memasukkan nilai) atau **Eliminasi** (menghilangkan variabel).
        """,
        "SPLTV & Bangun Ruang": r"""
        * **SPLTV**: Memiliki tiga variabel ($x, y, z$). Butuh minimal 3 persamaan.
        * **Volume Tabung**: $V = \pi r^2 t$
        * **Volume Kerucut**: $V = \frac{1}{3} \pi r^2 t$
        """
    },
    "SMA": {
        "Logika & Finansial": r"""
        * **Logaritma**: ${^a}\log b = c \iff a^c = b$
        * **Bunga Tunggal**: $B = M_0 \times i \times t$
        * **Bunga Majemuk**: $M_t = M_0 (1 + i)^t$
        """,
        "Kalkulus (Integral & Turunan)": r"""
        * **Turunan**: $f(x) = ax^n \rightarrow f'(x) = a \cdot n \cdot x^{n-1}$
        * **Integral Tak Tentu**: $\int ax^n \, dx = \frac{a}{n+1} x^{n+1} + C$
        * **Integral Tentu**: $\int_{a}^{b} f(x) \, dx = F(b) - F(a)$
        """
    }
}

# ==========================================
# 2. GENERATOR 10 SOAL ACAK CAMPURAN (PILIHAN GANDA & ESSAY)
# ==========================================
def generate_10_soal(jenjang):
    soal_campuran = []
    
    if jenjang == "SD":
        for i in range(5):
            a, b, c = random.randint(10, 30), random.randint(5, 15), random.randint(2, 6)
            hasil = a + (b * c)
            soal_campuran.append({
                "id": f"sd-pg-{i}", "tipe": "pilihan_ganda",
                "pertanyaan": fr"Berapakah hasil dari $ {a} + {b} \times {c} $ ?",
                "pilihan": [f"{hasil}", f"{hasil+3}", f"{hasil-5}", f"{hasil+10}"], "kunci": f"{hasil}",
                "pembahasan": fr"Dahulukan perkalian: $ {b} \times {c} = {b*c} $. Lalu $ {a} + {b*c} = {hasil} $."
            })
        for i in range(5):
            s = random.randint(4, 10)
            vol = s**3
            soal_campuran.append({
                "id": f"sd-es-{i}", "tipe": "essay",
                "pertanyaan": fr"Sebuah kubus memiliki panjang rusuk $ s = {s} \text{{ cm}} $. Berapakah Volume kubus tersebut (angka saja)?",
                "kunci": f"{vol}", "pembahasan": fr"Volume kubus: $ V = s^3 = {s}^3 = {vol} \text{{ cm}}^3 $."
            })
            
    elif jenjang == "SMP":
        for i in range(5):
            x_val = random.randint(2, 7)
            a, b = random.randint(2, 5), random.randint(1, 10)
            c = (a * x_val) + b
            soal_campuran.append({
                "id": f"smp-pg-{i}", "tipe": "pilihan_ganda",
                "pertanyaan": fr"Jika diketahui persamaan $ {a}x + {b} = {c} $, tentukan nilai $ x $!",
                "pilihan": [f"{x_val}", f"{x_val+1}", f"{x_val-2}", f"{x_val+3}"], "kunci": f"{x_val}",
                "pembahasan": fr"Pindah ruas: $ {a}x = {c} - {b} \rightarrow {a}x = {a*x_val} \rightarrow x = {x_val} $."
            })
        for i in range(5):
            x, y = random.randint(1, 4), random.randint(1, 4)
            c1, c2 = x + y, x - y
            soal_campuran.append({
                "id": f"smp-es-{i}", "tipe": "essay",
                "pertanyaan": fr"Diketahui sistem persamaan linear (SPLDV): $ x + y = {c1} $ dan $ x - y = {c2} $. Berapakah nilai dari $ x $?",
                "kunci": f"{x}", "pembahasan": fr"Eliminasi dengan menjumlahkan kedua persamaan: $ 2x = {c1+c2} \rightarrow x = {x} $."
            })
            
    else: # SMA
        for i in range(5):
            n = random.randint(2, 3)
            a = n + 1
            hasil = (2**a) - (1**a)
            soal_campuran.append({
                "id": f"sma-pg-{i}", "tipe": "pilihan_ganda",
                "pertanyaan": fr"Tentukan hasil nilai dari integral tentu berikut: $$ \int_{{1}}^{{2}} {a}x^{{{n}}} \, dx $$",
                "pilihan": [f"{hasil}", f"{hasil+2}", f"{hasil-1}", f"{hasil*2}"], "kunci": f"{hasil}",
                "pembahasan": fr"Antiturunan dari $ {a}x^{{{n}}} $ adalah $ x^{{{a}}} $. Evaluasi batas: $ 2^{{{a}}} - 1^{{{a}}} = {hasil} $."
            })
        for i in range(5):
            basis = random.choice([2, 3, 5])
            pangkat = random.randint(2, 4)
            numerus = basis**pangkat
            soal_campuran.append({
                "id": f"sma-es-{i}", "tipe": "essay",
                # Bagian kurung kurawal di bawah ini sudah diperbaiki total agar stabil
                "pertanyaan": fr"Berapakah nilai eksak dari ekspresi logaritma berikut: $ {{^{{{basis}}}}\log {numerus}} $?",
                "kunci": f"{pangkat}", "pembahasan": fr"Karena $ {basis}^{{{pangkat}}} = {numerus} $, maka nilai logaritmanya adalah $ {pangkat} $."
            })
            
    random.shuffle(soal_campuran)
    return soal_campuran

# ==========================================
# 3. INTERACTION SESSION STATE
# ==========================================
if "soal_aktif" not in st.session_state:
    st.session_state.soal_aktif = None
if "jenjang_pilihan" not in st.session_state:
    st.session_state.jenjang_pilihan = "SD"
if "calc_expression" not in st.session_state:
    st.session_state.calc_expression = ""

# SIDEBAR NAVIGATION
st.sidebar.title("🎛️ N-BrainTest Dashboard")
menu = st.sidebar.radio("Navigasi Menu:", ["🏠 Menu Utama & Kuis", "📖 Pelajaran (Rumus)", "🧮 Kalkulator Scientific"])

# ==========================================
# A. MENU UTAMA & KUIS
# ==========================================
if menu == "🏠 Menu Utama & Kuis":
    st.title("🧠 Menu Utama - Ujian Kuantitatif")
    
    jenjang = st.selectbox("Pilih Jenjang Sekolah:", ["SD", "SMP", "SMA"])
    
    if st.session_state.jenjang_pilihan != jenjang:
        st.session_state.jenjang_pilihan = jenjang
        st.session_state.soal_aktif = None

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🚀 Mulai / Acak Ujian Sesi Baru"):
            st.session_state.soal_aktif = generate_10_soal(jenjang)
    with col_btn2:
        if st.button("🔄 Restart Ulang Soal Sesi Ini"):
            st.rerun()

    st.write("---")

    if st.session_state.soal_aktif is not None:
        st.info(f"📋 10 Soal Acak Campuran Tingkat {jenjang} berhasil dimuat.")
        jawaban_user = {}
        
        for i, soal in enumerate(st.session_state.soal_aktif):
            st.markdown(f"#### Soal {i+1}:")
            st.markdown(soal["pertanyaan"])
            
            if soal["tipe"] == "pilihan_ganda":
                opsi_pg = [None] + soal["pilihan"]
                pilihan_terpilih = st.radio("Pilih Opsi Jawaban:", opsi_pg, key=f"soal-{soal['id']}", format_func=lambda x: "Belum Memilih..." if x is None else x)
                jawaban_user[soal["id"]] = pilihan_terpilih
            else:
                jawaban_user[soal["id"]] = st.text_input("Tulis jawaban eksak kamu (Angka):", key=f"soal-{soal['id']}")
            st.write("")

        if st.button("📤 Kirim Semua Lembar Jawaban"):
            skor_benar = 0
            for soal in st.session_state.soal_aktif:
                ans = jawaban_user.get(soal["id"])
                if ans is not None:
                    ans_clean = str(ans).strip().lower()
                    kunci_clean = str(soal["kunci"]).strip().lower()
                    if ans_clean == kunci_clean:
                        skor_benar += 1
                        
            total_skor = round((skor_benar / 10) * 100)
            st.success(f"🎯 Selesai! Skor Ujian Anda: {total_skor} / 100 ({skor_benar} dari 10 soal benar)")
            
            st.subheader("💡 Pembahasan Analitis Soal:")
            for i, soal in enumerate(st.session_state.soal_aktif):
                st.markdown(f"**Soal {i+1}:**")
                st.markdown(soal["pembahasan"])
    else:
        st.warning("Silakan klik tombol **'🚀 Mulai / Acak Ujian Sesi Baru'** di atas untuk menampilkan soal campuran.")

# ==========================================
# B. MENU PELAJARAN (RUMUS-RUMUS)
# ==========================================
elif menu == "📖 Pelajaran (Rumus)":
    st.title("📚 Ruang Teori & Rumus Resmi")
    jenjang_materi = st.selectbox("Lihat Rumus Jenjang:", ["SD", "SMP", "SMA"])
    
    st.write("---")
    st.subheader(f"Daftar Kompetensi Inti Matematika - {jenjang_materi}")
    
    for judul_topik, isi_rumus in RUMUS_MATEMATIKA[jenjang_materi].items():
        with st.expander(f"📁 Rumus: {judul_topik}"):
            st.markdown(isi_rumus)

# ==========================================
# C. KALKULATOR SCIENTIFIC (TOMBOL FISIK)
# ==========================================
elif menu == "🧮 Kalkulator Scientific":
    st.title("⚡ Scientific Calculator Pad")
    
    st.text_input("Screen / Nilai Operasi:", value=st.session_state.calc_expression, disabled=True)
    
    row1_c1, row1_c2, row1_c3, row1_c4, row1_c5 = st.columns(5)
    row2_c1, row2_c2, row2_c3, row2_c4, row2_c5 = st.columns(5)
    row3_c1, row3_c2, row3_c3, row3_c4, row3_c5 = st.columns(5)
    row4_c1, row4_c2, row4_c3, row4_c4, row4_c5 = st.columns(5)
    
    def add_to_calc(char):
        st.session_state.calc_expression += str(char)
        
    # Baris 1
    if row1_c1.button("sin"): add_to_calc("math.sin(")
    if row1_c2.button("cos"): add_to_calc("math.cos(")
    if row1_c3.button("tan"): add_to_calc("math.tan(")
    if row1_c4.button("log"): add_to_calc("math.log10(")
    if row1_c5.button("CLEAR"): st.session_state.calc_expression = ""
    
    # Baris 2
    if row2_c1.button("7"): add_to_calc("7")
    if row2_c2.button("8"): add_to_calc("8")
    if row2_c3.button("9"): add_to_calc("9")
    if row2_c4.button("÷"): add_to_calc("/")
    if row2_c5.button("sqrt (√)"): add_to_calc("math.sqrt(")
    
    # Baris 3
    if row3_c1.button("4"): add_to_calc("4")
    if row3_c2.button("5"): add_to_calc("5")
    if row3_c3.button("6"): add_to_calc("6")
    if row3_c4.button("×"): add_to_calc("*")
    if row3_c5.button("("): add_to_calc("(")
    
    # Baris 4
    if row4_c1.button("1"): add_to_calc("1")
    if row4_c2.button("2"): add_to_calc("2")
    if row4_c3.button("3"): add_to_calc("3")
    if row4_c4.button("-"): add_to_calc("-")
    if row4_c5.button(")"): add_to_calc(")")

    col_fin1, col_fin2, col_fin3 = st.columns([2, 1, 2])
    if col_fin1.button("0"): add_to_calc("0")
    if col_fin2.button("+"): add_to_calc("+")
    
    if col_fin3.button("== HITUNG HASIL =="):
        try:
            expr = st.session_state.calc_expression
            hasil_eval = eval(expr, {"math": math})
            st.success(f"Hasil Evaluasi Akhir: {hasil_eval}")
            st.session_state.calc_expression = str(hasil_eval)
        except Exception:
            st.error("Format Persamaan Error/Salah Tulis. Cek Kurung Tutup Anda.")
    
