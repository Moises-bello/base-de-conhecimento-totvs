---
content_hash: e69240f07a952b0d58179d82f6028a4ad62f724a67b7adc8fad6c4ae3f466f48
fetched_at: '2026-06-29T00:11:12.388188+00:00'
page_id: '652574837'
product: rm
source: tdn-rm
title: FISCAL01-16799 DT - Data de vencimento na Geração de Guias ISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=652574837
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração de Guias ISS |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16799 |

## **02. SITUAÇÃO/REQUISITO**

Implementar conforme Solicitado

## **03. SOLUÇÃO**

Durante a geração das guias de ISS o sistema deverá considerar o Dia informado no "Cadastro Fiscal de Município" e o Mês/Ano do mês seguinte  
ao do Período de Apuração, Caso não seja uma Data Valida, que seja preenchido com a Data de Vencimento do Período de Apuração.

Caso não seja encontrada uma data de vencimento no cadastro então deve ser mantido o comportamento atual, ou seja,   
considerar a data de vencimento do período de apuração

obs.:   
Continua sendo mantida a Obrigatoriedade de informar uma Data de Vencimento no Período de Apuração  
mesmo que ela não seja usada quando estiver preenchida a data default nos Dados Fiscais, isto para manter   
o comportamento anterior.
