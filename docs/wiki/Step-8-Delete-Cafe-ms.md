[English](Step-8-Delete-Cafe) · [Dansk](Step-8-Delete-Cafe-da) · **Bahasa Malaysia**

# 8. Kafe yang sudah tutup

![Kafe yang sudah tutup](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-8.png)

*Ilustrasi dengan data contoh, dilukis untuk repositori ini berdasarkan huraian pelajaran. Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `DELETE` | `/report-closed/<cafe_id>` |

## Apa yang dilakukan pelajaran

- Tambah laluan DELETE `/report-closed/<cafe_id>`.
- Lindungi dengan parameter `api-key`: kunci salah mendapat 403 Forbidden, kafe tiada mendapat 404.
- Padam baris dan simpan hanya apabila kunci betul dan kafe wujud.

## Apa yang kita pelajari

- Kebenaran ringkas: tidak semua orang boleh memadam data.
- Susunan semakan penting: benarkan dahulu, cari, kemudian ubah.

---

Sebelumnya: [Harga kopi sebuah kafe](Step-7-Update-Price-ms) · Seterusnya: [Dokumentasikan API](Step-9-API-Documentation-ms)
