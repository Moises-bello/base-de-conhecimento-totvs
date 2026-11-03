---
content_hash: 8826b4bd6b3cff2e8c5edcd2d1dfd8579319e3b4a0ffe5bd735cd45d4e5ee128
fetched_at: '2026-06-29T00:11:09.587135+00:00'
page_id: '640535509'
product: rm
source: tdn-rm
title: FISCAL01-16592 - DT DMA-BA - QUADRO 13 - VALORES FISCAIS DEDUTÍVEIS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=640535509
version: 7
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DMA-BA |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16592 |

## **02. SITUAÇÃO/REQUISITO**

Implementar o QUADRO 13 - VALORES FISCAIS DEDUTÍVEIS

## **03. SOLUÇÃO**

Origem dos Dados:  
Tela de Geração e Lançamentos Entrada/Saída

|  |  |  |
| --- | --- | --- |
| Quadro 13 | | |
| CAMPOS | DESCRIÇÃO | ORIGEM |
| TipoRegistro | Indica qual o registro do quadro | Valor Fixo = 13 |
| AnoReferencia | Ano Base | Data Inicial da Geração |
| MesReferencia | Mês Base | Data Inicial da Geração |
| InscricaoEstadual | Inscrição Estadual | Inscrição Estadual da Filial |
| StatusES | Indica se o Lançamento Fiscal é igual a 'Entrada' ou 'Saída' | Tipo do Lançamento Fiscal |
| VlrCompraAtivo | BaseRedICMS (DLAF.BASEREDICMS) + OutrosICMS (DLAF.OUTROSICMS) + IsentoICMS (DLAF.ISENTOICMS) | Lançamentos Fiscais Entrada |
| VlrAquisicaoMat | BaseRedICMS (DLAF.BASEREDICMS) + OutrosICMS (DLAF.OUTROSICMS) + IsentoICMS (DLAF.ISENTOICMS) | Lançamentos Fiscais Entrada |
| VlrTransfAtivo | BaseRedICMS (DLAF.BASEREDICMS) + OutrosICMS (DLAF.OUTROSICMS) + IsentoICMS (DLAF.ISENTOICMS) | Lançamentos Fiscais Entrada |
| VlrTransfMat | BaseRedICMS (DLAF.BASEREDICMS) + OutrosICMS (DLAF.OUTROSICMS) + IsentoICMS (DLAF.ISENTOICMS) | Lançamentos Fiscais Entrada |
| VlrRemessaSimb | **Entradas**: BaseRedICMS (DLAF.BASEREDICMS) + OutrosICMS (DLAF.OUTROSICMS) + IsentoICMS (DLAF.ISENTOICMS)  **Saídas**: OutrosICMS (DLAF.OUTROSICMS) + IsentoICMS (DLAF.ISENTOICMS) | Lançamentos Fiscais Entrada/Saída |
| VlrOutrasOperacoes | BaseRedICMS (DLAF.BASEREDICMS) + OutrosICMS (DLAF.OUTROSICMS) + IsentoICMS (DLAF.ISENTOICMS) | Lançamentos Fiscais Entrada/Saída |
| VlrTotal | Soma dos valores de todos os Lançamentos de Entrada/Saída:  VlrCompraAtivo + VlrAquisicaoMat + VlrTransfAtivo + VlrTransfMat + VlrRemessaSimb + VlrOutrasOperacoes | Lançamentos Fiscais Entrada/Saída |
