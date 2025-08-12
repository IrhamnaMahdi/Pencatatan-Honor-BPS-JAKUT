import streamlit as st
import pandas as pd
import os
import base64

# ---------- Background ----------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64("images/background.png")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Fungsi untuk load dan simpan ----------
def load_data(file_path, default_data):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        df = pd.DataFrame(default_data)
        df.to_csv(file_path, index=False)
        return df

def save_data(file_path, df):
    df.to_csv(file_path, index=False)

# ---------- Inisialisasi ----------
if "page" not in st.session_state:
    st.session_state.page = "bulan"

def go_to(page):
    st.session_state.page = page
    st.rerun()

# File penyimpanan
Pendataan_Jan = "pendataan_jan.csv"
Pendataan_Feb = "pendataan_feb.csv"
Pendataan_Mar = "pendataan_mar.csv"
Pendataan_Apr = "pendataan_apr.csv"
Pendataan_Mei = "pendataan_mei.csv"
Pendataan_Jun = "pendataan_jun.csv"
Pendataan_Jul = "pendataan_jul.csv"
Pendataan_Agu = "pendataan_agu.csv"
Pendataan_Sep = "pendataan_sep.csv"
Pendataan_Okt = "pendataan_okt.csv"
Pendataan_Nov = "pendataan_nov.csv"
Pendataan_Des = "pendataan_des.csv"

Pengolahan_Jan = "pengolahan_jan.csv"
Pengolahan_Feb = "pengolahan_feb.csv"
Pengolahan_Mar = "pengolahan_mar.csv"
Pengolahan_Apr = "pengolahan_apr.csv"
Pengolahan_Mei = "pengolahan_mei.csv"
Pengolahan_Jun = "pengolahan_jun.csv"
Pengolahan_Jul = "pengolahan_jul.csv"
Pengolahan_Agu = "pengolahan_agu.csv"
Pengolahan_Sep = "pengolahan_sep.csv"
Pengolahan_Okt = "pengolahan_okt.csv"
Pengolahan_Nov = "pengolahan_nov.csv"
Pengolahan_Des = "pengolahan_des.csv"

# Data awal
default_pml_ppl = {
    "Nama Mitra": [],
    "Kategori": [],
    "Sub Kategori": [],
    "Honor": []
}

default_pengolahan = {
    "Nama Mitra": [],
    "Kategori": [],
    "Sub Kategori": [],
    "Honor": []
}

