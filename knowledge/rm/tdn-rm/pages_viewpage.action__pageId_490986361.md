---
content_hash: d3040442d89fde3ce75cd11e3cf4f699f4f554178480db176364bdbf09eaaf26
fetched_at: '2026-06-29T00:10:21.320541+00:00'
page_id: '490986361'
product: rm
source: tdn-rm
title: Alteração de Contexto (Gestão Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490986361
version: 6
---

O módulo fiscal tem o contexto por filial e neste caso ao alterar a filial corrente o usuário precisa encerrar as telas abertas no contexto anterior. Esta regra será aplicada sempre que a alteração do contexto for referente a Coligada, Filial ou Exercício Fiscal.  
Foi modificado o processo de alteração de contexto para não permitir alterar a ***Coligada, Filial e  Exercícios** **Fiscal*** com telas do fiscal abertas. Será exibida uma mensagem ao usuário solicitando encerramento das telas que poderá ser de forma manual ou automática.

Exemplo: Telas de Lançamento Fiscal e Período de de Apuração:

* Realizada Troca de Filial:

* Trocando de Filial 1 para Filial 3

* Será exibida a seguinte mensagem:

 Ao clicar em **SIM** você concorda em fechar todas as telas pertinentes ao Gestão Fiscal abertas na filial atual.  
 Ao clicar em **NÃO** as telas do Gestão Fiscal não vão ser fechadas e a Filial não vai ser Alterada.

A mesma regra é válida para as trocas de **Coligada** e **Exercício Fiscal**.

**Importante!**

1. As telas de outros Módulos não serão fechadas.
2. O processo vai ter esse comportamento quando o usuário estiver no Módulo Gestão Fiscal

Para a Integração com TOTVS Gestão Estoque, Compras e Faturamento, deve ser configurado nas formulas do movimento para que esses valores sejam incluídos no conforme exemplo acima.

---
