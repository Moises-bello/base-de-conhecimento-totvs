---
content_hash: 3a22fd9748cb944434d5366988e9487876756ea9339bffc9f67cb1aaae6ced8c
fetched_at: '2026-06-29T00:05:51.147770+00:00'
page_id: '1047387522'
product: rm
source: tdn-rm
title: DT - S-1200 e S-1210 - Múltiplos Vínculos - Separação de demonstrativos por
  lançamento para Autônomo Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1047387522
version: 6
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1200 e S-1210 - Múltiplos Vínculos - Separação de demonstrativos por lançamento para Autônomo Externo |
| País: | Brasil |
| Issue: | DRHROTRM-17435 |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2506.276
* 12.1.2510.195
* 12.1.2602.117 e superiores

## **03. SITUAÇÃO/REQUISITO**

Adequação na geração dos eventos S-1200 e S-1210 para Autônomo Externo, tratando situações em que há mais de uma nota para o mesmo cliente/fornecedor, com datas distintas, porém dentro da mesma competência.

## **04. SOLUÇÃO**

Houve uma modificação na chave do evento S-1200 no leiaute S-1.0 do eSocial, onde a chave passou a ser composta pelo Tipo de Pagamento, Período de Referência e Identificação do Movimento. Em resposta a essa modificação, realizamos uma alteração na chave dos eventos S-1200 e S-1210 dos autônomos. Anteriormente, a tag <ideDmDev> unificava os lançamentos em um único ideDmDev; no entanto, a partir de agora, a chave passa a ser composta pelo código. Essa adaptação busca seguir as atualizações no leiaute do eSocial e assegurar a conformidade com as mudanças efetuadas.

**O QUE FOI ADEQUADO?**

No exemplo a seguir, foram encontrados para a competência 01/2026 e caixa 01/2026 o lançamento identificado pelo código 77713 no autônomo externo e um envelope lançado no período 1 para o funcionário.

1) No XML do **S-1200**, foram geradas duas tags `<ideDmDev>`: uma referente ao **período 1**, registrado no envelope de pagamento, e outra contendo os **quatro últimos dígitos do código de pagamento do autônomo externo**.

 

2) No XML do **S-1210**, foram geradas duas tags `<ideDmDev>`: uma referente ao **período 1**, registrado no envelope de pagamento, e outra contendo os **quatro últimos dígitos do código de pagamento do autônomo externo**.

ATENÇÃO:

1. Após a atualização do patch, será necessária a regeração de todos os periódicos dos autônomos externos do período atual.
2. Caso haja a necessidade de retificação do XML do S-1210 de períodos anteriores, é necessário enviar uma retificação do evento S-1200, pois os <ideDmDev> serão gerados por lançamento.
3. Para os casos de autônomos sem múltiplos vínculos será gerado o código do lançamento integral.
