---
article_id: 22544468609943
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 9050d82345cf2960e0d8ab18e85eab0eecb1bfacecc3b57b0bddafa740f55e2a
fetched_at: '2026-06-28T22:38:39.945768+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Pedido de venda sendo alterado
  mesmo com parâmetro "MV_ALTPED = N"
type: support-article
updated_at: '2024-04-04T12:46:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22544468609943-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-de-venda-sendo-alterado-mesmo-com-par%C3%A2metro-MV-ALTPED-N
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22544438935319) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Pedido de venda sendo alterado mesmo com parâmetro "MV\_ALTPED = N", como corrigir?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Como fazer o bloqueio de alteração de pedidos de venda ocorrer (os 5 tópicos a seguir devem estar simultaneamente da forma descrita):  
  
1) O parâmetro MV\_ALTPED tem que ser "N"  
  
2) "Tipo pedido (C5\_TIPO)" não pode ser "C", "I" ou "P"  
  
3) O pedido tem que ter o "Qtd. Entreg (C6\_QTDENT)" igual ao "Quantidade (C6\_QTDVEN)".  
  
4) Se o parâmetro MV\_EECFAT estiver ativo (.T.)

* Os campos "Num. Ped. Venda SIGAFAT (EEC\_PEDFAT)" e "Processo de exportação (C5\_PEDEXP)" tem de estarem preenchidos.

Qualquer alteração nos 4 itens acima fará com que o pedido de venda possa ser alterado.

**Saiba mais:**

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Parâmetro MV\_ALTPED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025018113-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Par%C3%A2metro-MV-ALTPED)
