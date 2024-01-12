// Exibir Mensagem
function exibirMensagem(mensagem, sucesso = true) {
    const mensagemElement = document.getElementById('mensagem');
    
    if (sucesso) {
        mensagemElement.classList.add('sucesso');
        mensagemElement.classList.remove('erro');
    } else {
        mensagemElement.classList.add('erro');
        mensagemElement.classList.remove('sucesso');
    }

    mensagemElement.innerText = mensagem;
}
