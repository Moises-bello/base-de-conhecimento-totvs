---
content_hash: ad9afc3adadf3cb17e0c5f48ad0e99da2045bc51ac67e6a4c07dada7fb0cde7a
fetched_at: '2026-06-29T00:10:59.728103+00:00'
page_id: '615389836'
product: rm
source: tdn-rm
title: Incluir Folha Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/Incluir+Folha+Tarefa
version: 19
---

Com o objetivo de facilitar a criação e as associações necessárias para que o usuário possa realizar apontamentos em folha tarefa, foi disponibilizado o processo de Incluir Folha Tarefa:

Informações Folha TarefaFolha Tarefa Padrão

Através do processo o usuário será guiado passo a passo para criação, associação e disponibilização da folha tarefa padrão de forma simples e rápida.

Na primeira tela o usuário cadastra a folha tarefa padrão:

Na sequência, deve selecionar as tarefas que serão associadas à folha tarefa: Lembrando que se esta tela se comportará conforme parâmetro **Planilha para Apontamentos [Mobilidade (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196)**

Depois realiza a associação do coletor à folha tarefa:

Caso a tarefa não tenha mão de obra, o processo é concluído nessa etapa: (é importante destacar que quando estiver parametrizado para utilizar Planilha executivas para apontamentos  (Conforme parâmetro **Planilha para Apontamentos [Mobilidade (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196))** o processo de alocação de mão de obra não estará disponível

Ao final do processo a folha tarefa criada já será disponibilizada para para apontamento e por essa razão, caso queira efetuar alterações deverá retorná-la para "Em processamento":

Caso o projeto esteja parametrizado para controlar o saldo da equipe na alocação de mão de obra, será exibida ainda a tela abaixo, para que o usuário selecione a equipe que deseja associar à folha, e a tarefa cuja alocação será realizada:

Folha de Produtividade

Através do processo o usuário será guiado passo a passo para criação, associação e disponibilização da folha tarefa de produtividade.

Na primeira tela o usuário cadastra a folha tarefa de produtividade com o membro associado podendo ser Equipe ou Funcionário:

Na sequência, deve selecionar as tarefas que serão associadas à folha tarefa podendo alterar o Valor Alocado e a Quantidade Planejada:

Quando utilizada com Planilha Executiva

* Se o projeto utilizar apontamentos com os itens da planilha executiva, o valor alocado será obtido do valor de mão de obra das tarefas vinculadas a esses itens, considerando o percentual vinculado, como por exemplo:

   Planilha Executiva: **Item 1**  
                 Tarefas vinculadas:  
                   **Tarefa 1** = Vinculada ao item com **50%**, valor de mão de obra **5.000,00**.  
                   **Tarefa 2** = Vinculada ao item com **50%**, valor de mão de obra **3.000,00**.           Ao associar o **Item 1** na folha de tarefa, o valor alocado de mão de obra será de **4.000,00**, pois apenas **50%** de cada tarefa foi vinculado, resultando na soma da metade dos valores.

Depois, o valor alocado será informado para a distribuição dos pesos ou valores para cada membro:

Assim, será apresentado os valores previstos de pagamento para cada membro de acordo com o peso ou valor informado:

Agora, devemos associar os coletores a folha de Produtividade e o processo será concluído nessa etapa:

Ao final do processo a folha tarefa criada já será disponibilizada para para apontamento e por essa razão, caso queira efetuar alterações deverá retorná-la para "Em processamento":
