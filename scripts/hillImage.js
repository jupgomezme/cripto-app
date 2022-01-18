const imageInput = document.getElementById("imageInput");
const imageResultsDiv = document.getElementById("imageResultsDiv");
const encodedImg = document.getElementById("encodedImg");
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

const onFileUpload = () => {
    imageResultsDiv.style.display = 'none'
    const inputFile = imageInput.files[0]

    const bodyFormDataEncode = new FormData();
    bodyFormDataEncode.append('file', inputFile);
    bodyFormDataEncode.append('action', 'cipher');

    const bodyFormDataDecode = new FormData();
    bodyFormDataDecode.append('file', inputFile);
    bodyFormDataDecode.append('action', 'decipher');

    sendImageRequest(bodyFormDataEncode)
        .then((results) => {
            return results.blob()
        })
        .then((results) => {
            encodedImg.src = URL.createObjectURL(results);
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

imageInput.onchange = onFileUpload;
