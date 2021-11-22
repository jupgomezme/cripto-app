
const cardText = document.getElementById("cardText")
const submitButton = document.getElementById("submitButton")
// const clearButton = document.getElementById("clearButton")

const cardTextContent = localStorage.getItem("cardTextContent")

if (cardTextContent) { cardText.innerHTML = cardTextContent }


async function postData(url = 'http://localhost:5000', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    // mode: 'cors',
    // cache: 'no-cache',
    // credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    },
    // redirect: 'follow',
    // referrerPolicy: 'no-referrer',
    body: JSON.stringify(data)
  });
  return response.json();
}

// postData('http://localhost:5000',
//   {
//     "algorithm": "cesar",
//     "action": "cipher",
//     "data": "HELLOWORLD",
//     "key": 1
//   })
//   .then(data => {
//     console.log(data);
//   });


const onClickForm = () => {
  const inputTextValue = document.getElementById("inputText").value;
  const inputKeyValue = document.getElementById("inputKey").value;

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

  fetch("http://localhost:5000", {
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
    const cardKeyText = document.getElementById("cardKeyText");
    const encryptionResultsDiv = document.getElementById("encryptionResultsDiv");

    encryptionResultsDiv.style.display = "flex";

    cardEncryptionText.innerHTML = data_processed[0]
    cardKeyText.innerHTML = data_processed[1]

  }).catch((error) => {
    console.log("Error with request to the Api!")
    console.log(error)
  })

}

const onClickClearButton = () => {
  localStorage.removeItem("cardTextContent")
  cardText.innerHTML = ""
}


submitButton.addEventListener("click", onClickForm)
// clearButton.addEventListener("click", onClickClearButton)