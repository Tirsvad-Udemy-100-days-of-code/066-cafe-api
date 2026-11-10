[English](Step-4-Search) · [Dansk](Step-4-Search-da) · **Bahasa Malaysia**

# 4. Cari kafe

![Cari kafe](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-4.png)

*Ilustrasi dengan data contoh, dilukis untuk repositori ini berdasarkan huraian pelajaran. Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `GET` | `/search?loc=...` |

## Apa yang dilakukan pelajaran

- Tambah laluan `/search`; pemanggil menghantar lokasi sebagai parameter pertanyaan selepas tanda soal, contohnya `?loc=Peckham`.
- Tapis pertanyaan dengan `where()` pada lajur lokasi.
- Jika tiada padanan, jawab dengan mesej ralat JSON yang jelas.

## Apa yang kita pelajari

- Parameter pertanyaan membolehkan pemanggil menyempitkan hasil tanpa mengubah laluan.
- Jawapan ralat yang membantu ialah sebahagian daripada reka bentuk API.

---

Sebelumnya: [Semua kafe](Step-3-All-Cafes-ms) · Seterusnya: [Postman](Step-5-Postman-ms)
