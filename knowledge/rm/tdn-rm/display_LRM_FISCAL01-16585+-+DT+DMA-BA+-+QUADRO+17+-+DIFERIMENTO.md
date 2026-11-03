---
content_hash: 446a9eb39f39e5326a2b24af6299f4d81a98dc64a9d4d4b35d954e96eab82e2d
fetched_at: '2026-06-29T00:11:10.437527+00:00'
page_id: '643759780'
product: rm
source: tdn-rm
title: FISCAL01-16585 - DT DMA-BA - QUADRO 17 - DIFERIMENTO
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-16585+-+DT+DMA-BA+-+QUADRO+17+-+DIFERIMENTO
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DMA-BA |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16585 |

## **02. SITUAÇÃO/REQUISITO**

Implementar o QUADRO 17 - DIFERIMENTO

## **03. SOLUÇÃO**

Origem dos Dados:  
Lançamentos de Entrada/Saída

|  |  |  |
| --- | --- | --- |
| Quadro 17 | | |
| CAMPOS | DESCRIÇÃO | ORIGEM |
| TipoRegistro | Indica qual o registro do quadro | Valor Fixo = 17 |
| AnoReferencia | Ano Base | Data Inicial da Geração |
| MesReferencia | Mês Base | Data Inicial da Geração |
| InscricaoEstadual | Inscrição Estadual | Inscrição Estadual da Filial |
| QtdeEmpregados | Quantidade de Empregados | Tela de Geração |
| QtdeEnergiaConsumida | Quantidade de Energia Consumida | Tela de Geração |
| VlrCofinsRecolhido | Valor Cofins Recolhido - Bloqueado versão 2002 | Valor 0 |
| VlrCompraAtivo\_7 | Valor Compra Ativo - 7% | DLAF.VALORICMS |
| VlrCompraAtivo\_12 | Valor Compra Ativo - 12% | DLAF.VALORICMS |
| VlrCompraAtivo\_17 | Valor Compra Ativo - 17% | DLAF.VALORICMS |
| VlrCompraUso\_7 | Valor Compra Uso - 7% - Bloqueado versão 2002 | Valor 0 |
| VlrCompraUso\_12 | Valor Compra Uso - 12% - Bloqueado versão 2002 | Valor 0 |
