---
article_id: 360043003113
category: ADVPL - Classe e Função
content_hash: d2b4793c0b2a5c14e6136dc28935a5188a5fb089ad60cb55019ebc4f1d1f0ef0
fetched_at: '2026-06-28T22:40:19.443616+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função para retornar
  logs de acesso
type: support-article
updated_at: '2022-01-10T21:56:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043003113-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-para-retornar-logs-de-acesso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Existe alguma função que nos retorne os Logs de acessos dos usuários: Datas e Horas de Logon/Logout.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.1.17  
  
**Solução**Possuímos o recurso **Embedded Audit Trail** que tem o objetivo auditar as atividades realizadas pelos usuários do Protheus no banco de dados.  
Pode ser habilitado a regra de auditoria nas políticas do Protheus.  
Existe um *log* específico (auditar autenticação/acesso).  
Logo após isto pode ser verificado estas informações em ambientes/auditoria, possuindo até mesmo um relatório.  
  
**Saiba mais**[Configuração de Embedded Audit Trail](https://tdn.totvs.com/display/public/PROT/Rotinas+de+Logs+e+Auditoria)
