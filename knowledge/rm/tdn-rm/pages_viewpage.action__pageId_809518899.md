---
content_hash: 53a53188404e0b90084cee7afdbd9a48d96408e7a34d1d0db45f7eb48bcee96f
fetched_at: '2026-06-29T00:11:44.084202+00:00'
page_id: '809518899'
product: rm
source: tdn-rm
title: DT - S-1200 e S-1210 - Separação de demonstrativos por lançamento para autônomos
  do TOTVS Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=809518899
version: 12
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1200 e S-1210: Adequação para autônomos do TOTVS Gestão Financeira |
| País: | Brasil |
| Issue: | [DRHROTRM-6684](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6684) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.125
* 12.1.2306.192
* 12.1.2302.243

## **03. SITUAÇÃO/REQUISITO**

Adequação na geração dos eventos S-1200 e S-1210 para autônomos no TOTVS Gestão Financeira, tratando situações em que há mais de uma nota para o mesmo cliente/fornecedor, com datas distintas, porém dentro da mesma competência.

## **04. SOLUÇÃO**

Houve uma modificação na chave do evento S-1200 no leiaute S-1.0 do eSocial, onde a chave passou a ser composta pelo Tipo de Pagamento, Período de Referência e Identificação do Movimento. Em resposta a essa modificação, realizamos uma alteração na chave dos eventos S-1200 e S-1210 dos autônomos. Anteriormente, a tag <ideDmDev> unificava os lançamentos em um único ideDmDev; no entanto, a partir de agora, a chave passa a ser composta pelo código do lançamento. Essa adaptação busca seguir as atualizações no leiaute do eSocial e assegurar a conformidade com as mudanças efetuadas.

**O QUE FOI AJUSTADO?**

No exemplo a seguir, analisaremos os dois lançamentos, identificados pelos códigos **7144** e **7139**.

1) No XML S-1200, foram gerados dois <ideDmDev> com o código do lançamento.

2) No XML S-1210, foram gerados dois <ideDmDev> com o código do lançamento.

ATENÇÃO:

1. Após a atualização, será necessária a regeração de todos os periódicos dos autônomos do TOTVS Gestão Financeira do período atual.
2. Caso haja a necessidade de retificação do XML do S-1210 de períodos anteriores, é necessário enviar uma retificação do evento S-1200, pois os <ideDmDev> serão gerados por lançamento.
