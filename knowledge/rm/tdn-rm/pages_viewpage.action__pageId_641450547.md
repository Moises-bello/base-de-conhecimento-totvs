---
content_hash: cfe649bf6bc7c4e797716742dd658838b80554790cd3e77a9e5ee96f7e211493
fetched_at: '2026-06-29T00:11:10.115106+00:00'
page_id: '641450547'
product: rm
source: tdn-rm
title: FISCAL01-16583 - DT DMA-BA - QUADRO 16 - ICMS IMPORTAÇÃO PARA INDUSTRIALIZAÇÃO/COMERCIALIZAÇÃO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641450547
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16583 |

## **02. SITUAÇÃO/REQUISITO**

Implementar o QUADRO 16 - ICMS IMPORTAÇÃO PARA INDUSTRIALIZAÇÃO/COMERCIALIZAÇÃO

## **03. SOLUÇÃO**

Origem dos Dados:  
Tela de Geração e Lançamentos Entrada/Saída

|  |  |  |
| --- | --- | --- |
| Quadro 16 | | |
| CAMPOS | DESCRIÇÃO | ORIGEM |
| TipoRegistro | Indica qual o registro do quadro | Valor Fixo = 16 |
| AnoReferencia | Ano Base | Data Inicial da Geração |
| MesReferencia | Mês Base | Data Inicial da Geração |
| InscricaoEstadual | Inscrição Estadual | Inscrição Estadual da Filial |
| VlrStAntecipado | Valor Subst Antecipado - DLAF.VALORSUBST | Lançamentos de Entrada |
| VlrStRetencao | Valor Subst Retencao - DLAF.VALORSUBST | Lançamentos de Entrada/Saída |
| VlrImportIndust | Valor Import Industrialização - DLAF.VALORICMS | Lançamentos de Entrada |
| VlrImportImobiliz | Valor Import Imobilizado - DLAF.VALORICMS | Lançamentos de Entrada |
| VlrDiferimento | Valor Diferimento - Não gerado | Gera valor zerado |
| VlrImpostoRecolhido | Imposto a Recolher - Não gerado | Gera valor zerado |