kategori_dict = {
    "A. PUBLIKASI/LAPORAN STATISTIK NERACA PENGELUARAN (2898.BMA.007.005.A.521213)": [
        "Honor petugas pendataan lapangan survei penyusunan disagregasi pmtb di kab/kota",
        "Honor petugas pendataan lapangan sklnpt",
        "Honor petugas pendataan lapangan skps",
        "Honor petugas pendataan lapangan sksppi",
        "Honor petugas pendataan lapangan updating direktori lnprt di kab/kota",
        "Honor petugas pengolahan survei penyusunan disagregasi pmtb di kab/kota (non pns)",
        "Honor petugas pengolahan survei SKPS"
    ],
    "B. PUBLIKASI/LAPORAN NERACA PRODUKSI (2899.BMA.006.005A.521213)": [
        "Honor petugas pendataan lapangan survei in-depth study seea",
        "Honor petugas pendataan lapangan survei khusus neraca produksi",
        "Honor petugas pendataan lapangan survei sktnp barang",
        "Honor petugas pendataan lapangan survei SKTNP Jasa",
        "Honor petugas pengolahan survei In-depth Study SEEA",
        "Honor petugas pengolahan survei sknp barang",
        "Honor petugas pengolahan survei sktnp barang",
        "Honor petugas pengolahan survei SKTNP Jasa"
    ],
    "C. PUBLIKASI/LAPORAN STATISTIK DISTRIBUSI (2902.BMA.004.005A.521213)": [
        "Honor petugas pendataan lapangan Survei Jasa Penunjang Angkutan (Pergudangan dan Kurir)",
        "Honor petugas pendataan lapangan survei perdagangan barang domestic",
        "Honor petugas pendataan lapangan Survei Pola Distribusi Barang",
        "Honor petugas pendataan lapangan Survei Pola Usaha Non Pertanian",
        "Honor petugas pengolahan survei perdagangan barang domestik",
        "Honor petugas pengolahan Survei Pola Usaha Non Pertanian",
        "Honor petugas pengolahan survei pola distribusi barang"
    ],
    "D. PUBLIKASI/LAPORAN SENSUS EKONOMI (2902.BMA.006.005A.521213)": [
        "Honor petugas pendataan lapangan (pemetaan)",
        "Honor petugas pemeriksa lapangan (non organik)",
        "Honor petugas pemeriksa lapangan (organik)",
        "Honor petugas pengolahan peta dan muatan",
        "Honor pengawas pengolahan peta dan muatan",
        "Honor petugas updating direktori usaha/perusahaan ekonomi lanjutan"
    ],
    "E. PUBLIKASI/LAPORAN STATISTIK HARGA (2903.BMA.009.005A.521213)": [
        "Honor Petugas Pendataan Lapangan Updating Survei Kesejahteraan Petani",
        "Honor Petugas Pengolahan Updating Survei Kesejahteraan Petani",
        "Honor Petugas Pendataan Lapangan Survei Kesejahteraan Petani",
        "Honor Petugas Pengolahan Survei Kesejahteraan Petani",
        "Honor petugas pendataan lapangan Survei Harga Kemahalan Konstruksi",
        "Honor petugas pengolahan Survei Harga Kemahalan Konstruksi)",
        "Honor petugas pendataan lapangan Survei Harga Perdagangan Besar)",
        "Honor petugas pendataan lapangan Survei Harga Mesin dan Peralatan (SHMP)",
        "Honor petugas pendataan lapangan Survei Harga Perumahan dan Properti (SHPP)",
        "Honor petugas pendataan lapangan Survei Harga Perdagangan Besar Mingguan",
        "Honor petugas pengolahan Survei Harga Perdagangan Besar",
        "Honor petugas pengolahan data hasil Honor petugas pengolahan Survei Harga Mesin dan Peralatan (SHMP)",
        "Honor petugas pengolahan Survei Harga Perumahan dan Properti (SHPP)",
        "Honor petugas pengolahan Survei Harga Perdagangan Besar Mingguan",
        "Honor petugas pendataan lapangan Survei Harga Konsumen Perdesaan (HKD)",
        "honor petugas pendataan lapangan survei harga konsumen perdesaan (hkd) non pns",
        "Honor petugas pendataan lapangan Survei Harga Produsen Perdesaan (HD)",
        "Honor petugas pengolahan Survei Harga Konsumen Perdesaan (HKD)",
        "Honor petugas pengolahan Survei Harga Produsen Perdesaan (HD)",
        "Honor petugas pendataan lapangan Survei Harga Produsen Sektor Industri Pengolahan dan Sektor Pertambangan dan Penggalian (HP)",
        "Honor petugas pendataan lapangan Survei Harga Produsen Sektor Jasa (HPJ)",
        "Honor petugas pendataan lapangan Survei Harga Produsen Sektor Pertanian (HPT)",
        "Honor petugas pendataan lapangan Survei Harga Produsen Identifikasi Komoditas Utama",
        "Honor petugas pengolahan Survei Harga Produsen Sektor Industri Pengolahan dan Sektor Pertambangan dan Penggalian (HP)",
        "Honor petugas pengolahan Survei Harga Produsen Sektor Jasa (HPJ)",
        "Honor petugas pengolahan Survei Harga Produsen Sektor Pertanian (HPT)",
        "Honor petugas pendataan lapangan Survei Harga Produsen Beras di Penggilingan (HPBG)",
        "Honor petugas pengolahan Survei Harga Produsen Beras di Penggilingan (HPBG)"
    ],
    "F. PUBLIKASI/LAPORAN PENYUSUNAN INFLASI (2903.QMA.006.005A.521213)":[
        "Honor petugas pendataan lapangan Survei Harga Konsumen (HK 1.1 pasar)",
        "Honor petugas pendataan lapangan Survei Harga Konsumen (HK 1.2 pasar)",
        "Honor petugas pendataan lapangan Survei Harga Konsumen (HK 2.1 pasar)",
        "Honor petugas pendataan lapangan Survei Harga Konsumen (HK 2.1 outlet)",
        "Honor petugas pendataan lapangan Survei Harga Konsumen (HK 2.2 pasar)",
        "Honor petugas pendataan lapangan Survei Harga Konsumen (HK 2.2 outlet)",
        "Honor petugas pendataan lapangan Survei Harga Konsumen (HK 3 pasar)",
        "Honor petugas pendataan lapangan Survei Harga Konsumen (HK 3 outlet)",
        "Honor petugas pendataan lapangan Survei Harga Konsumen (HK 4; HK 5; dan HK 6)",
        "Honor petugas pendataan lapangan Survei Pedagang Beras",
        "Honor petugas pendataan lapangan Survei Volume Penjualan Komoditas Spesifik",
        "Honor petugas pendataan lapangan Honor petugas pendataan lapangan Listing Survei Pedagang Beras",
        "Honor petugas pendataan lapangan Honor petugas pengolahan lapangan Survei Harga Konsumen (HK 1.1 pasar)",
        "Honor petugas pengolahan lapangan Survei Harga Konsumen (HK 1.2 pasar)",
        "Honor petugas pengolahan lapangan Survei Harga Konsumen (HK 2.1 pasar)",
        "Honor petugas pengolahan lapangan Survei Harga Konsumen (HK 2.1 outlet)",
        "Honor petugas pengolahan lapangan Survei Harga Konsumen (HK 2.2 pasar)",
        "Honor petugas pengolahan lapangan Survei Harga Konsumen (HK 2.2 outlet)",
        "Honor petugas pengolahan lapangan Survei Harga Konsumen (HK 3 pasar)",
        "Honor petugas pengolahan lapangan Survei Harga Konsumen (HK 3 outlet)",
        "Honor petugas pengolahan lapangan Survei Harga Konsumen (HK 4; HK 5; dan HK 6)",
        "Honor petugas pengolahan Listing Survei Pedagang Beras",
        "Honor petugas pengolahan Survei Pedagang Beras",
        "Honor petugas pengolahan Survei Volume Komoditas Spesifik (SVK)",
    ],
    "G. STATISTIK INDUSTRI, PERTAMBANGAN DAN PENGGALIAN, ENERGI, DAN KONSTRUKSI (2904.BMA.006.005A.521213)":[
        "Honor petugas pendataan listing Survei IMK Tahunan",
        "Honor petugas pendataan lapangan pemutakhiran direktori perusahaan awal (dpa)",
        "Honor petugas pendataan lapangan survei captive power",
        "Honor petugas pendataan lapangan Survei Industri Besar dan Sedang (IBS) Bulanan",
        "Honor petugas pendataan lapangan Survei Perusahaan Konstruksi Tahunan",
        "Honor petugas pendataan lapangan Survei Perusahaan Konstruksi Triwulanan",
        "Honor petugas pendataan lapangan Survei Perusahaan Pertambangan Non Migas",
        "Honor petugas pendataan lapangan survei tahunan perusahaan industri manufaktur",
        "Honor petugas pendataan lapangan survei vimk24 triwulanan triwulan 4",
        "Honor petugas pendataan lapangan Survei IMK Tahunan",
        "Honor petugas pendataan lapangan Survei IMK Triwulanan",
        "Honor petugas pendataan lapangan updating direktori perusahaan konstruksi (udp)",
        "Honor petugas pendataan lapangan updating direktori perusahaan pertambangan dan energi",
        "Honor petugas pendataan lapangan listing survei IMK Triwulanan",
        "Honor petugas pendataan lapangan Survei Karakteristik Usaha Integrasi",
        "Honor petugas pengolahan listing Survei IMK Tahunan",
        "Honor petugas pengolahan listing Survei IMK Triwulanan",
        "Honor petugas pengolahan survei captive power",
        "Honor petugas pengolahan Survei Perusahaan Konstruksi Tahunan",
        "Honor petugas pengolahan Survei Perusahaan Konstruksi Triwulanan",
        "Honor petugas pengolahan Survei Perusahaan Pertambangan Non Migas",
        "Honor petugas pengolahan survei vimk24 triwulanan iv",
        "Honor petugas pengolahan Survei IMK Tahunan",
        "Honor petugas pengolahan Survei IMK Triwulanan i - iii",
        "Honor petugas pengolahan updating direktori perusahaan konstruksi (udp)",
        "Honor petugas pengolahan updating direktori perusahaan pertambangan dan energi",
        "Honor petugas pengolahan Survei Karakteristik Usaha Integrasi"
    ],
    "H. PUBLIKASI/LAPORAN SAKERNAS (2905.BMA.004.005A.521213)":[ 
        "Honor petugas pemeriksaan lapangan (sakernas agustus non organik)",
        "Honor petugas pemeriksaan lapangan updating listing BS (sakernas agustus non organik)",
        "Honor petugas pendataan lapangan (sakernas agustus)",
        "Honor petugas pendataan lapangan (sakernas februari)",
        "Honor petugas pendataan lapangan updating listing BS (sakernas agustus)",
        "Honor petugas pendataan lapangan updating listing BS (sakernas februari)",
        "Honor petugas pendataan lapangan updating listing BS (sakernas mei)",
        "Honor petugas pendataan lapangan (sakernas mei)",
        "Honor petugas pendataan lapangan updating listing BS (sakernas november)",
        "Honor petugas pendataan lapangan (sakernas november)"
    ],
    "I. PUBLIKASI/LAPORAN STATISTIK KEPENDUDUKAN DAN KETENAGAKERJAAN (2905.BMA.005.005A.521213)":[ 
        "Honor petugas pendataan lapangan updating listing BS (SUPAS 2025)",
        "Honor petugas pemeriksaan lapangan updating listing BS (SUPAS 2025)",
        "Honor petugas pendataan lapangan CAPI (SUPAS 2025)",
        "Honor petugas pemeriksaan lapangan CAPI (SUPAS 2025)"
    ],
    "J. PUBLIKASI/LAPORAN SUSENAS (2906.BMA.006.005A.521213)":[
        "Honor petugas pendataan lapangan (susenas maret 2025)",
        "Honor petugas pendataan lapangan (susenas mkp 2025)",
        "Honor petugas pendataan lapangan updating listing (susenas maret 2025)",
        "Honor petugas pendataan lapangan updating listing (susenas mkp 2025)",
        "Honor petugas pengolahan (susenas maret 2025)",
        "Honor petugas pengolahan (susenas mkp 2025)",
        "Honor petugas pengolahan updating listing (susenas maret 2025)",
        "Honor petugas pengolahan updating listing (susenas mkp 2025)",
        "Honor petugas pemeriksaan updating listing (susenas maret 2025)",
        "Honor petugas pemeriksaan lapangan (susenas maret 2025)",
        "Honor petugas pendataan lapangan (Survei Ekonomi Rumah Tangga Triwulanan (Seruti) terintegrasi Susenas) Triwulan I-2025",
        "Honor petugas pengolahan (Survei Ekonomi Rumah Tangga Triwulanan (Seruti) terintegrasi Susenas)",
        "Honor petugas pendataan lapangan ( Survei Ekonomi Rumah Tangga Triwulanan (Seruti)) Triwulan I-2025",
        "Honor petugas pengolahan (Survei Ekonomi Rumah Tangga Triwulanan (Seruti))"
    ],
    "K. PUBLIKASI/LAPORAN STATISTIK KETAHANAN SOSIAL (2907.BMA.006.005A.521213)":[
        "Honor petugas pendataan lapangan (SPAK)"
    ],
    "L. PUBLIKASI/LAPORAN PENDATAAN PODES (2907.BMA.008.005A.521213)":[
        "Honor petugas pendataan lapangan Pemutakhiran Data Perkembangan Desa"
    ],
    "M. SURVEI NASIONAL LITERASI DAN INKLUSI KEUANGAN":[
        "Honor petugas pendataan Updating listing BS SNLIK",
        "Honor petugas pendataan lapangan SNLIK"
    ],
    "N. STATISTIK KEUANGAN, TEKNOLOGI INFORMASI, DAN PARIWISATA (2908.BMA.004.005A.521213)":[
        "Honor petugas pengolahan Survei Statistik Keuangan BUMD",
        "Honor petugas pengolahan survei SLK Koperasi Simpan Pinjam",
        "Honor petugas pengolahan survei SLK Pedagang Valuta Asing",
        "Honor petugas pengolahan Survei Usaha/Perusahaan Daya Tarik Wisata",
        "Honor petugas pengolahan Survei Usaha/Perusahaan Penyedia Jasa Akomodasi Tahunan",
        "Honor petugas pengolahan Survei Usaha/Perusahaan Penyedia Jasa Akomodasi Bulanan",
        "Honor petugas pengolahan Survei Perusahaan/Usaha Penyedia Makan Minum UMB",
        "Honor Petugas Pendataan Lapangan Survei Lembaga Keuangan Pedagang Valuta Asing",
        "Honor Petugas Pendataan Lapangan Survei Lembaga Keuangan Koperasi Simpan Pinjam",
        "Honor Petugas Pendataan Lapangan Survei Perusahaan/Usaha Penyedia Makan Minum UMB",
        "Honor Petugas Pendataan Lapangan Survei Usaha/Perusahaan Daya Tarik Wisata",
        "Honor Petugas Pendataan Lapangan Survei Usaha/Perusahaan Penyedia Jasa Akomodasi Bulanan",
        "Honor Petugas Pendataan Lapangan Survei Usaha/Perusahaan Penyedia Jasa Akomodasi Tahunan",
        "Honor Petugas Pendataan Lapangan Survei Bidang Usaha Pariwisata (Updating Direktori Survei Usaha Penyedia Jasa Pariwisata)",
        "Honor Petugas Pendataan Lapangan Survei Statistik Keuangan BUMD"
    ],
    "O. PUBLIKASI/LAPORAN STATISTIK E-COMMERCE (2908.BMA.009.005A.521213)":[
        "Honor petugas pendataan lapangan survei e-commerce",
        "Honor petugas pengolahan listing survei e-commerce",
        "Honor Petugas Pendataan Lapangan Listing Survei E-Commerce",
        "Honor petugas pengolahan survei ecommerce"
    ],
    "P. STATISTIK PETERNAKAN, PERIKANAN, DAN KEHUTANAN (2909.BMA.005.005A.521213)":[
        "Honor petugas pendataan lapangan Laporan Triwulanan Pelabuhan Perikanan dan Tempat Pelelangan Ikan",
        "Honor petugas pendataan lapangan Laporan Pemotongan Ternak Bulanan",
        "Honor petugas pendataan lapangan survei perusahaan kehutanan",
        "Honor petugas pendataan lapangan Laporan Tahunan Perusahaan Penangkapan Ikan"
    ],
    "Q. PUBLIKASI/ LAPORAN STATISTIK TANAMAN PANGAN (2910.BMA.007.005A.521213)":[
        "Honor petugas pendataan lapangan updating Survei Pertanian Tanaman Pangan/Ubinan",
        "Honor petugas pengolahan updating Survei Pertanian Tanaman Pangan/Ubinan",
        "Honor petugas pendataan lapangan Survei Pertanian Tanaman Pangan/Ubinan",
        "Honor petugas pengolahan Survei Pertanian Tanaman Pangan/Ubinan",
        "Honor petugas pendataan lapangan Kerangka Sampel Area (KSA) Padi"
    ],
    "R. STATISTIK  STATISTIK HORTIKULTURA DAN PERKEBUNAN (2910.BMA.008.005A.521213)":[
        "Honor petugas pendataan lapangan Updating Direktori Perusahaan Pertanian (DPP) dan Direktori Usaha Pertanian Lainnya (DUTL)",
        "Honor petugas pendataan lapangan survei usaha hortikultura lainnya (vn-horti)",
        "Honor petugas pengolahan survei usaha hortikultura lainnya",
        "Honor petugas pengolahan Updating Direktori Perusahaan Pertanian (DPP) dan Direktori Usaha Pertanian Lainnya (DUTL)"		
    ]
}

