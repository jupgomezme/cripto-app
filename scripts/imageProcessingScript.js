const imageInput = document.getElementById("imageInput");
const imageResultsDiv = document.getElementById("imageResultsDiv");
const encodedImg = document.getElementById("encodedImg");
const encodedBtn = document.getElementById("encodedBtn");
const decodedImg = document.getElementById("decodedImg");
const keyImageInput = document.getElementById("keyImageInput");

const sendImageRequest = (body) =>
    new Promise((resolve, reject) => {
        fetch(API_ENDPOINT + "img", {
            method: 'post',
            body,
        }).then((results) => {
            resolve(results)
        }).catch((error) => {
            reject(error)
        })
    })

const onFileUpload = (algorithm) => {
    return () => {
        imageResultsDiv.style.display = 'none'
        const inputFile = imageInput.files[0]
        const file_name = inputFile.name;

        const bodyFormDataEncode = new FormData();
        bodyFormDataEncode.append('file', inputFile);
        bodyFormDataEncode.append('action', 'cipher');
        bodyFormDataEncode.append('algorithm', algorithm);

        const bodyFormDataDecode = new FormData();
        bodyFormDataDecode.append('file', inputFile);
        bodyFormDataDecode.append('action', 'decipher');
        bodyFormDataDecode.append('algorithm', algorithm);

        let fakeKey;
        if (algorithm === "des" || algorithm === "3des") {
            fakeKey = keyImageInput.value.toUpperCase();
            if (fakeKey) {
                const keyImageChecker = getKeyChecker(algorithm);
                if (!keyImageChecker(fakeKey)) {
                    alert("Please introduce a Valid key");
                    return;
                }
            }
        }

        sendImageRequest(bodyFormDataEncode)
            .then((results) => {
                return results.blob()
            })
            .then((results) => {
                const objectUrl = URL.createObjectURL(results)
                if (algorithm === "hill") {
                    encodedImg.src = objectUrl;
                } else {
                    encodedBtn.href = objectUrl;
                    if (algorithm === "aes") {
                        encodedBtn.download = "encrypted.enc";
                    } else {
                        encodedBtn.download = "encoded_" + file_name;
                    }

                }
                return sendImageRequest(bodyFormDataDecode)
            })
            .then((results) => {
                return results.blob()
            })
            .then((results) => {
                decodedImg.src = URL.createObjectURL(results);
                imageResultsDiv.style.display = 'flex'
            })
            .catch((error) => {
                console.log(error);
                alert("Request failed to the API")
            })
    }

}

const runImageScript = (algorithm) => {
    imageInput.onchange = onFileUpload(algorithm);
}

runImageScript(document.currentScript.getAttribute('algorithm'))