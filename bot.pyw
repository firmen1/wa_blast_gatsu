import pywhatkit as kit
import pandas as pd

# Baca file pesan dari pesan.txt
with open('pesan.txt', 'r', encoding='utf-8') as file:
    template_pesan = file.read()

df = pd.read_excel('data.xlsx', dtype={'NoHP': str})

nomor = "+" + df['NoHP'].fillna("628123123")
if 'Nama' in df.columns:
    nama = df['Nama'].fillna("")
if 'Gender' in df.columns:
    gender = df['Gender'].fillna("")
if 'Perusahaan' in df.columns:
    perusahaan = df['Perusahaan'].fillna("")

for idx in range(len(nomor)):
    print(f"Mengirim pesan ke-{idx + 1}...")  # Counter print

    sapaan = ''
    if 'Gender' in df.columns:
        sapaan = "Bpk" if gender[idx] == "Laki-laki" else "Ibu" 

    nama_perusahaan = ''
    if 'Perusahaan' in df.columns:
        nama_perusahaan = perusahaan[idx]

    nama_nasabah = ''
    if 'Nama' in df.columns:
        nama_nasabah = nama[idx]

    pesan = template_pesan.replace("{Nama}", nama_nasabah).replace("{Gender}", sapaan).replace("{Perusahaan}", nama_perusahaan)
    
    kit.sendwhatmsg_instantly(
        phone_no=nomor[idx],
        message=pesan,
        wait_time=20,
        tab_close=True
    )

print("Semua pesan telah dikirim!")
