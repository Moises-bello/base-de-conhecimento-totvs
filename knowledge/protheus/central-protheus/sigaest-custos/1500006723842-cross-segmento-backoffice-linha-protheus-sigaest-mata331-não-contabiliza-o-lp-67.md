---
article_id: 1500006723842
category: SIGAEST - CUSTOS
content_hash: 25631a59ff85758953d57eff906dd8691620cd4c1a1f0c85b8b08eaf204b6a84
fetched_at: '2026-06-28T22:39:02.246103+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA331 - Não contabiliza
  o LP 678 O que fazer?
type: support-article
updated_at: '2025-03-12T12:23:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006723842-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA331-N%C3%A3o-contabiliza-o-LP-678-O-que-fazer
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30504062364567)** Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**

Ao efetuar a Contabilização do Custo Médio usando o Lançamento Padronizado 678, não está contabilizando Devolução de Compras e Devolução de Poder de Terceiros, o que fazer para ser contabilizado?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**Por padrão, no Lançamento Padronizado 678 é considerado apenas **P****edidos de Venda (MATA410) do tipo normal (D2\_TIPO = N)** com TES sem controlar poder de terceiro (F4\_PODER3 = N).

Caso o usuário queria que este Lançamento Padronizado 678 passe a considerar Devolução de Compra D2\_TIPO = D ou mesmo Devolução de Poder de Terceiros (com TES configurada com F4\_PODER3 = D), deve-se fazer uso do Ponto de Entrada **[A330CDEV](https://tdn.totvs.com/pages/releaseview.action?pageId=236427384)**, onde é possível determinar quais os movimentos de saída para o Protheus contabilizar no LP 678 além de vendas simples.

**Saiba mais:**

*[MP - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-MP-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)*
