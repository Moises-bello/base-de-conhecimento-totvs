---
content_hash: e518bec1ab8bdae21bd3455079ba7d4e1ae901499c05d603f37910b663c1f4a8
fetched_at: '2026-06-29T00:11:10.402813+00:00'
page_id: '643560159'
product: rm
source: tdn-rm
title: FISCAL01-16661 - DT DMA-BA - QUADRO 15 - ICMS SUBSTITUIÇÃO TRIBUTÁRIA POR ANTECIPAÇÃO
  PROPRIAMENTE DITA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=643560159
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16661 |

## **02. SITUAÇÃO/REQUISITO**

Implementar o QUADRO 15 - ICMS SUBSTITUIÇÃO TRIBUTÁRIA POR ANTECIPAÇÃO PROPRIAMENTE DITA

## **03. SOLUÇÃO**

Origem dos Dados:  
Tela de Geração, Lançamentos de Outros/Débitos/Créditos e valores do Quadro 15

|  |  |  |
| --- | --- | --- |
| Quadro 15 | | |
| CAMPOS | DESCRIÇÃO | ORIGEM |
| TipoRegistro | Indica qual o registro do quadro | Valor Fixo = 15 |
| AnoReferencia | Ano Base | Data Inicial da Geração |
| MesReferencia | Mês Base | Data Inicial da Geração |
| InscricaoEstadual | Inscrição Estadual | Inscrição Estadual da Filial |
| VlrDeducoes | Valor Deduções | DLDC.VALORLDC |
| VlrImpostoRecolher | Valor Imposto Recolher | VlrSaldoDevedor - VlrDeducoes |
| VlrTotalDebito | Valor Total Debito | VlrSaidaTributada (Quadro\_14) + VlrOutrosDebitos (Quadro\_14) + VlrEstornoCredito (Quadro\_14) + VlrDifAliquota (Quadro\_15) |
| VlrTotalCredito | Valor Total Credito | VlrEntradaTributada (Quadro\_14) + VlrEstornoDebitos (Quadro\_14) + VlrOutrosCreditos (Quadro\_14) + VlrSaldoCredAnterior (Quadro\_14) |
| VlrSaldoDevedor | Valor Saldo Devedor | VlrTotalDebito - VlrTotalCredito |
| VlrSaldoCredor | Valor Saldo Credor Devedor | VlrTotalCredito - VlrTotalDebito |
| VlrDifAliquota | Valor Diferencial de Alíquota | DLAF.VALORDIFALIQ |
