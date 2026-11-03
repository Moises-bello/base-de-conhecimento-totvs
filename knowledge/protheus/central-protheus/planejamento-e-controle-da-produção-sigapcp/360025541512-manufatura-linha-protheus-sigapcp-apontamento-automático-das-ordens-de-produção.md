---
article_id: 360025541512
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d5ccf96dc5abcbe37a72e887586df2a92cfe38f185920f3602bef3e17f10f9a5
fetched_at: '2026-06-28T22:42:40.800997+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Apontamento automático das ordens de
  produção intermediárias
type: support-article
updated_at: '2023-05-19T18:40:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025541512-Manufatura-Linha-Protheus-SIGAPCP-Apontamento-autom%C3%A1tico-das-ordens-de-produ%C3%A7%C3%A3o-intermedi%C3%A1rias
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura:**00:00:50 min****Dúvida**É possível apontar automaticamente as **OPs - Ordens de Produção** intermediárias ao apontar a **OP** pai?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Preencha o parâmetro **MV\_PRODAUT - Gera Lançamentos Automáticos de Produção das Ordens de Produções Vinculadas a OP Pai** com o conteúdo **T**, desse modo, ao efetuar o apontamento por meio da rotina **MATA250 - Apontamento Simples**, as **OPs** intermediárias serão apontadas automaticamente.  
  
**Importante**  
Essa funcionalidade **não** está disponível nos apontamentos através das rotinas **Apontamento de Produção Modelo I - MATA680** e **Apontamento de Produção Modelo II -** **MATA681**, pois nessas rotinas são informados os apontamentos por operação, informando recurso e duração da operação.
