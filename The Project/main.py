import streamlit as st
import streamlit.components.v1 as components
import time
import openai
import os
import random
import base64
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from itertools import permutations, combinations
from PIL import Image


list_api = [
    "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",
    "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",
    "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",
    "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",
    "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"

]

st.set_page_config(layout="wide")


def get_base64(bin_file):
    """membaca binary file dengan menggunakan encode decode dengan base64 bit

    Args:
        bin_file (location file): file path

    Returns:
        image: binary string
    """
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    """Mensetting background ke streamlit dengan html internal

    Args:
        png_file (file location): file path
    """
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


# setting background
set_background("./img/2.jpg")


# memanggil OpenAI API key
model_engine = "text-davinci-003"
openai.api_key = random.choice(list_api)

# membuat judul di tiap fitur


def title(text):
    st.title(text)
    st.markdown('''
    <hr style="height:2px;width:100%;border-width:0;color:gray;background-color:gray">
                ''', unsafe_allow_html=True)


# membuat sidebar menu vertikal
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Theory", "About", "Developer"],
                           icons=['house', 'book-half', 'info-circle', 'person-workspace'], menu_icon="list", default_index=1)


if selected == 'Theory':

    # st.markdown("# Apa itu Permutasi & Kombinasi ?", unsafe_allow_html=True)
    title("Apa itu Permutasi & Kombinasi ?")

    st.markdown("")

    st.markdown("""
                <font size="4">
                Dalam konsep peluang, dikenal juga istilah kombinasi dan permutasi. Keduanya digunakan untuk mencari peluang atau probabilitas dari suatu kejadian. Perbedaan yang mencolok dari keduanya, yaitu:
                </font><br>
                """, unsafe_allow_html=True)
    st.markdown("")

    st.markdown("""
                <li><b>Kombinasi</b> (C) : cara menyusun objek <b>tanpa memperhatikan urutan</b>
                <li><b>Permutasi</b> (P) : cara menyusun objek <b>dengan memperhatikan urutan</b>
                """, unsafe_allow_html=True)

    st.markdown("""
                 <font size="4"> <b>Contoh</b>: </font>
                 """, unsafe_allow_html=True)

    st.markdown("""
                <li><b>Kombinasi</b><br>
                <p>
                <blockquote>Suatu kelompok memiliki 3 orang anggota, yaitu A, B, dan C. Seorang guru harus memilih 2 orang anggota untuk mengikuti lomba vokal. Tentukan ada berapa kombinasi yang digunakan untuk mengambil dua orang dari tiga anggota yang tersedia!
                </p>

                <p>
                Kombinasi adalah permutasi tanpa memperhatikan nilai acak. Karena pada kombinasi gak memperhatikan urutan, jadi cara yang bisa diambil dari kejadian di atas adalah A-B, A-C, dan B-C. Dengan begitu, ada 3 kombinasi cara untuk mengambil dua orang dari tiga anggota untuk menjadi peserta lomba vokal.
                </p>
                """, unsafe_allow_html=True)

    st.markdown("""
                <li><b>Permutasi</b><br>
                <p>
                <blockquote>Di dalam kotak, terdapat 3 buah bola yang masing-masing berwarna merah, kuning, dan hijau. Andi diminta untuk mengambil dua buah bola secara acak dan urutan pengambilannya harus diperhatikan. Tentukan ada berapa permutasi yang digunakan untuk mengambil dua buah bola dari dalam kotak tersebut!
                </p>

                <p>
                Karena pada permutasi harus memperhatikan urutan, maka cara yang bisa diambil dari kejadian di atas adalah M-K, K-M, K-H, H-K, M-H, dan H-M. Jadi, ada 6 permutasi yang bisa digunakan untuk mengambil dua bola secara acak dan berurutan. Tentu rumus permutasi dan kombinasi nantinya akan berbeda.
                </p>
                """, unsafe_allow_html=True)

    dic = {
        'Kombinasi':
            [
                'Urutan gak diperhatikan',
                'Memilih tim/kelompok, baju, mata pelajaran, daftar makanan',
                'Mengambil beberapa anggota dari grup',
                'Mengambil dua warna dari kotak secara acak',
                'Mengambil tiga orang pemenang'
            ],

        'Permutasi':
            [
                'Urutan harus diperhatikan',
                'Menyusun orang, nomor telepon, angka, warna',
                'Mengambil ketua tim, menyusun jobdesk tiap orang',
                'Mengambil dua warna favorit dan berurutan',
                'Mengambil pemenang secara berurutan (juara 1, 2, dan 3)'
            ]
    }

    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5, 3, 0.5])

    with col2:
        df = pd.DataFrame(data=dic)

        data = st.dataframe(df)

    st.markdown("")

    st.markdown("""
                <blockquote><blockquote><blockquote><font size='6'>
                Rumus Permutasi
                </font>
                """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("")

    st.latex(
        r""" ^nP_r = \frac{n!}{(n-r)!} """)    # menampilkan rumus permutasi

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    col1, col2, col3 = st.columns([1, 3, 0.5])

    with col2:
        st.markdown("""
                <p>
                Keterangan:<br>
                P = Permutasi<br>
                n = Jumlah kejadian yang bisa dipilih<br>
                r = Jumlah kejadian yang harus dipilih<br>
                ! = Simbol faktorial
                </p>
                
                Contoh:

                Ada anak Andi (A), Budi (B), dan Cecep (C) yang akan menempati 3 buah kursi di ruangan kelas. Tentukan variasi tempat duduk yang bisa dilakukan ketiga anak tersebut menggunakan konsep permutasi!

                Penyelesaian:

                Andi, Budi, Cecep → ABC, BCA, CAB, ACB, BAC, CBA = 6 variasi tempat duduk.

                Kalau menggunakan rumus, berarti: 
                """, unsafe_allow_html=True)

    st.latex(
        r""" ^nP_r = \frac{n!}{(n-r)!} """)    # menampilkan rumus permutasi

    st.markdown("")

    st.latex(r"^3P_3 = \frac{3!}{0!} = 3! = 3x2x1 = 6")

    st.markdown("""
                <blockquote><blockquote><blockquote><font size='6'>
                Rumus Kombinasi
                </font>
                """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("")

    st.latex(
        r""" ^nC_r = \frac{n!}{(n-r)!r!} """)    # menampilkan rumus kombinasi

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    col1, col2, col3 = st.columns([1, 3, 0.5])

    with col2:
        st.markdown("""
                <p>
                Keterangan:<br>
                P = kombinasi<br>
                n = Jumlah kejadian yang bisa dipilih<br>
                r = Jumlah kejadian yang harus dipilih<br>
                ! = Simbol faktorial
                </p>
                
                Contoh:

                Ada anak Andi (A), Budi (B), dan Cecep (C) yang akan menempati 3 buah kursi di ruangan kelas. Tentukan variasi tempat duduk yang bisa dilakukan ketiga anak tersebut menggunakan konsep <b>kombinasi</b> !

                Penyelesaian:

                Andi, Budi, Cecep → ABC, BCA, CAB, ACB, BAC, CBA = 6 variasi tempat duduk.

                Kalau menggunakan rumus, berarti: 
                """, unsafe_allow_html=True)

    st.latex(
        r""" ^nC_r = \frac{n!}{(n-r)!r!} """)    # menampilkan rumus kombinasi

    st.markdown("")

    st.latex(r"^3C_3 = \frac{3!}{(3-3)! 3!} = \frac{3!}{1 . 3!} = 1")

elif selected == 'Home':
    title('Home')

    # horizontal Menu
    selected2 = option_menu(None, ['Permutation', 'Combination', 'AingBotz'],
                            icons=['paypal', 'bullseye', 'robot'], default_index=0, orientation="horizontal")

    if selected2 == 'Permutation':
        st.header("""Permutation""")
        st.header("")
        st.latex(r""" ^nP_r = \frac{n!}{(n-r)!} """)
        st.header("")

        # text input buat masukin iterable nya
        iterable = st.text_input(
            label="Masukkan Iterable dipisahkan oleh spasi")

        if iterable:
            iterable = list(n for n in iterable.split(' ') if n != '')

        try:

            num2 = int(st.number_input("Masukkan nomor untuk **r**"))
            calc = permutations(iterable, num2)

            calc = [i for i in calc]
            result = str(calc).strip('[]')

            if iterable:
                with st.spinner(text='Process'):
                    time.sleep(1)
                    st.success(f"""Hasil : \n\n{result}\n\nAda **{len(calc)}** 
                            cara untuk mempermutasi iterable tersebut""")

        except ValueError as err:
            st.warning(f"{err}")

    # isi opsi combinations
    elif selected2 == 'Combination':
        st.header("""Combination""")
        st.header("")
        st.latex(r""" ^nC_k = \frac{n!}{k!(n-r)!} """)
        st.header("")

        # menyediakan text input untuk iterable atau sequence
        iterable = st.text_input(
            label="Masukkan Iterable dipisahkan oleh spasi")

        if iterable:
            iterable = list(n for n in iterable.split(' ') if n != '')

        try:

            num2 = int(st.number_input("Masukkan nomor untuk **k**"))
            calc = combinations(iterable, num2)

            calc = [i for i in calc]
            result = str(calc).strip('[]')

            if iterable:
                with st.spinner(text='Process'):
                    time.sleep(1)
                    st.success(f"""Hasil : \n\n{result}\n\nAda **{len(calc)}** 
                            cara untuk menggabungkan iterable""")

        except ValueError as err:
            st.warning(f"{err}")

    elif selected2 == 'AingBotz':

        @st.cache_data
        def ChatGPT(user_query):
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=user_query,
                max_tokens=1024,
                n=1,
                temperature=0.5,
            )
            response = completion.choices[0].text
            return response

        st.title("AingBotz:sparkles:")
        st.sidebar.header("Siapa AingBotz ini?")
        st.sidebar.info('''Ini adalah aplikasi web yang memungkinkan Anda untuk berinteraksi dengan
             implementasi model ChatGPT OpenAI API.
             Masukkan **kueri** di **kotak teks** dan **tekan enter** untuk menerima
             **tanggapan** dari ChatGPT
            ''')

        # Mendapatkan inputand dari user
        st.markdown("""Kamu Nanya:grey_question:""")
        user_query = st.text_input("Ketik pertanyanmu disini::")

        if user_query:
            # Generate response
            response = ChatGPT(user_query)
            # Display response
            st.success(response)

elif selected == 'About':
    title('About')

    col1, col2, col3 = st.columns([0.8, 2, 1])
    with col2:
        components.html("""
        <center><iframe width="1000" height="600" src="https://www.youtube-nocookie.com/embed/OcQd93hesEk?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
        </iframe></center>""", width=1000, height=600)

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    st.markdown(""" <font size="4"> Permutation dan Permutation Calculator adalah sebuah proyek **kelompok 4** yang bertujuan untuk membantu pengguna dalam mengecek **permutasi dan kombinasi** dari suatu set data. Proyek ini juga dilengkapi dengan kalkulator permutasi yang dapat menghitung hasil permutasi dari suatu set data dengan cepat dan akurat.</font>""", unsafe_allow_html=True)
    st.markdown("""""")
    st.markdown(""" <font size="4"> Untuk mencapai tujuannya, proyek ini  menggunakan base perhitungan Permutation dan Permutation Calculator, pengguna dapat dengan mudah mengecek hasil permutasi dan kombinasi dari suatu set data tanpa perlu menghitung secara manual. Ini akan menghemat waktu dan mempermudah proses pemecahan masalah yang berhubungan dengan permutasi dan kombinasi.</font>""", unsafe_allow_html=True)
    st.markdown("""""")
    st.markdown(""" <font size="4"> Secara keseluruhan, Permutation dan Permutation Calculator adalah solusi yang bermanfaat bagi para ahli matematika, ilmuwan, dan mereka yang membutuhkan bantuan dalam mengecek hasil permutasi dan kombinasi dari suatu data.</font>""", unsafe_allow_html=True)


elif selected == 'Developer':
    title('Kelompok 4 - IF09N')

    col1, col2, col3, col4 = st.columns([1.1, 1.1, 1.1, 1.1])

    memory = {}

    def memoize_image(func):

        def inner(img):
            if img not in memory:
                memory[img] = func(img)  # path as a key, image name as a value

            return memory[img]

        return inner

    @memoize_image
    def show_image(path):
        image = Image.open(path)
        st.image(image=image)

        return os.path.basename(path)

    with col1:
        show_image(
            r'img/asyafa.png')

        st.write("### <center> Asyafa Ditra Al Hauna<br><br>21102116</center>",
                 unsafe_allow_html=True)

    with col2:
        show_image(
            r'img/ammar.png')

        st.write("### <center> M. Ammar Izzudin <br><br> 21102122</center>",
                 unsafe_allow_html=True)

    with col3:
        show_image(
            r'img/mansur.png')

        st.write("### <center> Mansur Julianto <br><br>21102121</center>",
                 unsafe_allow_html=True)

    with col4:
        show_image(
            r'img/yoko.png')

        st.write("### <center> Setyoko Almuludin <br><br>21102128 </center>",
                 unsafe_allow_html=True)
        st.write("### <center>  </center>",
                 unsafe_allow_html=True)

    st.snow()
    # st.write(memory)  # ? Check memoization
    # end = time.time()
    # st.write(end - start)
