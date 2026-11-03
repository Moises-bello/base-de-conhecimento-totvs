---
content_hash: 67b2524bba846199644237c1b52ca2b3cc00f5c0a4a0ee8925f999ac0480a1a3
fetched_at: '2026-06-28T21:35:27.645624+00:00'
page_id: '563414690'
product: fluig
source: tdn-fluig
title: Como cadastrar a variável jQueryMigratePluginMode
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563414690
version: 1
---

# Índice

true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar como preencher a variável do plugin de migração do jQuery através dos dados adicionais da empresa e sua vantagem ao utilizá-lo. 

Seu principal valor está nos modos de uso do plugin entre desenvolvimento e produção.

No modo Desenvolvimento são exibidas mensagens no console do navegador utilizado mostrando o que está errado no seu código auxiliando no encontro de problemas, porém deixa o console "poluído" ou seja sobrecarregado.

Já no modo Produção as mensagens no console do navegador não são exibidas ocasionando uma limpeza na geração dos logs porém uma mensagem é exibida avisando que o plugin está em uso e qual sua versão.

## Cadastrando a variável jQueryMigratePluginMode no plugin jQuery

Para o cadastro da variável siga os passos abaixo:

falsesample1Passo 01

* Efetue a autenticação no TOTVS Fluig Plataforma utilizando o usuário **wcmadmin** e então acesse **Painel de controle** > **WCM** >**Empresas**;

2Passo 02

* Selecione a empresa que deseja cadastrar as variáveis e acione opção **Editar**;

3Passo 03

* A tela de dados da empresa será apresentada. Acione **Cadastrar dados adicionais**;

4Passo 04

* A tela de Dados adicionais da empresa será apresentada. No campo **Chave** informe a variável:  
    
  + jQueryMigratePluginMode| valor: DEVELOPMENT ou PRODUCTION | Para definir qual o modo entre Desenvolvimento e Produção | Quando nada é definido, ele está em modo DEVELOPMENT por "padrão".

* Acione o botão **Salvar** para registrar a variável nos dados adicionais da empresa.
Atenção!

A configuração dessa variável é feita por empresa, e não para o sistema como um todo.
