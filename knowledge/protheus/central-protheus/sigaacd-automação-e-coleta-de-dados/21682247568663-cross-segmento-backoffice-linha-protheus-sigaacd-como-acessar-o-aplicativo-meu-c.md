---
article_id: 21682247568663
category: SIGAACD - Automação e Coleta de Dados
content_hash: df9bf02f2c7712f65d036619ad81c64bfbe861951adfd20d9452b5dbb4ca5ddb
fetched_at: '2026-06-28T22:39:12.526363+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como acessar o aplicativo
  Meu Coletor de Dados ?
type: support-article
updated_at: '2025-03-12T12:45:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21682247568663-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-acessar-o-aplicativo-Meu-Coletor-de-Dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21682247546519) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como posso acessar o aplicativo Meu Coletor de Dados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

Para acessar o aplicativo Meu Coletor de Dados até a autenticação do Usuário basta seguir os passos abaixo:

1. Configurar no Appserver.ini o REST do Meu Coletor de dados conforme nossa documentação  abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Configuração do REST Mobile](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043179314-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configura%C3%A7%C3%A3o-do-REST-Mobile)

2. Cadastre um operador e vincule ao usuário que irá ter acesso ao aplicativo, para incluir siga os passos abaixo:

2. 1 Acessar SIGACFG entrar no cadastro de usuário através do caminho: Usuário > Senhas > Usuários e incluir o novo usuário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21684394733591)

2. 2 Acessar o módulo de Estoque e Custo e faça a seguinte seleção no menu:  **Menu > Atualizações > ACD> Operadores**e selecionar no campo operador o usuário cadastro no passo anterior ou um usuário existente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21684342373783)

3. Avalie se esse usuário tem acesso ao módulo 46 no configurador, pois é requisito necessário.

Acesse o Configurador e faça a seguinte seleção no menu: **Menu > Usuários > Senhas > Usuários > Selecione o usuário e clique em alterar > Restrições de acesso > Ambientes > Módulo 46 - SIGAACD:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21682754414615)

**Observação**: Se o usuário não tiver acesso ao módulo e quando for logar no aplicativo "Meu coletor de Dados", não irá conseguir se autenticar.

4. Baixar o aplicativo Meu Coletor de Dados em sua loja de Aplicativo.

**OBS:**O aplicativo suporta versões dos Android 11 ou superiores. Mais detalhes em: [Pré-requisitos](https://tdn.totvs.com/pages/releaseview.action?pageId=465385584)

Caso o dispositivo não seja compatível, validar a documentação: [Incompatibilidade de Versão no App Meu Coletor de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21013430753943-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Incompatibilidade-de-Vers%C3%A3o-no-App-Meu-Coletor-de-Dados)

5. Configurar o REST do Protheus no Aplicativo  conforme documentação citada abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Configuração do REST Mobile](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043179314-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configura%C3%A7%C3%A3o-do-REST-Mobile)

6. Faça o login e senha do usuário Protheus que esteja vinculado como Operador conforme o item 2:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21682947481111)

7. Ao fazer a autenticação, poderá avaliar qual processo abaixo deseja prosseguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21683194489751)

8. Para validação de como é feito cada processo no aplicativo Meu Coletor pode avaliar na nossa guia de referencia:

# [Meu Coletor de Dados : Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=506994322)

***Saiba mais:***

[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
