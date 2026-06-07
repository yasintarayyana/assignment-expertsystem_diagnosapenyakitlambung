const tanggalLahir =
document.getElementById(
'tanggal_lahir'
);

const umurInput =
document.getElementById(
'umur'
);

tanggalLahir.addEventListener(
'change',
function(){

    const birthDate =
    new Date(this.value);

    const today =
    new Date();

    let age =
    today.getFullYear()
    -
    birthDate.getFullYear();

    const monthDiff =
    today.getMonth()
    -
    birthDate.getMonth();

    if(
        monthDiff < 0
        ||
        (
            monthDiff === 0
            &&
            today.getDate()
            <
            birthDate.getDate()
        )
    ){
        age--;
    }

    umurInput.value =
    age;
});