# ---------------- Halaman Pilih Bulan ----------------
if st.session_state.page == "bulan":
    st.markdown(
    """
    <style>
    .center-title {
        text-align: center;
        color: darkblue;
        font-size: 40px;
        font-weight: bold;
    }
    </style>
    <h1 class="center-title">PILIH BULAN PENCATATAN</h1>
    """,
    unsafe_allow_html=True
    )
    if st.button("JANUARI", use_container_width=True):
        go_to("JAN")
    elif st.button("FEBRUARI", use_container_width=True):
        go_to("FEB")
    elif st.button("MARET", use_container_width=True):
        go_to("MAR")
    elif st.button("APRIL", use_container_width=True):
        go_to("APR")
    elif st.button("MEI", use_container_width=True):
        go_to("MEI")
    elif st.button("JUNI", use_container_width=True):
        go_to("JUN")
    elif st.button("JULI", use_container_width=True):
        go_to("JUL")
    elif st.button("AGUSTUS", use_container_width=True):
        go_to("AGU")
    elif st.button("SEPTEMBER", use_container_width=True):
        go_to("SEP")
    elif st.button("OKTOBER", use_container_width=True):
        go_to("OKT")
    elif st.button("NOVEMBER", use_container_width=True):
        go_to("NOV")
    elif st.button("DESEMBER", use_container_width=True):
        go_to("DES")
    
