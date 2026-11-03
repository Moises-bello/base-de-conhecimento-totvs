---
article_id: 29363738155031
category: SIGAEST - LEGAIS
content_hash: bd15e2d1149d89ce4ce0014b0ba5f70b69ef6793cafd3a2378925ee9fb81e9ba
fetched_at: '2026-06-28T22:38:51.595959+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Ao executar
  o relatório MATC300 é gerado errorlog: InterFunctionCall: cannot find function TOTVS.FRAMEWORK.CSS.GETNEWWEBAPPTHEME'
type: support-article
updated_at: '2025-03-12T12:27:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29363738155031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Ao-executar-o-relat%C3%B3rio-MATC300-%C3%A9-gerado-errorlog-InterFunctionCall-cannot-find-function-TOTVS-FRAMEWORK-CSS-GETNEWWEBAPPTHEME
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29363738138263) Tempo aproximado para leitura: 00**:01:00 min****Ocorrência**Ao executar o relatório de Diagnóstico do Bloco K (MATC300) é gerado o errorlog: **"InterFunctionCall: cannot find function TOTVS.FRAMEWORK.CSS.GETNEWWEBAPPTHEME",** o que fazer para corrigir?  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Esse cenário ocorre quando a LIB do sistema esteja inferior á 01/07/2024, pois caso esteja com a LIB inferior, o fonte TOTVS.FRAMEWORK.CSS.GETNEWWEBAPPTHEME ainda não estava disponível e com isso pode gerar errorlog:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29363738140567)

Conforme documentação abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=844248713>

**Solução**

Para esse cenário sugerimos que atualize sua LIB com a última versão do portal do cliente, realizando o teste primeiro na base de homologação antes de passar para a base de produção:

<https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFLIB/search/searchAll>

**Saiba mais:**

***[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)***
