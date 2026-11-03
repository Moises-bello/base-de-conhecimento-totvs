---
article_id: 360023820791
category: ADVPL - Classe e Função
content_hash: 6ef0f6551b0aa871d969f858e08415633113a13c172f3d5d4d39aaec8a89a362
fetched_at: '2026-06-28T22:40:14.081980+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus)  - ADVPL - Compilando um
  Relatório Modelo (Padrão)
type: support-article
updated_at: '2021-05-06T20:12:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023820791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Compilando-um-Relat%C3%B3rio-Modelo-Padr%C3%A3o
---

**Dúvida**Baixei do portal um Rdmake e preciso alterar o código fonte desse relatório, como compilar e executar?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Por padrão o Fonte vem como ***FUNCTION*** é necessário modificar todas as *function* para ***USER FUNCTION, depois é só compilar no RPO.***

A Rotina assumira esse novo relatório ou poderá ser executado pelo configurador.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021298591/mceclip0.png)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021298831/mceclip1.png)**

**Para execução pelo configurador**

Para incluir o relatório no menu, acesse o***Configurador > Ambiente > Cadastros > Menus***.  A partir desse ponto o processo é o mesmo para incluir uma nova rotina no menu. Selecione no campo tipo a opção ***Função de Usuário*** , depois no campo

Programa clique no botão ![Screenshot_10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018761332/Screenshot_10.png) para selecionar o relatório que deseja incluir no menu.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021285771/mceclip4.png)**

**Visualizando no menu do seu respectivo modulo**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021349992/mceclip3.png)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021287111/mceclip6.png)

**Saiba mais**[Personalização de menus](http://tdn.totvs.com/pages/viewpage.action?pageId=271164329)
