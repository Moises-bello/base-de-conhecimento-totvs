---
content_hash: 7ca6c096faecea208364cf357ff9c390f6d5f3dbe35b6e94c90fdca76e9be3dc
fetched_at: '2026-06-29T00:11:25.499032+00:00'
page_id: '710546502'
product: rm
source: tdn-rm
title: FISCAL01-18377 - DT Registro C170
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18377+-+DT+Registro+C170
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18377 |

## **02. SITUAÇÃO/REQUISITO**

Registro C170, campo 06 (UNID)  
Caso a unidade de medida do documento fiscal seja diferente da unidade de medida de controle de estoque informada no  
Registro 0200, o valor informado deve existir no registro 0220 para o código do item (Campo 03 - COD\_ITEM desse registro)  
com a correspondente conversão, exceto se o campo 07 - TIPO\_ITEM do registro 0200 for igual a 07 (Material de Uso e  
Consumo).

## **03. SOLUÇÃO**

A partir de janeiro de 2023, para produtos onde o campo 07 - TIPO\_ITEM do registro 0200 for igual a 07 (Material de Uso e  
Consumo) e a unidade de medida do documento fiscal seja diferente da unidade de medida de controle de estoque informada no  
Registro 0200, o registro 0220 não será gerado.

Disponível a partir da biblioteca 12.1.34
