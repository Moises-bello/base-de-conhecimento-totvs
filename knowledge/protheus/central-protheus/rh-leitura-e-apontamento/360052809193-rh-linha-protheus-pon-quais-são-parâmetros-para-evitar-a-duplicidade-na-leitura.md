---
article_id: 360052809193
category: RH - Leitura e Apontamento
content_hash: 83da48a87634fa3cbf58c40153fdf8d9c761c28b22776574af75e9f13b866ecd
fetched_at: '2026-06-28T22:44:46.002991+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Quais são parâmetros para evitar a duplicidade
  na Leitura e Apontamento
type: support-article
updated_at: '2025-08-07T17:55:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052809193-RH-Linha-Protheus-PON-Quais-s%C3%A3o-par%C3%A2metros-para-evitar-a-duplicidade-na-Leitura-e-Apontamento
---

**Dúvida**Quais são parâmetros para evitar a duplicidade na Leitura e Apontamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Seja a Leitura e Apontamento via rotina PONM010, via *Schedule ou* na Leitura com integração ao App Meu RH, temos 3 parâmetros que deverão estar preenchidos para evitar a duplicidade nas marcações.  
  
Segue abaixo os parâmetros, e nossa orientação de conteúdo em cada um deles:  
MV\_DESPMIN = 05 (irá desconsiderar marcações com até 5 minutos de igualdade)  
MV\_MCIGUAL = N (determina se permite ou não, gravar marcações iguais)  
MV\_MCIMPAR = S (despreza marcação que menos coincida ao padrão, quando houver imparidade)

**Informações complementares**Marcações Duplicadas? Como corrigir:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=274333684>

Documentação sobre o parâmetro MV\_MCIGUAL:   
<http://tdn.totvs.com/pages/releaseview.action?pageId=6082510>

Documentação sobre o parâmetro MV\_DESPMIN:  
[RH - Linha Protheus - PON - Funcionamento do MV\_DESPMIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403030035223-RH-Linha-Protheus-PON-Funcionamento-do-MV-DESPMIN?source=search)  
  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
