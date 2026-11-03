---
article_id: 35932157939735
category: Financeiro - Contas a Pagar
content_hash: f20d248be48253c924a88e3a1290eb55034da23ab473ff0b530e2fa576524257
fetched_at: '2026-06-28T22:38:09.856039+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a
  Pagar - FINA080 - Cancelamento de baixa do título principal com impostos
type: support-article
updated_at: '2025-10-28T13:14:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35932157939735-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-Contas-a-Pagar-FINA080-Cancelamento-de-baixa-do-t%C3%ADtulo-principal-com-impostos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35932157914519) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao estornar baixas parciais de títulos pais que contém títulos filhos de impostos, é apresentado o HELP FINIMPBX: Não é possível estornar este movimento pois este título possui impostos calculados na baixa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35932157915671)

**Solução**

**Em alguns casos, é necessário validar o** parâmetro **MV\_CB10925**:

Ele tem por finalidade definir se permite ou não o cancelamento de baixa de títulos pais que possuem títulos filhos de impostos baixados.

1=Permite cancelar

2=Não permite

Saiba mais: [Cancelamento de baixa do título principal com impostos baixados](https://tdn.totvs.com/pages/viewpage.action?pageId=244435815)
