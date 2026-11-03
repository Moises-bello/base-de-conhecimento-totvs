---
article_id: 360028793851
category: ADVPL - Classe e Função
content_hash: e1d527b8deeb9d1bd011a67e35d405c50efb1d9dab618dbd6404db5a4cdd1a47
fetched_at: '2026-06-28T22:40:15.792914+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro ao conectar
  em servidor de e-mail utilizando os protocolos SMTP, POP3 ou IMAP
type: support-article
updated_at: '2022-03-09T19:17:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028793851-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-ao-conectar-em-servidor-de-e-mail-utilizando-os-protocolos-SMTP-POP3-ou-IMAP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao tentar conectar em um servidor de e-mail utilizando os protocolos SMTP, POP3 ou IMAP é gerado erro abaixo:

```
Erro de conexão: Aborted by User
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**Este erro ocorre porque a classe TMailManager() tenta realizar a conexão por meio dos protocolos acima listados com a versão SSL incorreta.  
  
**Solução**Adicionar a chave SSLVERSION na seção *MAIL* do arquivo \*.INI do *Application Server*.  
  
**Observação**  
É necessário que as permissões de conexão para os protocolos desejados esteja habilitada em seu servidor de e-mail.  
  
**Saiba mais**  
[Correção - TMailManager não conecta em contas do Office 365](http://tdn.totvs.com/pages/viewpage.action?pageId=187534851)  
[SSLVersion](http://tdn.totvs.com/display/tec/SSLVersion)
