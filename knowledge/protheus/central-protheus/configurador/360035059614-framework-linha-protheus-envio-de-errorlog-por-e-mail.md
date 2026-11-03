---
article_id: 360035059614
category: Configurador
content_hash: ffa46f242a080780224cdefb5ef58fb7be108007579d1e96004be8bc9d70bc0a
fetched_at: '2026-06-28T22:42:19.281598+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus - Envio de error.log por e-mail
type: support-article
updated_at: '2024-05-08T11:49:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035059614-Framework-Linha-Protheus-Envio-de-error-log-por-e-mail
---

**Dúvida**Como configurar o envio de error.log por e-mail?  
   
 **Ambiente**Protheus - Configurador - A partir da versão 11  
**Solução**O envio de **error.log por e-mail** utiliza as mesmas configurações de **E-mail/Proxy** para enviar os e-mails:  
[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025393071](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025393071-MP-FRAME-Configurar-o-SMTP-para-envio-de-relat%C3%B3rios-por-e-mail)  
  
Além da configuração de **E-mail/Proxy**, deve-se executar os seguintes passos:  
1. Acessar Configurador > Usuários > Senhas > Política > Aba Outros > **Aba Parâmetros**, e definir a opção "Habilita log de erro por e-mail" como **"Sim".  
  
![Erro1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046407413)**2. Acessar Configurador > Ambientes > Cadastros > Parâmetros e configurar o e-mail que vai receber os error.log nos parâmetros **MV\_LOGMAIL** e **MV\_LOGTT**.  
  
![Erro2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046407913)  
  
![Erro3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045551554)
