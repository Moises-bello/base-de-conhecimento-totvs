---
content_hash: 0059c47c347bcf87b155eba4b02f1a4a146266fab657ec6cf153140917c56611
fetched_at: '2026-06-29T00:11:10.219410+00:00'
page_id: '642638456'
product: rm
source: tdn-rm
title: FISCAL01-16661 - DT DMA-BA - QUADRO 14 - APURAÇÃO DO ICMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642638456
version: 6
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16661 |

## **02. SITUAÇÃO/REQUISITO**

Implementar o QUADRO 14 - APURAÇÃO DO ICMS

## **03. SOLUÇÃO**

Origem dos Dados:  
Tela de Geração e Lançamentos Entrada/Saída e Lançamentos de Outros/Débitos/Créditos

|  |  |  |
| --- | --- | --- |
| Quadro 14 | | |
| CAMPOS | DESCRIÇÃO | ORIGEM |
| TipoRegistro | Indica qual o registro do quadro | Valor Fixo = 14 |
| AnoReferencia | Ano Base | Data Inicial da Geração |
| MesReferencia | Mês Base | Data Inicial da Geração |
| InscricaoEstadual | Inscrição Estadual | Inscrição Estadual da Filial |
| VlrSaidaTributada | Valor Saida Tributada | Total DLAF.VALORICMS lanc Entrada |
| VlrOutrosDebitos | Valor Outros Debitos | DLDC.VALORLDC |
| VlrEstornoCredito | Valor Estorno Credito | DLDC.VALORLDC |
| VlrEntradaTributada | Valor Entrada Tributada | Total DLAF.VALORICMS lanc Saída |
| VlrOutrosCreditos | Valor Outros Creditos | DLDC.VALORLDC |
| VlrEstornoDebitos | Valor Estorno Debitos | DLDC.VALORLDC |
| VlrSaldoCredAnterior | Valor Saldo Cred Anterior | Total DPERIODO.SALDOTRBANT |
