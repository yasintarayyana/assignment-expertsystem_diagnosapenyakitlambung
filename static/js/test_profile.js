const profileData = window.profileData;

const useProfile =
document.getElementById(
    "useProfile"
);

function fillProfile(){

    document.getElementById(
        "nama"
    ).value =
    profileData.nama;

    document.getElementById(
        "email"
    ).value =
    profileData.email;

    document.getElementById(
        "tanggal_lahir"
    ).value =
    profileData.tanggal_lahir;

    document.getElementById(
        "umur"
    ).value =
    profileData.umur;

    document.getElementById(
        "jk"
    ).value =
    profileData.jenis_kelamin;

    validateForm();
}

function clearProfile(){

    document.getElementById(
        "nama"
    ).value = "";

    document.getElementById(
        "email"
    ).value = "";

    document.getElementById(
        "tanggal_lahir"
    ).value = "";

    document.getElementById(
        "umur"
    ).value = "";

    document.getElementById(
        "jk"
    ).value = "";

    validateForm();
}

function validateForm(){

    const nama =
        document.getElementById(
            "nama"
        ).value.trim();

    const email =
        document.getElementById(
            "email"
        ).value.trim();

    const tanggalLahir =
        document.getElementById(
            "tanggal_lahir"
        ).value.trim();

    const umur =
        document.getElementById(
            "umur"
        ).value.trim();

    const jk =
        document.getElementById(
            "jk"
        ).value.trim();

    const confirm =
        document.getElementById(
            "confirmData"
        ).checked;

    const lengkap =
        nama &&
        email &&
        tanggalLahir &&
        umur &&
        jk;

    document
        .getElementById(
            "startBtn"
        )
        .classList.toggle(
            "disabled",
            !(lengkap && confirm)
        );
}

fillProfile();

useProfile.addEventListener(
    "change",
    function(){

        if(this.checked){

            fillProfile();

        }else{

            clearProfile();

        }
    }
);

document
.getElementById(
    "nama"
)
.addEventListener(
    "input",
    validateForm
);

document
.getElementById(
    "email"
)
.addEventListener(
    "input",
    validateForm
);

document
.getElementById(
    "tanggal_lahir"
)
.addEventListener(
    "change",
    validateForm
);

document
.getElementById(
    "umur"
)
.addEventListener(
    "input",
    validateForm
);

document
.getElementById(
    "jk"
)
.addEventListener(
    "change",
    validateForm
);

document
.getElementById(
    "confirmData"
)
.addEventListener(
    "change",
    validateForm
);

document
.getElementById(
    "startBtn"
)
.addEventListener(
    "click",
    function(e){

        if(
            this.classList.contains(
                "disabled"
            )
        ){

            e.preventDefault();
        }
    }
);

validateForm();