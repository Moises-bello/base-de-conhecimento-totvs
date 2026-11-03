---
article_id: 8839351287191
category: Materiais - Compras (SIGACOM)
content_hash: 19835f1091487669813678213870def29180ccfdebf3b1bdb51311e1167659a8
fetched_at: '2026-06-28T22:41:14.213258+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Array out of bounds
  ( 0 of 109 )  on A120PRODUTO(MATA120.PRX)
type: support-article
updated_at: '2022-09-13T14:32:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8839351287191-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Array-out-of-bounds-0-of-109-on-A120PRODUTO-MATA120-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Ao incluir um item no pedido de compra, seja via pesquisa ou digitando o código do item surge o seguinte error.log : *Array out of bounds ( 0 of 109 ) on A120PRODUTO(MATA120.PRX)*  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Causa**Este incidente ocorre porque não esta encontrando o campo de Segunda Uniade de Medida no Pedido de Compras

**Solução**

Verifique se :

1. Ao incluir o item no pedido de compras, observe se o campo c7\_segum da segunda unidade de medida foi preenchido;

![cx.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8839259636759/cx.png)

2. Se campo esta com o nível 1 e usado para todos os módulos;

No ambiente Configurador : Base de Dados -> Dicionário -> Base de Dados -> Tabela SC7 -> C7\_SEGUM;

**![segum.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8839190583575/segum.png)**

**SAIBA MAIS EM :**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
