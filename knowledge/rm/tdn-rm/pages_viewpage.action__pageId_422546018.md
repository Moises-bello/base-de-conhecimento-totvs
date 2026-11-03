---
content_hash: 843fcefddd4194e1895e234aba173365655d41494ccaf408f2375f46d04b362e
fetched_at: '2026-06-29T00:09:22.732653+00:00'
page_id: '422546018'
product: rm
source: tdn-rm
title: Compensação do Prejuízo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546018
version: 4
---

Por esta opção, o usuário deverá cadastrar as Compensações do Prejuízos Fiscais para as diversas situações de tributação do IRPJ. Devera lançar manualmente o mês e o valor a compensar de cada tipo de prejuízo neste mês. Estes valores serão utilizados pelo sistema no momento da apuração do imposto.  
Já está disponível o processo de Automação de Lançamentos - Lalur B.

**Regra de Compensação do Tributo**

O valor do grupo compensação do tributo foi tratado para que não ultrapasse o valor do imposto a pagar.

* Caso parametrizado no Item do Evento Tributário as origens Contábil ou Natureza será verificado se o valor processado ultrapassa o valor do imposto a pagar, se sim o valor processado do Item será reduzido.
* Não será permitido Encerrar período com Lançamento Lalur B ou Lançamento Manual do Grupo de compensação do Tributo cujo o valor processado ultrapasse o valor do imposto.
