---
article_id: 4412247075351
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: db9a2f43a4dd7dc3048829ee192f9a2984d6a4b3a0e3eb66593657f3e1281bf4
fetched_at: '2026-06-28T22:42:47.088342+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Tratamento dos alternativos no MRP
  Multi-Empresa
type: support-article
updated_at: '2021-11-05T10:40:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412247075351-Manufatura-Linha-Protheus-SIGAPCP-Tratamento-dos-alternativos-no-MRP-Multi-Empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Qual o critério através do qual o **MRP - Material Requiriment Planning** determina qual alternativo é reservada para a produção de um item?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versao 12  
  
**Solução**Quando um componente possui mais de um alternativo o **MRP** primeiramente avalia a posição de estoque dos alternativos na filial na qual há a necessidade e faz a reserva da quantidade necessária/disponível nesta filial, e não encontrando estoque suficiente verifica novamente o saldo de todos os alternativos agora nas demais filiais.   
Desse modo ele pode gerar o empenho de um componente que não necessariamente é o primeiro alternativo, mas que possui saldo na filial da necessidade.
