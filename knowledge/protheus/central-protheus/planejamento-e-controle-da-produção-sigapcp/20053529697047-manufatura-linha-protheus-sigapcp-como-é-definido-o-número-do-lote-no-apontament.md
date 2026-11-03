---
article_id: 20053529697047
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f562452844b51c071cd0d56a5879725b082f92aa861d5c984c39decfd396aa96
fetched_at: '2026-06-28T22:42:41.077496+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como é definido o número do lote no
  apontamento de produção
type: support-article
updated_at: '2025-04-07T18:30:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20053529697047-Manufatura-Linha-Protheus-SIGAPCP-Como-%C3%A9-definido-o-n%C3%BAmero-do-lote-no-apontamento-de-produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20053502181399)***Tempo aproximado para leitura: **00:01:22 min  
  
Dúvida**Ao fazer o apontamento de produção, como é definido o **número de lote** do produto?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O número do lote pode ser gerado através de uma fórmula definida no campo **B1\_FORMLOT - Código da fórmula para preenchimento do lote**.  
Se não houver fórmula definida neste campo, mas houver no parâmetro **MV\_FORMLOT - Código da fórmula default utilizada para preenchimento dos lotes**, será definido o número do lote a partir da fórmula deste parâmetro.  
Se ainda não tiver essa definição, será feita a partir do parâmetro **MV\_PRXLOTC - Próximo lote** e por último, caso não consiga definir das formas anteriores, será atribuído o lote **AUTO** seguido de uma sequencia numérica.  
  
**Importante**O lote é definido por apontamento, assim se tivermos dez apontamentos podemos ter dez números de lotes diferente para a mesma ordem.  
  
**Saiba mais  
[Manufatura - Linha Protheus - SIGAPCP - Definição do número de lote ao subproduto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008689882-Manufatura-Linha-Protheus-SIGAPCP-Defini%C3%A7%C3%A3o-do-n%C3%BAmero-de-lote-ao-subproduto)**
