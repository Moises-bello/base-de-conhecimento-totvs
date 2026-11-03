---
content_hash: dfa625811a4c00f74db69dbaa1f8e499e76e13bee854d476947e4b7394644c8c
fetched_at: '2026-06-29T00:11:26.379292+00:00'
page_id: '716356698'
product: rm
source: tdn-rm
title: infoProcRetAd
type: documentation
url: https://tdn.totvs.com/display/LRM/infoProcRetAd
version: 1
---

## Identificação do prestador de serviços mediante cessão de mão de obra ou empreitada.

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| tpProcRetAdic | infoProcRetAd | 0-1 | 1 | Preencher com o código correspondente ao tipo de processo: 1 - Administrativo; 2 - Judicial.  Validação: Preenchimento obrigatório se {vlrTotalNRetPrinc}>0 | DPROCESSOJUDICIAL.TIPOPROCESSO |
| nrProcRetAdic | infoProcRetAd | 0-1 | 21 | Informar o número do processo administrativo/judicial.  Validação: O processo deve existir na tabela de PROCESSOS. Preenchimento obrigatório se {vlrTotalNRetAdic}>0 | DPROCESSOJUDICIAL.NUMERO |
| codSuspAdic | infoProcRetAd | 0-1 | 14 | Código do Indicativo da Suspensão, atribuído pelo contribuinte.    Não preencher se {tpProcRetPrinc} = [3]. | DTRIBDISCUTIDOSPROCJUDICIAL.CODINDICSUSPEXIG |
| valorAdic | infoProcRetAd | 1-1 | 14 | Valor da retenção de contribuição previdenciária adicional que deixou de ser efetuada em função de processo administrativo ou judicial. | Somatório do campo  DTRBITEMCALCCONTRPREV.VLRRETADICSUSPDEPJUIZO de todos os lançamentos fiscais que possuem o processo associado. |
