---
article_id: 360041433234
category: TAF - REINF
content_hash: 513ddb6d0859bbb2972d99cf8973ea9c5fbc9de033931ec9a8aba6feaef978d9
fetched_at: '2026-06-28T22:41:33.618933+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Chave duplicada na tabela
  C5M
type: support-article
updated_at: '2023-03-31T17:00:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041433234-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Chave-duplicada-na-tabela-C5M
---

**Dúvida**Ao incluir informações referente a CPRB para geração do evento R-2060 é apresentado o erro de chave duplicada na tabela C5M, Como solucionar?

**Ambiente**  
TAF – TAF– A partir da versão 12  
  
**Solução**

 Acesse a rotina **APCFG110** no Configurador a numeração deverá estar conforme a imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055306574/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056173773/mceclip1.png)

Na área **Números em uso / Números liberados**, irá aparecer o que deverá ser o próximo número quando alguém incluir um novo registro CPRB, neste caso, **000003**.

Na área **Próximos números** será exibido o número subsequente na ordem, neste caso, **000004**.

Se por algum motivo, ao incluir um registro CPRB na rotina TAFA097, a próxima numeração não estiver sendo 000004, então você deve clicar 2 vezes no número que está em **Números em uso**, alterar para o que seria o próximo, e na área **Próximos números** inserir o subsequente correto. Com isso você redefine a ordem que o sistema de numeração automática deve seguir.

O processo acima deverá ser executado para a tabela C5M.

Informações Adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=269086104>

<https://tdn.totvs.com/pages/releaseview.action?pageId=309411140>
