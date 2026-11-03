---
content_hash: 112927188d5091d30c88ad6fe3ecacade28a829e8f7c10ad9ffbfd7becffb608
fetched_at: '2026-06-29T00:05:47.365191+00:00'
page_id: '1011554304'
product: rm
source: tdn-rm
title: DT - Lançamento Financeiro - Tipo "24-Total Guia FGTS Digital" - Tratativa
  para desconsiderar FGTS mês anterior no tipo de guia Mensal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1011554304
version: 5
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Lançamento Financeiro - Tipo "24-Total Guia FGTS Digital" - Tratativa para desconsiderar FGTS mês anterior no tipo de guia Mensal |
| País: | Brasil |
| Issue: | [DRHROTRM-15166](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15166 "View this issue") |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir dos patches:

* 12.1.2502.221
* 12.1.2506.169
* 12.1.2510.101 e superiores

## **03. SITUAÇÃO/REQUISITO**

Adequar a geração do Lançamento Financeiro do tipo **“24 – Total Guia FGTS Digital”**, referente ao tipo de guia**Mensal**, paranão considerar o valor de FGTS do mês anterior que já tenha sido gerado no tipo de guia **Rescisório**.

## **04. SOLUÇÃO**

Foi realizada uma tratativa no processamento do Lançamento Financeiro do tipo **“24 – Total Guia FGTS Digital”**, referente ao tipo de guia **Mensal**, para desconsiderar o valor do FGTS que já foi gerado no tipo de guia **Rescisório**. garantindo que não ocorra duplicidade no valor calculado.

**Exemplo:**

* + **Competência atual:** 05/2025
  + **Chapa:** 90810
  + **Data de demissão:** 05/05/2025
  + O calculo da rescisão foi realizado com a flag “FGTS mês anterior será recolhido na GRFC/FGTS Digital” marcada, conforme demonstrado abaixo:

.

Ao gerar olançamento financeiro para o tipo de guia**Rescisório + Mensal**, o sistema gerou corretamente o valor referente à **rescisão + mês anterior**.

Ao gerar olançamento financeiro para o tipo de guia **Mensal** da competência **04/2025**, o valor não foi gerado novamente, pois já havia sido recolhido na guia do tipo **Rescisório + Mensal**.

## **05. DEMAIS INFORMAÇÕES**
