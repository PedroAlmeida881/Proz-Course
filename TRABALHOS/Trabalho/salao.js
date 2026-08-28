function cadastrarAgendamento() {


    let nome = document.getElementById("nome").value.trim();

    let profissional =
        document.getElementById("profissional").value;

    let sexoSelecionado =
        document.querySelector('input[name="sexo"]:checked');

    let data =
        document.getElementById("data").value;

    let horario =
        document.getElementById("horario").value;


    if (nome === "") {

        alert("Por favor, informe o nome do cliente.");

        document.getElementById("nome").focus();

        return false;
    }


    if (!sexoSelecionado) {

        alert("Por favor, selecione o sexo do cliente.");

        return false;
    }


    let sexo = sexoSelecionado.value;



    let servicos =
        document.querySelectorAll(".serv:checked");


    if (servicos.length === 0) {

        alert(
            "Selecione pelo menos um serviço antes de confirmar o agendamento."
        );

        return false;
    }



    let listaServicos = [];



    servicos.forEach(function(servico) {

        listaServicos.push(servico.value);

    });



    if (data === "") {

        alert("Informe a data do atendimento.");

        return false;
    }



    if (horario === "") {

        alert("Informe o horário do atendimento.");

        return false;
    }


    sessionStorage.setItem(
        "nomeCliente",
        nome
    );

    sessionStorage.setItem(
        "profissional",
        profissional
    );

    sessionStorage.setItem(
        "sexoCliente",
        sexo
    );

    sessionStorage.setItem(
        "listaServicos",
        listaServicos.join(", ")
    );

    sessionStorage.setItem(
        "data",
        data
    );

    sessionStorage.setItem(
        "horario",
        horario
    );


    window.location.href = "comprovante.html";

    return false;
}


function cancelarAgendamento() {

    let confirmar = confirm(
        "Tem certeza que deseja cancelar este agendamento?\n\n" +
        "Todos os dados do agendamento serão apagados."
    );


    if (!confirmar) {

        return;
    }



    sessionStorage.removeItem("nomeCliente");

    sessionStorage.removeItem("profissional");

    sessionStorage.removeItem("sexoCliente");

    sessionStorage.removeItem("listaServicos");

    sessionStorage.removeItem("data");

    sessionStorage.removeItem("horario");


    alert("Agendamento cancelado com sucesso.");

    window.location.href = "cadastro_agendamento.html";
}
