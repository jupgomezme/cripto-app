const sendDocRequest = (body) =>
    new Promise((resolve, reject) => {
        fetch(API_ENDPOINT + "doc", {
            method: 'post',
            body,
        })
            .then((results) => {
                return results.json()
            })
            .then((results) => {
                resolve(results)
            })
            .catch((error) => {
                reject(error)
            })
    })

const onFileUpload = (action) => () => {

    const docInputSign = document.getElementById("docInputSign");

    const signResultsDiv = document.getElementById("signResultsDiv");
    const fileUploadedSignSpan = document.getElementById("fileUploadedSignSpan");
    const signatureSignSpan = document.getElementById("signatureSignSpan");
    const keySignSpan = document.getElementById("keySignSpan");

    const docInputVSign = document.getElementById("docInputVSign");
    const signatureVSign = document.getElementById("signatureVSign");

    const vSignResultsDiv = document.getElementById("vSignResultsDiv");
    const fileUploadedVSignSpan = document.getElementById("fileUploadedVSignSpan");
    const signatureVSignSpan = document.getElementById("signatureVSignSpan");
    const keyVSignSpan = document.getElementById("keyVSignSpan");

    const verifiedSpan = document.getElementById("verifiedSpan");

    if (action === "verify" && !signatureVSign.value) {
        alert("Please introduce the signature!")
        return;
    }

    let resultsDiv;
    let fileInput;
    let signature;
    let fileUploadedSpan;
    let signatureSpan;
    let keySpan;
    switch (action) {
        case "sign":
            resultsDiv = signResultsDiv;
            fileInput = docInputSign;
            fileUploadedSpan = fileUploadedSignSpan;
            signatureSpan = signatureSignSpan;
            keySpan = keySignSpan;
            break;
        case "verify":
            resultsDiv = vSignResultsDiv;
            fileInput = docInputVSign;
            signature = signatureVSign.value;
            fileUploadedSpan = fileUploadedVSignSpan;
            signatureSpan = signatureVSignSpan;
            keySpan = keyVSignSpan;
            break;
    }
    resultsDiv.style.display = 'none';


    const inputFile = fileInput.files[0]
    const fileName = inputFile.name;

    const bodyFormDataEncode = new FormData();
    bodyFormDataEncode.append('file', inputFile);
    bodyFormDataEncode.append('action', action);
    bodyFormDataEncode.append('signature', signature);

    sendDocRequest(bodyFormDataEncode)
        .then((results) => {
            const signatureOutput = results[0];
            const keyOutput = results[1];
            let is_verified;
            if (action === "verify") {
                is_verified = results[2];
            }

            fileUploadedSpan.innerHTML = fileName;
            signatureSpan.innerHTML = signatureOutput;
            keySpan.innerHTML = keyOutput;

            if (action === "verify") {
                let innerHtmlVS;
                switch (is_verified) {
                    case true:
                        innerHtmlVS = "<p class=\"text-success\">True</p>"
                        break
                    case false:
                        innerHtmlVS = "<p class=\"text-danger\">False</p>"
                }
                verifiedSpan.innerHTML = innerHtmlVS;
            }

            resultsDiv.style.display = 'flex';
        })
        .catch((error) => {
            alert("There was an error with the API, Please review your request.")
            console.log(error)
        })

}

docInputSign.onchange = onFileUpload("sign");
docInputVSign.onchange = onFileUpload("verify");