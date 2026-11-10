[English](Step-2-Random-Cafe) · [Dansk](Step-2-Random-Cafe-da) · **Bahasa Malaysia**

# 2. Kafe rawak

![Kafe rawak](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-2.png)

*Ilustrasi dengan data contoh, dilukis untuk repositori ini berdasarkan huraian pelajaran. Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `GET` | `/random` |

## Apa yang dilakukan pelajaran

- Tambah laluan `/random` yang menerima permintaan GET dan memilih satu kafe rawak daripada pangkalan data.
- API memulangkan JSON, bukan templat HTML, jadi objek SQLAlchemy mesti disiri.
- `jsonify()` membina JSON; anda boleh menulis setiap medan sendiri untuk membentuk jawapan, atau menukar baris kepada kamus dan menjsonify-kannya.

## Apa yang kita pelajari

- Penyirian: menukar objek pangkalan data kepada JSON.
- JSON buatan tangan memberi kawalan penuh (sembunyi id, kumpul boolean); kamus lebih pantas apabila anda mahu semua medan.

---

Sebelumnya: [Projek permulaan](Step-1-Starting-Project-ms) · Seterusnya: [Semua kafe](Step-3-All-Cafes-ms)
