---
article_id: 360044530853
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 44555eca6a41d3c8dad15f7f3ef14685d423190057e6218b7da08c5fbc01c040
fetched_at: '2026-06-28T22:42:45.829000+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quebrar OP por pedido de venda em uma
  determinada quantidade
type: support-article
updated_at: '2024-06-11T17:37:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044530853-Manufatura-Linha-Protheus-SIGAPCP-Quebrar-OP-por-pedido-de-venda-em-uma-determinada-quantidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:20 min****Dúvida**Como quebrar uma **OP - Ordem de produção** aberta por **pedido de venda** em uma determinada quantidade?  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para quebrar uma **OP** por **pedido de venda** em uma determinada quantidade, utilizamos **B1\_LE - Lote Econômico** para o produto, o cadastro é feito pela rotina **MATA010 - Cadastro de produtos** na aba **MRP/Suprimentos.**Parâmetros utilizados:   
**1.** **MV\_QUEBROP- Define se as OPs serão quebradas de acordo com o lote econômico ou se será gerada apenas uma ordem de produto com quantidade total;****2. MV\_FORCALM- Indica se as ordens de produção geradas pelo Sistema devem ser geradas de acordo com a quantidade de lote econômico.****Exemplo 1**Determinar que a **OP** por **pedido de venda** será quebrada a cada 500 unidades, com pedido de venda de 1500 unidades:  
  
1- Definir para o produto, **lote econômico** de **500**;  
2- Parametrização:   
**MV\_QUEBROP = S**  
**MV\_FORCALM = .F**.  
  
Serão abertas três **OPs**de 500 unidades.  
  
**Exemplo 2**Determinar que a **OP** por **pedido de venda** será quebrada a cada 250 unidades, com pedido de venda de 400 unidades:  
  
1- Definir para o produto, **lote econômico** de **250**;  
2- Parametrização:   
**MV\_QUEBROP = S**  
**MV\_FORCALM = .F**.  
  
Será aberta uma **OP**de 250 unidades e outra **OP**de 150 unidades.
