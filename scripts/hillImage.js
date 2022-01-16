const imageInput = document.getElementById("imageInput");
const imageResultsDiv = document.getElementById("imageResultsDiv");
const encodedImg = document.getElementById("encodedImg");
const decodedImg = document.getElementById("decodedImg");

const onFileUpload = () => {
    const inputFile = imageInput.files[0]
    const bodyFormData = new FormData();
    bodyFormData.append('file', inputFile);

    fetch(API_ENDPOINT + "img", {
        method: 'post',
        body: bodyFormData
    })
        .then((results) => {
            return results.blob()
        })
        .then((results) => {
            encodedImg.src = URL.createObjectURL(results);
            imageResultsDiv.style.display = 'flex'
        })

}

imageInput.onchange = onFileUpload;
