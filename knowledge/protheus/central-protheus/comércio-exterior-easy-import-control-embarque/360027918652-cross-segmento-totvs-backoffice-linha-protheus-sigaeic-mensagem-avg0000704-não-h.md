---
article_id: 360027918652
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: e664a6ef8e6a1cec76da9b94c833533c2e16ff798c0299fc28e597eeeefb572d
fetched_at: '2026-06-28T22:39:48.739263+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem: "AVG0000704
  Não há itens a serem selecionados"'
type: support-article
updated_at: '2022-03-09T20:27:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027918652-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-AVG0000704-N%C3%A3o-h%C3%A1-itens-a-serem-selecionados
---

**Dúvida**O que verificar ao incluir o Embarque\Desembaraço e apresentar a mensagem: "AVG0000704 Não há itens a serem selecionados"?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028082631/mceclip0.png)  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Neste caso, a mensagem é apresentada devido a PO não ter saldo quantidade para inclusão de um Embarque\Desembaraço, sendo assim, acesse a rotina Purchase Order (EICPO400) e consulte se a PO informada no Embarque encontra-se com Saldo Qtde:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028083691/mceclip2.png)

No campo Qtde Embarcada é possível verificar a quantidade vinculada ao Embarque:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028083531/mceclip1.png)
