---
article_id: 360053359054
category: Configurador
content_hash: da49eec1dc1d48f31b7d9cba308b2981408010b95ea2f9dbfe65b45c204e1343
fetched_at: '2026-06-28T22:42:18.951156+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Configuração Amazon SES-SMTP
type: support-article
updated_at: '2024-05-08T11:37:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053359054-Framework-Linha-Protheus-Configura%C3%A7%C3%A3o-Amazon-SES-SMTP
---

**Dúvida**Como efetuar a configuração do SMTP no Protheus usando o Amazon SES?  
  
**Ambiente**Protheus – Configurador – A partir da versão 12  
  
**Solução**  
Para configuração do SMTP no Protheus com **Amazon SES** efetue as seguintes configurações no **Amazon SES**:  
  
***Domain***:   
![Amazon-SES1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090988613)  
  
**Destinatário**, ele irá enviar apenas para o mesmo domínio, caso queira enviar para um e-mail de domínio diferente é necessário verificar este e-mail que pertence a outro domínio:  
![Amazon-SES2a.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090994593)  
  
É muito importante também o cliente verificar se ele não **excedeu** o limite de e-mails enviados, caso exceda ele pode contatar a **Amazon** para **aumentar** esse limite:  
![Amazon-SES3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090990193)

O cliente pode consultar as configurações do SMTP na tela a seguir, ele deve criar a credencia SMTP e realizar o download da mesma pois caso ele se esqueça do login e senha será necessário criar uma nova autenticação:  
![Amazon-SES4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088855074)  
  
![Amazon-SES10a.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088859554)  
  

Isso já é suficiente para enviarmos e-mails veja:  
![Amazon-SES11a.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090995013)  
  

As configurações no Protheus devem ficar da seguinte forma:

![Amazon-SES5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090990893)  
  
  
![Amazon-SES6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088855754)  
  
  
![Amazon-SES7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088855814)  
  

Seção mail appserver.ini:

[MAIL]

PROTOCOL=POP3

TLSVERSION=1

SSLVERSION=3

TRYPROTOCOLS=0

AUTHLOGIN=1

AUTHPLAIN=1

AUTHNTLM=1  
  

Validação do envio:  
![Amazon-SES8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088855834)  
  
![Amazon-SES9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088855954)  
  

O Protheus está funcional para envio através dessa ferramenta.
