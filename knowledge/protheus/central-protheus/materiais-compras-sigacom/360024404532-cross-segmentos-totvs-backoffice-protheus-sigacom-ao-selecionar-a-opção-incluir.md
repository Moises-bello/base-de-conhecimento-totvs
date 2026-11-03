---
article_id: 360024404532
category: Materiais - Compras (SIGACOM)
content_hash: aaf76747b94608ebba439e395f2aeb6a37dd861cab3e7215ce6663572ae9c7ab
fetched_at: '2026-06-28T22:41:07.453600+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao selecionar a opção
  incluir no pedido de compras, o sistema apresenta help A120COMP
type: support-article
updated_at: '2026-01-16T13:57:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024404532-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-selecionar-a-op%C3%A7%C3%A3o-incluir-no-pedido-de-compras-o-sistema-apresenta-help-A120COMP
---

**Ocorrência**

Ao selecionar a opção incluir no pedido de compras, o sistema apresenta help A120COMP.

**Ambiente**

Microsiga Protheus – Compras – A partir da versão P12.1.2210

**Causa**

Esse incidente ocorre, pois, um usuário Não Cadastrado como Comprador Tenta Incluir um Pedido de Compras quando o parâmetro MV\_RESTINC = S.

**Solução**

**1.** Com o parâmetro MV\_RESTINC = S apenas usuários cadastrados como Compradores podem Incluir Pedido de Compras. Dessa forma o usuário que está realizando processo necessita ser cadastrado como Comprador, na rotina de Compradores.

Caso o usuário possa ser Cadastrado como Comprador valide também o campo  'Ped s/ SC' (SY1->Y1\_PEDIDO) e configure conforme sua necessidade na Rotina COMA087 - Cadastro de Compradores.

**2.** Caso ele não possa ser Cadastrado como Comprador deve-se verificar a configuração do parâmetro MV\_RESTINC, desabilitando-o (MV\_RESTINC = N).

***Obs:***

Este Help A120COMP também pode Ocorrer na rotina de Medição (***CNTA121***), ao ser encerrada uma medição que gera Pedido de Compras, ou na rotina de Liberação de Documentos (***MATA094***) ao Aprovar a alçada de uma Medição, quando se está configurado para encerrar a medição (e gerar Pedido de Compras) ao ser liberada a sua alçada ([MV\_CNMDEAT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009301161-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-MV-CNMDEAT-Como-realizar-o-Encerramento-Autom%C3%A1tico-de-Uma-Medi%C3%A7%C3%A3o-na-Libera%C3%A7%C3%A3o-de-Al%C3%A7adas)).

***Saiba Mais :***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Restringir a Inclusão de Pedidos Apenas para Usuários Compradores](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23687885851927?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao salvar o pedido de compras, o sistema apresenta help A120RESTR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4500895030039-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-salvar-o-pedido-de-compras-o-sistema-apresenta-help-A120RESTR?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O que é o Cadastro de Compradores MATA087 / COMA087 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024650292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-%C3%A9-o-Cadastro-de-Compradores-MATA087-COMA087?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - MV\_CNMDEAT - Como realizar o Encerramento Automático de Uma Medição na Liberação de Alçadas ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009301161-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-MV-CNMDEAT-Como-realizar-o-Encerramento-Autom%C3%A1tico-de-Uma-Medi%C3%A7%C3%A3o-na-Libera%C3%A7%C3%A3o-de-Al%C3%A7adas)
* [PÁGINA CENTRALIZADORA COMPRAS](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
* [Mais Artigos Materiais - Compras (SIGACOM)Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