# ---------------- JANUARI ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "JAN":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_jan")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_jan")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_jan":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Jan, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan Januari.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Jan, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Jan, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("JAN")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_jan")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_jan":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Jan, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan Januari.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Jan, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Jan, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("JAN")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_jan")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_jan":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Jan, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Jan, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_jan")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_jan":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Jan, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Jan, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_jan")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- FEBRUARI ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "FEB":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_feb")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_feb")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_feb":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Feb, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan Februari.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Feb, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Feb, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("FEB")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_feb")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_feb":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Feb, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan Februari.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Feb, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Feb, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("FEB")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_feb")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_feb":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Feb, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Feb, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_feb")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_feb":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Feb, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Feb, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_feb")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- MARET ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "MAR":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_mar")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_mar")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_mar":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Mar, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan Maret.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Mar, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Mar, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("MAR")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_mar")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_mar":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Mar, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan Maret.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Mar, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Mar, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("MAR")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_mar")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_mar":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Mar, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Mar, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_mar")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_mar":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Mar, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Mar, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_mar")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- APRIL ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "APR":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_apr")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_apr")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_apr":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Apr, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan April.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Apr, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Apr, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("APR")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_apr")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_apr":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Apr, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan April.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Apr, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Apr, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("APR")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_apr")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_apr":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Apr, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Apr, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_apr")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_apr":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Apr, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Apr, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_apr")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- MEI ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "MEI":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_mei")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_mei")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_mei":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Mei, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan Mei.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Mei, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Mei, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("MEI")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_mei")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_mei":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Mei, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan Mei.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Mei, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Mei, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("MEI")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_mei")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_mei":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Mei, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Mei, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_mei")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_mei":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Mei, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Mei, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_mei")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- JUNI ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "JUN":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_jun")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_jun")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_jun":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Jun, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan Juni.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Jun, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Jun, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("JUN")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_jun")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_jun":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Jun, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan Juni.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Jun, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Jun, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("JUN")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_jun")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_jun":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Jun, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Jun, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_jun")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_jun":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Jun, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Jun, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_jun")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- JULI ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "JUL":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_jul")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_jul")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_jul":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Jul, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan Juli.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Jul, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Jul, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("JUL")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_jul")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_jul":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Jul, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan Juli.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Jul, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Jul, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("JUL")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_jul")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_jul":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Jul, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Jul, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_jul")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_jul":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Jul, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Jul, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_jul")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- AGUSTUS ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "AGU":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_agu")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_agu")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_agu":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Agu, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan Agustus.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Agu, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Agu, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("AGU")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_agu")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_agu":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Agu, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan Agustus.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Agu, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Agu, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("AGU")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_agu")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_agu":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Agu, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Agu, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_agu")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_agu":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Agu, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Agu, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_agu")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- SEPTEMBER ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "SEP":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_sep")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_sep")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_sep":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Sep, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan September.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Sep, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Sep, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("SEP")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_sep")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_sep":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Sep, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan September.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Sep, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Sep, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("SEP")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_sep")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_sep":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Sep, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Sep, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_sep")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_sep":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Sep, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Sep, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_sep")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- OKTOBER ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "OKT":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_okt")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_okt")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_okt":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Okt, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan Oktober.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Okt, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Okt, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("OKT")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_okt")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_okt":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Okt, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan Oktober.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Okt, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Okt, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("OKT")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_okt")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_okt":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Okt, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Okt, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_okt")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_okt":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Okt, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Okt, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_okt")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- NOVEMBER ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "NOV":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_nov")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_nov")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_nov":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Nov, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan November.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Nov, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Nov, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("NOV")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_nov")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_nov":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Nov, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan November.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Nov, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Nov, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("NOV")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_nov")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_nov":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Nov, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Nov, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_nov")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_nov":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Nov, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Nov, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_nov")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- DESEMBER ----------------
# ---------------- Halaman Home ----------------
elif st.session_state.page == "DES":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Petugas Pendataan", use_container_width=True):
            go_to("pendataan_des")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan_des")
    if st.button("Back"):
        go_to("bulan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pendataan_des":
    st.title("Daftar Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Des, default_pml_ppl)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 4_000_000
        total_diterima = st.session_state.data_pml_ppl.loc[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pml_ppl[
            st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pml_ppl.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pendataan Desember.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pml_ppl = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] != pilihan_nama]
            save_data(Pendataan_Des, st.session_state.data_pml_ppl)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pml_ppl = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pendataan_Des, st.session_state.data_pml_ppl)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("DES")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1_des")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan_des":
    st.title("Daftar Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Des, default_pengolahan)
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        batas_honor = 3_700_000
        total_diterima = st.session_state.data_pengolahan.loc[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama, "Honor"
        ].sum()
        sisa_honor = batas_honor - total_diterima

        detail = st.session_state.data_pengolahan[
            st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama
        ][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        st.write(f"**Total Honor :** Rp {total_diterima:,.0f}")
        st.write(f"**Sisa Honor :** Rp {sisa_honor:,.0f}")

    csv_data = st.session_state.data_pengolahan.to_csv(index=False).encode("utf-8")
    # Tombol download CSV
    col1, col2, col3 = st.columns(3)
    # Tombol download CSV
    with col1:
        st.download_button("Download CSV", csv_data, "Honor Petugas Pengolahan Desember.csv", "text/csv")
    # Tombol hapus data mitra terpilih
    with col2:
        if st.button("Hapus Mitra Terpilih"):
            st.session_state.data_pengolahan = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] != pilihan_nama]
            save_data(Pengolahan_Des, st.session_state.data_pengolahan)
            st.success(f"Data {pilihan_nama} berhasil dihapus!")
            st.rerun()
    # Tombol hapus semua data
    with col3:
        if st.button("Hapus Semua Data"):
            st.session_state.data_pengolahan = pd.DataFrame(columns=["Nama Mitra", "Kategori", "Sub Kategori", "Honor"])
            save_data(Pengolahan_Des, st.session_state.data_pengolahan)
            st.success("Semua data berhasil dihapus!")
            st.rerun()

    if st.button("Kembali", use_container_width=True):
        go_to("DES")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2_des")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1_des":
    st.title("Catat Honor Petugas Pendataan")
    st.session_state.data_pml_ppl = load_data(Pendataan_Des, default_pml_ppl)

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 4_000_000
    total_diterima = st.session_state.data_pml_ppl.loc[
        st.session_state.data_pml_ppl["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pendataan_Des, st.session_state.data_pml_ppl)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pendataan_des")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2_des":
    st.title("Catat Honor Petugas Pengolahan")
    st.session_state.data_pengolahan = load_data(Pengolahan_Des, default_pengolahan)
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Masukkan Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    volume_baru = st.number_input("Volume", min_value=0, step=1)
    harga_satuan_baru = st.number_input("Harga Satuan", min_value=0, step=1000)
    honor_baru = volume_baru * harga_satuan_baru

    batas_honor = 3_700_000
    total_diterima = st.session_state.data_pengolahan.loc[
        st.session_state.data_pengolahan["Nama Mitra"] == nama_baru, "Honor"
    ].sum()
    sisa_honor = batas_honor - total_diterima

    if st.button("Catat Honor"):
        if honor_baru > sisa_honor:
            st.error("Honor melebihi batas yang diperbolehkan!")
        else:
            st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
                nama_baru, kategori_baru, sub_kategori_baru, honor_baru
            ]
            save_data(Pengolahan_Des, st.session_state.data_pengolahan)
            st.success(f"{nama_baru} Telah Menerima Honor Sebesar Rp {honor_baru} Pada Kegiatan {sub_kategori_baru}!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan_des")
    elif st.button("Home", use_container_width=True):
        go_to("bulan")
