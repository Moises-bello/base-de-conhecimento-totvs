---
article_id: 31721155777687
category: Faturamento - Integrações
content_hash: cb27df53968e06e0002f6eb0e7632da32a8d9d9bb42b1e34c34b6c2c835325d5
fetched_at: '2026-06-28T22:38:26.527955+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Pontos de entrada na importação
  XML
type: support-article
updated_at: '2025-04-29T18:54:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31721155777687-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pontos-de-entrada-na-importa%C3%A7%C3%A3o-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31721126711575) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Quais os pontos de entrada na importação XML?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

|  |  |
| --- | --- |
| Ponto de Entrada | Descrição |
| [MA411GRV](https://tdn.totvs.com/x/oxc-Dg) | Manipula os dados do Pedido de Venda gerado por meio do EDI de Vendas |
| [MA411CLI](https://tdn.totvs.com/x/RRc-Dg) | Altera o Cliente do Faturamento por meio da tag específica no EDI de Vendas |
| [MA411PRD](https://tdn.totvs.com/x/BUYCE) | Manipula o Código do Produto informado no XML (tag ItemCode) |

**OBS:** Para ir a documentação, clique no nome do ponto de entrada.

**Saiba mais:**

[IX02 - Pontos de Entrada - Faturamento - P12](https://tdn.totvs.com/x/xkLuIw)

[FAT0305 Integrador XML para Pedido de Vendas - módulo Faturamento](https://tdn.totvs.com/x/uQoxJw)
