---
article_id: 5225454246679
category: Materiais - Compras (SIGACOM)
content_hash: 26d7e16dedcf2b4941898d5c7d633acb8ba408c509fae822e4a19d9cb8c5087d
fetched_at: '2026-06-28T22:41:14.377156+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Central de Compras
  - Como efetivar Sugestão de Compras?  
type: support-article
updated_at: '2022-04-04T18:18:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5225454246679-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Central-de-Compras-Como-efetivar-Sugest%C3%A3o-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03 min** **Dúvida**

Como efetivar Sugestão de Compras?    
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as Versões

**Solução**

O processamento da efetivação é feito para cada produto calculado em cada uma das filiais abastecidas e realizado da seguinte forma:

* Ao marcar a opção **Efetivar** e tendo o campo**Quantidade** maior que zero é gerado um documento de compra (solicitação de compra ou pedido de compra, conforme definição no campo **Doc. Compra**). Este documento é gerado na filial **(campo FILIAL)** definida no campo **Comprar Na**. Da mesma forma informe na filial de entrega no documento (campo **FILENT**) a filial definida no campo **Entregar Na**.
* Ao marcar a opção **Distribuidora** tendo o documento de compra gerado com filial de entrega na filial distribuidora (campo **Entregar Na** como Distribuidora), é gerado um Pedido de Venda na filial distribuidora com o cliente igual à filial abastecida e a quantidade igual à quantidade a comprar (campo **Comprar**).

Segue abaixo o processo de como Efetivar a Sugestão de Compras.

![20220404_145516.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5225268237207/20220404_145516.gif)

**Saiba mais em :**

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a funcionalidade do processo de Central de Compras (MATA179)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021601092-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-funcionalidade-do-processo-de-Central-de-Compras-MATA179-) [?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021601092-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-funcionalidade-do-processo-de-Central-de-Compras-MATA179-)
* [Central de Compras - Efetivação (MATA179 - SIGACOM)](https://tdn.totvs.com/x/Jq9GJg)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
