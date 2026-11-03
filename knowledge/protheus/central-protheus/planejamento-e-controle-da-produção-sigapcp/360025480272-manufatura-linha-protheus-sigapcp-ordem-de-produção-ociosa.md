---
article_id: 360025480272
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1c492f7c24fd485cf202ad158d87fbfbe7fbba47cf78d581cde2c25e0a081f37
fetched_at: '2026-06-28T22:42:44.701079+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Ordem de Produção ociosa
type: support-article
updated_at: '2025-09-23T16:59:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025480272-Manufatura-Linha-Protheus-SIGAPCP-Ordem-de-Produ%C3%A7%C3%A3o-ociosa
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35143687580823)*** Tempo aproximado para leitura: **00:01:19** **min****Dúvida**Onde é definido o tempo que a **OP** - **Ordem de Produção** ficará ociosa?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Através do parâmetro **MV\_DIASOCI** **- Indica o número de dias sem movimentação para considerar as Ordens de Produções como ociosa**. Porém quando a OP é aberta manualmente esse número de dias pode ser alterado no campo **C2\_DIASOCI - Indica o número de dias sem movimentação para considerar a OP como ociosa**.  
  
Não há como desativar o parâmetro. Quando o parâmetro **MV\_DIASOCI** estiver em branco as ordens com data de início anterior a data atual são consideradas ociosas. Quando o parâmetro não existir o conteúdo é preenchido com 99.  
  
A ordem é considerada ociosa quando o campo **C2\_TPOP**com o conteúdo **F**, o campo **C2\_DATRF** vazio e a data base subtraída da data do último movimento ou do conteúdo do campo **C2\_DATPRI** for maior ou igual ao tempo definido no campo **C2\_DIASOCI**.
