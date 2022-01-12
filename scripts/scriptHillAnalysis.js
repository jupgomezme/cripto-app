const apiEndpoint = "http://127.0.0.1:8000/";

const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

const textChecker = (allegedValidText) => {
    allegedValidText = allegedValidText.toUpperCase();

    for (let i = 0; i < allegedValidText.length; i++) {
        const char = allegedValidText[i]
        if (!letters.includes(char)) {
            return false
        }
    }

    return true

}

function createTable(tableData) {
    var table = document.createElement('table');
    var tableBody = document.createElement('tbody');
  
    tableData.forEach(function(rowData) {
      var row = document.createElement('tr');
  
      rowData.forEach(function(cellData) {
        var cell = document.createElement('td');
        cell.style.padding = "10px"
        cell.appendChild(document.createTextNode(cellData));
        row.appendChild(cell);
      });
  
      tableBody.appendChild(row);
    });
  
    table.appendChild(tableBody);

    const cardEncryptionKey = document.getElementById("cardEncryptionKey");
    cardEncryptionKey.innerHTML = "";
    cardEncryptionKey.appendChild(table);
  }

const onClickFormEncrypt = () => {
    const inputTextValue = document.getElementById("inputText").value;
    const encryptedTextValue = document.getElementById("encryptedText").value;
    const matrixSize = document.getElementById("matrixSize").value;

    if (!inputTextValue) {
        alert("Please introduce the text!")
        return;
    }

    if (!encryptedTextValue) {
        alert("Please introduce the text encrypted!")
        return;
    }

    if (!matrixSize) {
        alert("Please introduce the matrix size!")
        return;
    }

    if (!textChecker(inputTextValue)) {
        alert("Please use alphabetic characters exclusively");
        return;
    }

    if (!textChecker(encryptedTextValue)) {
        alert("Please use alphabetic characters exclusively");
        return;
    }

    const data = {
        algorithm: "hillAnalysis",
        action: null,
        data: inputTextValue.toUpperCase(),
        key: null,
        encrypted_for_hill_analysis: encryptedTextValue.toUpperCase(),
        matrix_size_for_hill_analysis: parseInt(matrixSize)
    }

    fetch(apiEndpoint, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then((response) => {
        return response.json()
    }).then((data_processed) => {
        
        if (data_processed === "invalid size of key") {
            alert("Invalid matrix size");
            return;
        }

        const encryptionResultsDiv = document.getElementById("encryptionResultsDiv");
        encryptionResultsDiv.style.display = "flex";

        createTable(data_processed)

    }).catch((error) => {
        console.log("Error with request to the Api!")
        console.log(error)
    })

}

const submitButtonEncrypt = document.getElementById("submitButtonEncrypt")
submitButtonEncrypt.addEventListener("click", onClickFormEncrypt)


