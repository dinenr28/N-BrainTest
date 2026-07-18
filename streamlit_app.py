import streamlit as st

# ==========================================
# 1. DATABASE SOAL MATEMATIKA SUPER BANYAK & SUSAH
# ==========================================
MATEMATIKA_DATA = {
    "SD": [
        {
            "id": "mat-sd-01",
            "judul": "Pecahan, Desimal, dan Persen (HOTS)",
            "isi_konten": "Untuk menyelesaikan soal pecahan cerita, samakan penyebutnya terlebih dahulu atau ubah semua bentuk menjadi desimal agar lebih mudah dihitung.",
            "soal_latihan": [
                {
                    "id": "mat-sd-q1",
                    "tipe": "pilihan_ganda",
                    "pertanyaan": "Ibu membeli 2 1/2 kg tepung. Sebanyak 40% digunakan untuk membuat kue, dan 3/4 kg diberikan kepada tetangga. Sisa tepung Ibu adalah...",
                    "pilihan": ["A. 0,75 kg", "B. 0,65 kg", "C. 0,55 kg", "D. 0,45 kg"],
                    "kunci_jawaban": "A",
                    "pembahasan": "Total = 2,5 kg. Kue = 40% x 2,5 = 1 kg. Diberikan = 3/4 = 0,75 kg. Sisa = 2,5 - 1 - 0,75 = 0,75 kg."
                },
                {
                    "id": "mat-sd-q2",
                    "tipe": "pilihan_ganda",
                    "pertanyaan": "Hasil dari 125% + 2,25 - 4/5 adalah...",
                    "pilihan": ["A. 2,7", "B. 2,5", "C. 3,1", "D. 1,9"],
                    "kunci_jawaban": "A",
                    "pembahasan": "1,25 + 2,25 - 0,8 = 3,5 - 0,8 = 2,7."
                },
                {
                    "id": "mat-sd-q3",
                    "tipe": "essay",
                    "pertanyaan": "Berapakah hasil dari 15 x (24 + 36) : 9?",
                    "kunci_jawaban": "100",
                    "pembahasan": "Kerjakan dalam kurung dulu: 24 + 36 = 60. Lalu kalikan: 15 x 60 = 900. Terakhir bagi: 900 : 9 = 100."
                }
            ]
        }
    ],
    "SMP": [
        {
            "id": "mat-smp-01",
            "judul": "Persamaan Kuadrat & Fungsi Kuadrat",
            "isi_konten": "Akar-akar persamaan kuadrat ax^2 + bx + c = 0 dapat dicari dengan faktorisasi atau rumus abc. Nilai diskriminan (D = b^2 - 4ac) menentukan jenis akar.",
            "soal_latihan": [
                {
                    "id": "mat-smp-q1",
                    "tipe": "pilihan_ganda",
                    "pertanyaan": "Jika salah satu akar dari persamaan x^2 - bx - 24 = 0 adalah -3, maka nilai b adalah...",
                    "pilihan": ["A. -5", "B. 5", "C. -3", "D. 3"],
                    "kunci_jawaban": "B",
                    "pembahasan": "Substitusi x = -3 ke persamaan: (-3)^2 - b(-3) - 24 = 0 -> 9 + 3b - 24 = 0 -> 3b = 15 -> b = 5."
                },
                {
                    "id": "mat-smp-q2",
                    "tipe": "pilihan_ganda",
                    "pertanyaan": "Himpunan penyelesaian dari x^2 - 5x + 6 = 0 adalah...",
                    "pilihan": ["A. {1, 6}", "B. {-2, -3}", "C. {2, 3}", "D. {-1, 6}"],
                    "kunci_jawaban": "C",
                    "pembahasan": "Faktorisasi menjadi (x - 2)(x - 3) = 0. Maka x = 2 atau x = 3."
                },
                {
                    "id": "mat-smp-q3",
                    "tipe": "essay",
                    "pertanyaan": "Berapakah nilai diskriminan dari persamaan x^2 - 4x + 4 = 0?",
                    "kunci_jawaban": "0",
                    "pembahasan": "D = b^2 - 4ac = (-4)^2 - 4(1)(4) = 16 - 16 = 0."
                }
            ]
        }
    ],
    "SMA": [
        {
            "id": "mat-sma-01",
            "judul": "Integral Tentu & Aplikasi Turunan",
            "isi_konten": "Integral merupakan antiturunan. Integral tentu memiliki batas atas dan batas bawah untuk menghitung luas daerah di bawah kurva.",
            "soal_latihan": [
                {
                    "id": "mat-sma-q1",
                    "tipe": "pilihan_ganda",
                    "pertanyaan": "Hasil dari integral tentu ∫ (from 1 to 3) (3x^2 + 2x) dx adalah...",
                    "pilihan": ["A. 34", "B. 26", "C. 28", "D. 32"],
                    "kunci_jawaban": "A",
                    "pembahasan": "Integralkan menjadi [x^3 + x^2] dari 1 ke 3. Masukkan batas atas: 3^3 + 3^2 = 27 + 9 = 36. Batas bawah: 1^3 + 1^2 = 2. Hasil: 36 - 2 = 34."
                },
                {
                    "id": "mat-sma-q2",
                    "tipe": "pilihan_ganda",
                    "pertanyaan": "Persamaan garis singgung kurva y = x^2 - 4x + 3 di titik (1, 0) adalah...",
                    "pilihan": ["A. y = -2x + 2", "B. y = 2x - 2", "C. y = -2x - 2", "D. y = 4x - 4"],
                    "kunci_jawaban": "A",
                    "pembahasan": "m = y' = 2x - 4. Di x = 1, m = 2(1) - 4 = -2. Persamaan garis: y - 0 = -2(x - 1) -> y = -2x + 2."
                },
                {
                    "id": "mat-sma-q3",
                    "tipe": "essay",
                    "pertanyaan": "Tentukan nilai lim (x->3) dari (x^2 - 9) / (x - 3)!",
                    "kunci_jawaban": "6",
                    "pembahasan": "Faktorkan pembilang: (x-3)(x+3)/(x-3) = x + 3. Masukkan nilai x = 3: 3 + 3 = 6."
                }
            ]
        }
    ]
}

