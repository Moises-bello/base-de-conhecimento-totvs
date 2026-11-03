---
content_hash: 58f9a0f9937e0c8e8f4537205d9c38f17eeea05f27c95b6e7fc9bf8d33ef6d58
fetched_at: '2026-06-29T00:10:59.701016+00:00'
page_id: '615383198'
product: rm
source: tdn-rm
title: Medicamentos PEP RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Medicamentos+PEP+RM
version: 27
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Medicamentos "simples"**
3. **Medicamentos com diluição**
4. **Campo "Observação"**
5. **Medicamentos do Paciente**
6. **Campo "Se necessário"**
7. **Alerta Dosagem Mínima e Máxima**
8. **Alerta de Medicamento de Alto Custo**
9. **Prescrição de antibióticos e prorrogação do tratamento**
10. **Horário Padrão**

MedicamentosVisão Geral

## **01. VISÃO GERAL**

Possibilidade de prescrever medicamentos para realização do tratamento do paciente.

Medicamentos "simples"

## **02. MEDICAMENTOS "SIMPLES"**

No menu de prescrição, na tela principal, no campo de busca, é possível o usuário realizar a busca por um determinado medicamento. Dessa forma, ao pesquisar pelo item, ao clicar, já será habilitada a modal de medicamento com o item selecionado.

No submenu de medicamentos, ao clicar em adicionar será habilitada a modal para inclusão do item. No campo de busca, podemos digitar o nome comercial ou o principio ativo do medicamento. Ao digitar, serão listados todos que os que possuem o texto da busca. Após selecionar um item, serão habilitados os campos para definição. Sendo obrigatórios definir via, quantidade, unidade e frequência. Ao selecionar frequência e inicio, o sistema irá sugerir horários de realização do item dentro do prazo de validade da prescrição médica.

Poderá ser possível marcar o item como se necessário, ou a critério médico. Caso marcada a checkbox de se necessário, o campo condição se torna obrigatório.

Quando houver integração com o EMS2, apenas os saldos dos medicamentos controlados por lote serão validados.

Caso o medicamento selecionado possua apenas uma via, o sistema carregara automaticamente a via que foi encontrada.

Medicamentos com diluição

## **03. MEDICAMENTOS COM DILUIÇÃO**

Ao selecionar um medicamento que tenha amarrado ao mesmo um padrão de diluição, com itens diluentes devidamente amarrado ao cadastro, ao selecionar o medicamento o sistema já habilita os campos diluição e padrão de diluição.

O sistema trará o campo diluição com a opção de "informar o padrão de diluição", logo o usuário precisará informar o padrão especifico. Em seguida, o sistema irá habilitar os campos com os componentes que fazem parte daquele padrão. Ao selecionar o componente que será utilizado e informar as opções desejadas, basta clicar no botão de incluir.

Campo "Observação"

## **04. CAMPO "OBSERVAÇÃO"**

Ao selecionar uma opção no campo via, o campo observação será preenchido automaticamente se houver uma observação padrão vinculada com o medicamento.

Medicamentos do Paciente

## **05. MEDICAMENTOS DO PACIENTE**

Quando o usuário inserir um medicamento é possível marcar a checkbox de "medicamento do paciente".

Medicamentos selecionados como medicamento do paciente, serão sinalizados na tela principal da prescrição.

Medicamentos selecionados como medicamento do paciente serão sinalizados na impressão

Campo "Se necessário"

## **06. CAMPO "SE NECESSÁRIO"**

É possível registrar condições para medicamentos utilizando o campo se necessário, ao digitar e pressionar enter sobre o campo o registro será feito.

Após incluir o registro, as condições inseridas serão visualizadas na tela inicial da prescrição.

Alerta Dosagem Mínima e Máxima

## **07.** **Alerta Dosagem Mínima e****Máxima**

Ao selecionar um medicamento e possível gerar um alerta para dosagem pedindo a justificativa para inclusão do item.

para configurar o alerta abra o RM menu Cadastros > Produto > "selecionar um medicamento" > Anexos > informações - TOTVS saúde > Anexos > Doses Máxima e Mínima.

no painel e possível definir o alerta de dosagem máximo e mínimo para o medicamento selecionado.

