---
content_hash: 83666f960ffa3e7303fd8b0af2dd77db22f71e6f35f0e948477e548df92dc0c3
fetched_at: '2026-06-29T00:11:04.497436+00:00'
page_id: '627734910'
product: rm
source: tdn-rm
title: FISCAL01-15552 DT Cadastro de Regra de ICMS
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-15552+DT+Cadastro+de+Regra+de+ICMS
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro de Regra de ICMS |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15552 |

## **02. SITUAÇÃO/REQUISITO**

Os Fornecedores Optante de Simples, destaca a Alíquota e o Valor do ICMS nos Dados adicionais da NFe, para que os clientes possam utilizar o Credito do Imposto.

O cliente fez a compra para utilizar no Ativo Imobilizado, nesta situação deve ser utilizada o valor do Imposto como credito e calcular o Diferencial de Alíquota.

O Cálculo do Diferencial de Alíquota deve ser feito entre a "Alíquota Interestadual e a Alíquota Interna".

Nesta situação temos 3 Alíquotas para cálculo.

Alíquota do Simples: 2,04% (não existe campo especifico)

Alíquota Interestadual: 12%

Alíquota Interna: 18%

Para atender esta situação é necessário cria na Regra do ICMS - Sub Pasta Dados ICMS ST, um novo campo **"Utilizar Alíquota Interestadual Calculo DIFAL"** ,

## **03. SOLUÇÃO**

Foi criado no cadastro de Regra de ICMS o campo "DIFAL utiliza alíquota Interestadual para Natureza de entrada", que está disponível através da aba "Dados ICMS S.T."

Este campo deverá ser utilizado apenas para Naturezas do tipo entrada.
