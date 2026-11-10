[English](Step-7-Update-Price) · [Dansk](Step-7-Update-Price-da) · **Bahasa Malaysia**

# 7. Harga kopi sebuah kafe

![Harga kopi sebuah kafe](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-7.png)

*Ilustrasi dengan data contoh, dilukis untuk repositori ini berdasarkan huraian pelajaran. Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `PATCH` | `/update-price/<cafe_id>` |

## Apa yang dilakukan pelajaran

- Mula-mula idea PUT lawan PATCH: ganti semuanya, atau ubah bahagian yang rosak sahaja.
- Tambah laluan PATCH `/update-price/<cafe_id>`; harga baharu ialah parameter.
- Dapatkan kafe mengikut id dalam try/except; jika tidak wujud, jawab dengan ralat dan status HTTP 404 dan bukannya 200 lalai.

## Apa yang kita pelajari

- Pilih PATCH apabila hanya satu medan berubah.
- Kod status HTTP yang betul (404 tidak ditemui) memberitahu klien apa yang berlaku, bukan sekadar teks mesej.

---

Sebelumnya: [Kafe baharu](Step-6-Add-Cafe-ms) · Seterusnya: [Kafe yang sudah tutup](Step-8-Delete-Cafe-ms)
