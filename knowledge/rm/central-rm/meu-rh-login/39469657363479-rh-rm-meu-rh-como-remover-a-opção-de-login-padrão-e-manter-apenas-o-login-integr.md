---
article_id: 39469657363479
category: Meu RH - Login
content_hash: e458dd2760692b6443bc98ffb4a2c160a2d80415d5ef50d07f34b3c01b80c8d0
fetched_at: '2026-06-28T22:47:27.197183+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Como remover a opção de login padrão e manter apenas o login
  integrado via Azure no Meu RH?
type: support-article
updated_at: '2026-04-06T10:58:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39469657363479-RH-RM-Meu-RH-Como-remover-a-op%C3%A7%C3%A3o-de-login-padr%C3%A3o-e-manter-apenas-o-login-integrado-via-Azure-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39469690124439) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como desabilitar o campo de usuário e senha no Meu RH, permitindo apenas o login pelo Azure?  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39469657350039)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.34  
  
**Solução**  
Atualmente, o portal Meu RH permite duas formas de acesso: o login nativo (usuário e senha do RM) e o login integrado via Azure. Caso deseje desabilitar a opção nativa e manter apenas a autenticação integrada, será necessário acrescentar a TAG  `<add key="ForceOauthLogin" value="true" />` no arquivo Web.config.

Realize os seguintes passos para este ajuste:

1. Acesse a pasta de instalação do portal Meu RH no servidor *(Ex: unidade:\TOTVS\CorporeRM\FrameHTML);*
2. Abra o arquivo **Web.config** com um editor de texto;
3. Localize a seção `<appSettings>` e adicione a linha abaixo: `<add key="ForceOauthLogin" value="true" />`
4. Salve o arquivo e reinicie o IIS para validação;

Ao acessar o Meu RH, será exibido apenas a opção para o login integrado via Azure.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39469690126487)

**Saiba Mais**

[Configurações de Login e Autenticação Meu RH](https://tdn.totvs.com/pages/viewpage.action?pageId=654103174)
