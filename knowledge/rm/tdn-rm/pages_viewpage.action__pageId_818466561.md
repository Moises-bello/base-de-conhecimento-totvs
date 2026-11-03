---
content_hash: 48c9eaf6203ba22dcea4d1bcf8c666f9c821dd01bdc3f66cf7e3d87349771c74
fetched_at: '2026-06-29T00:11:44.995993+00:00'
page_id: '818466561'
product: rm
source: tdn-rm
title: DT - S-1200 e S-1210 - Múltiplos Vínculos - Separação de demonstrativos por
  lançamento para autônomos do TOTVS Gestão Financeira (Middleware)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=818466561
version: 4
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1200 e S-1210: Múltiplos Vínculos - Separação de demonstrativos por lançamento para autônomos do TOTVS Gestão Financeira (Middleware) |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-8437](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8437) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.138
* 12.1.2306.204
* 12.1.2302.252

## **03. SITUAÇÃO/REQUISITO**

Adequação na geração dos eventos S-1200 e S-1210 para autônomos no TOTVS Gestão Financeira com Múltiplos Vínculos, com um funcionário da folha de pagamento e quando utiliza Middleware, tratando situações em que há mais de uma nota para o mesmo cliente/fornecedor, com datas distintas, porém dentro da mesma competência.

## **04. SOLUÇÃO**

Houve uma modificação na chave do evento S-1200 no leiaute S-1.0 do eSocial, onde a chave passou a ser composta pelo Tipo de Pagamento, Período de Referência e Identificação do Movimento. Em resposta a essa modificação, realizamos uma alteração na chave dos eventos S-1200 e S-1210 dos autônomos. Anteriormente, a tag <ideDmDev> unificava os lançamentos em um único ideDmDev; no entanto, a partir de agora, a chave passa a ser composta pelos quatro ultimos numeros do código do lançamento. Essa adaptação busca seguir as atualizações no leiaute do eSocial e assegurar a conformidade com as mudanças efetuadas.

**O QUE FOI ADEQUADO?**

No exemplo a seguir, foram adequados os lançamentos identificados pelos códigos 997336 e 997341, bem como um envelope lançado para o funcionário.

1) No XML S-1200, foram geradas duas tags <ideDmDev>, cada uma contendo os quatro últimos números do código do lançamento.

 

2) No XML S-1210, foram geradas duas tags <ideDmDev>, cada uma contendo os quatro últimos números do código do lançamento.

Importante!

1. Após a atualização, será necessária a regeração de todos os periódicos dos autônomos do TOTVS Gestão Financeira do período atual.
2. Caso haja a necessidade de retificação do XML do S-1210 de períodos anteriores, é necessário enviar uma retificação do evento S-1200, pois os <ideDmDev> serão gerados por lançamento.
3. Para os casos de autonomos sem multiplos vinculos será gerado o codigo do lançamento integral. Mais informações acesse aqui .
