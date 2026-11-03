---
article_id: 37322488607767
category: Materiais - Compras (SIGACOM)
content_hash: 7f38d16a1519653f21183a0d4d9527252f91a8dc1c4dc2da7ae6ca9a9278e263
fetched_at: '2026-06-28T22:41:21.856161+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - O que fazer para
  não aglutinar os itens ao gerar a Cotação?
type: support-article
updated_at: '2025-12-29T17:42:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37322488607767-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-O-que-fazer-para-n%C3%A3o-aglutinar-os-itens-ao-gerar-a-Cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37322495360535) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
No Novo Fluxo de Compras, ao selecionar itens da Solicitação de Compras e gerar a Cotação esses itens são aglutinados. O que fazer para não aglutinar os itens ao gerar a Cotação?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2410

**Causa**

Quando houver mais de uma solicitação possuindo produtos iguais, com a mesma Data de necessidade, conta contábil, entre outras similaridades, haverá um agrupamento de solicitações. Surgindo então na tela um campo chamado **Solicitações agrupadas.** Nele o usuário conseguirá visualizar através de um *disclaimer* azul, o número da Solicitação e o número do item, apresentada nesse mesma ordem **Solicitação-Item,**somando as quantidades solicitadas à quantidade total.

![](https://tdn.totvs.com.br/download/attachments/680260500/SC%20agrupada.png?version=1&modificationDate=1712772084363&api=v2)

**Solução**

Para não aglutinar, será necessário utilizar o Ponto de Entrada abaixo. Esse ponto de entrada determina o Critério de quebra dos itens da solicitação de compra.

**Nome do ponto de entrada**: **MA131QSC**

**Objetivo**: Este ponto de entrada é para definir o critério de quebra dos itens da SC na geração da cotação por meio de um bloco de código.

**Documentação**: [Clique Aqui - Documentação MA131QSC](https://tdn.totvs.com.br/pages/releaseview.action?pageId=908331220)

***Saiba Mais:***

[Documentação MA131QSC](https://tdn.totvs.com.br/pages/releaseview.action?pageId=908331220)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
