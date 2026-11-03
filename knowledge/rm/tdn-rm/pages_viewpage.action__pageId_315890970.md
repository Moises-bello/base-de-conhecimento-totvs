---
content_hash: 3bbe305dc0c3997fb2bd76064c7485fd5872922324a1b0b8e7438d1355676dca
fetched_at: '2026-06-29T00:08:45.778791+00:00'
page_id: '315890970'
product: rm
source: tdn-rm
title: Conexão a Banco de Dados Externo Progress
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315890970
version: 33
---

# Índice:

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é demonstrar como configurar uma conexão em Banco de Dados Externo Progress e como utilizá-lo em uma Consulta SQL.

# Introdução

---

          O RM permite a utilização de Banco de Dados Externo com o Progress para execução de Consultas SQL. A configuração da Conexão de banco pode ser feita na própria tela de edição da Consulta, em qualquer módulo, menu '**Gestão | Visão de Dados**', ou no módulo '**Serviços Globais**'**,**menu'**Segurança | Conexões a banco de dados externos**'.

          Veja nos passos a seguir como deve ser feito o procedimento para utilização desse recurso.

falsefalse

Para funcionamento desta conexão torna-se necessário baixar o drive de conexão ODBC Progress.

[Página sugerida para download do drive](https://www.progress.com/odbc/openedge)

Desenvolvimento/ProcedimentoPasso 1Passo 1Passo 1

Crie a conexão com o **SGBD** Progress via **Conexão ODBC**. Selecione o drive correto e conclua as configurações obtendo exito na conexão. Na sequência acesse o sistema RM para configurarmos as conexões externas.

Passo 2Passo 2Passo 2

Para cadastrar uma conexão externa através do sistema o usuário possui duas opções, mediante suas permissões de acesso.

A primeira opção pode ser feita através do módulo **“Serviços Globais”** acessando o menu **“Segurança | Conexões | Conexões a Banco de Dados Externos”**.

Na visão de cadastro de Conexões a Banco de Dados Externos clique em **“novo”**. Preencha as informações cadastrais e clique nas reticências de **“String de Conexão”**.

A segunda, através do cadastro de consultas SQL, opção **“Banco de dados externo”**, é possível acessar o mesmo formulário.

Passo 3Passo 3Passo 3

Feito acesso ao formulário de conexões a bancos de dados externos, clique em **novo**.

Preencha as informações cadastrais do novo registro e clique no botão de reticencias. Selecione a seguir a opção **“Microsoft ODBC Data Source”**.

Selecione a conexão **ODBC** criada e conclua as configurações informando usuário e senha de conexão e testando a conexão.

Passo 4Passo 4Passo 4

Configurada a conexão externa corretamente, basta escrever a consulta SQL a ser realizada no banco da conexão externa e executar.

falseATENÇÃO - Teremos limitações:

Será possível somente executar querys **sem passagem de parâmetros**, pois via ODBC a passagem de parâmetros ocorre via SQL ANSI, ou seja, o cadastro de consulta SQL não está preparado para a passagem de parâmetros ANSI.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX ou 12.01.XX

false

**Processo:** Banco de Dados Externo

false

**Subprocesso:** Conexão a Banco de Dados Externo Progress

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
