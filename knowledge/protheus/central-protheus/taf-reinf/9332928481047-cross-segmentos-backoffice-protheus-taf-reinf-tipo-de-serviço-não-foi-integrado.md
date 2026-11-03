---
article_id: 9332928481047
category: TAF - REINF
content_hash: b9bfbe4b63e76b71893cb3f73cd10614ed21c372bd43fbf040ba0812c68f3349
fetched_at: '2026-06-28T22:41:34.877595+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Tipo de serviço não foi
  integrado no TAF mesmo com o cadastro na rotina MATA963
type: support-article
updated_at: '2023-04-04T12:06:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9332928481047-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Tipo-de-servi%C3%A7o-n%C3%A3o-foi-integrado-no-TAF-mesmo-com-o-cadastro-na-rotina-MATA963
---

**Dúvida**O que verificar quando a nota fiscal para os eventos R-2010/R-2020 não levou o tipo de serviço para o TAF, mesmo com o cadastro na rotina MATA963?  
  
**Ambiente**A partir de 12.1.27  
  
**Solução**

Verificar 3 possibilidades:

1 - Se o FT\_CODISS está preenchido com o código de serviço. Caso a nota tenha sido escriturada com esse campo vazio, o tipo de serviço não será levado.

2 - Se o FT\_CODISS gravou um código de serviço diferente do código que foi feito o cadastro na rotina MATA963.

3 - O campo FT\_CODISS possuir tamanho diferente do campo CDN\_CODISS. Os campos precisam ter o mesmo tamanho.
