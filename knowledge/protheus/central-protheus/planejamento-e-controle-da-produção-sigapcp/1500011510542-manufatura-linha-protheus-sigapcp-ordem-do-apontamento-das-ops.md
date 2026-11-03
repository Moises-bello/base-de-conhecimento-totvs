---
article_id: 1500011510542
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 748d5fccda09424f566c08f8d36dddceeec40818c4456bf4e2b551f2df39df74
fetched_at: '2026-06-28T22:42:44.704054+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Ordem do apontamento das OPs
type: support-article
updated_at: '2021-05-21T10:39:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011510542-Manufatura-Linha-Protheus-SIGAPCP-Ordem-do-apontamento-das-OPs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:50 min**  
**Dúvida**Quando uma **OP - Ordem de produção**, gera uma ou mais **OPs - Ordens de Produções intermediárias**, em que ordem essas **OPs** devem ser apontadas?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**No momento do apontamento o Sistema não valida a ordem do apontamento, exigindo que uma **OP** intermediária seja apontada antes da sua **OP** pai.   
Neste momento somente o estoque dos componentes empenhados é validado, quando o parâmetro **MV\_ESTNEG - Identifica se o sistema permitirá que o saldos em estoque dos produtos fique negativo através de movimentação**, tiver o conteúdo **N**, sendo assim, havendo estoque dos itens empenhados para a OP que se deseja apontar, esse apontamento pode ser realizado.
