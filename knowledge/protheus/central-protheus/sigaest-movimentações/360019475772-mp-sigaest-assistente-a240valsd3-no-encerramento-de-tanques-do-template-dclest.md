---
article_id: 360019475772
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 6ee1222589e1d96e87d4884326f0908a300663785c5ba9626349b96cb34a0197
fetched_at: '2026-06-28T22:38:54.192900+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST- Assistente A240VALSD3 no encerramento de tanques do template
  DCLEST
type: support-article
updated_at: '2021-04-28T15:45:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019475772-MP-SIGAEST-Assistente-A240VALSD3-no-encerramento-de-tanques-do-template-DCLEST
---

**Ocorrência**No módulo **Estoque/Custos** com template **DCLEST**, ao tentar realizar o encerramento de tanques é apresentado o assistente **A240VALSD3**. O que fazer para resolver?  
**Ambiente**Protheus – Estoque/Custos – A partir da versão 11.80.  
  
**Causa**O assistente é apresentado quando o cadastro do movimento interno de apuração (D3\_X\_TMT = AP) está configurado com o campo "**Valorizado (F5\_VAL)"** = Sim.  
  
**Solução**Os movimentos gerados pelo encerramento do tanque devem ser do tipo não valorizado para que o custo médio em estoque do produto não seja alterado. Dessa forma, o campo "**Valorizado (F5\_VAL)"** deve ser configurado como Não.

**OBS:** É importante validar também se a tabela SF5 não está compartilhada com outra empresa antes de se efetuar o ajuste na rotina MATA230 (Tipo de Movimentos)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
