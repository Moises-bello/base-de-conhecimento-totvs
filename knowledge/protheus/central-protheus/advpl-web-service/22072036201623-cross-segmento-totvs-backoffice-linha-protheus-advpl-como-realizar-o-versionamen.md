---
article_id: 22072036201623
category: ADVPL - Web Service
content_hash: 01b0d06dfe0da714e959e474fa2142c3eabf8938fc138fbd02bb33741b940f0e
fetched_at: '2026-06-28T22:40:10.527907+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- Como realizar o versionamento
  em API´s Rest?
type: support-article
updated_at: '2024-03-14T17:21:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22072036201623-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-realizar-o-versionamento-em-API-s-Rest
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22072055517463) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Quais os erros comuns do Printer.exe?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

As APIs devem ser versionadas sempre que alguma alteração quebrar o contrato entre o usuário e a plataforma, a versão deve estar presente na URI e deve estar no forma v{major.minor}.  
A versão major indica uma grande versão da API, ou seja, a API mudou significativamente em seu formato e comportamento.  
A versão minor indica uma alteração que pode quebrar o código do cliente.

Por exemplo:

http://totvs.com/api/fluig/fdn/v1/users  
http://totvs.com/api/fluig/fdn/v1.5/users  
http://totvs.com/api/fluig/fdn/v2/users

**Saiba Mais**

[Guia Implementação de API´s Totvs](https://tdn.totvs.com/display/public/INT/Guia+de+implementacao+das+APIs+TOTVS#GuiadeimplementacaodasAPIsTOTVS-Versionamento)
