---
content_hash: 9dc577f528f4a74ab568380d800e0ec01165cebabb892459812fcfc9b2ed1e29
fetched_at: '2026-06-29T00:11:16.333913+00:00'
page_id: '666454107'
product: rm
source: tdn-rm
title: FISCAL01-17441 - DT - Apuração Tributo CIDE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=666454107
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Apuração de Tributos |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17441 |

## **02. SITUAÇÃO/REQUISITO**

Implementação do Tributo CIDE

## **03. SOLUÇÃO**

Foi Implementada a Apuração do Tributo CIDE.

Regras para Apuração:

Serão considerados os Lançamentos Fiscais de Entrada com incidência do Tributo onde os campos Base, Valor, e Alíquota sejam maiores que 0 e que o campo Código da Receita esteja preenchido.

A Soma destes valores serão atribuídos ao Campo Saldo Credor Devedor do Período de Apuração de forma Negativa e este valor será utilizado para gerar a Guia DARF e consequentemente o lançamento Financeiro.
