---
article_id: 360058115614
category: RH - Períodos de Apontamento
content_hash: bb55e96df67e698be23138baba2cbff69aaba68296e520c6fe3e5ace08945ae4
fetched_at: '2026-06-28T22:44:45.093995+00:00'
product: protheus
section_id: 32419304439959
source: central-protheus
title: RH - Linha Protheus - PON - Alteração de Período de Apontamento após ter efetuado
  leitura das marcações
type: support-article
updated_at: '2025-06-13T18:43:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058115614-RH-Linha-Protheus-PON-Altera%C3%A7%C3%A3o-de-Per%C3%ADodo-de-Apontamento-ap%C3%B3s-ter-efetuado-leitura-das-marca%C3%A7%C3%B5es
---

**Dúvida**Alteração de Período de Apontamento após ter efetuado leitura das marcações  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**É de extrema importância que antes de realizar a primeira Leitura/Apontamento do período, o usuário **confira se as datas inicial/final informadas no parâmetro MV\_PONMES** estão de acordo com a necessidade da empresa.   
Quando processamos a leitura, esses dados são gravados na tabela SP8 (Tabela de Marcações do Período) associados ao período de apontamento informado no parâmetro, ou seja, se por qualquer motivo houver necessidade de alterar as datas do período, os dados já estarão gravados com as datas do período antigo, então neste caso, a única forma de correção seria desprezar esses dados e efetuar a leitura do zero.  
Em casos onde a empresa trabalha com férias coletivas no final do ano ou precisa antecipar o fechamento do SIGAPON por qualquer motivo, é necessário validar qual será o período utilizado exatamente e só depois processar a leitura.  
  
Saiba mais:  
[MP - PON - Como trabalhar com um período de apontamento menor ou maior que 30 dias no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011060231-MP-PON-Como-trabalhar-com-um-per%C3%ADodo-de-apontamento-menor-ou-maior-que-30-dias-no-Ponto-Eletr%C3%B4nico?source=search)
