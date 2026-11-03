---
content_hash: 077faccc6dc9ef77e72c67dfa8963071f2b475c837453dcf91c26daf44cea7ab
fetched_at: '2026-06-29T00:11:26.403497+00:00'
page_id: '716359351'
product: rm
source: tdn-rm
title: infoProc-recursosRec
type: documentation
url: https://tdn.totvs.com/display/LRM/infoProc-recursosRec
version: 2
---

## Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte.

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| infoProc | recursosRec recursosRep | 0-3 | - | Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte |  |
| tpProc | infoProc | 1-1 | 1 | Preencher com o código correspondente ao tipo de processo:  Valores Válidos: 1 - Administrativo; 2 - Judicial. | DPROCESSOJUDICIAL.TIPOPROCESSO |
| nrProc | infoProc | 1-1 | 21 | Informar o número do processo administrativo/judicial.  Validação: Deve ser um número de processo administrativo ou judicial válido e existente na Tabela de Processos | DPROCESSOJUDICIAL.NUMERO |
| codSusp | infoProcRetAd | 0-1 | 14 | Código do Indicativo da Suspensão, atribuído pelo contribuinte.    Não preencher se {tpProcRetPrinc} = [3]. | DTRIBDISCUTIDOSPROCJUDICIAL.CODINDICSUSPEXIG |
| vlrNRet | infoProc | 0-1 | 14 | Valor da Contribuição Previdenciária com exigibilidade suspensa  Validação: Preenchimento obrigatório se {vrRatSusp} e {vrSenarSusp} não tiverem sido preenchidos. Deve ser um valor maior que zero. | Somatório do campo  DTRBITEMCALCCONTRPREV.VLRRETADICSUSPDEPJUIZO de todos os lançamentos fiscais que possuem o processo associado. |
