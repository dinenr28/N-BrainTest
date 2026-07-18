import streamlit as st

# ==========================================
# 1. DATABASE SOAL MATEMATIKA
# ==========================================
MATEMATIKA_DATA = {
    "SD": [
        {
            "id": "mat-sd-01",
            "judul": "Pecahan Sederhana",
            "isi_konten": "Pecahan terdiri dari pembilang (atas) dan penyebut (bawah). Contoh: 1/2 berarti 1 bagian dari total 2 bagian.",
            "soal_latihan": [
                {
                    "id": "mat-sd-q1",
                    "tipe": "pilihan_ganda",
                    "pertanyaan": "Bentuk paling sederhana dari 2/4 adalah...",
                    "pilihan": ["A. 1/2", "B. 1/3", "C. 1/4", "D. 2/2"],
                    "kunci_jawaban": "A",
                    "pembahasan": "Bagi pembilang dan penyebut dengan angka 2. Hasilnya 1/2."
                }
            ]
        }
    ],
    "SMP": [
        {
            "id": "mat-smp-01",
            "judul": "Aljabar Dasar",
            "isi_konten": "Aljabar menggunakan variabel (huruf) untuk mewakili angka yang belum diketahui. Contoh: x + 5 = 7, maka x = 2.",
            "soal_latihan": [
                {
                    "id": "mat-smp-q1",
                    "tipe": "pilihan_ganda",
                    "pertanyaan": "Jika 2x = 10, berapakah nilai x?",
                    "pilihan": ["A. 2", "B. 3", "C. 5", "D. 10"],
                    "kunci_jawaban": "C",
                    "pembahasan": "Bagi kedua sisi dengan angka 2. x = 10 / 2 = 5."
                }
            ]
        }
    ],
    "SMA": [
        {
            "id": "mat-sma-01",
            "judul": "Turunan Fungsi Aljabar",
            "isi_konten": "Ingat rumus utama turunan: Jika f(x) = x^n, maka turunan pertamanya adalah f'(x) = n * x^(n-1).",
            "soal_latihan": [
                {
                    "id": "mat-sma-q1",
                    "tipe": "pilihan_ganda",
                    "pertanyaan": "Turunan pertama dari f(x) = 3x^2 adalah...",
                    "pilihan": ["A. 3x", "B. 6x", "C. 6x^2", "D. 2x"],
                    "kunci_jawaban": "B",
                    "pembahasan": "Kalikan pangkat dengan koefisien: 2 * 3x = 6x."
                },
                {
                    "id": "mat-sma-q2",
                    "tipe": "essay",
                    "pertanyaan": "Berapakah nilai turunan dari f(x) = 5x?",
                    "kunci_jawaban": "5",
                    "pembahasan": "Turunan dari x adalah 1, sehingga turunan dari 5x adalah 5."
                }
            ]
        }
    ]
}

PRE_POST_MATEMATIKA = {
    "pre_test": {
        "SD": [{"id": "pre-mat-sd", "tipe": "pilihan_ganda", "pertanyaan": "1 + 1 = ...", "pilihan": ["A. 2", "B. 3"], "kunci_jawaban": "A", "pembahasan": "Penjumlahan dasar."}],
        "SMP": [{"id": "pre-mat-smp", "tipe": "pilihan_ganda", "pertanyaan": "Hasil dari -5 + 3 adalah...", "pilihan": ["A. -2", "B. 2", "C. 8", "D. -8"], "kunci_jawaban": "A", "pembahasan": "-5 ditambah 3 sama dengan -2."}],
        "SMA": [{"id": "pre-mat-sma", "tipe": "pilihan_ganda", "pertanyaan": "Nilai dari log 10 adalah...", "pilihan": ["A. 0", "B. 1", "C. 10"], "kunci_jawaban": "B", "pembahasan": "Logaritma basis 10 dari 10 adalah 1."}]
    },
    "post_test": {
        "SD": [{"id": "post-mat-sd", "tipe": "pilihan_ganda", "pertanyaan": "2 - 1 = ...", "pilihan": ["A. 1", "B. 0"], "kunci_jawaban": "A", "pembahasan": "Pengurangan dasar."}],
        "SMP": [{"id": "post-mat-smp", "tipe": "pilihan_ganda", "pertanyaan": "Hasil dari (-2) x 3 adalah...", "pilihan": ["A. -6", "B. 6", "C. -5"], "kunci_jawaban": "A", "pembahasan": "Negatif dikali positif hasilnya negatif."}],
        "SMA": [{"id": "post-mat-sma", "tipe": "pilihan_ganda", "pertanyaan": "Nilai dari 2^3 adalah...", "pilihan": ["A. 6", "B. 8", "C. 9"], "kunci_jawaban": "B", "pembahasan": "2 x 2 x 2 = 8."}]
    }
}

# ==========================================
# 2. LOGIKA HITUNG SKOR
# ==========================================
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

# ==========================================
# 3. TAMPILAN UTAMA APLIKASI
# ==========================================
st.title("🔢 Aplikasi Belajar Matematika")

jenjang = st.selectbox("Pilih Jenjang Sekolah:", ["SD", "SMP", "SMA"])

data_materi = MATEMATIKA_DATA.get(jenjang, [])
tes_data = PRE_POST_MATEMATIKA

menu = st.radio("Pilih Aktivitas:", ["Pre-Test", "Belajar Materi & Latihan", "Post-Test"], horizontal=True)

if menu == "Belajar Materi & Latihan":
    if not data_materi:
        st.info("Materi belum tersedia untuk jenjang ini.")
    else:
        judul_materi = st.selectbox("Pilih Materi:", [m["judul"] for m in data_materi])
        materi_terpilih = next(m for m in data_materi if m["judul"] == str(judul_materi))
        
        st.subheader(f"📖 Materi: {materi_terpilih['judul']}")
        st.write(materi_terpilih["isi_konten"])
        
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
    tipe_tes = "pre_test" if menu == "Pre-Test" else "post_test"
    soal_tes = tes_data[tipe_tes].get(jenjang, [])
    
    if not soal_tes:
        st.info(f"Soal {menu} belum tersedia untuk jenjang ini.")
    else:
        st.subheader(f"📝 {menu} - Matematika {jenjang}")
        jawaban_user = {}
        for soal in soal_tes:
            st.write(soal["pertanyaan"])
            jawaban_user[soal["id"]] = st.radio("Pilih jawaban:", soal["pilihan"], key=soal["id"])[0]
            
        if st.button(f"Selesaikan {menu}"):
            skor = hitung_skor(soal_tes, jawaban_user)
            st.success(f"Hasil Akhir {menu}: {skor} / 100")
