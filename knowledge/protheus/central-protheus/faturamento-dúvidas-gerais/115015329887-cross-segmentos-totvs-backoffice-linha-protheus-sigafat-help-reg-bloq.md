---
article_id: 115015329887
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 62222e0fdc63aab8b02609a5d511ace6f2274b926b6fef2dfa014c38078946e5
fetched_at: '2026-06-28T22:38:30.105089+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT-Help REG BLOQ
type: support-article
updated_at: '2022-07-05T12:23:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015329887-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-REG-BLOQ
---

**Ocorrência**

Ao inserir um orçamento e informar o código do produto, o sistema está validando o tipo de saída padrão, mesmo quando este campo não está preenchido no cadastro do produto.

**![](https://totvssuporte.zendesk.com/attachments/token/DszbRYBJZ2kRXWA948h5at1LW/?name=inline2075753073.png)**  
**Causa**

Por padrão sistêmico, o orçamento sempre sugere uma TES de uso padrão através do parâmetro MV\_TESSAI.

Ocorre que neste caso, o TES utilizado no parâmetro MV\_TESSAI está bloqueado e com isso, quando insere o produto já gera a mensagem de bloqueio.  
  
**Ambiente**  
  
Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- versão 11 e versão 12  
  
**Solução**  
  
Para corrigir, acerte o TES no parâmetro MV\_TESSAI para uma TES que esteja desbloqueado ou desbloqueie o TES que está sendo utilizado no parâmetro.

Saiba mais: [REGBLOQ - Problema: Este registro está bloqueado para uso](http://tdn.totvs.com/pages/viewpage.action?pageId=335348440)
