---
article_id: 1500004957661
category: Controle de Auditorias (SIGAQAD)
content_hash: 6ddb4cc7402acfb513a86f594377c0c191ad44b430eb79d62c09ee5748265931
fetched_at: '2026-06-28T22:42:30.841436+00:00'
product: protheus
section_id: 360005876634
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQAD - Deseja que todos os tópicos cadastrados
  neste check-list sejam montados automaticamente
type: support-article
updated_at: '2021-08-16T11:55:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004957661-Manufatura-Linha-Protheus-SIGAQAD-Deseja-que-todos-os-t%C3%B3picos-cadastrados-neste-check-list-sejam-montados-automaticamente
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No módulo **SIGAQAD - Controle de Auditorias**, ao selecionar o campo **Check-list** da aba **Áreas Auditadas** da rotina **QADA100 - Auditorias** é exibida a mensagem **Deseja que todos os Tópicos cadastrados neste check-list sejam montados Automaticamente? Conforme Parâmetro MV\_QADTOPA**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Auditorias (SIGAQAD) - Todas as versões  
  
**Causa**Esta mensagem é exibida na rotina **QADA100** quando o conteúdo do parâmetro **MV\_QADTOPA - Define que todos os Topicos cadastrados neste check-list sejam montados Automaticamente** está com conteúdo igual à **1-Sim**.   
  
**Solução**Quando o parâmetro **MV\_QADTOPA** está como **1-Sim**, indica que todos os tópicos cadastrados na rotina **QADA025 - Tópicos** para o *check-list* selecionado, serão carregados automaticamente. Caso o parâmetro esteja com conteúdo igual à **2-Não**, deve-se selecionar tópico por tópico.
