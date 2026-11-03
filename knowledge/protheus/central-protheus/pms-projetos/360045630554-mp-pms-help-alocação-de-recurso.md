---
article_id: 360045630554
category: PMS - Projetos
content_hash: 3db74f34b1e22ae435fba84f751fadc3803aadf6ce5aa314b9c153a8e88ee9df
fetched_at: '2026-06-28T22:37:15.022976+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP - PMS - Help Alocação de Recurso
type: support-article
updated_at: '2021-04-29T21:12:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045630554-MP-PMS-Help-Aloca%C3%A7%C3%A3o-de-Recurso
---

**Ocorrência**

Sistema apresenta help abaixo quando informado somente recurso no projeto:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063972734/mceclip0.png)

**Ambiente**

Microsiga Protheus –  A partir da versão 12.1.17.  
   
 **Causa**

O campo Duracao Hrs. **AF9\_HDURAC**  esta em branco.  
   
 **Solução**

Para que na gravação da tarefa, caso seja informado **Recurso** para esta (tabela **AFA**) e o campo **AF9\_HDURAC** estiver zerado, sera apresentado **Help** informando a necessidade de preenchimento da duração. Preencha o campo Duracao Hrs. **AF9\_HDURAC** para prosseguir.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063972934/mceclip1.png)
