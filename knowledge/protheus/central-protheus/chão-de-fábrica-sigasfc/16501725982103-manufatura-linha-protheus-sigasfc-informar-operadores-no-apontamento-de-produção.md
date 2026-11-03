---
article_id: 16501725982103
category: Chão de Fábrica (SIGASFC)
content_hash: 418ddf9f02f8677e141275b1494ab8915a5c2d0021eab575e083beff12cc8328
fetched_at: '2026-06-28T22:42:49.867167+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Informar operadores no apontamento
  de produção
type: support-article
updated_at: '2023-08-07T17:13:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16501725982103-Manufatura-Linha-Protheus-SIGASFC-Informar-operadores-no-apontamento-de-produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16501705917207) Tempo aproximado para leitura: **00:00:47 min** **Dúvida**Como informar operadores no apontamento de produção nas rotinas de apontamento do **SIGASFC** - **Chão de Fábrica** ?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12  
  
**Solução**Para que seja possível informar operadores, é necessário que o centro de trabalho vinculado ao recurso que se deseja apontar, tenha o campo **CYI\_TPMOD - Reporte MOB** preenchido com **2 - Operador**, na rotina **SFCA001 - Centro de Trabalho.**  
Além disso, na rotina **SFCA002 - Máquina**, na aba **Recurso**, deve-se cadastrar os operadores vinculados ao recurso e que podem ser informados ou selecionados no apontamento de produção.
