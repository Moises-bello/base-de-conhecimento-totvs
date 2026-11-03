---
content_hash: ceb319997812186c7f084f12207c05311c4129d860c52ab1e7eb70b4bb570a86
fetched_at: '2026-06-29T00:11:06.245656+00:00'
page_id: '633054392'
product: rm
source: tdn-rm
title: Processo de Faturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+de+Faturamento
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Existem três formas de Elaboração de contas para o faturamento do convênio SUS, são elas:

* AIH (Autorização de Internação Hospitalar) – Paciente interno.
* BPA (Boletim de Procedimento Ambulatorial) – Paciente externo.
* APAC (Autorização de Procedimentos de Alta Complexidade) – Paciente interno/externo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Na TOTVS Gestão Hospitalar acesse Faturamento/Faturamento SUS/Processos/Faturamento AIH, BPA e APAC.

Na tela do processo, devem ser preenchidas as seguintes informações:

- Unidade de Faturamento: campo somente leitura, já vem preenchido de acordo com a remessa selecionada.- Opções de faturamento: faturamento, refaturamento, reprocessamento.

- Tipo de faturamento: BPA, AIH, AIH Rejeitada, APAC.

- Filtro por data: campo opcional, caso queira filtrar a seleção de contas as opções são período por data de saída, data final da parcial ou data de liberação.   
Quando utilizar um filtro por data, é obrigatório preencher a data inicial e final. A data inicial não pode ser maior que a final.

- Unidade de Atendimento (opcional).

- Responsável pela Liberação (opcional).

- Informe o Tipo de Faturamento: BPA, AIH, AIH Rejeitada, APAC

- Mês / Ano da apresentação: competência para apresentação do faturamento SUS (obrigatório)

### **Incluir novas Contas**

No segundo passo de refaturamento é possível incluir novas contas como é mostrado abaixo:

Ao clica em incluir novas contas uma tela de pesquisa é aberta:

Dessa forma, o usuário pode incluir contas que foram excluídas de uma outra remessa, por exemplo.

## **03. TABELAS UTILIZADAS**

* SZFATURACONVENIO
* SZATENDIMENTO
* SZPARCIALATEND
