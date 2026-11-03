---
content_hash: 50d18cac29086c5953b49c5ee26ca326fd2c6487d7190b1ec3197a2680600ba6
fetched_at: '2026-06-29T00:09:13.720641+00:00'
page_id: '421385095'
product: rm
source: tdn-rm
title: Apontamentos Conciliados
type: documentation
url: https://tdn.totvs.com/display/LRM/Apontamentos+Conciliados
version: 12
---

---

No cadastro de Ciclos de Transporte através do anexo de "Apontamentos Conciliados" é possível visualizar, analisar e ajustar as informações de Ciclos de Transportes gerados por pares de registros no processo de "Conciliar Apontamentos".

Através do menu Controle | Minha Obra | Ciclos de Transporte, temos o Anexos de Apontamentos Conciliados, onde o usuário pode visualizar os apontamentos já conciliados de Ciclos de Transporte.  
Os registros deste anexo são o "casamento" de dois registros, um de carga e outro de descarga, que originalmente estão no anexo de "Apontamentos dos Coletores" e conterão as referências (identificadores) dos apontamentos que o originaram.

**Apontamentos Conciliados**

Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra \ Ciclos de Transporte.

São exibidos apontamentos pendentes, validados e conciliados. Sendo assim, são disponibilizados filtros previamente configurados (como um botão na barra de ferramentas da visão) onde tais filtros permitem maior agilidade no gerenciamento dos registros, principalmente para localização e seleção para operação em grupo;

Os filtros inicialmente idealizados para esta opção são os de “Apontamentos dos últimos 7 dias”, “Apontamentos dos últimos 30 dias”, “Apontamentos por data”, “Apontamentos Pendentes”, “Apontamentos Validados”. Lembrando ainda das funcionalidades inerentes da visão que são a ordenação e agrupamentos por campos, capacidade de se utilizar funções de média, somatórios, etc. por campo;

Apresenta para o usuário os seguintes dados:

* **Status**: Indica se o apontamento está pendente ou conciliado.
  + **Pendente**: Status inicial de um registro que foi conciliado;
  + **Validado**: Apontamento conciliado que foi validado pelo usuário. Este status indica que os dados conciliados estão corretos;
  + **Apropriado**: O apontamento conciliado teve seu custo apropriado. E um registro de apropriação foi gerado na apropriação de Serviços/Insumos.
* **Equipamento**: Equipamento em que foi realizado o apontamento;
* **Apontamento de carga**: Apontamento do início (saída) do ciclo de transporte.  É exibida a data e hora em que o apontamento do início do ciclo foi realizado. A data irá também considerar os minutos e segundos (HH:mm:ss);
* **Apontamento de descarga**: Apontamento do fim (entrada) do ciclo de transporte.  É exibida a data e hora em que o apontamento do fim do ciclo foi realizado. A data irá também considerar os minutos e segundos (HH:mm:ss);
* **Tarefa Apropriação**: Exibe a tarefa em que o apontamento foi apropriado;
* **Equipamento Responsável pela Carga:**Traz a informação do equipamento que realizou a carga no veículo que irá transportá-la (esse campo fica visível somente com a marcação do [parâmetro correspondente](https://tdn.totvs.com/pages/viewpage.action?pageId=662419328));
* **Observação:** Texto das observações incluidas nos apontamentos de carga e descarga.
* **Capacidade do Bem e Unidade**: Exibe a capacidade do equipamento e a unidade em que é calculada.
* **Duração**: A duração do ciclo de transporte será a diferença em horas entre a data fim e a data início. Esta informação será calculada ao exibir a tela;
* **Distância Total (Km):** Distância calculada no trajeto da carga até a descarga dos apontamentos de ciclo que forem do tipo distância percorrida. Para saber como é feito esse cáclulo,

Observação

Registros com o status "Apropriado" não poderão mais sofrer ajustes.   
Os apontamentos conciliados não poderão ser editados. Somente as seguintes ações poderão ser aplicadas sobre estes apontamentos:

* Desfazer conciliação;
* Validar conciliação;
* Apropriar apontamento conciliado.

O status só será alterado através de processos. Registros com o status "Apropriado" não poderão ser desconciliados.

**Validar Apontamentos**

Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra \ Ciclos de Transporte \ Anexo \ Apontamentos Conciliados \ Processos \ Validar Apontamentos;

É necessário que após a conciliação de dois apontamentos realizados pelos coletores o apontamento conciliado seja analisado e validado, com o intuído de certificar que as informações conciliadas estão corretas.

O status Validado não possui uma forma automática que o valor, pois é uma situação onde o apontamento deve passar por uma verificação manual, uma análise pelo usuário a fim de garantir que suas informações estejam consistentes. Após esta verificação deve-se alterar o status do apontamento para “Validado".

Através da lista de registros selecionados previamente na visão de apontamentos o sistema atualiza o STATUS de cada apontamento da lista para o valor “Validado”.

Este processo é disparado sem a necessidade de uma interface específica em que o usuário precise informar algum dado em particular.

**Desfazer Conciliação**

Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra \ Ciclos de Transporte \ Anexo \ Apontamentos Conciliados \ Processos \ Desfazer conciliação.

Este processo altera o STATUS dos apontamentos originais valorando-os como “Pendente” e exclui o registro de apontamento conciliado. Além disso, este é disparado sem a necessidade de uma interface específica em que o usuário precise informar algum dado em particular.

Para execução deverá ser selecionado pelo menos um apontamento conciliado, porém, poderá ser executado para vários registros simultaneamente.

Ao ser disparado somente serão desfeitas conciliações de registros com o status de “Pendente” ou “Validado”. Caso algum registro não possua algum destes status o processo executará normalmente e será incluída mensagem no final do processo informando que a conciliação não foi realizada.

 Como Fazer

---
