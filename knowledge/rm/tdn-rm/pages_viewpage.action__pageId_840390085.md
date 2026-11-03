---
content_hash: b746738561071b00626f918b96446ea0c6ff7b8536d47e626a6ed71ca5fa6443
fetched_at: '2026-06-29T00:11:50.364851+00:00'
page_id: '840390085'
product: rm
source: tdn-rm
title: DT - Visualização dos Relatórios Smart View no Portal e App Meu RH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=840390085
version: 22
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Visualização dos Relatórios Smart View no Portal RH e Meu RH |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-8760](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8760) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.151
* 12.1.2406 e superiores

## **03. SITUAÇÃO/REQUISITO**

Possibilitar em visualizar os relatórios Aviso de Férias, Recibo de Pagamento e Recibo de Férias desenvolvidos no Smart View, acessíveis através do Portal e App Meu RH.

## **04. SOLUÇÃO**

Estes relatórios foram criados na plataforma Smart View com o objetivo de proporcionar uma experiência mais aprimorada ao usuário final durante a conferência das informações apresentadas.

**Relatório Aviso de Férias**

**Relatório Recibo de Pagamento**

**Relatório Recibo de Férias**

falseATENÇÃO!

Esses relatórios possuem parâmetros específicos para funcionarem corretamente quando chamados pelo Portal RM e Meu RH. Isso significa que é realizado o mapeamento adequado dos argumentos recebidos pelo servidor para esses parâmetros. Abaixo estão descrito os parâmetros específicos de cada relatório:

**Aviso de férias:** CODCOLIGADA (Cód. Coligada), CHAPA (Chapa do Funcionário), 1DTAVDE e 2DTAVATE

**Recibo Pagamento parâmetros:** CODCOLIGADA (Cód. Coligada), CHAPA (Chapa do Funcionário), ANOINICIO (Ano Inicial), ANOFIM (Ano Final),  MESINICIO (Mês Inicial), MESFIM (Mês Final) e PERIODO (Período)

**Recibo de férias parâmetros:** CODCOLIGADA (Cód. Coligada), CHAPA (Chapa do Funcionário), SITUACAO (Situação das Férias), DATAPAGTO (Data de Pagamento das Férias >=) e VacationPaymentDate (Data de Pagamento das Férias <=)

## **05. DEMAIS INFORMAÇÕES**
