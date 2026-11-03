---
content_hash: 3b180b79cc466ee8723d7282ea368665fc28f87badb8d8b36bb87ee4dae216c6
fetched_at: '2026-06-29T00:11:38.016152+00:00'
page_id: '781190238'
product: rm
source: tdn-rm
title: 'DT - S-1200: Desconsiderar o código de cálculo "56- /3 Abono de Férias" na
  soma dos eventos do parâmetro "Evento Abono Férias Envelope"'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=781190238
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1200: Desconsiderar o código de cálculo "56- /3 Abono de Férias" na soma dos eventos do parâmetro "Evento Abono Férias Envelope" |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-6710](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6710) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2209.247
* 12.1.2302.171
* 12.1.2306.115

## **03. SITUAÇÃO/REQUISITO**

Desconsiderar o evento com o código de calculo "56- 1/3 Abono de Férias" na soma dos eventos do parâmetro "Evento Abono Férias Envelope" existente em "Parametrizador | eSocial | Configurações 6/7".

## **04. SOLUÇÃO**

De acordo com o retorno da [consultoria](https://tdn.totvs.com/pages/releaseview.action?pageId=663845768), foi identificado que o evento com código de cálculo "56 - 1/3 Abono de Férias" possui incidência em IRRF. Por conta disso, o produto foi ajustado para não incluir esse evento na soma dos eventos do parâmetro "Evento Abono Férias Envelope".

## **05. ASSUNTOS RELACIONADOS**
