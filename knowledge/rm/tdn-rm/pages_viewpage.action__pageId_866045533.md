---
content_hash: 4ddfb3863b880136bd53d4780544512b82e708de2164b3113c79450c0beb36b8
fetched_at: '2026-06-29T00:11:56.452522+00:00'
page_id: '866045533'
product: rm
source: tdn-rm
title: Alteração de status dos XMLs no monitor de arquivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866045533
version: 6
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão de Estoque, Compras e Faturamento |
| Processo | Monitor de Arquivos |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-23682 |

## **02. SITUAÇÃO/REQUISITO**

A alteração do status de um grande volume de arquivos XML no monitor de arquivos era limitada, pois exigia a seleção manual de cada registro na tela antes de executar o processo.

## **03. SOLUÇÃO**

Foi adicionado um formulário ao processo de alteração de status dos XMLs no monitor de arquivos, incluindo um botão que abre uma tela de filtro. Agora, o processo é aplicado com base no filtro configurado, eliminando a necessidade de selecionar cada registro individualmente.

Disponível à partir da biblioteca 12.1.2402
