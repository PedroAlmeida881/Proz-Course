function verificarMensagem() {
    const veri =document.getElementById("mensagem");
    const codigoDigitado ="Hulk7";
    const cod  =document.getElementById("codigo").value;
    const bot =document.getElementById("botão");
    if(cod == codigoDigitado) {
    veri.innerHTML ="Código válido!"
    }
    else{
    veri.innerHTML="ERRO! Código inválido."
    }
}