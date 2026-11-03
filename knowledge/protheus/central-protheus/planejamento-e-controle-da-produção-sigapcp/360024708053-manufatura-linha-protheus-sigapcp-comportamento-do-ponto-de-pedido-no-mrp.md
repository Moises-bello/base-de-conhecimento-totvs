---
article_id: 360024708053
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7f13621bbbc7ef416bfb4ec48f500d19174303a3f87e8111f8ace623645c0ad9
fetched_at: '2026-06-28T22:42:42.076397+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Comportamento do ponto de pedido no
  MRP
type: support-article
updated_at: '2021-07-29T15:59:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024708053-Manufatura-Linha-Protheus-SIGAPCP-Comportamento-do-ponto-de-pedido-no-MRP
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:00 min**  
 **Dúvida**Qual é o comportamento da utilização do **Ponto de pedido** no **MATA712 - MRP**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**No processamento do **MRP - Material Requiriments Planning**, quando são geradas as ordens de produção e solicitações de compras que possuem parametrização no campo **Ponto Pedido** na rotina **MATA010 - Cadastro de produto** na aba **MRP/Suprimentos**, o Sistema gera as ordens na quantidade do ponto de pedido + 1. Isso ocorre para que no próximo processamento, não entre no ponto de pedido novamente.  
  
Exemplo: Se o ponto de pedido parametrizado é de 100, o **MRP** gera a ordem com quantidade de 101.  
No próximo processamento é verificado a parametrização novamente e consistido com a ordem já gerada, 100 < 101 onde é verificado que não é necessário gerar uma nova ordem.
