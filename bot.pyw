import pywhatkit as kit
import pandas as pd

# Baca file pesan dari pesan.txt
with open('pesan.txt', 'r', encoding='utf-8') as file:
    template_pesan = file.read()

df = pd.read_excel('data.xlsx', dtype={'NoHP': str})

nomor = "+" + df['NoHP'].fillna("628123123")
if 'Nama' in df.columns:
    nama = df['Nama']
if 'Jenis Kelamin' in df.columns:
    gender = df['Jenis Kelamin']

if 'Perusahaan' in df.columns:
    perusahaan = df['Perusahaan']

for i in range(len(nomor)):
    sapaan = ''
    if 'Jenis Kelamin' in df.columns:
        sapaan = "Bpk" if gender[i] == "Laki-laki" else "Ibu" 
    nama_perusahaan = ''
    if 'Perusahaan' in df.columns:
        nama_perusahaan = perusahaan[i]
    nama_nasabah = ''
    if 'Nama' in df.columns:
        nama_nasabah =nama[i]
    pesan = template_pesan.replace("{Nama}", nama_nasabah).replace("{Gender}", sapaan).replace("{Perusahaan}", nama_perusahaan)
    
    kit.sendwhatmsg_instantly(
        phone_no=nomor[i],
        message=pesan,
        wait_time=20,
        tab_close=True
    )

print("Pesan siap sudah terkirim bosku!")
