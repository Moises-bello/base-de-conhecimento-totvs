---
article_id: 22542764407959
category: PMS - Projetos
content_hash: 88f7de1c594fa97c494134d8340bcd5305ce90396b18990b4e181458cedbfd48
fetched_at: '2026-06-28T22:37:14.928602+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Help PMSNOEMP
type: support-article
updated_at: '2024-04-05T12:14:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22542764407959-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Help-PMSNOEMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22542795100951) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como resolver o Help PMSNOEMP?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**

Significado dos campos:

* Saldo de Empenho (AFJ\_EMPEST)
* Código do Planejamento(AFJ\_PLANEJ)
* Quantidade Atual (AFJ\_QATU)
* Quantidade Empenhada (AFJ\_QEMP)
* Código do Planejamento (AFM\_PLANEJ)
* Liberado do Controle de Qualidade (AFN\_LIBCQ)

**Esse erro ocorre ao varrer (enquanto for a mesma filial), o projeto, tarefa, código e armazém (AFJ), para que ele não ocorra, cheque os campos para que a sentença não seja uma verdade.**

* **Caso 1:** Não sendo estorno do empenho acontece quando isso ocorre:  
  AFJ->AFJ\_QEMP não é maior que (AFJ\_QATU+AFJ\_EMPEST)

* **Caso 2:** Sendo estorno do empenho acontece quando isso ocorre:  
  AFJ->AFJ\_QATU + AFJ->AFJ\_EMPEST é zero.

* **Caso 3:** Se o AFJ->AFJ\_QEMP for maior que (AFJ\_QATU+FJ\_EMPEST) somado com AFN\_LIBCQ

* **Caso 4:** Campos 'AFM\_PLANEJ' ou 'AFJ\_PLANEJ' não está zerado (é maior que zero)
