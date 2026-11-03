---
article_id: 34876209418519
category: Meu RH - Login
content_hash: 904613158fa1b0e9d41c64afa801565c515f582564396ee2e0ee0e34bab781bf
fetched_at: '2026-06-28T22:47:27.238664+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Loop ao realizar login no Meu RH integrado com o Azure
type: support-article
updated_at: '2026-01-16T15:17:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34876209418519-RH-RM-Meu-RH-Loop-ao-realizar-login-no-Meu-RH-integrado-com-o-Azure
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34876218173719) Tempo aproximado para leitura: **00:02:19 min**  
  
**Ocorrência**  
Ao realizar o login integrado com o Azure no Meu RH, ocorre um loop de autenticação, no qual a tela de login é reaberta repetidamente após a inserção das credenciais.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34890926957591)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
O problema ocorre devido à configuração de cabeçalhos adicionais no IIS, que bloqueiam a comunicação necessária entre o Meu RH e o Microsoft Azure durante o processo de autenticação.

Cabeçalhos que causam o erro:  
  
***\* Cross-Origin-Opener-Policy***  
***\* Cross-Origin-Resource-Policy***  
***\* Strict-Transport-Security***  
***\* Referrer Policy***  
  
**Solução**  
Para corrigir o erro de loop no login, é necessário remover esses cabeçalhos dos sites **FrameHTML** e **Default Web Site** no IIS.  
  
1. No servidor do Portal, abra o **IIS** (Internet Information Services).  
2. Selecione o **Default Web Site** > **Cabeçalhos de respostas**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34876209403927)  
  
3. Remova os cabeçalhos que impedem a comunicação.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34876209404311)

4. Faça o mesmo processo de remoção no site **FrameHTML**.

5. Reinicie todos os serviços **Host** e, em seguida, reinicie o **IIS** para aplicar as alterações.

**Saiba mais**

[**RH - RM - Meu RH - Integração OAuth2, Meu RH X Azure**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418231971991-RH-RM-Meu-RH-Integra%C3%A7%C3%A3o-OAuth2-Meu-RH-X-Azure)
