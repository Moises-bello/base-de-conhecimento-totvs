---
article_id: 360035870214
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 64df08ace3915f3d83cfe7e54de689dc141598771a574991905430d77db792a0
fetched_at: '2026-06-28T22:42:47.293494+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Mensagem A650NAOALT
type: support-article
updated_at: '2019-12-27T11:49:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035870214-MP-SIGAPCP-Mensagem-A650NAOALT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:40 min**  
  **Ocorrência**Ao tentar alterar uma **OP - Ordem de Produção** o **MATA650 - Ordens de Produção**  que esteja **encerrada** é apresentada a mensagem **A650NAOALT**.  
  
**Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Causa**Esse incidente ocorre, pois o parâmetro **MV\_ATOPFEC - Permite alterar OP encerrada para campos do usuário, caso seu conteúdo seja o valor 2** está com o valor igual a **1**.**Solução**No configurador alterar o parâmetro**MV\_ATOPFEC** para **2** e será possível alterar algumas informações da **OP** **encerrada**.
