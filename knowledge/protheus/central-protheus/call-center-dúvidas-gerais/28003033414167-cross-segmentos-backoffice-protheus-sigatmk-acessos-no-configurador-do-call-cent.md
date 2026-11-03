---
article_id: 28003033414167
category: Call Center - Dúvidas Gerais
content_hash: 324d1bc0b8d9feb070108e8c82d831f4e44a0851b77f7ccab3d287c73cb29b47
fetched_at: '2026-06-28T22:41:26.935801+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Acessos no configurador do
  Call Center
type: support-article
updated_at: '2024-11-22T22:19:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28003033414167-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Acessos-no-configurador-do-Call-Center
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28003033384471) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Quais são os acessos no configurador do módulo Call Center?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGATMK - Todas as versões  
  
**Solução**Acessos de usuários (tópico 4: [Permissões, acessos e privilégios no Protheus](https://tdn.totvs.com/x/tEZpMg)) no configurador correspondentes ao módulo call center (SIGATMK):

|  |  |  |  |
| --- | --- | --- | --- |
| ACESSO | DESCRIÇÃO | EXPLICAÇÃO | ROTINAS |
| 20 e 21 | Alterar pedidos de venda (20) e Excluir pedidos de venda (21) | Define se o usuário possui acesso para alterar (20) ou excluir (21) pedido de vendas | Call Center - TMKA271 |
| 25 | Rotina de atendimento | Define se o usuário possui acesso à rotina de atendimento | Call Center - TMKA271 |
| 56 | Excluir tabelas | Define se o usuário tem permissão para excluir tabelas | Suspects - TMKA341 |
| 104 | Consulta posição cliente | Define se o usuário tem permissão para consultar a posição do cliente | Perfil do Contato - TMKC010 |
