---
content_hash: 2afbb89b57df9e3d7fda4d58d16a05d38ad65962a191beb37e6cb7273f77b204
fetched_at: '2026-06-29T00:11:48.854581+00:00'
page_id: '828432067'
product: rm
source: tdn-rm
title: DT - Reembolso da Operadora de Assistência a Saúde - Indicativo da origem do
  reembolso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=828432067
version: 4
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Reembolso da Operadora de Assistência a Saúde - Indicativo da origem do reembolso |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9129](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9129) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2302.261
* 12.1.2306.222
* 12.1.2310.158
* 12.1.2402.101 e superiores

## **03. SITUAÇÃO/REQUISITO**

Possibilitar que no cadastro de Reembolso da Operadora de Assistência à Saúde, quando o **Indicativo da origem do reembolso** for igual á "**2- Reembolso efetuado pelo empregador como benefício do próprio empregador",** não seja obrigatório o preenchimento do campo "**Operadora".**

## **04. SOLUÇÃO**

Devido o cadastro de "Reembolso da Operadora de Assistência a Saúde" ser utilizado tanto para o eSocial quanto para a DIRF, e considerando que na DIRF esse campo é obrigatório, a solução não pode ser implementada diretamente no cadastro. Portanto, optamos por realizar a tratativa na geração do XML do evento S-1210, de forma a não incluir a tag <**regANS**> quando o indicativo da origem do reembolso <**IndOrgReemb**> for igual a '**2**'.

## **05. DEMAIS INFORMAÇÕES**
