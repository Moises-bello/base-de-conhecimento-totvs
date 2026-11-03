---
content_hash: 28d2af2de476ff02a7aff6a17524ec90b9eadf4198aa133901f029f6b6251a90
fetched_at: '2026-06-29T00:11:26.438234+00:00'
page_id: '716369883'
product: rm
source: tdn-rm
title: infoProc
type: documentation
url: https://tdn.totvs.com/display/LRM/infoProc
version: 1
---

## Informações de Processos

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| infoProc | tipoCom | 0-3 |  | Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte | Gerar um registro para cada processo e tipo de suspensão |
| tpProc | infoProc | 1-1 | 1 | Preencher com o código correspondente ao tipo de processo:  Valores Válidos: 1 - Administrativo; 2 - Judicial. | DPROCESSOJUDICIAL.TIPOPROCESSO |
| nrProc | infoProc | 1-1 | 21 | Informar o número do processo administrativo/judicial.  Validação: Deve ser um número de processo administrativo ou judicial válido e existente na Tabela de Processos | DPROCESSOJUDICIAL.NUMERO |
| codSusp | infoProcRetAd | 0-1 | 14 | Código do Indicativo da Suspensão, atribuído pelo contribuinte.    Não preencher se {tpProcRetPrinc} = [3]. | DTRIBDISCUTIDOSPROCJUDICIAL.CODINDICSUSPEXIG |
| vlrCPSusp | infoProc | 0-1 | 14 | Valor da Contribuição Previdenciária com exigibilidade suspensa  Validação: Preenchimento obrigatório se {vrRatSusp} e {vrSenarSusp} não tiverem sido preenchidos. Deve ser um valor maior que zero. | DTRBITEMCALCCONTRPREV.VLRRETSUSPDEPJUIZO |
| vlrRatSusp | infoProc | 0-1 | 14 | Valor da contribuição para Gilrat com exigibilidade suspensa  Validação: Preenchimento obrigatório se {vlrCPSusp} e {vlrSenarSusp} não tiverem sido preenchidos. Deve ser um valor maior que zero. | DTRBITEMCALCCONTRPREV.VALORNAORETGILRAT |
| vlrSenarSusp | infoProc | 0-1 | 14 | Valor da contribuição para o Senar com exigibilidade suspensa  Validação: Preenchimento obrigatório se {vlrCPSusp} e {vlrSenarSusp} não tiverem sido preenchidos. Deve ser um valor maior que zero. | DTRBITEMCALCCONTRPREV.VALORNAORETSENAR |
