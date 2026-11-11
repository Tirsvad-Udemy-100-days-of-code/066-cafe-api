[English](Step-9-API-Documentation) · [Dansk](Step-9-API-Documentation-da) · **Bahasa Malaysia**

# 9. Dokumentasikan API

![Dokumentasikan API](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-9.png)

*Ilustrasi dengan data contoh, dilukis untuk repositori ini berdasarkan huraian pelajaran. Ia bukan tangkapan projek kursus.*

## Apa yang dilakukan pelajaran

- Orang lain tidak dapat melihat kod pelayan, jadi API mesti didokumentasikan: laluan, parameter dan apa yang dipulangkan.
- Beri setiap permintaan Postman nama dan huraian, simpan dalam satu koleksi dan guna Publish Docs.
- Pautkan dokumentasi yang diterbitkan daripada `index.html` projek dengan teg anchor.

## API dalam repositori ini

Repositori ini mempunyai pelaksanaan API sendiri. Mulakan dengan `python -m cafe_api`; ia mendengar di `http://127.0.0.1:5000`.

| Kata kerja | Laluan | Fungsinya | Berjaya | Ralat |
| --- | --- | --- | --- | --- |
| `GET` | `/random` | Satu kafe secara rawak | 200 `{"cafe": {...}}` | 404 jika tiada kafe |
| `GET` | `/all` | Semua kafe | 200 `{"cafes": [...]}` |  |
| `GET` | `/search?loc=...` | Kafe di sesuatu lokasi, tanpa mengira huruf besar atau kecil | 200 `{"cafes": [...]}` | 400 tanpa `loc`, 404 jika tiada yang sepadan |
| `POST` | `/add` | Cipta kafe daripada badan JSON | 201 `{"cafe": {...}}` | 400 untuk medan yang tiada, kosong atau jenis salah, atau nama yang sudah wujud |
| `PATCH` | `/update-price/<cafe_id>?new_price=...` | Tukar harga kopi | 200 `{"cafe": {...}}` | 400 tanpa `new_price`, 404 untuk id yang tidak dikenali |
| `DELETE` | `/report-closed/<cafe_id>` | Buang kafe yang sudah tutup; perlukan pengepala `X-API-Key` | 200 `{"message": "..."}` | 403 untuk kunci salah atau tiada, 404 untuk id yang tidak dikenali |

- Setiap ralat ialah JSON: `{"error": "..."}`.
- Kunci API dibaca daripada pemboleh ubah persekitaran `CAFE_API_KEY` apabila permintaan tiba. Tiada kunci lalai: jika pemboleh ubah itu tidak ditetapkan, setiap pemadaman dijawab 403.
- Pelajaran menghantar kunci sebagai parameter pertanyaan `api-key`. Di sini ia dihantar dalam pengepala `X-API-Key`, supaya kunci tidak berakhir dalam URL dan log.
- Badan `POST /add` ialah objek JSON dengan medan teks `name`, `map_url`, `img_url`, `location`, `seats`, medan benar/palsu `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls` dan `coffee_price` yang pilihan.

Cuba (dalam Windows PowerShell guna `curl.exe`, atau hantar permintaan daripada Postman):

```bash
curl http://127.0.0.1:5000/random
curl "http://127.0.0.1:5000/search?loc=Peckham"
curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"name": "Example Cafe", "map_url": "https://example.com/map", "img_url": "https://example.com/img.jpg", "location": "Peckham", "seats": "10-20", "has_toilet": true, "has_wifi": true, "has_sockets": false, "can_take_calls": false, "coffee_price": "2.80"}'
curl -X PATCH "http://127.0.0.1:5000/update-price/1?new_price=3.20"
curl -X DELETE http://127.0.0.1:5000/report-closed/1 -H "X-API-Key: <your-key>"
```

## Apa yang kita pelajari

- Dokumentasi ialah sebahagian daripada produk API.
- Postman menjananya daripada permintaan yang disimpan, jadi ujian dan dokumentasi sentiasa seiring.

---

Sebelumnya: [Kafe yang sudah tutup](Step-8-Delete-Cafe-ms) · [Utama](Home-ms)
