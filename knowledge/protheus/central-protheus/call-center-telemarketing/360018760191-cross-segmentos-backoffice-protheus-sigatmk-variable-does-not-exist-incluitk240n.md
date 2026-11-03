---
article_id: 360018760191
category: Call Center - Telemarketing
content_hash: 02fe4ac0b2fd4b29dd40b9ce696031e63ad72d2e5f5ec9356a7bbdb8a72d0955
fetched_at: '2026-06-28T22:41:29.394294+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - variable does not exist INCLUI,TK240Nome
type: support-article
updated_at: '2024-04-25T14:40:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018760191-Cross-Segmentos-Backoffice-Protheus-SIGATMK-variable-does-not-exist-INCLUI-TK240Nome
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23052197936279) Tempo aproximado para leitura: 00:02:00 min****

**Ocorrência**

Ao incluir uma ação, gera o error.log : variable does not exist INCLUI on { ||IIF(!INCLUI,TK240Nome(),"")

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Causa**

O erro ocorre por que a validação IIF(!INCLUI,TK240Nome(),"") está no  **x3\_inibrw** do campo **UQ\_RESP**.

**Solução**

Para correção deste erro, retire a validação **IIF(!INCLUI,TK240Nome(),"")** que encontra-se o **x3\_inibrw** do campo **UQ\_RESP**, e coloque a informação no **x3\_relação** do campo em questão, desta forma, o erro deixará de ocorrer.

Outra opção, é fazer o download do dicionário de dados do portal do cliente relacionado a release utilizada e processar o **UPDDISTR** para que o dicionário de dados seja corrigido e fique conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409047396119)

**Obs**: O tratamento indicado na FAQ, requer conhecimento técnico de estrutura Protheus, caso necessite de apoio mais técnico, contate a equipe de Atendimento Framework.
