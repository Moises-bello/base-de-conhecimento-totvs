---
article_id: 20255307678615
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 0205cb4fd99f5a56e26f2960a0ef2d89ddc7770ccd33d526079984b49cfdae83
fetched_at: '2026-06-28T22:42:45.879362+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Requisição dos empenhos no último apontamento
type: support-article
updated_at: '2024-01-02T14:00:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20255307678615-Manufatura-Linha-Protheus-SIGAPCP-Requisi%C3%A7%C3%A3o-dos-empenhos-no-%C3%BAltimo-apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20255339033367) Tempo aproximado para leitura: **00:00:57 min** **Dúvida**É possível realizar vários apontamentos parciais e somente no último apontamento realizar as requisições?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Não, se o parâmetro **MV\_BXPROP - Proporcionaliza baixa automática da matéria-prima** tiver o conteúdo **N**, será feita a requisição total dos itens empenhados no primeiro apontamento, e se esse mesmo parâmetro tiver o conteúdo **S** será feita a requisição proporcional a cada apontamento, mas o Sistema atualmente não dispõem de uma configuração que permita diversos apontam parciais e somente no apontamento total a requisição dos itens empenhados.
