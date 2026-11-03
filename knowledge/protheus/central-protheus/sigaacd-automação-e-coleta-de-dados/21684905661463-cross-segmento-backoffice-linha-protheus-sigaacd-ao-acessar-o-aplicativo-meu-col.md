---
article_id: 21684905661463
category: SIGAACD - Automação e Coleta de Dados
content_hash: c765a19bb38d3c3744df7ec08521a5c29f7e97438e9fa9428cb7a80d309a9fad
fetched_at: '2026-06-28T22:39:11.118472+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD -  Ao acessar o aplicativo
  Meu Coletor de Dados apresenta erro de Operador não cadastrado ou usuário e senha
  invalida, o que fazer?
type: support-article
updated_at: '2025-02-25T18:46:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21684905661463-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Ao-acessar-o-aplicativo-Meu-Coletor-de-Dados-apresenta-erro-de-Operador-n%C3%A3o-cadastrado-ou-usu%C3%A1rio-e-senha-invalida-o-que-fazer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21684888852759)  Tempo aproximado para leitura: **00:01:00 min****Dúvida**  
Ao acessar o aplicativo Meu Coletor de Dados apresenta erro de Operador não cadastrado ou usuário e senha invalida, o que fazer?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

Para que não ocorra esses erros ao acessar o aplicativo Meu Coletor de Dados favor seguir os passos abaixo:

1. Revisar a Configuração no Appserver.ini nas chaves referentes ao REST do Meu Coletor de dados conforme nossa documentação abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Configuração do REST Mobile](https://tdn.totvs.com/pages/releaseview.action?pageId=519719292)

Observação importante: Exclusivamente para o aplicativo Meu Coletor de Dados, é necessário incluir a chave MODULE na seção HTTPURI:

**`[HTTPURI]`**

**`Module=46`**

2. Revisar o Operador e vincular ao usuário que irá ter acesso ao aplicativo: detalhes abaixo:

2. 1 Acessar SIGACFG, entrar no cadastro de usuário através do caminho: Usuário > Senhas > Usuários e incluir o novo usuário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21684888854551)

2. 2 Acessar o módulo de Estoque e Custo e faça a seguinte seleção no menu:  **Menu > Atualizações > ACD> Operadores**e selecionar no campo operador o usuário cadastro no passo anterior ou um usuário existente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21684905648535)

3. Avalie se esse usuário tem acesso ao módulo 46 no configurador, pois é requisito necessário.

Acesse o Configurador e faça a seguinte seleção no menu: **Menu > Usuários > Senhas > Usuários > Selecione o usuário e clique em alterar > Restrições de acesso > Ambientes > Módulo 46 - SIGAACD:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21684888859415)

**Observação**: Se o usuário não tiver acesso ao módulo e quando for logar no aplicativo "Meu coletor de Dados", não irá conseguir se autenticar.

4. Se mesmo assim persistir, revise se o mesmo está na sua ultima versão e limpe os dados do aplicativo no seu celular.

5. Faça o login e senha do usuário Protheus que esteja vinculado como Operador conforme o item 2:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21684888861335)

7. Ao fazer a autenticação, poderá avaliar qual processo abaixo deseja prosseguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21684888862999)

8. Para validação de como é feito cada processo no aplicativo Meu Coletor pode avaliar na nossa guia de referencia:

# [Meu Coletor de Dados : Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=506994322)

***Saiba mais:***

[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
