import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def fungsi_eksponen(x, a, b):
    """Menghitung nilai fungsi eksponen f(x) = a * b^x."""
    return a * (b ** x)

def main():
    st.set_page_config(layout="wide")
    
    # 1. Header dan Deskripsi
    st.title("🔬 Virtual Lab: Fungsi Naik & Fungsi Eksponen")
    st.markdown("""
        Eksplorasi interaktif tentang sifat **Fungsi Naik** dan **Fungsi Turun** melalui contoh spesifik 
        fungsi eksponen: $\\mathbf{f(x) = a \\cdot b^x}$.
        
        Ubah slider di bawah untuk melihat bagaimana perubahan konstanta $\\mathbf{a}$ dan basis $\\mathbf{b}$ 
        memengaruhi bentuk dan sifat fungsi!
    """)
    
    st.markdown("---")
    
    # 2. Sidebar Kontrol Interaktif
    st.sidebar.header("Kontrol Parameter Fungsi")
    
    # Input parameter a (Konstanta pengali)
    a = st.sidebar.slider(
        'Pilih nilai Konstanta (a):',
        min_value=-5.0, max_value=5.0, value=1.0, step=0.5
    )
    
    # Input parameter b (Basis eksponen)
    # Basis harus positif (b > 0)
    b = st.sidebar.slider(
        'Pilih nilai Basis (b):',
        min_value=0.1, max_value=4.0, value=2.0, step=0.1
    )
    
    # Rentang nilai x
    x_min = st.sidebar.slider('Rentang X minimum:', -5, 0, -2)
    x_max = st.sidebar.slider('Rentang X maksimum:', 0, 5, 3)

    st.sidebar.markdown("---")
    
    # 3. Area Plot
    
    # Membuat array nilai x
    x = np.linspace(x_min, x_max, 400)
    # Menghitung nilai y
    y = fungsi_eksponen(x, a, b)
    
    # Membuat figure Matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, label=f'$f(x) = {a} \\cdot {b}^x$', color='darkblue')
    
    # Menambahkan garis bantu (sumbu x dan y)
    ax.axhline(0, color='gray', linestyle='--')
    ax.axvline(0, color='gray', linestyle='--')
    
    # Memberi label dan judul
    ax.set_title(f"Grafik Fungsi: f(x) = {a} * {b}^x")
    ax.set_xlabel("Nilai X")
    ax.set_ylabel("Nilai f(x)")
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()
    
    # Menampilkan plot di Streamlit
    st.pyplot(fig)
    
    st.markdown("---")

    # 4. Analisis dan Kesimpulan Interaktif (Fokus pada Fungsi Naik/Turun)
    st.header("🎯 Analisis Sifat Fungsi")

    # Logika penentuan Sifat Fungsi Naik/Turun
    sifat_fungsi = ""
    analisis_basis = ""
    analisis_koefisien = ""
    
    # Analisis Fungsi Naik/Turun
    if b > 1:
        analisis_basis = f"Karena **Basis ($b$) = {b} > 1**, kurva eksponen cenderung **naik** (membesar seiring $x$ membesar)."
        if a > 0:
            sifat_fungsi = "Fungsi Naik (Increasing Function) 📈"
            analisis_koefisien = f"Karena Koefisien ($a$) = {a} > 0, kurva mengikuti tren naik."
            st.success(f"**Kesimpulan:** Fungsi ini adalah **{sifat_fungsi}**")
        elif a < 0:
            sifat_fungsi = "Fungsi Turun (Decreasing Function) 📉"
            analisis_koefisien = f"Karena Koefisien ($a$) = {a} < 0, kurva **terbalik (refleksi)** dari fungsi naik, sehingga menjadi **fungsi turun**."
            st.warning(f"**Kesimpulan:** Fungsi ini adalah **{sifat_fungsi}**")
        else:
            sifat_fungsi = "Fungsi Konstan"
            analisis_koefisien = f"Karena $a = 0$, fungsi menjadi $f(x)=0$, garis lurus horizontal."
            st.info(f"**Kesimpulan:** Fungsi ini adalah **{sifat_fungsi}**")
            
    elif 0 < b < 1:
        analisis_basis = f"Karena **Basis ($b$) = {b}** berada di antara 0 dan 1, kurva eksponen cenderung **turun** (meluruh seiring $x$ membesar)."
        if a > 0:
            sifat_fungsi = "Fungsi Turun (Decreasing Function) 📉"
            analisis_koefisien = f"Karena Koefisien ($a$) = {a} > 0, kurva mengikuti tren turun."
            st.error(f"**Kesimpulan:** Fungsi ini adalah **{sifat_fungsi}**")
        elif a < 0:
            sifat_fungsi = "Fungsi Naik (Increasing Function) 📈"
            analisis_koefisien = f"Karena Koefisien ($a$) = {a} < 0, kurva **terbalik (refleksi)** dari fungsi turun, sehingga menjadi **fungsi naik**."
            st.success(f"**Kesimpulan:** Fungsi ini adalah **{sifat_fungsi}**")
        else:
            sifat_fungsi = "Fungsi Konstan"
            analisis_koefisien = f"Karena $a = 0$, fungsi menjadi $f(x)=0$, garis lurus horizontal."
            st.info(f"**Kesimpulan:** Fungsi ini adalah **{sifat_fungsi}**")
            
    elif b == 1:
        sifat_fungsi = "Fungsi Konstan"
        analisis_basis = f"Karena **Basis ($b$) = 1**, maka $f(x) = a \\cdot 1^x = a$. Ini adalah garis lurus horizontal."
        analisis_koefisien = f"Nilai fungsi selalu sama dengan **$a = {a}$**."
        st.info(f"**Kesimpulan:** Fungsi ini adalah **{sifat_fungsi}**")

    # Menampilkan ringkasan poin kunci
    st.markdown(f"""
        ### $f(x) = {a} \\cdot {b}^x$
        
        * **Parameter $b$ (Basis):** {analisis_basis}
        * **
