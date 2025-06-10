console.log("Script inicializado");

const inputNome = document.getElementById("inptNome");
const inputSenha = document.getElementById("inptSenha");
const btnSalvar = document.getElementById("btnSalvar");
const divResponse = document.getElementById("response");

btnSalvar.addEventListener('click',btnSalvarClick);

function btnSalvarClick(){
    console.log("Btn clicado!")
    
    readTxt()
    .then(resposta => {
        if (resposta) {
            console.log("Usuário Válido!")
            divResponse.innerHTML = 
            `
            <nav>
                <a href="./paginas/home.html" > Página Principal </a>
            </nav>
            `;
        }
        else {
            console.log("Usuário Inválido!")
            divResponse.innerHTML = `Usuário inválido`

        }
    })
    console.log("CONSOLE LOG QUE VEM DEPOIS")
}

async function readTxt(){
    console.log("readTxt...")
    return fetch("credenciais.txt")
    .then(resposta => resposta.text())
    .then(text => {
        return credValidate(text)
    })
    .catch(error => {
        console.log("Erro: ",error)
        return false
    })
}

function credValidate(credenciais){
    console.log("credValidate...",credenciais)
    let inptNome = inputNome.value;
    let inptSenha = inputSenha.value;
    let txtNome = credenciais.split("/")[0]
    let txtSenha = credenciais.split("/")[1]
    return inptNome == txtNome && inptSenha == txtSenha
}
    