# BookBuddies (Kelompok PBP B02)
## Anggota Kelompok
- Farah Dhiya Ramadhina (2206082934)
- Fikri Massaid Wahab (2206083395)
- Gallan Adrizqi Samudra
- Marchelina Anjani S (2206082770)
- Nabil Nazir Ahmad
- Syarna Savitri
## Cerita Aplikasi
BookBuddies hadir sebagai aplikasi yang menjembatani komunitas pecinta buku yang inin saling berbagi dan meminjamkan koleksi buku satu sama lain. Tujuan aplikasi ini selain untuk meningkatkan literasi, adalah memberikan manfaat lebih untuk buku-buku yang sudah kita miliki dan kita baca dengan meminjamkannya ke pengguna lain yang ingin membaca buku yang kita miliki. Aplikasi ini memiliki manfaat untuk memudahkan akses membaca buku, misalnya meminjam buku antik yang tidak lagi dicetak, juga memungkinkan pengguna untuk meminjamkan buku yang telah mereka baca dan tidak lagi digunakan secara gratis. Selain itu, aplikasi ini juga menyediakan fitur review serta ulasan buku antar pengguna.
Berikut penjabaran manfaat dari aplikasi yang ingin kami buat:
### 1. Meningkatkan Akses ke Dunia Buku:
Aplikasi ini memungkinkan pengguna untuk meminjam buku tanpa harus membelinya secara fisik, yang lebih praktis dibandingkan dengan pergi ke perpustakaan.
### 2. Meningkatkan Literasi
Pengguna dapat berinteraksi dengan anggota komunitas lainnya untuk membahas buku, memberikan ulasan, dan berbagi pengalaman membaca, sehingga meningkatkan pemahaman dan minat literasi.
### 3. Pengurangan Pembelian Buku Bajakan:
Dengan adanya aplikasi ini, pengguna dapat menghindari pembelian buku bajakan dan lebih memilih untuk meminjam buku yang masih dalam kondisi asli.
## Dataset Katalog Buku
Sumber dataset katalog buku yang kami tetapkan adalah Google Books API.
## Daftar Modul yang akan Diimplementasikan
### 1. Beranda
Halaman ini menampilkan katalog buku-buku terbaru yang ready di pinjam dalam bentuk kartu (cards). Akan ada tampilan pop up card, untuk user/guest yang ingin melakukan sign in atau register. (tidak masuk modul utama)
### 2. Autentikasi Akun
Halaman ini memungkinkan pengguna untuk masuk (login) atau membuat akun (register) di aplikasi. (tidak masuk modul utama)
### 3. Dashboard Member
Halaman ini adalah dashboard pribadi bagi anggota yang telah melakukan login. Mereka dapat melihat aktivitas peminjaman mereka, buku-buku yang mereka pinjam, dan lain-lain. (Nabil Nazir)
### 4. Dashboard Admin
Halaman ini digunakan oleh admin untuk mengelola akun dan statistik peminjaman buku. Selain itu, jika kontributor ingin meminjamkan buku, maka harus melalui admin terlebih dahulu, nantinya admin yang akan memasukkan buku ke katalog buku (card). (Fikri Massaid Wahab)
### 5. Halaman Review
Halaman khusus bagi anggota untuk mereview tentang buku yang mereka baca, memberikan ulasan dan rating. (Farah Dhiya R)
### 6. Halaman Informasi Buku
Halaman ini berisi informasi rinci tentang buku, termasuk deskripsi, ulasan, dan informasi peminjaman. (Marchelina Anjani S) 
### 7. Halaman Bookmark
Halaman ini digunakan bagi member untuk menyimpan buku yang sedang dipinjam oleh orang lain ke dalam daftar tunggu (waiting list) mereka. Untuk membookmark suatu buku member harus memasukkan data seperti nama dan kapan mereka ingin meminjam buku tersebut. (Syarna Savitri) 
### 8. Halaman Rekomendasi Buku
Halaman ini akan menampilkan buku terfavorit yang dinilai berdasarkan rata-rata rating tertinggi dalam rentan waktu satu bulan dan juga banyak peminjaman buku tersebut. List buku terfavorit tersebut nantinya akan ditampilkan sebagai rekomendasi buku pada bulan tersebut. (Gallan Adrizqi)

## Role Pengguna
### 1. Guest
Pengguna yang hanya mengunjungi situs web tanpa membuat akun. Mereka dapat mengakses katalog buku, database buku, dan deskripsi buku.
### 2. Member
Pengguna yang telah mendaftar dan memiliki akun. Mereka memiliki dashboard pribadi, memungkinkan mereka untuk meminjam atau meminjamkan buku, dan menerima informasi terkait batas waktu peminjaman serta denda. Ada tombol/menu untuk contribute, kemudian me-redirect ke halaman untuk pengisian data atau informasi tentang buku ingin dipinjamkan.
### 3. Admin
Pengguna yang mengelola peminjaman, seperti menetapkan tenggat waktu peminjaman dan mengelola kasus keterlambatan pengembalian buku. Selain itu, admin juga berperan dalam menyetujui request kontribusi dari member yang ingin meminjamkan buku. Jika admin telah meng-approve sebuah buku, maka buku tersebut akan ditambahkan pada katalog buku dan database yang nantinya akan menjadi visible bagi guest maupun member.
