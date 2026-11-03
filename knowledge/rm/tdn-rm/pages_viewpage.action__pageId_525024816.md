---
content_hash: 5e7015445807b470dfb3b371126c43e4ccc9d779c2d17cfa246f82cffe0aed2c
fetched_at: '2026-06-29T00:10:32.053771+00:00'
page_id: '525024816'
product: rm
source: tdn-rm
title: FISCAL01-11178 SPED Fiscal - Gerar Bloco B considerando as datas de apuração
  do ISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525024816
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11178 |

## **02. SITUAÇÃO/REQUISITO**

Geração do Bloco B do SPED Fiscal não está respeitando a parametrização de Datas do ISS.

## **03. SOLUÇÃO**

Foram realizadas evoluções na geração do SPED Fiscal para que o mesmo passe a utilizar a mesma lógica de geração do Ato Cotepe e das Rotinas Municipais via Gerador de Saídas. Os parâmetros de seleção de  
Datas do ISS serão utilizados para montar o SQL que servirá de insumo para a geração dos registros do Bloco B.
