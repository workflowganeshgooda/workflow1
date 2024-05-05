// PAN VALIVDATION
function validatePAN() {
    var panInput = document.getElementById("pan");
    var panPattern = /^([A-Z]{5}[0-9]{4}[A-Z]{1})$/;
    var isValid = panPattern.test(panInput.value);

    if (!isValid) {
        alert("Invalid PAN Number. PAN should be in the format: ABCDE1234F");
        return false;
    }

    return true;
}
