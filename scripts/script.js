// const API_ENDPOINT = "http://0.0.0.0:8000/";
const API_ENDPOINT = "http://54.156.2.139:8000/";

const lettersAndSpace = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
const numbersAndComma = "0123456789,"
const letters = lettersAndSpace.slice(0, -1)
const numbers = numbersAndComma.slice(0, -1)
const lettersAndNumbers = letters + numbers
const lettersAndNumbersWithSpace = lettersAndSpace + numbers

const createTable = (tableData) => {
    const table = document.createElement('table');
    const tableBody = document.createElement('tbody');

    tableData.forEach(function (rowData) {
        const row = document.createElement('tr');

        rowData.forEach(function (cellData) {
            const cell = document.createElement('td');
            cell.style.padding = "10px"
            cell.appendChild(document.createTextNode(cellData));
            row.appendChild(cell);
        });

        tableBody.appendChild(row);
    });

    table.appendChild(tableBody);

    return table
}

const alphabetLikeChecker = (allegedValidText) => {

    for (let i = 0; i < allegedValidText.length; i++) {
        const char = allegedValidText[i]
        if (!lettersAndSpace.includes(char)) {
            return false
        }
    }

    return true

}

const numbersChecker = (allegedValidNumbers) => {

    for (let i = 0; i < allegedValidNumbers.length; i++) {
        const char = allegedValidNumbers[i]
        if (!numbersAndComma.includes(char)) {
            return false
        }
    }

    return true

}

const alphabetWithoutSpaceChecker = (allegedValidText) => {

    for (let i = 0; i < allegedValidText.length; i++) {
        const char = allegedValidText[i]
        if (!letters.includes(char)) {
            return false
        }
    }

    return true

}

const stringChecker = (allegedValidString) => {

    for (let i = 0; i < allegedValidString.length; i++) {
        const char = allegedValidString[i]
        if (!lettersAndNumbers.includes(char)) {
            return false
        }
    }

    return true

}

const stringWithSpaceChecker = (allegedValidString) => {

    for (let i = 0; i < allegedValidString.length; i++) {
        const char = allegedValidString[i]
        if (!lettersAndNumbersWithSpace.includes(char)) {
            return false
        }
    }

    return true

}

const binaryStringChecker = (allegedBinaryString) => {
    for (let i = 0; i < allegedBinaryString.length; i++) {
        const char = allegedBinaryString[i];
        if (char !== "1" && char !== "0") return false
    }
    return true
}

const alphabetChecker = (allegedUnsortedAlphabet) => {
    for (let i = 0; i < letters.length; i++) {
        const letter = letters[i]
        if (!allegedUnsortedAlphabet.includes(letter)) {
            return false
        }
    }
    return allegedUnsortedAlphabet.length === 26;
}

const integerMod26Checker = (allegedIntegerMod26) => {
    const allegedIntegerMod26Casted = parseInt(allegedIntegerMod26)
    return !(allegedIntegerMod26Casted < 0 || allegedIntegerMod26Casted >= 26);
}

const MCD = (a, b) => {
    let temp;
    while (b !== 0) {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
};

const pairIntegersMod26Checker = (allegedIntegersMod26) => {

    for (let i = 0; i < allegedIntegersMod26.length; i++) {
        const char = allegedIntegersMod26[i]
        if (!numbersAndComma.includes(char)) {
            return false
        }
    }

    let allegedKey;
    try {
        allegedKey = allegedIntegersMod26.split(",").map((element) => {
            return parseInt(element)
        });
    } catch (error) {
        return false;
    }
    if (allegedKey.length !== 2) {
        return false
    }
    const a = allegedKey[0];
    const b = allegedKey[1];

    if (typeof a !== "number" || typeof b !== "number") {
        return false
    }

    if (a <= 0 || a >= 26 || b <= 0 || b >= 26) {
        return false
    }

    return MCD(a, 26) === 1;
}

const stringFixedLengthsChecker = (lengths) => {
    return (allegedStringFixedLengthChecker) => {
        let count = 0
        for (let i = 0; i < lengths.length; i++) {
            length = lengths[i]
            if (allegedStringFixedLengthChecker.length === length) {
                count += 1;
            }
        }
        return stringChecker(allegedStringFixedLengthChecker) && count > 0;
    }
}

const alphabetSubPermutationChecker = (permutation) => {
    let allegedKey;
    try {
        allegedKey = permutation.split(",").map((element) => {
            return parseInt(element)
        });
    } catch (error) {
        return false;
    }
    allegedKey.sort();
    if (allegedKey[0] !== 0) {
        return false
    }
    for (let i = 1; i < allegedKey.length; i++) {
        if (allegedKey[i] !== allegedKey[i - 1] + 1) {
            return false
        }
    }
    return true
}

const getKeyChecker = (algorithm) => {
    switch (algorithm) {
        case 'displacement':
        case 'displacementAnalysis':
            return integerMod26Checker
        case 'substitution':
            return alphabetChecker
        case 'permutation':
            return alphabetSubPermutationChecker
        case 'affine':
            return pairIntegersMod26Checker
        case 'vigenere':
        case 'hill':
        case 'hillAnalysis':
            return alphabetLikeChecker
        case 'des':
            return stringFixedLengthsChecker([8])
        case '3des':
            return stringFixedLengthsChecker([16, 24])
        case 'sdes':
            return binaryStringChecker
        case 'rsa':
        case 'el_gamal':
        case 'rabin':
            return numbersChecker;
        case 'gamma_pentagonal':
            return () => true;
        default:
            throw new Error("Wrong algorithm!")
    }
}

const getTextChecker = (algorithm, action) => {
    switch (algorithm) {
        case 'des':
        case '3des':
            if (action === "cipher") return stringWithSpaceChecker
            else return stringChecker
        case 'sdes':
            return binaryStringChecker
        case 'permutation':
            return alphabetWithoutSpaceChecker
        case 'rsa':
        case 'el_gamal':
            if (action === "cipher") return stringWithSpaceChecker
            else return numbersChecker
        case 'rabin':
            if (action === "cipher") return () => true;
            else return numbersChecker
        case 'gamma_pentagonal':
            if (action === "cipher") return alphabetWithoutSpaceChecker
            else return () => true;
        default:
            return alphabetLikeChecker
    }
}

const getInputsForm = (action) => {

    let inputTextId, inputKeyId

    switch (action) {
        case "cipher":
            inputTextId = "inputTextEncrypt"
            inputKeyId = "inputKeyEncrypt"
            break
        case "decipher":
        case "analyze":
            inputTextId = "inputTextDecrypt"
            inputKeyId = "inputKeyDecrypt"
            break
        default:
            throw new Error("Wrong action!")
    }

    const data = document.getElementById(inputTextId).value.toString().toUpperCase();

    let key = document.getElementById(inputKeyId)
    if (key) {
        key = key.value.toString().toUpperCase();
    }

    return {
        data,
        key
    }
}

const sendRequest = (requestData) =>
    new Promise((resolve, reject) => {
        fetch(API_ENDPOINT, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        }).then((response) => {
            return response.json()
        }).then((data_processed) => {
            resolve(data_processed)
        }).catch((error) => {
            alert("There was an error with the API, Please review your request.")
            console.log(error)
            reject(error)
        })

    })

