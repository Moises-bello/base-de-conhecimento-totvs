---
content_hash: 83b7101a009ebf9d25022f62ed97eee3ba6c1b57cdfb31fab8e36c4bc185558c
fetched_at: '2026-06-29T00:11:50.647926+00:00'
page_id: '844260511'
product: rm
source: tdn-rm
title: Hemocomponentes
type: documentation
url: https://tdn.totvs.com/display/LRM/Hemocomponentes
version: 10
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Cadastro RM**

HemocomponentesVisão Geral

## **01. VISÃO GERAL**

A nova funcionalidade de prescrição de hemocomponentes será integrada na aba de prescrição médica do prontuário eletrônico, permitindo aos médicos prescreverem os hemocomponentes necessários diretamente no sistema. Isso garantirá uma comunicação eficiente e precisa com a equipe de enfermagem, a segurança do paciente e a eficiência operacional do hospital.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

No menu de prescrição médica, submenu de Hemocomponentes, ao clicar em adicionar, uma modal será habilitada para preenchimento. A tela de preenchimento é composta por: 

**Dados Clínicos:**

1. Diagnóstico do paciente - Campo de busca pelo CID e indicação clínica para a transfusão de hemocomponentes.
2. Data do diagnóstico - Campo para preenchimento da data do diagnóstico do paciente.
3. Classificação do atendimento - O usuário poderá selecionar se a infusão será "Urgente", "Não urgente", "Programada" ou "Reserva". Caso o usuário selecione "Programado" ou "Reserva", os campos "Data" e "Hora" serão habilitados para preenchimento. Se o usuário selecionar "Urgente" ou "Não urgente", os campos "Data" e "Hora"  permanecerão bloqueados para preenchimento.
4. Transfusões anteriores - O usuário poderá preencher os campos "Sim" ou "Não" para informar se o paciente já realizou ou não transfusões anteriormente.
5. Houve reação? - Caso o paciente tenha realizado transfusões anteriormente e o usuário marcou a opção "Sim", o campo "Houve reação?" será habilitado para preenchimento com as opções "Sim" e "Não".
6. Descreva o tipo de reação, gravidade e conduta anterior - Caso o paciente tenha apresentado alguma reação na transfusão anterior e o usuário marcou a opção "Sim", um campo de texto livre será habilitado para que o usuário possa descrever o tipo de reação, gravidade e conduta anterior.
7. Prescrito profilaxia? - O usuário poderá sinalizar se será ou não prescrito algum medicamento profilático  para o paciente marcando as opções "Sim" ou "Não".

**Exames Clínicos:**

1. O usuário poderá preencher os resultados de exames anteriores:  Hemoglobina, Hematócrito, Plaqueta, TPA, TTPA e Fibrinogênio.

**Hemocomponente:**

1. Selecione o hemocomponente - O usuário poderá selecionar o tipo de hemocomponente necessário para o paciente (o cadastro da lista de hemocomponentes será realizado pelo RM).
2. Via de aplicação - O usuário poderá selecionar a opção de via de administração indicada (o cadastro da lista de Vias de administração será realizado pelo RM).
3. Procedimento - O usuário poderá selecionar o procedimento indicado (Filtrado, Irradiado, Lavado, Aférese e Pool), podendo selecionar mais de uma opção.
4. Quantidade - O usuário poderá especificar a quantidade necessária de cada tipo de hemocomponente.
5. Volume - O usuário poderá especificar o volume necessário para cada tipo de hemocomponente.
6. Tempo de Infusão - O usuário poderá especificar o tempo de infusão indicado para o hemocomponente.
7. Campos S/N e ACM - O usuário poderá sinalizar se a administração do hemocomponente será a critério médico ou se necessário.
8. Observações e outros - Campo de texto livre para observações.

* Para finalizar o preenchimento, clique no botão "Incluir". As solicitações de hemocomponentes serão encaminhadas para as telas de  e
* Caso o usuário realize duas solicitações de hemocomponentes na mesma prescrição médica, os campos de "Dados Clínicos" e "Resultados de Exames" serão exibidos pré-preenchidos com os dados da prescrição anterior e com possibilidade de edição.

Cadastro RM

## **03. CADASTRO RM**

* **Cadastro da lista de hemocomponentes:** Ao realizar o preenchimento da solicitação de hemocomponentes, o usuário conseguirá realizar a busca pelos produtos cadastrados e classificados como hemocomponentes.

Sinalização do produto cadastrado como Hemocomponente: RM> Cadastro > Estoque > Produtos > Anexo: Informações - Totvs Saúde > Identificação I > Tipo Item: Medicamento > Identificação II > Hemocomponentes.

* **Cadastro das vias de administração:** RM > Cadastro > Prescrição médica > Vias de Administração de Medicamentos.
