---
article_id: 360038197733
category: Ativo Fixo - Tabelas, Parâmetros, Campos .Gatilho
content_hash: 14060711c94c9f919a926f8481c696129429d7c415d646d30fd02c33e21410c2
fetched_at: '2026-06-28T22:41:50.325964+00:00'
product: protheus
section_id: 1500001536201
source: central-protheus
title: MP - SIGAATF - ATFA036 - Parâmetro MV_ATFRTBX
type: support-article
updated_at: '2021-04-28T21:54:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038197733-MP-SIGAATF-ATFA036-Par%C3%A2metro-MV-ATFRTBX
---

**Dúvida**Gostaria de saber qual o conceito atual do parâmetro **MV\_ATFRTBX?**  
   
 **Ambiente**A partir da versão 11.80  
  
**Solução**O parâmetro **MV\_ATFRTBX** é considerado apenas até a versão 11 do Protheus, e está na **SX6** da release 12 devido ao legado.

Este tem na P11 a função de definir qual a rotina de baixa será utilizada no sistema, podendo ser a **ATFA030** ou a **ATFA035**. Segue a Definição do parâmetro:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050370653/mceclip2.png)

A diferença entre as rotinas ATFA030 e ATFA036 pode ser verificada no link: [ATFA030 e ATFA035](https://tdn.totvs.com/pages/releaseview.action?pageId=113803735)

A rotina de **baixa correta na release 12 é a ATFA036**, pois segue os conceitos em MVC e a ATFA030(da P11) foi descontinuada nessa release. Abaixo segue a documentação desta rotina:   
[MP - SIGAATF - BAIXA DE ATIVO - ATFA036](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018556171-MP-SIGAATF-BAIXA-DE-ATIVO-ATFA036?source=search)

**Veja mais:**

[MP-SIGAATF-ATFA036-AJUSTE-ROTINA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006606032-MP-SIGAATF-ATFA036-AJUSTE-ROTINA)
