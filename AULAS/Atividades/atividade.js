function verifica() {
    let nomes = ["Pedro", "Lucas", "Ana"];
    let senhas = ["123", "1234", "12345"];

    const tilt = document.getElementById("titulo");
    const mensagem = document.getElementById("msg");
    const name = document.getElementById("username").value;
    const acesso = document.getElementById("senha").value;

    let correto = false;

    for (let i = 0; i < nomes.length; i++) {
        if (name === nomes[i] && acesso === senhas[i]) {
            correto = true;
            break;
        }
    }

    if (correto) {
        mensagem.innerHTML = "Redirecionando...";
          setTimeout(() => {
            window.location.href = "https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChsSEwj2p5zNtaiPAxWAW0gAHZlyB_oYACICCAEQABoCY2U&co=1&ase=2&gclid=EAIaIQobChMI9qeczbWojwMVgFtIAB2Zcgf6EAAYASAAEgIfXPD_BwE&ohost=www.google.com&cid=CAASJeRoYPev6p-p_jAbJFF3_vrMWMiBv49etrnBUUeELNLoEHrXZns&category=acrcp_v1_40&sig=AOD64_2Z8Uop2c0EJAkqVYHV-2esFJLvGA&q&nis=4&adurl&ved=2ahUKEwi34pbNtaiPAxWKr5UCHco_AIgQ0Qx6BAgJEAE" 
        }, 2000);
    } else {
          setTimeout(() => {
        mensagem.innerHTML = "Login ou senha incorretos,tente novamente!";
         document.getElementById("username").value = "";
            document.getElementById("senha").value = "";
        }, 2000);
    }

    setTimeout(() => {
        mensagem.innerHTML = "Será que você está cadastrado?";
        titulo,innerHTML = "Validação de Usuário!"
    }, 5000);

}