---
article_id: 360029183931
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: bef35e9a1b1a8cda84fd428d7cafc2d4f9b9e9679caf4b4bdc2da3b6998605c6
fetched_at: '2026-06-28T22:47:29.594054+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Erro HTTP 404 Not Found
type: support-article
updated_at: '2025-02-10T18:15:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029183931-RH-RM-Meu-RH-Erro-HTTP-404-Not-Found
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:00:22 min**

**Ocorrência**

Ao acessar o Meu RH via desktop ocorre o erro: HTTP 404 Not Found.**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.18  
  
**Causa**Falta de parametrizações no web.config do Meu RH.  
  
**Solução**Para corrigir o erro, veja os passos abaixo:  
  
**01.** Acesse **c:\totvs\CorporeRM\FrameHTML;  
02.** Edite o arquivo **web.config**;  
**03.** Altere a tag **RMRoutePrefix**. Veja o exemplo:

```
ANTES:  <add key="RMRoutePrefix" value="" />  
DEPOIS: <add key="RMRoutePrefix" value="RM" />
```

**04.** Após aplicar as alterações, reinicie o Host e tente novamente o acesso via Desktop.