A tabela das opções listadas para a seleção de uma unidade dentro do painel de dose máxima e mínima, fica vinculado a tabela de preços

caminho: Cadastros > Produto > "selecionar um medicamento" > Anexos > informações - TOTVS saúde > Anexos > **Tabela de Preço**.

ao configurar uma unidade na tabela de preço ela e exibida nas opções do campo dosagem máxima e mínima no RM.

**Lembrando que a comparação das unidades para exibir o alerta leva em consideração o código do produto e não a descrição dele.**

Exemplo: se no menu Cadastros > Produto > "selecionar um medicamento" > Anexos > informações - TOTVS saúde > Anexos > **Unidade de Dosagem** eu selecionei o comprimido com o

Código: "COM" descrição: comprimido

E na configuração de dose máxima e mínima selecionei:

Código: "CO" descrição: comprimido.

**O Prontuário "PEP-RM" vai entender que são dois produtos diferentes e não será exibido o alerta de dosagem.**

Após definição dos alertas com o PEP-RM aberto navegue até o menu **prescrição médica** ao selecionar o medicamento com os parâmetros configurados o alerta e exibido.

Alerta de Medicamento de Alto Custo

## **08.** **Alerta de Medicamento de Alto Custo**

O Alerta de alto custo no sistema está diretamente vinculado à existência e à configuração de uma **Condição Contratual** específica para o convênio do paciente.

* **Finalidade:** O objetivo do alerta é sinalizar, no momento da prescrição ou validação, quando um medicamento se enquadra nos critérios de alto custo, conforme as regras definidas para o convênio do paciente.
* **Condição para o Alerta:** Para que o sistema possa realizar a validação e acionar o alerta de alto custo, é fundamental que a Condição Contratual correspondente ao convênio do paciente (por exemplo, "convênio da parcial") esteja corretamente configurada.
* **Sem Condição Contratual:** Na ausência de uma Condição Contratual configurada para um convênio específico, o sistema não identifica regras de alto custo aplicáveis, e o alerta para o medicamento não é emitido.

Para configurar a condição contratual abra o RM menu Cadastros > Faturamento > Condições contratuais

Após definição da condição contratual de alto custo para medicamentos com o PEP-RM aberto navegue até o menu **prescrição médica** ao selecionar o medicamento com os parâmetros configurados o alerta e exibido.

Prescrição de antibióticos e prorrogação do tratamento

## **09.** **Prescrição de Antibióticos e prorrogação do tratamento**

Ao prescrever um medicamento antibiótico será sinalizado do lado direito no accordion as iniciais “ATB”.

As informações de “tempo de uso em dias/duração total do tratamento em dias” serão exibidas antes do nome do antibiótico, permitindo uma visualização rápida.

**A prorrogação do ATB** poderá ser realizada quando o paciente chegar ao fim do tratamento proposto e a equipe médica decidir manter a utilização do antibiótico, aumentando a duração do tratamento.

O antibiótico será considerado como prorrogado sempre que a duração de tratamento for maior do que a prescrição anterior, independente de ser cópia ou prescrição nova.

A prorrogação é sinalizada para o usuário com a data de término do antibiótico e a duração do tratamento. A sinalização ocorre junto ao campo de alerta de uso:

Horário Padrão

## **10. HORÁRIO PADRÃO**

Parametrização da prescrição médica com frequência x horário padrão no RM:

Utilizaremos como exemplo uma frequência padronizada de 8h/8h:

Parametrização do **Horário Padrão**: RM > Unidade de Atendimento > Aba "PEP RM" >  Aba "Prescrição Médica" > Campo "Utiliza Horário Padrão":

* Quando o usuário marcar a opção **"Sim e obriga selecionar um dos horários padrão"**, o PEP exibirá apenas os horários obrigatórios para utilização, com o preenchimento de acordo com a ordem parametrizada:

* Quando o usuário marcar a opção **"Sim, como sugestão, o usuário pode selecionar qualquer horário"**, o PEP exibirá os horários parametrizados como sugestão, com a possibilidade de alteração pelo médico:

* Quando o usuário marcar a opção **"Não utiliza horário padrão"**, o PEP exibirá a hora de início com base no próximo horário da lista:
