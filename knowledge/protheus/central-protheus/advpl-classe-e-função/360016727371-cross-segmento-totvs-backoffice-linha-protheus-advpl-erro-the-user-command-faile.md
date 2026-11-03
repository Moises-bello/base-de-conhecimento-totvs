---
article_id: 360016727371
category: ADVPL - Classe e Função
content_hash: 2ebfeffc7057db1d927f1e2cf69ca44e08413e497f9bb7596d831d63f5e61ce6
fetched_at: '2026-06-28T22:40:20.713391+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: The USER
  command failed'
type: support-article
updated_at: '2022-01-03T19:48:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016727371-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-The-USER-command-failed
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Durante o envio de e-mails pelo Protheus, de maneira intermitente está sendo retornado o erro abaixo:

```
The USER command failed.
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Causa**Quando intermitente, o erro caracteriza-se pela falta de conexão com o servidor de e-mails.

Quando reincidente sequencialmente (aconteça diversas vezes seguidas sem resultado positivo), o erro terá relação com a função de envio de *e-mail* e binários desatualizados  
  
**Solução**Quando o erro ocorra esporadicamente, deve se verificar se momento das falhas o servidor não passou por alguma instabilidade.

Caso o erro tenha reincidência sequencial, deve ser identificada a função de envio de *e-mail* e atualizado os binários de *SmartClient* e *Application Server* (*AppServer*).  
  
**Importante**  
Caso esteja utilizando servidores de e-mail providos pelo GMail, torna-se necessária a adição das seguintes chaves na seção [MAIL]:

```
[MAIL]  
AUTHLOGIN = 1  
AUTHNTLM  = 1  
AUTHPLAIN = 1
```

**Saiba mais**  
[Mudança de comportamento - Autenticação SMTP](http://tdn.totvs.com/pages/viewpage.action?pageId=6065276)
