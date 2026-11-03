---
content_hash: 3e62688290b79c9876d5e4c43f6fd43f3e3a4e7dd7a67e228950e6d384bb0abb
fetched_at: '2026-06-29T00:11:27.428703+00:00'
page_id: '725282359'
product: rm
source: tdn-rm
title: Cancelar Associação de Cenários de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=725282359
version: 2
---

Este processo tem como objetivo excluir toda a estrutura de cenário de cálculo vinculados a um grupo de patrimônios.

São executados os seguintes passos:

* Exclui a estrutura contábil da amarração entre Grupo de Patrimônio e Cenário de Cálculo - default evento contábil e default cenário de cálculo
* Exclui o grupo de contas vinculado ao cenário de cálculo
* Exclui cálculos de depreciação dos patrimônios envolvidos no processo(que são vinculados ao grupo).
* Exclui estruturas de taxa de depreciação, saldos, cálculos, moedas e índices.

Para que o processo seja executado as seguintes regras são aplicadas:

* Cenário com início de vigência anterior ao período de cálculo atual, não pode ser desassociado
* É necessário o fechamento de período para execução do processo
* Não devem existir operações patrimoniais vinculadas ao cenário/grupo de contas no período de cálculo atual
* Não devem existir contabilizações no período de cálculo atual para o cenário de cálculo selecionado
