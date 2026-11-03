---
article_id: 360016178972
category: Financeiro
content_hash: 4646bb3f65b922cd53f22b0b9d7c97831b5986a2580a040105188b29d22812e5
fetched_at: '2026-06-28T22:38:03.426417+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Quais as principais
  variáveis que contêm os tipos de títulos '
type: support-article
updated_at: '2022-06-15T00:12:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016178972-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Quais-as-principais-vari%C3%A1veis-que-cont%C3%AAm-os-tipos-de-t%C3%ADtulos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Quais as principais variáveis que contêm os tipos de títulos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Abaixo estão listadas as principais variáveis que contêm os tipos de títulos mais utilizados no módulo financeiro.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012182532/mceclip1.png)

A finalidade desse documento é de informar o correto tratamento dos tipos de títulos na codificação de rotinas do financeiro.

De acordo com a tabela acima, exemplificaremos uma aplicação que geralmente é utilizada nas rotinas:

If E1\_TIPO == “PA”    ERRADO !

If E1\_TIPO $ **MVPAGANT**  CORRETO !
