const imageInput = document.getElementById("imageInput");
const imageResultsDiv = document.getElementById("imageResultsDiv");
const encodedImg = document.getElementById("encodedImg");
const encodedBtn = document.getElementById("encodedBtn");
const decodedImg = document.getElementById("decodedImg");

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
        const file_name  = inputFile.name;

        const bodyFormDataEncode = new FormData();
        bodyFormDataEncode.append('file', inputFile);
        bodyFormDataEncode.append('action', 'cipher');
        bodyFormDataEncode.append('algorithm', algorithm);
        bodyFormDataEncode.append('key', '0');

        const bodyFormDataDecode = new FormData();
        bodyFormDataDecode.append('file', inputFile);
        bodyFormDataDecode.append('action', 'decipher');
        bodyFormDataDecode.append('algorithm', algorithm);
        bodyFormDataDecode.append('key', '0');

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
                    encodedBtn.download = "encoded_" + file_name;
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