PRE_POST_MATEMATIKA = {
    "pre_test": {
        "SD": [{"id": "pre-mat-sd", "tipe": "pilihan_ganda", "pertanyaan": "KPK dari 12 dan 18 adalah...", "pilihan": ["A. 36", "B. 72", "C. 54"], "kunci_jawaban": "A", "pembahasan": "12 = 2^2 x 3, 18 = 2 x 3^2. KPK = 2^2 x 3^2 = 36."}],
        "SMP": [{"id": "pre-mat-smp", "tipe": "pilihan_ganda", "pertanyaan": "Gradien garis yang melalui titik (0,0) dan (3,6) adalah...", "pilihan": ["A. 2", "B. -2", "C. 3"], "kunci_jawaban": "A", "pembahasan": "m = (6 - 0) / (3 - 0) = 2."}],
        "SMA": [{"id": "pre-mat-sma", "tipe": "pilihan_ganda", "pertanyaan": "Nilai dari sin 150 derajat adalah...", "pilihan": ["A. 1/2", "B. -1/2", "C. 1/2 √3"], "kunci_jawaban": "A", "pembahasan": "sin 150 = sin(180 - 30) = sin 30 = 1/2."}]
    },
    "post_test": {
        "SD": [{"id": "post-mat-sd", "tipe": "pilihan_ganda", "pertanyaan": "Sebuah kubus memiliki volume 216 cm³. Panjang rusuknya adalah...", "pilihan": ["A. 6 cm", "B. 7 cm", "C. 8 cm"], "kunci_jawaban": "A", "pembahasan": "Akar pangkat tiga dari 216 adalah 6."}],
        "SMP": [{"id": "post-mat-smp", "tipe": "pilihan_ganda", "pertanyaan": "Jika f(x) = 3x - 5, maka f(2) adalah...", "pilihan": ["A. 1", "B. -1", "C. 6"], "kunci_jawaban": "A", "pembahasan": "f(2) = 3(2) - 5 = 6 - 5 = 1."}],
        "SMA": [{"id": "post-mat-sma", "tipe": "pilihan_ganda", "pertanyaan": "Nilai dari log 1000 dengan basis 10 adalah...", "pilihan": ["A. 3", "B. 2", "C. 4"], "kunci_jawaban": "A", "pembahasan": "10 pangkat 3 = 1000, jadi nilainya 3."}]
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
        if soal['tipe'] == 'pilihan_ganda':
            # Ambil huruf depannya saja (A, B, C, D)
            ans_letter = ans[0].upper() if ans else ""
            if ans_letter == kunci.upper():
                benar += 1
        elif soal['tipe'] == 'essay' and (kunci in ans or ans in kunci):
            benar += 1
    return round((benar / len(daftar_soal)) * 100)

# ==========================================
# 3. TAMPILAN UTAMA APLIKASI
# ==========================================
st.title("🔢 Aplikasi Belajar Matematika (HOTS Edition)")

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
        
        st.subheader("✍️ Soal Latihan Tantangan")
        jawaban_user = {}
        
        for soal in materi_terpilih["soal_latihan"]:
            st.write(f"**{soal['pertanyaan']}**")
            if soal["tipe"] == "pilihan_ganda":
                jawaban_user[soal["id"]] = st.radio("Pilih jawaban:", soal["pilihan"], key=soal["id"])
            else:
                jawaban_user[soal["id"]] = st.text_input("Tulis jawaban angka/kata kamu:", key=soal["id"])
        
        if st.button("Kirim Jawaban & Lihat Pembahasan"):
            skor = hitung_skor(materi_terpilih["soal_latihan"], jawaban_user)
            st.success(f"Skor kamu: {skor} / 100")
            
            st.subheader("💡 Pembahasan Analitis Soal:")
            for soal in materi_terpilih["soal_latihan"]:
                st.info(f"Soal: {soal['pertanyaan']}\n\n**Kunci Jawaban:** {soal['kunci_jawaban']}\n\n**Cara Pengerjaan:** {soal['pembahasan']}")

else:
    tipe_tes = "pre_test" if menu == "Pre-Test" else "post_test"
    soal_tes = tes_data[tipe_tes].get(jenjang, [])
    
    if not soal_tes:
        st.info(f"Soal {menu} belum tersedia untuk jenjang ini.")
    else:
        st.subheader(f"📝 {menu} - Matematika {jenjang}")
        jawaban_user = {}
        for soal in soal_tes:
            st.write(f"**{soal['pertanyaan']}**")
            jawaban_user[soal["id"]] = st.radio("Pilih jawaban:", soal["pilihan"], key=soal["id"])
            
        if st.button(f"Selesaikan {menu}"):
            skor = hitung_skor(soal_tes, jawaban_user)
            st.success(f"Hasil Akhir {menu}: {skor} / 100")
