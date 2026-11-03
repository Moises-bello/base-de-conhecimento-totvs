---
content_hash: 314a2da1c20276b03a197b8a0359717b245760e354fdbd9d417647ce8d2ccf46
fetched_at: '2026-06-29T00:10:36.989443+00:00'
page_id: '533735670'
product: rm
source: tdn-rm
title: FISCAL01-11330 DT indSitPJ - Geração da TAG no evento R-1000
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=533735670
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Transmissão de Eventos Cadastrais |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11330 |

## **02. SITUAÇÃO/REQUISITO**

Tratar geração da tag indSitPJ - R-1000

## **03. SOLUÇÃO**

Funcionalidade: Transmissão de Evento Cadastral  
Cenário I: Situação da Pessoa Jurídica Diferente de Normal  
  
Dado que um evento R-1000 não foi transmitido  
E o parâmetro do processo é selecionado uma situação de pessoa jurídica diferente de normal,  
Ao executar a transmissão de Evento Cadastral   
Então, o xml de Envio deve preencher a tag <indSitPJ> com o código correspondente da Situação da PJ.
