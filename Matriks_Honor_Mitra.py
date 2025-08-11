import streamlit as st
import pandas as pd
import os

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
    st.session_state.page = "home"

def go_to(page):
    st.session_state.page = page
    st.rerun()

# File penyimpanan
file_pml_ppl = "data_pml_ppl.csv"
file_pengolahan = "data_pengolahan.csv"

# Data awal
default_pml_ppl = {
    "Nama Mitra": ["Andi", "Budi", "Citra"],
    "Kategori": ["Lapangan", "Lapangan", "Lapangan"],
    "Sub Kategori": ["PML", "PPL", "PML"],
    "Honor": [1500000, 1200000, 1400000]
}

default_pengolahan = {
    "Nama Mitra": ["Dewi", "Eka", "Fajar"],
    "Kategori": ["Pengolahan", "Pengolahan", "Pengolahan"],
    "Sub Kategori": ["Entri Data", "QC Data", "Entri Data"],
    "Honor": [1300000, 1600000, 1250000]
}

# Load data dari CSV
if "data_pml_ppl" not in st.session_state:
    st.session_state.data_pml_ppl = load_data(file_pml_ppl, default_pml_ppl)

if "data_pengolahan" not in st.session_state:
    st.session_state.data_pengolahan = load_data(file_pengolahan, default_pengolahan)

kategori_dict = {
    "A. PUBLIKASI/LAPORAN STATISTIK NERACA PENGELUARAN": [
        "Honor petugas pendataan lapangan survei penyusunan disagregasi pmtb di kab/kota",
        "Honor petugas pendataan lapangan sklnpt",
        "Honor petugas pendataan lapangan skps",
        "Honor petugas pendataan lapangan sksppi",
    ],
    "B. PUBLIKASI/LAPORAN STATISTIK NERACA PENGELUARAN": [
        "Honor petugas pendataan lapangan updating direktori lnprt di kab/kota",
        "Honor petugas pengolahan survei penyusunan disagregasi pmtb di kab/kota (non pns)",
        "Honor petugas pengolahan survei SKPS",
    ],
}

# ---------------- Halaman Home ----------------
if st.session_state.page == "home":
    st.title("Pilih Jenis Mitra")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("PML & PPL", use_container_width=True):
            go_to("pml_ppl")
    with col2:
        if st.button("Petugas Pengolahan", use_container_width=True):
            go_to("pengolahan")

# ---------------- Halaman PML & PPL ----------------
elif st.session_state.page == "pml_ppl":
    st.title("Daftar Mitra PML & PPL")
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pml_ppl["Nama Mitra"].unique())

    if pilihan_nama:
        detail = st.session_state.data_pml_ppl[st.session_state.data_pml_ppl["Nama Mitra"] == pilihan_nama][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        total_honor = detail["Honor"].sum()
        st.write(f"**Total Honor :** Rp {total_honor:,.0f}")

    if st.button("Kembali", use_container_width=True):
        go_to("home")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.1")

# ---------------- Halaman Pengolahan ----------------
elif st.session_state.page == "pengolahan":
    st.title("Daftar Petugas Pengolahan")
    pilihan_nama = st.selectbox("Pilih Mitra", st.session_state.data_pengolahan["Nama Mitra"].unique())

    if pilihan_nama:
        detail = st.session_state.data_pengolahan[st.session_state.data_pengolahan["Nama Mitra"] == pilihan_nama][["Kategori", "Sub Kategori", "Honor"]]
        st.table(detail)

        total_honor = detail["Honor"].sum()
        st.write(f"**Total Honor :** Rp {total_honor:,.0f}")

    if st.button("Kembali", use_container_width=True):
        go_to("home")
    elif st.button("Catat Honor", use_container_width=True):
        go_to("3.2")

# ---------------- Halaman Catat Honor Mitra PPL & PML ----------------
elif st.session_state.page == "3.1":
    st.title("Catat Honor Mitra PPL & PML")
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    honor_baru = st.number_input("Masukkan Honor", min_value=0)

    if st.button("Catat  Honor"):
        st.session_state.data_pml_ppl.loc[len(st.session_state.data_pml_ppl)] = [
            nama_baru, kategori_baru, sub_kategori_baru, honor_baru
        ]
        save_data(file_pml_ppl, st.session_state.data_pml_ppl)
        st.success(f"Honor {nama_baru} berhasil dicatat!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pml_ppl")
    elif st.button("Home", use_container_width=True):
        go_to("home")

# ---------------- Halaman Catat Honor Petugas Pengolahan ----------------
elif st.session_state.page == "3.2":
    st.title("Catat Honor Petugas Pengolahan")
    st.subheader("Tambah Mitra Baru")

    nama_baru = st.text_input("Nama Mitra")
    kategori_baru = st.selectbox("Pilih Kategori", list(kategori_dict.keys()))
    sub_kategori_baru = st.selectbox("Pilih Sub Kategori", kategori_dict[kategori_baru])
    honor_baru = st.number_input("Masukkan Honor", min_value=0)

    if st.button("Catat  Honor"):
        st.session_state.data_pengolahan.loc[len(st.session_state.data_pengolahan)] = [
            nama_baru, kategori_baru, sub_kategori_baru, honor_baru
        ]
        save_data(file_pengolahan, st.session_state.data_pengolahan)
        st.success(f"Honor {nama_baru} berhasil dicatat!")
    
    if st.button("Cek Riwayat Honor", use_container_width=True):
        go_to("pengolahan")
    elif st.button("Home", use_container_width=True):
        go_to("home")
