---
article_id: 360061922813
category: Rescisão
content_hash: df11c8bf2e5b43730938d6aa1e39a4032d3ebb16a59e1380596a520b01810a94
fetched_at: '2026-06-28T22:46:55.260257+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Código de Cálculo 48 sendo lançado indevidamente na rescisão
  comum acordo (Tipo V)
type: support-article
updated_at: '2021-06-18T16:55:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061922813-RH-RM-FOP-C%C3%B3digo-de-C%C3%A1lculo-48-sendo-lan%C3%A7ado-indevidamente-na-rescis%C3%A3o-comum-acordo-Tipo-V
---

**Dúvida**

Por que ao calcular rescisão (comum acordo) de um funcionário, é lançado o evento com [Código de Cálculo 48 - 13º Salário Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=452718487) [,](https://tdn.totvs.com/pages/viewpage.action?pageId=452718487) e não lança corretamente o evento com [Código de Cálculo 71 - 13º Salário Indenizado](https://tdn.totvs.com/pages/viewpage.action?pageId=452718484)?  
  
**Ambiente**

RM - Totvs Folha de Pagamento - Todas as versões  
  
**Solução**

Devido aos 2 eventos com códigos de cálculo 48 e 71 terem algumas tratativas semelhantes, é necessário avaliar a **Prioridade**. Se a prioridade do código de cálculo 48 for maior, ele será lançado no envelope, se for a prioridade do código de cálculo 71 maior, ele é que será lançado no envelope.   
  
**Para solucionar essa dúvida, veja as duas situações abaixo:**

**1º Situação:**

Ao calcular e lançar a rescisão comum acordo (tipo V) com o código de cálculo 48 com prioridade maior, o mesmo é lançado no envelope.  
  
**Código de Cálculo 48, prioridade 2:**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100396894/mceclip5.png)  
  
**Código de cálculo 71, prioridade 0:**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100396614/mceclip3.png)  
  
**No envelope é lançado o Código de Cálculo 48:**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100396854/mceclip4.png)  
  
**2º Situação:**Se alterar a prioridade do código de cálculo 71 para 10, que é maior que a prioridade do código de cálculo 48, o código de cálculo 71 será lançado no envelope.  
  
**Código de Cálculo 71, prioridade 10:**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102570193/mceclip0.png)  
  
**Código de Cálculo 48, prioridade 2:**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100396594/mceclip2.png)  
  
**O Código de Cálculo 71 é lançado no envelope:**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102570233/mceclip1.png)
