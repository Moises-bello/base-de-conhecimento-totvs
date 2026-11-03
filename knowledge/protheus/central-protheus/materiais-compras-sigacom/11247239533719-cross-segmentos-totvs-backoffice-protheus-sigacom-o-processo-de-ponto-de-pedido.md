---
article_id: 11247239533719
category: Materiais - Compras (SIGACOM)
content_hash: d493c8a9d64c9a35beaee6888d38051c2ea93db4ec5e6ba2d4cb9c1a7300e96e
fetched_at: '2026-06-28T22:41:21.968545+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O processo de ponto
  de pedido leva em consideração a tabela SBZ?
type: support-article
updated_at: '2022-12-27T16:53:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11247239533719-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-processo-de-ponto-de-pedido-leva-em-considera%C3%A7%C3%A3o-a-tabela-SBZ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00min** **Dúvida**O processo de ponto de pedido leva em consideração a tabela SBZ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**Em analise verificando os fontes da rotina MATA170 (Solicitação por Ponto de Pedido) é possível identificar que a rotina valida o **MV\_ARQPROD**, como pode ser visto abaixo:  
![](https://totvssuporte.zendesk.com/attachments/token/vxIBh22pTCg44zTVOuZLQpAjL/?name=image.png)  
  
Levando isso em consideração entendemos que a rotina além de utilizar o campo B1\_EMIN a rotina utiliza também a BZ\_EMIN. Validando essa informação nos fontes mais recentes e nos fontes ate 2018 fica entendido que mesmo que o campo de ponto de pedido da tabela SB1 esteja zerado, caso na tabela SBZ esteja configurado a MATA170 gera o ponto de pedido normalmente.   
  
Fica então entendido verificando os fontes que esses campos são os únicos que a rotina verifica para realizar o calculo.

**Saiba mais:**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAEST - Como é calculado a quantidade à ser solicitada na rotina de solicitação por ponto de pedido ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028618332-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAEST-Como-%C3%A9-calculado-a-quantidade-%C3%A0-ser-solicitada-na-rotina-de-solicita%C3%A7%C3%A3o-por-ponto-de-pedido-)

**Pontos de entrada MATA170:** <https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408775373207-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-Solicita%C3%A7%C3%A3o-por-Ponto-de-Pedido-MATA170->
