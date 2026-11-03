---
content_hash: 69b5a0c3292d7e45d7fd37f9cd8c1d3b3e0ef10a40c93966c2a6918a4bc005c5
fetched_at: '2026-06-29T00:11:53.985032+00:00'
page_id: '852910227'
product: rm
source: tdn-rm
title: DT - S-1210 - Autônomo Residente no Exterior - TOTVS Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852910227
version: 16
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | S-1210 - Autônomo Residente no Exterior - TOTVS Gestão Financeira |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10284](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10284) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.229
* 12.1.2402.174
* 12.1.2406.105 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Possibilitar a geração das informações relativas aos dados dos autônomos residentes no exterior gerados através do produto TOTVS Gestão Financeira, de forma similar aos autônomos cadastrados na folha de pagamento.

## **04. SOLUÇÃO**

O sistema agora gera as informações do evento S-1210 para autônomos residentes no exterior que estão cadastrados como Clientes e Fornecedores no TOTVS Gestão Financeira.

**1)** Acesse o menu Administração de Pessoal | Cliente e Fornecedor | Aba Identificação e preencha as informações do endereço na aba **Principal**, conforme demonstrado.

**Atenção:** Essas informações serão levadas no campo <**paisResidExt**> e no grupo <**endExt**> do evento S-1210.

2) Acesse o menu Administração de Pessoal | Cliente e Fornecedor | Aba Tributos e preencha os campos: "Situação do NIF" e "Forma de Tributação", conforme demonstrado abaixo:

**Atenção:** Essas informações serão levadas no grupo <**infoPgtoExt**> do evento S-1210.

3) Geração do XML do evento S-1210:

## **05. DOCUMENTAÇÃO**
