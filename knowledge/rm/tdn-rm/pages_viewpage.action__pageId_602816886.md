---
content_hash: 79088c6e24de6099cd9ff66188f90d70783b7afc10582ce708563eb51c4a1c5f
fetched_at: '2026-06-29T00:10:58.035780+00:00'
page_id: '602816886'
product: rm
source: tdn-rm
title: 14.01 - Parâmetros do sistema - Prova Fácil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=602816886
version: 16
---

Importante

Esta funcionalidade está disponível a partir da versão **12.1.32**.

Para ativar a integração com o Prova Fácil, deve-se acessar os parâmetros do sistema (Educacional | Processo seletivo | Parâmetros | Parâmetros do Sistema | Aba Integração | Aba Prova Fácil) e realizar algumas configurações necessárias.

## **01. Dados de conexão**

Os dados de conexão devem ser obtidos com o parceiro "Prova Fácil", e informados nos parâmetros do sistema.

Depois de informar os campos "**Url de conexão com a API**", "**Usuário de autenticação da API**" e "**Senha**", deve-se clicar no botão "Carregar Token" para que seja realizado a autenticação no parceiro "Prova Fácil", conforme mostra a figura abaixo:

Aviso

Após carregar o token, o sistema atualiza alguns dados necessários para a que a integração funcione corretamente, um deles é a configuração dos acadêmicos, que no Prova Fácil deve estar configurado em três níveis:

* Área ofertada
* Etapa
* Data da prova

## **02.****Contexto**

Para que a integração funcione corretamente, deve-se acessar a plataforma do Prova fácil (**CONFIGURAÇÕES | Grupo Empresarial**) e recuperar as informações de "Grupo empresarial" e "Unidade de negócio" e informar no contexto da integração.

* Grupo Empresarial:

* Unidade de negócio:

Informar o campo "Chave do parceiro" nos parâmetros, conforme mostra a figura abaixo:

## **03.****Tipo de Avaliação**

Para que a integração funcione corretamente, deve-se acessar a plataforma do Prova fácil (**CONFIGURAÇÕES | Tipos de avaliação**) e recuperar as informações do tipo de avaliação.
