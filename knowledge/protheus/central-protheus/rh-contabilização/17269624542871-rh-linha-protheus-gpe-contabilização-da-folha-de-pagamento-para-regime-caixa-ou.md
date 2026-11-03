---
article_id: 17269624542871
category: RH - Contabilização
content_hash: b664d3d23005e214bf2408e1857a6fd8947662bb26194c09431a3399844df1a9
fetched_at: '2026-06-28T22:43:45.921525+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização da folha de pagamento para regime
  Caixa ou Competência
type: support-article
updated_at: '2025-07-22T20:53:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17269624542871-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-da-folha-de-pagamento-para-regime-Caixa-ou-Compet%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17269615301015) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Contabilização da folha de pagamento para regime Caixa ou Competência.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
  
**Solução**

Por padrão, o conceito de contabilização do Protheus é tratar como espelho da folha de pagamento os lançamentos contábeis, indiferente do regime da empresa.   
   
A contabilização fará a validação apenas das verbas que existem na folha de pagamento da competência selecionada na segunda janela da rotina GPEM110 (Miscelânea -> Fechamentos -> Contabilização): 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17282583754263).  
  
A rotina de contabilização também não filtra PROCESSOS. Desta forma uma vez selecionada a competência , em todos os processos com data de competência 01/2023 (seguinte o exemplo do print), todas as verbas que possuem lançamento padrão serão contabilizadas.   
  
**Saiba Mais:**  
[Página Centralizadora de Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
