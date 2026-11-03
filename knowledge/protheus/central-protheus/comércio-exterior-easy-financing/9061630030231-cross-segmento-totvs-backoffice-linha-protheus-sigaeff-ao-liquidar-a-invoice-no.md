---
article_id: 9061630030231
category: Comércio Exterior - Easy - Financing
content_hash: fa4c563e166b87f0e20d53d2b17e4eebc12962ab58244033ba244c1a581e6e6e
fetched_at: '2026-06-28T22:39:53.014812+00:00'
product: protheus
section_id: 1500001538101
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEFF - Ao liquidar a
  invoice no painel de câmbio, no contrato de financiamento, não grava data do evento
  640
type: support-article
updated_at: '2022-09-22T15:00:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9061630030231-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEFF-Ao-liquidar-a-invoice-no-painel-de-c%C3%A2mbio-no-contrato-de-financiamento-n%C3%A3o-grava-data-do-evento-640
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Ao liquidar a invoice no painel de câmbio, no contrato de financiamento, não grava data do evento 640.  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Financing Control* – Todas versões  
  
**Solução**Se no contrato de Financiamento **"SIGAEFF"**,  o campo  Baixa automática de juros **(EF1\_PGJURO)** estiver **2 -Não** ao liquidar o cambio de exportação o evento **640** será criado porém a data não será informada pois, será necessário alterar o contrato, selecionar o evento **640** e selecionar a opção Liquidar. Efetuando a liquidação a data do evento será gravada corretamente.

![](https://totvssuporte.zendesk.com/attachments/token/IpKjGCaBx4NSU9qmYkH51WGWa/?name=image.png)

Para que a data do evento **640** seja gravada, o campo  Baixa automática de juros **(EF1\_PGJURO)** precisa estar informado o numeral **2- Sim** ao liquidar o cambio de exportação a data do evento **640** será criado automaticamente com a data.
