---
article_id: 360043192694
category: Chão de Fábrica (SIGASFC)
content_hash: b368fc242bc54d6bbe07c5422b14ce1eabb5f4def280cc924a0368eb0f65dbaf
fetched_at: '2026-06-28T22:42:49.886282+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Status split
type: support-article
updated_at: '2022-04-01T11:51:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043192694-Manufatura-Linha-Protheus-SIGASFC-Status-split
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:35 min**  
**Dúvida** Por que ao dividir o **split** os apontamentos fechados continuam com *status* **Verde - Disponível para Apontamento**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12   
  
**Solução**Se o parâmetro **MV\_SFCQTS - Apontamento sugere quantidade do Split** estiver como **T** o Sistema vai considerar o apontamento de cada **split**, e o *status* do **split** já apontado ficará **Vermelho - Indisponível para apontamento**.  
Se estiver como **F** o Sistema vai considerar a quantidade no todo, ou seja, ficará **Disponível para apontamento**, porque ainda não foi reportada a quantidade total.
