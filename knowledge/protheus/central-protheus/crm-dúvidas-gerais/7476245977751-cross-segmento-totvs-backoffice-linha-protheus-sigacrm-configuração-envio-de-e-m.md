---
article_id: 7476245977751
category: CRM - Dúvidas Gerais
content_hash: 4120de43bf81f47cee178c065b6ead2a461d2b2e3b08f632308b6d3ff24baa40
fetched_at: '2026-06-28T22:40:27.607391+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACRM - Configuração
  envio de E-mail na Atividade (CRMA180)
type: support-article
updated_at: '2022-07-15T11:21:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7476245977751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACRM-Configura%C3%A7%C3%A3o-envio-de-E-mail-na-Atividade-CRMA180
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como configurar o envio de e-mails na rotina de Atividades (CRMA180)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACRM - Todas as versões  
  
**Solução**  
Passos para configuração:  
  
1- Configuração do Proxy do E-mail: [MP - FRAME - Configurar o SMTP para envio de relatórios por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025393071-MP-FRAME-Configurar-o-SMTP-para-envio-de-relat%C3%B3rios-por-e-mail)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7475380009623/mceclip3.png)  
  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7475381951255/mceclip4.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7475432772503/mceclip5.png)  
  
2- Configurar parâmetros:  
  
MV\_EXGAUT = 2  
MV\_RELACNT = Inclua o e-mail com domínio [user@empresa.com.br](mailto:user@empresa.com.br)  
MV\_RELAPSW = senha do e-mail  
MV\_EMCONTA = Inclua o e-mail com domínio [user@empresa.com.br](mailto:user@empresa.com.br)  
MV\_EMSENHA = senha do e-mail  
MV\_RELAUTH = .T.  
MV\_RELFROM = user@empresa.com.br (Quando é utilizado um servidor autenticado, não é permitido enviar mensagens com o campo "FROM" de outra conta)  
MV\_RELPSW = senha do e-mail  
MV\_RELSSL = .F.  
MV\_RELTLS = .T. 

3-  Informe o e-mail no usuário do sistema no Configurador SIGACFG:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7474860558871/mceclip0.png)

3- Informe o e-mail no campos "Usuario Exc" (AO3\_EXGUSR) e "E-mail" (AO3\_EXGEMA), no módulo 73 (SIGACRM) na rotina "Usuário CRM" (CRMA210)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7474997740567/mceclip2.png)

Exemplo de envio de e-mail:  
  
![20220714_155359.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7475900866327/20220714_155359.gif)

Esta trata-se da configuração para o envio de e-mails, não recebimento.   
  
**Observação**: A rotina Atividade é preparada para integrar o envio e recebimento de e-mails, compromissos ou tarefas para servidor no Exchange da Microsoft:  
[Integração do Cadastro de Atividades com Exchange Server](https://tdn.totvs.com/x/7kFBE)  
[Integração do Cadastro de Atividades com Exchange Online ( Office 365 )](https://tdn.totvs.com/x/sedeE)
