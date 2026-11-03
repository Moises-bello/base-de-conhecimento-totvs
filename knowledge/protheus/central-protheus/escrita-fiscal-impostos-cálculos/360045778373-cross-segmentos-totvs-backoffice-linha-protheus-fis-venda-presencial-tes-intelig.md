---
article_id: 360045778373
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 134775c9d2937cb0d0fcd73afa5bd34eb189b8b846b4f1c884667e3c3e508f27
fetched_at: '2026-06-28T22:39:31.156197+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Venda Presencial -
  TES Inteligente
type: support-article
updated_at: '2021-07-29T13:09:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045778373-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Venda-Presencial-TES-Inteligente
---

**[Remover as instruções entre colchetes]**  
 **Dúvida**Solicitação para que na TES inteligente haja o campo "Venda Presencial = SIM/NÃO" para que possa ser tratado as vendas presenciais e não-presenciais referente o cálculo do Difal Partilha.   
  
Para o estado do Mato Grosso, o cadastro de TES de vendas presenciais são diferentes das TES de vendas não-presenciais, pois quando é uma operação interna no MT não é calculado o ICMS Próprio e quando é operação interestadual para fora do MT é calculado o IICMS próprio.  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**Esta solicitação não poderá ser atendida no sistema. Um dos campos que classifica a operação de venda presencial esta no cadastro da própria TES ( F4\_VENPRES) por isto ao fazer este tratamento teríamos uma referência circular.

Neste caso a recomendação é que sejam criados um tipo de operação para vendas presenciais e vinculado a TES que tem o campo F4\_VENPRES preenchido como SIM.
