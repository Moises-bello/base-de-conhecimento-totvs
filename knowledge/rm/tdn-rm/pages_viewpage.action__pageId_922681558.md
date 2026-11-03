---
content_hash: 32de3d2e4acc40808aa4bad9cb974a8158075200dd52f176983876178df75194
fetched_at: '2026-06-29T00:12:07.211609+00:00'
page_id: '922681558'
product: rm
source: tdn-rm
title: FISCAL01-24871 - CT-e XMLs não estão carregando o Histórico para o movimento.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=922681558
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão de Estoque |
| Função: | Importação de Movimento através de XML - CT-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-24871 |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a Importação do XML de CT-e o Sistema não está copiando o conteúdo da Tag **<xObs>** de um determinado XML para a Observação do Movimento.

## **03. SOLUÇÃO**

 Ajuste para sistema considerar os parâmetros do tipo de movimento: Histórico longo / Histórico curto para exibição do conteúdo da tag **<xObs>** dentro do campo Observações da aba Informações adicionais

Disponível a partir da biblioteca 12.1.2406
