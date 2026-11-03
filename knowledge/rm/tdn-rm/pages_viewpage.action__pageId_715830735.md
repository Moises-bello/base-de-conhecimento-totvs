---
content_hash: f6ca4b8e4cab317dd5c003c2394d480fca2893b0b09b345544c70ed5c30fe6c7
fetched_at: '2026-06-29T00:11:26.249006+00:00'
page_id: '715830735'
product: rm
source: tdn-rm
title: R-2060 - Contribuição Previdenciária sobre a Receita Bruta - CPRB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715830735
version: 12
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-2060

## **Conteúdo**



## **01. Regras****1**

### Regras Específicas

* Para geração desse evento deverá ser realizada a apuração da contribuição previdenciária, o evento será gerado com os valores do período de apuração.
* O Evento deve agrupar todos os lançamentos do período por cliente fornecedor.
* Os Lançamentos de ajuste não são gerados neste registro.

### Regras Gerais

## **02. Exemplo****2**

xmlExemplo R-2060


{...}
{...}

{...}
]]>ideContri

Utiliza um grupo **ideEstab** especifico para este tipo

## **03. Origem dos Dados****3**

1evtCPRBevtCPRB

| Elemento | Elemento Pai | Nível | Descrição | Ocorrência | Elemento Chave | Origem RM |
| --- | --- | --- | --- | --- | --- | --- |
| ideEvento | evtCPRB | 3 | Informações de identificação do evento | 1-1 |  |  |
| ideContri | evtCPRB | 3 | Informações de identificação do contribuinte | 1-1 | tpInsc, nrInsc |  |
| infoCPRB | evtCPRB | 3 | Informação da contribuição previdenciária sobre a receita bruta | 1-1 |  |  |
| ideEstab | infoCPRB | 4 | Identificação do estabelecimento | 1-1 |  |  |
| tipoCod | tipoCod | 5 | Registro que apresenta o valor total da receita por tipo de código de atividade econômica. | 1-N | codAtivEcon |  |
| tipoAjuste | tipoCod | 6 | Tipo do ajuste da CPRB | 0-N |  |  |
| infoProc | tipoCod | 6 | Informações de Processos | 0-50 | tpProc, nrProc, codSusp |  |

ideEventoideEventoideContriideContriideEstabideEstabtipoCodtipoCodinfoProcinfoProcideEstabxmlideEstab
123
str1234
str1234
str1234
str1234
{...}
]]>

### Origem dos dados

| Elemento do XML | Origem |
| --- | --- |
| tpInscEstab | Preenchimento de acordo com o campo abaixo |
| nrInscEstab | GFILIAL.CGC |
| vlrRecBrutaTotal | DPERIODO.VLRRECEITAFINANCEIRA |
| vlrCPApurTotal | Somatório dos grupos "filhos" |
| vlrCPRBSuspTotal | Não aderência |
