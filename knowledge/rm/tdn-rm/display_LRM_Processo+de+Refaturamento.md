---
content_hash: fb67795c0d60839173ec71705c9b78734b9eb480ae58f9cec9bd5ffb8e3df50b
fetched_at: '2026-06-29T00:11:06.248488+00:00'
page_id: '633054451'
product: rm
source: tdn-rm
title: Processo de Refaturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+de+Refaturamento
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Existem três formas de Elaboração de contas para o refaturamento do convênio SUS, são elas:

* AIH (Autorização de Internação Hospitalar) – Paciente interno.
* BPA (Boletim de Procedimento Ambulatorial) – Paciente externo.
* APAC (Autorização de Procedimentos de Alta Complexidade) – Paciente interno/externo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Na TOTVS Gestão Hospitalar acesse Faturamento/Faturamento SUS/Processos/Faturamento AIH, BPA e APAC.

Na tela do processo, devem ser preenchidas as seguintes informações:

- Unidade de Faturamento: campo somente leitura, já vem preenchido de acordo com a remessa selecionada.

- Opções de faturamento: Selecionar a opção refaturamento.

- O Tipo de faturamento (BPA, AIH, AIH Rejeitada, APAC) já é preenchido conforme a fatura selecionada.

- Filtro por data: campo opcional, caso queira filtrar a seleção de contas as opções são período por data de saída, data final da parcial ou data de liberação.   
Quando utilizar um filtro por data, é obrigatório preencher a data inicial e final. A data inicial não pode ser maior que a final.

- Unidade de Atendimento (opcional).

- Responsável pela Liberação (opcional).

## **03. TABELAS UTILIZADAS**

* SZFATURACONVENIO
* SZATENDIMENTO
* SZPARCIALATEND