const updateResults = (dataProcessed, algorithm, action) => {

    let [textProcessed, keyUsed] = dataProcessed

    let idResultsDiv, idResultsCardText, idResultsCardKey

    switch (action) {
        case "cipher":
            idResultsDiv = "encryptionResultsDiv"
            idResultsCardText = "cardEncryptionText"
            idResultsCardKey = "cardEncryptionKey"
            break
        case "decipher":
        case "analyze":
            idResultsDiv = "decryptionResultsDiv"
            idResultsCardText = "cardDecryptionText"
            idResultsCardKey = "cardDecryptionKey"
            break
        default:
            throw new Error("Wrong action!")
    }

    const encryptionResultsDiv = document.getElementById(idResultsDiv);
    encryptionResultsDiv.style.display = "flex";

    const resultsCardText = document.getElementById(idResultsCardText);
    const resultsCardKey = document.getElementById(idResultsCardKey);

    resultsCardText.innerHTML = textProcessed;

    if (algorithm === "hill" || algorithm === "hillAnalysis") {
        resultsCardKey.innerHTML = "";
        resultsCardKey.appendChild(createTable(keyUsed))
    } else {
        resultsCardKey.innerHTML = keyUsed;
    }

}

const onClickButton = (algorithm, action) => {
    return () => {
        {
            const {
                data,
                key
            } = getInputsForm(action)

            if (!data) {
                alert("Please introduce the text!")
                return;
            }

            const textChecker = getTextChecker(algorithm, action);
            if (!textChecker(data)) {
                alert("Please introduce valid text!")
                return;
            }

            const keyChecker = getKeyChecker(algorithm);
            switch (action) {
                case "cipher":
                    if (key) {
                        if (!keyChecker(key)) {
                            alert("Please introduce a valid key!")
                            return;
                        }
                    }
                    break
                case "decipher":
                    if (!key || !keyChecker(key)) {
                        alert("Please introduce a valid key!!")
                        return;
                    }
                    break
                case "analyze":
                    break
                default:
                    throw new Error("Wrong action!")
            }

            sendRequest({
                algorithm,
                action,
                data,
                key
            })
                .then((dataProcessed) => {
                    if (dataProcessed === "Invalid key") {
                        alert("Please introduce a valid key!")
                        return;
                    }
                    updateResults(dataProcessed, algorithm, action)
                })
        }
    }
}


const runScript = (algorithm) => {

    if (algorithm === "aes") {
        return;
    }

    let decipherOrAnalyze = "decipher";
    if (!algorithm.includes("Analysis")) {
        const onClickFormEncrypt = onClickButton(algorithm, "cipher");
        const submitButtonEncrypt = document.getElementById("submitButtonEncrypt")
        submitButtonEncrypt.addEventListener("click", onClickFormEncrypt)
    } else {
        decipherOrAnalyze = "analyze"
    }

    const onClickFormDecrypt = onClickButton(algorithm, decipherOrAnalyze);
    const submitButtonDecrypt = document.getElementById("submitButtonDecrypt")
    submitButtonDecrypt.addEventListener("click", onClickFormDecrypt)
}

const algorithm = document.currentScript.getAttribute('algorithm')
if (algorithm !== "") {
    runScript(algorithm)
}
