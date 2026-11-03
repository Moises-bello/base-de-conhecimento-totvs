---
article_id: 26462882370711
category: Financeiro - Reinf
content_hash: f24971fe4ae4072fff230fc6ecc103089907e4dd99f6631d0cbf16bd504d7c1e
fetched_at: '2026-06-28T22:37:51.714402+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Pagamento de
  PCC parcial
type: support-article
updated_at: '2024-09-19T19:29:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26462882370711-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Pagamento-de-PCC-parcial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26493302368407)Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**

O que fazer quando os impostos de PIS, COFINS e CSLL foram gerados na emissão, porém está subindo parcialmente para o painel do TAF?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Importante**

Independentemente da configuração do parâmetro **MV\_BX10925**, que permite a geração dos **TX's** **desses impostos na emissão ou na baixa, o Extrator Fiscal considerará como fato gerador do PIS, COFINS e CSLL** o pagamento do título principal (por exemplo: **título do tipo NF, DP, BOL**, etc.), utilizando o campo **FK2\_DATA**.

Quando o parâmetro **MV\_BX10925** estiver configurado como 2 (gerando **TX's** na inclusão do título a pagar), o **Extrator Fiscal** verificará se o título principal foi baixado antes de enviar os tributos ao **TAF**. Em caso de baixa parcial, serão enviados os valores dos tributos proporcionais ao montante baixado.

**Saiba mais**

[FAQ - 0016 - Quais os fatos geradores serão considerados no extrator financeiro?](https://tdn.totvs.com/pages/releaseview.action?pageId=737543501)
