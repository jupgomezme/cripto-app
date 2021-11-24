const apiEndpoint = "http://localhost:5000";



const onClickFormEncrypt = () => {
  const inputTextValue = document.getElementById("inputTextEncrypt").value;
  const inputKeyValue = document.getElementById("inputKeyEncrypt").value;

  if (!inputTextValue) {
    alert("Please introduce some text!")
    return;
  }

  const data = {
    algorithm: "cesar",
    action: "cipher",
    data: inputTextValue.toUpperCase(),
    key: parseInt(inputKeyValue)
  }

  fetch(apiEndpoint, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  }).then((response) => {
    return response.json()
  }).then((responseJson) => {
    const { data_processed } = responseJson;

    const cardEncryptionText = document.getElementById("cardEncryptionText");
    const cardEncryptionKey = document.getElementById("cardEncryptionKey");

  
    const encryptionResultsDiv = document.getElementById("encryptionResultsDiv");
    encryptionResultsDiv.style.display = "flex";

    cardEncryptionText.innerHTML = data_processed[0]
    cardEncryptionKey.innerHTML = data_processed[1]

  }).catch((error) => {
    console.log("Error with request to the Api!")
    console.log(error)
  })

}

const submitButtonEncrypt = document.getElementById("submitButtonEncrypt")
submitButtonEncrypt.addEventListener("click", onClickFormEncrypt)




const onClickFormDecrypt = () => {
  const inputTextValue = document.getElementById("inputTextDecrypt").value;
  const inputKeyValue = document.getElementById("inputKeyDecrypt").value;

  if (!inputTextValue) {
    alert("Please introduce the text!")
    return;
  }

  if (!inputKeyValue) {
    alert("Please introduce the key!")
    return;
  }

  const data = {
    algorithm: "cesar",
    action: "decipher",
    data: inputTextValue.toUpperCase(),
    key: parseInt(inputKeyValue)
  }

  fetch(apiEndpoint, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  }).then((response) => {
    return response.json()
  }).then((responseJson) => {
    const { data_processed } = responseJson;

    const cardDecryptionText = document.getElementById("cardDecryptionText");

    const decryptionResultsDiv = document.getElementById("decryptionResultsDiv");
    decryptionResultsDiv.style.display = "flex";

    cardDecryptionText.innerHTML = data_processed[0]

  }).catch((error) => {
    console.log("Error with request to the Api!")
    console.log(error)
  })

}

const submitButtonDecrypt = document.getElementById("submitButtonDecrypt")
submitButtonDecrypt.addEventListener("click", onClickFormDecrypt)