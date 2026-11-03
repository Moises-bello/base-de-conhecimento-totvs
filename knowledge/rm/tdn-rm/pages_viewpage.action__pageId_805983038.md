---
content_hash: 3f673d0a267a08ea69e21cf67dfed2752feea2fb9d05f93156a87c5cd02d7a23
fetched_at: '2026-06-29T00:11:43.398079+00:00'
page_id: '805983038'
product: rm
source: tdn-rm
title: DT - Retenção Lei 9711/98 do EFD-Reinf
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=805983038
version: 6
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Lançamento Financeiro //Relatório de Conferência INSS Patronal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-6098](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6098) |

## **01. VERSÕES**

**A partir das Versões:**

* 12.1.2302.238
* 12.1.2306.185
* 12.1.2310.119

## **02. SITUAÇÃO/REQUISITO**

Na geração do lançamento financeiro para os tipos "**25-DCTFWeb Folha**" e "**26-Total Guia INSS DCTFWeb 13º Salário**", assim como no processo de geração do **Relatório de Conferência INSS Patronal,** detectamos que o sistema está sempre considerando os valores de Retenção Lei 9711/98 do EFD-Reinf do TOTVS Gestão Financeira. E não identificamos a existência de uma opção para excluir ou desconsiderar esses valores durante o processo. 

## **03. SOLUÇÃO**

Conduzimos uma análise detalhada sobre a Retenção Lei 9.711/68 e identificamos a necessidade de ajustar o comportamento do produto TOTVS Folha de Pagamento.

Esta adaptação é essencial devido a importância das informações para a geração da DCTFWeb, que são transmitidas não apenas via eSocial, mas também através da EFD-Reinf, conforme detalhado no fluxo de informações na página 10 do [Manual de Orientação da DCTFWeb](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/DCTFWeb/arquivos/manual-dctfweb-fevereiro-2023.pdf). Onde demonstra que o valor da Retenção Lei 9711/98 deve ser enviado pelo EFD-Reinf e não pelo eSocial.

Vale ressaltar que, com a unificação, a DARF no setor financeiro passa a incorporar não apenas os dados do eSocial, mas também os da REINF. Cada produto deve encaminhar essas informações ao setor financeiro para o cálculo do valor da DARF.

Diante desse contexto e com o objetivo de evitar duplicidade de informações, implementamos as seguintes tratativas no produto TOTVS Folha de Pagamento:

**1)** Remoção do parâmetro **"Buscar Retenção Lei 9711/98 do EFD-Reinf"**, anteriormente presente nos parâmetros do eSocial, como demonstrado abaixo:

**2)** Remoção do parâmetro **"Valor Retenção Lei 9711/98"**, anteriormente existente no menu "Período de Apuração", como demonstrado abaixo:

**3)** Desconsiderada à **Retenção da Lei 9.711/88** no campo "Total Deduções" durante a geração do relatório de **Conferência INSS Patronal**.

**4)** Desconsiderada à **Retenção da Lei 9.711/88** no campo "Total Deduções" durante a geração do lançamento financeiro para os tipos: **25-DCTFWeb Folha" e "26-Total Guia INSS DCTFWeb 13º Salário".**
