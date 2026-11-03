---
article_id: 9610549316247
category: Materiais - Compras (SIGACOM)
content_hash: 734ff7394d8bc4bef4b65ffcd2ddcc3caf79bc8768ac52c0c72b0ee9b88474fb
fetched_at: '2026-06-28T22:41:14.369576+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Card Lead Time no Dashboard
  Compras
type: support-article
updated_at: '2022-10-17T19:59:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9610549316247-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Card-Lead-Time-no-Dashboard-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**

Como é feita o cálculo do Lead Time no Dashboard Compras ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12

**Solução**

**Card Lead Time PC x NF**

O Card Lead Time PC x NF exibe a Média do Lead Time em dias de atendimento dos Pedidos de Compra através de Notas Fiscais de Entrada, dentre os Pedidos de Compra avaliados também são contabilizadas os Pedidos que ainda estão em Atendimento e que já foram finalizados.

**Para o card de *Lead Time PC x NF* o cálculo realizado para o Lead Time é: Data do campo *(D1\_DTDIGIT)* - Data do campo *(C7\_EMISSAO)* = Lead Time**

**Card Lead Time SC x PC**

O Card Lead Time SC x PC exibe a Média do Lead Time em dias de atendimento das Solicitações de Compra através de Pedidos de Compra, dentre as Solicitações avaliadas também são contabilizadas as Solicitações que ainda estão em Atendimento e que já foram finalizadas.

**Para o card de *Lead Time SC x PC* o cálculo realizado para o Lead Time é: Data do campo *(C7\_EMISSAO)* - Data do campo *(C1\_EMISSAO)* = Lead Time**

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [Card Lead Time SC x PC](https://tdn.totvs.com/display/public/PROT/Card+Lead+Time+SC+x+PC)
* [Card Lead Time SC x PC](https://tdn.totvs.com/display/public/PROT/Card+Lead+Time+SC+x+PC)
