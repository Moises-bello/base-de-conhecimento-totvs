---
article_id: 360044358234
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 298725783cd4c44e772f26b01b900cd90295f985eef78eefaed2554ebd022e0e
fetched_at: '2026-06-28T22:42:41.032648+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Carga máquina não respeita a previsão
  inicial da OP
type: support-article
updated_at: '2021-11-09T20:05:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044358234-Manufatura-Linha-Protheus-SIGAPCP-Carga-m%C3%A1quina-n%C3%A3o-respeita-a-previs%C3%A3o-inicial-da-OP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**Por que o **MATA690 - Carga Máquina** não respeita a previsão inicial da **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Na alocação pelo início, o Sistema considera a data informada no parâmetro **Data Início?** e realiza todas as alocações a partir daquela data, sem considerar a **C2\_DATPRI - Previsão Inicial** da **OP**, com o objetivo de concluir no menor tempo possível a produção das **Ordens de Produção** em questão.
