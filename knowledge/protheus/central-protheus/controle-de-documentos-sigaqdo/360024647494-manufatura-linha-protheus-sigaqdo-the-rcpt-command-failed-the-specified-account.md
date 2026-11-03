---
article_id: 360024647494
category: Controle de Documentos (SIGAQDO)
content_hash: debf66edc6a7fd07e43327b817ec72413ccd4a9ebbcc9216f334559f739aa3db
fetched_at: '2026-06-28T22:42:29.937466+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - The RCPT command failed. The specified
  account does not exist
type: support-article
updated_at: '2021-05-28T13:15:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024647494-Manufatura-Linha-Protheus-SIGAQDO-The-RCPT-command-failed-The-specified-account-does-not-exist
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:50 min**  
**Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao realizar a distribuição do documento na rotina **QDOA110 - Distribuição** ocorre a mensagem **The RCPT command failed. The specified account does not exist**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esta mensagem ocorre quando o domínio especificado no *e-mail* do usuário no campo **End. E-mail** na rotina **QAXA010 - Responsáveis/Usuários**, difere do especificado no parâmetro **MV\_RELSERV - Nome do Servidor de Envio de E-mail utilizado nos relatórios**.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se o domínio está correto no parâmetro **MV\_RELSERV**;  
2. Altere o campo **End. E-mail** da rotina **QAXA010** para um **e-mail** válido.
