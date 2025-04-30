import pywhatkit as kit
import pandas as pd
import time
import os
import pyautogui

# Baca pesan dari file
with open('pesan.txt', 'r', encoding='utf-8') as file:
    template_pesan = file.read()

# Load data
df = pd.read_excel('data.xlsx', dtype={'NoHP': str})

nomor = "+" + df['NoHP'].fillna("628123123")
nama = df['Nama'].fillna("") if 'Nama' in df.columns else ""
gender = df['Gender'].fillna("") if 'Gender' in df.columns else ""
perusahaan = df['Perusahaan'].fillna("") if 'Perusahaan' in df.columns else ""

# Cek dan ambil gambar dari folder 'gambar' jika ada
image_folder = 'gambar'
image_files = []
if os.path.exists(image_folder):
    image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

def send_images(image_paths):
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'alt', 'a')  # Shortcut untuk attach file, sesuaikan jika berbeda
    time.sleep(2)

    for img_path in image_paths:
        pyautogui.write(img_path)
        pyautogui.press('enter')
        time.sleep(1)

    time.sleep(2)
    pyautogui.press('enter')  # Kirim gambar

# Kirim pesan ke semua kontak
for idx in range(len(nomor)):
    print(f"Mengirim pesan ke-{idx + 1}...")

    sapaan = "Bpk" if gender[idx] == "Laki-laki" else "Ibu"
    nama_nasabah = nama[idx]
    nama_perusahaan = perusahaan[idx]

    pesan = template_pesan.replace("{Nama}", nama_nasabah).replace("{Gender}", sapaan).replace("{Perusahaan}", nama_perusahaan)

    kit.sendwhatmsg_instantly(
        phone_no=nomor[idx],
        message=pesan,
        wait_time=20,
        tab_close=False  # Jangan ditutup agar bisa kirim gambar jika ada
    )

    # Kirim gambar hanya jika image_files tidak kosong
    if image_files:
        send_images(image_files)

    time.sleep(5)  # Tunggu sebelum kirim ke kontak berikutnya

print("Semua pesan telah dikirim. Gambar hanya dikirim jika tersedia.")
