---
article_id: 4411625532567
category: Faturamento - Cadastros
content_hash: f9048c43edcfb8184d38ebb39845472ec6aa2e2e3bfc55ef2eb780db6367f19e
fetched_at: '2026-06-28T22:38:35.449777+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - É necessária adaptação do
  ExecAuto MATA030 para CRMA980?
type: support-article
updated_at: '2024-11-12T12:02:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411625532567-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-%C3%89-necess%C3%A1ria-adapta%C3%A7%C3%A3o-do-ExecAuto-MATA030-para-CRMA980
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15370076342423) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**É necessária adaptação na chamada do ExecAuto do MATA030 (Cadastro de Clientes) após sua descontinuação e início da obrigatoriedade de uso do CRMA980 (MVC)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**  
Assim como **não** será necessária a manutenção da configuração dos menus que acessem a rotina **MATA030**, pois a nova rotina **CRMA980** será executada, automaticamente, no momento em que for solicitada a chamada à rotina **MATA030**, a chamada via **ExecAuto/MSExecAuto** também não precisará ser alterada.

**Saiba Mais**

* **[How To | MP - SIGAFAT - Rotina MATA030 Descontinuada](https://youtu.be/aEY_Xk_wnCg)**
* **[MATA030 - Cadastro de Clientes - Descontinuada em 04/04/22](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=604230458)**
* **[DT Novo Fonte de Cadastro de Clientes em MVC](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=604230458)**
