---
article_id: 34330806385047
category: SIGAEST - INTEGRAÇÕES
content_hash: 846b012c4ef82d6d499260e9551e5bcc110b39e976aab99c0594b698f5094049
fetched_at: '2026-06-28T22:38:46.177617+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Variable does not
  exist OAPP on PSWLOGIN(SIGAPSW.PRG)
type: support-article
updated_at: '2025-08-21T12:57:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34330806385047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Variable-does-not-exist-OAPP-on-PSWLOGIN-SIGAPSW-PRG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34330848328343) Tempo aproximado para leitura: 00**:03:00 min**  
  
**Ocorrência**  
Ao realizar uma integração via WebServices com o Protheus, após a migração para o Release 12.1.2410, o sistema está gerando o erro: variable does not exist OAPP on PSWLOGIN(SIGAPSW.PRG)  
  
**Ambiente**  
Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Causa**  
Conforme indicado pelo time de Framework da TOTVS, este erro pode ocorrer caso a chave "PREPAREIN" não esteja configurada no WebService. Esta chave informa a qual empresa/filial o Serviço esta vinculado.  
  
**Solução**  
Basta configurar o WebService a partir do wizard "SRVWIZARD" que o mesmo já criará o serviço com a chave, ou inserir a chave seguindo o exemplo da documentação:

* [Configurar Portais e Webservices](https://tdn.totvs.com/x/apk4E)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Integrações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
