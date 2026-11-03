---
content_hash: 857d810a017b29d8a345cbd24ef0ae0f28ee731e04f8c5015875b85b46f888b6
fetched_at: '2026-06-29T00:10:32.070423+00:00'
page_id: '525032518'
product: rm
source: tdn-rm
title: FISCAL01-11264 DT Layout TAF - Registro T154 - Contribuições Sociais Pessoa
  Jurídica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525032518
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | TAF |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11264 |

## **02. SITUAÇÃO/REQUISITO**

1. Buscar dados

Devem ser selecionados os lançamentos que atendam aos seguintes requisitos:

* Cliente/Fornecedor seja Pessoa Jurídica
* Status "Normal"
* Data esteja dentro do período selecionado para integração \*
* Possuam um tributo do tipo **CSRF** "E/OU" **PIS-RF** "E/OU" **COFINS-RF** "E/OU" **CSLL-RF** associado

2. Ligar os campos no layout do Registro T154

## **03. SOLUÇÃO**

Foi implementado a Geração do Registro T154 para Lançamento Fiscal com os Tributos

* **CSRF**
* **PIS-RF**
* **COFINS-RF**
* **CSLL-RF**
