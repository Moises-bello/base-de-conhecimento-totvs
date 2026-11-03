---
article_id: 360019869032
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 14d54eeff3370e7596fb329784d2d5154529ffcab9e477751d961c764e09badb
fetched_at: '2026-06-28T22:38:29.908179+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Estorno de Endereçamento na Exclusão do Documento de Saída
type: support-article
updated_at: '2021-05-10T19:33:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019869032-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Estorno-de-Endere%C3%A7amento-na-Exclus%C3%A3o-do-Documento-de-Sa%C3%ADda
---

**Dúvida**Ao excluir uma nota que possui produto com endereçamento, quais tratamentos o sistema pode realizar para devolver o produto ao estoque?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Causa**

Isso depende da configuração do parâmetro **MV\_PDEVLOC** ele pode determinar:

* MV\_PDEVLOC = 0 (Redistribuir): O produto volta ao estoque para redistribuição, sendo necessário realizar um novo endereçamento;
* MV\_PDEVLOC = 1 (Localização Original): O produto retorna ao Endereço que estava antes, dessa forma não é necessário realizar um novo endereçamento;
* MV\_PDEVLOC = 2 (Perguntar): O sistema exibe uma tela perguntando se deseja redistribuir ou retornar o produto ao endereço que estava antes:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500016146441/mceclip0.png)

**Solução**Configure o parâmetro **MV\_PDEVLOC** de acordo com sua necessidade.

**Saiba mais**: **[https://tdn.totvs.com/x/EKgfGg](http://tdn.totvs.com/display/PROT/FAT0282+Tela+de+tratamento+de+estorno)**
