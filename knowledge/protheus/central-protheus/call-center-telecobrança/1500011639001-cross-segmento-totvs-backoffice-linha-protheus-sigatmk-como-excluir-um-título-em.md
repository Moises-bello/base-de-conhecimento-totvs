---
article_id: 1500011639001
category: Call Center - Telecobrança
content_hash: b758fc190d8d788e84af49cf9e960e2475a658ff926e66a5f26431e96c488e52
fetched_at: '2026-06-28T22:41:28.542752+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Como excluir
  um título em um atendimento telecobrança
type: support-article
updated_at: '2021-05-26T17:05:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011639001-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Como-excluir-um-t%C3%ADtulo-em-um-atendimento-telecobran%C3%A7a
---

**Dúvida**Como excluir um título em um atendimento telecobrança?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK- Todas as versões  
  
**Solução**

Não é possível excluir como no pedido de vendas(**mata410**), onde ao dar um delete na linha, o sistema exclui o registro, no telecobrança (**TMKA274**), o sistema não acata.

O que pode ser feito:

**1-** Se a seleção do título for manual, é possível substituir este título por outro que possa ser cobrado:

![](https://totvssuporte.zendesk.com/attachments/token/1Na8rWmzWF5pZcDIBCQxcVFrc/?name=inline-931894480.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/PNZPYWMgOkLl6ACC8zGlE48oh/?name=inline-1031353259.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/dlWpsexgRmE6ErX5tHr4ZBG3a/?name=inline825254998.png)

​  
**1.1** - Para deixar como seleção manual, basta alterar a regra de negociação (**TMKA190**):  
![](https://totvssuporte.zendesk.com/attachments/token/DureoUzRWEH8B5RKUOSaCt4Iw/?name=inline8005436.png)​  
  
**2 -** Ou em último caso, cancelar o atendimento de cobrança , colocar o título em exceção na seleção de títulos (**TMKA180**), outras ações, e gerar um novo atendimento sem o título em questão.
