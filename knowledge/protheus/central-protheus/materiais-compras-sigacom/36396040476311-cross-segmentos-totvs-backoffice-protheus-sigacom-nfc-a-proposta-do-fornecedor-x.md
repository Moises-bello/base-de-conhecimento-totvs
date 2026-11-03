---
article_id: 36396040476311
category: Materiais - Compras (SIGACOM)
content_hash: 6b0db186fc2fb6bcb33e0e032b50e9c30b0e1205838e52432e2494ac5c12f61c
fetched_at: '2026-06-28T22:41:20.280126+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - A proposta do
  fornecedor XXX para a cotação XXX já foi analisada
type: support-article
updated_at: '2025-11-17T19:43:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36396040476311-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-A-proposta-do-fornecedor-XXX-para-a-cota%C3%A7%C3%A3o-XXX-j%C3%A1-foi-analisada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36396040459543) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**

Ao clicar em Analisar a Cotação **Por Proposta**, no Novo Fluxo de Compras, é gerado o erro " A proposta do fornecedor XXX para a cotação XXX já foi analisada "

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36396040460823)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - a partir da Release 12.1.2310

**Causa**

Esse erro ocorre quando **um item da cotação já foi analisado previamente,** gerando Pedido de Compra ou Contrato GCT e tentamos analisar a Cotação Por Proposta. Nessas situações, já temos um item analisado e ao tentar analisar novamente a cotação completa **pela opção “Analisar Por Proposta Completa”**, o sistema identifica que existe análise registrada para um ou mais itens e, por isso, **bloqueia a análise por proposta**, já que esse método só é permitido quando nenhum item da cotação foi analisado anteriormente.

**Solução**

Para prosseguir com a análise dessa cotação, é necessário utilizar a opção **“Analisar Por Item”**, avaliando apenas os itens que ainda não foram analisados. Esse método mantém a consistência da análise já existente e permite concluir o processo sem conflitos.

Segue abaixo GIF do passo a passo de como Analisar a Cotação Por Item.

![](https://tdn.totvs.com.br/download/attachments/680260500/Analise%20por%20item.gif?version=3&modificationDate=1712955574280&api=v2)

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
