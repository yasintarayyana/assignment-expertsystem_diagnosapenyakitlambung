const riwayatYa = document.getElementById("riwayatYa");
const riwayatTidak = document.getElementById("riwayatTidak");
const riwayatDetail = document.getElementById("riwayatDetail");
const jenisRiwayat = document.querySelector('select[name="jenis_riwayat"]');
const submitBtn = document.querySelector('button[type="submit"]');

// =====================
// TOGGLE FIELD DETAIL
// =====================
function toggleRiwayat() {

    if (riwayatYa.checked) {
        riwayatDetail.style.display = "block";
    } else {
        riwayatDetail.style.display = "none";

        // reset value kalau "Tidak"
        if (jenisRiwayat) {
            jenisRiwayat.value = "";
        }
    }

    validateForm();
}

// =====================
// VALIDASI FORM
// =====================
function validateForm() {

    const onsetChecked = document.querySelector('input[name="onset"]:checked');
    const riwayatChecked = document.querySelector('input[name="riwayat"]:checked');

    let valid = true;

    // onset wajib
    if (!onsetChecked) valid = false;

    // riwayat wajib
    if (!riwayatChecked) valid = false;

    // kalau YA → wajib isi detail
    if (riwayatYa.checked) {
        if (!jenisRiwayat.value) valid = false;
    }

    // toggle button
    if (valid) {
        submitBtn.disabled = false;
        submitBtn.classList.remove("disabled");
    } else {
        submitBtn.disabled = true;
        submitBtn.classList.add("disabled");
        startBtn.setAttribute("aria-disabled", "true");
    }
}

// =====================
// EVENT LISTENER
// =====================

// radio riwayat
riwayatYa.addEventListener("change", toggleRiwayat);
riwayatTidak.addEventListener("change", toggleRiwayat);

// select perubahan
jenisRiwayat.addEventListener("change", validateForm);

// semua radio onset
document.querySelectorAll('input[name="onset"]').forEach(el => {
    el.addEventListener("change", validateForm);
});

// init saat load
toggleRiwayat();
validateForm();