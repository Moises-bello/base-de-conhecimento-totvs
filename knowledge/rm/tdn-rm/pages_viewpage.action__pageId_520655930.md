---
content_hash: 10ebf5214661c0dfdc6f47b340296bc8c1aa2d8a00da7855371cfbde967c0b8f
fetched_at: '2026-06-29T00:10:30.945447+00:00'
page_id: '520655930'
product: rm
source: tdn-rm
title: FISCAL01-11262 DT Registro T154 - IRRF Pessoa Jurídica (Origem do Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520655930
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | TAF |
| Ticket: | FISCAL01-11262 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11262 |

## **02. SITUAÇÃO/REQUISITO**

1. Buscar dados

Devem ser selecionados os lançamentos que atendam aos seguintes requisitos:

* Cliente/Fornecedor seja Pessoa Jurídica
* Status "Normal"
* Data esteja dentro do período selecionado para integração \*
* Possuam um tributo do tipo **IRRF** "E/OU" **IRRFPJ** associado

Verificar se a apuração do IRRF/IRRFPJ está "olhando" para o parâmetro de data base do Financeiro. Se estiver, fazer a seleção das datas de acordo com este parâmetro. Ou seja, a seleção dos dados deve ser coerente com a apuração do tributo.

2. Ligar os campos no layout do Registro T154

## **03. SOLUÇÃO**

Foi implementado na solução uma validação para o requisito solicitado na issue. Todo o Lançamento Fiscal no sistema em que o Cliente/Fornecedor for pessoa jurídica, em que um dos itens tenha tributo IRRF-PJ e que esteja parametrizado no Financeiro como Data Emissão, rotina no TAF irá gerar o registro T154.
