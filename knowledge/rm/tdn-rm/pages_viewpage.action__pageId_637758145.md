---
content_hash: 2d2672de0e2f11f076d555fab4f53f7684fbd72e80f70274f3bead2a80a5b2a0
fetched_at: '2026-06-29T00:11:06.943942+00:00'
page_id: '637758145'
product: rm
source: tdn-rm
title: Página de Login
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=637758145
version: 15
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Atualização versão**
4. **Seletor de alias**

4.1. **Configuração multi-tenancy**

1. **Recuperação de senha**

Página de LoginVisão Geral

## **01. VISÃO GERAL**

Esta tela tem como objetivo identificar o profissional que irá acessar o Prontuário Eletrônico através de login e senha e fornecer acesso as funcionalidades que possui permissão para uso.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

## **02.1 - Usuário com acesso ao sistema**

Para acessar o sistema é necessário digitar o login e senha e em seguida apertar o botão entrar.

Caso o usuário digitado possua permissão de acesso será redirecionado para a .

## **02.2 - Usuário sem acesso ao sistema**

Caso o usuário não possua permissão de acesso ou não esteja vinculado a um prestador será direcionado para a tela abaixo:

## **02.3 - Tentativa de acesso com informações inválidas**

Caso o usuário digite informações inválidas de login ou senha, uma mensagem de erro será exibida ao tentar efetuar o login:

Enquanto digita as informações, caso o usuário esteja com a tecla "CAPS LOCK" ativa, o mesmo será informado conforme imagem abaixo:

Atualização versão 12.1.2410

## **03. ATUALIZAÇÃO VERSÃO**

A partir da versão 12.1.2410, a página de login do sistema passou por atualização visual e foram adicionadas novas funções:

* Seletor de Alias;
* Recuperação de senha;

Seletor de Alias

## **04. SELETOR DE ALIAS**

##### **Funcionalidade disponível a partir da versão 12.1.2410.**

Para utilizar a função basta selecionar o Alias configurado. Você poderá apenas selecionar, porém será possível realizar a configuração destes no RM.

É possível definir um alias padrão, para que ao abrir o sistema já venha com a opção selecionada. Basta utilizar a tag **DefaultDB** no arquivo de configuração do **Host:**

**<add key="DefaultDB" value="NomeDoAlias" />**

## **04.1 CONFIGURAÇÃO MULTI-TENANCY**

Ao utilizar o ambiente **multi-tenancy** é necessário configurar as seguintes tagsno arquivo de configuração do **Host:**

**<add key="SubDomainMask" value="[ALIAS].totvs.com.br" />  
<add key="TenantPathEnabled" value="true" />**

Deve-se também alterar o arquivo **config.json** dentro da pasta **"assets"** do sistema, para que o URL de consulta de API seja criado dinamicamente:

* + Remover a tag: **"apiUrl"**
  + Adicionar a tag: **"httpPort"** com a porta padrão de APIs.

Recuperação de senha 

## **05. RECUPERAÇÃO DE SENHA**

##### **Funcionalidade disponível a partir da versão 12.1.2410.**

Para utilizar a função é necessário o preenchimento do alias, caso contrário o sistema irá disparar uma mensagem:

Ao utilizar a função uma janela será aberta para preenchimento de Usuário e E-mail:

Após o preenchimento e uso da função "Enviar e-mail", uma mensagem de confirmação será exibida e um e-mail será enviado para o usuário:

Ao utilizar o URL enviado para o e-mail, o usuário será redirecionado para a página de redefinição de senha, bastando criar uma nova para entrar no sistema automaticamente:
