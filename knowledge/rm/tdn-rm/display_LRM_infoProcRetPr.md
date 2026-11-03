---
content_hash: 02788feffd7ef04120fa8df81e6839f3273cfec2bf9c30cb28f6860558c2092a
fetched_at: '2026-06-29T00:11:26.375686+00:00'
page_id: '716356631'
product: rm
source: tdn-rm
title: infoProcRetPr
type: documentation
url: https://tdn.totvs.com/display/LRM/infoProcRetPr
version: 3
---

## Informações de processos relacionados a não retenção de contribuição previdenciária.

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| tpProcRetPrinc | infoProcRetPr | 0-1 | 1 | Preencher com o código correspondente ao tipo de processo: 1 - Administrativo; 2 - Judicial.  Validação: Preenchimento obrigatório se {vlrTotalNRetPrinc}>0 | DPROCESSOJUDICIAL.TIPOPROCESSO |
| nrProcRetPrinc | infoProcRetPr | 0-1 | 21 | Informar o número do processo administrativo/judicial.  Validação: O processo deve existir na tabela de PROCESSOS. Preenchimento obrigatório se {vlrTotalNRetPrinc}>0 | DPROCESSOJUDICIAL.NUMERO |
| codSuspPrinc | infoProcRetPr | 0-1 | 14 | Código do Indicativo da Suspensão, atribuído pelo contribuinte.    Não preencher se {tpProcRetPrinc} = [3]. | DTRIBDISCUTIDOSPROCJUDICIAL.CODINDICSUSPEXIG |
| valorPrinc | infoProcRetPr | 1-1 | 14 | Valor da retenção de contribuição previdenciária principal que deixou de ser efetuada em função de processo administrativo ou judicial. | Somatório do campo  DTRBITEMCALCCONTRPREV.VLRRETSUSPDEPJUIZO de todos os lançamentos fiscais que possuem o processo associado. |
