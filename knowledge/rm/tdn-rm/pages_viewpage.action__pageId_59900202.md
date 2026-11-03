---
content_hash: 29f6e73d114c691c9ab6a587fde1d8422ebbfd56c2975d2e3080c8f85121af8d
fetched_at: '2026-06-29T00:10:57.626264+00:00'
page_id: '59900202'
product: rm
source: tdn-rm
title: Configuração de Banco de Dados Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=59900202
version: 12
---

# Índice:

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é demonstrar como configurar uma conexão em Banco de Dados Externo e como utilizá-lo em uma Consulta SQL.

# Introdução

---

          O RM permite a utilização de Banco de Dados Externo para execução de Consultas SQL. Para isso, é necessário configurar a Conexão de banco na própria tela de edição da Consulta.

Observação

Para os Data Source de Microsoft ODBC e Microsoft SQL Server utilizando Data Provider OLE DB não será permitido a utilização de parâmetros na consulta SQL (Ex. CODIGO = :CODIGO) por limitação dos data sources.

Veja nos passos a seguir como deve ser feito o procedimento para utilização desse recurso.

falseDesenvolvimento/ProcedimentoPasso 1Passo 1Passo 1

 Crie a sentença SQL desejada, acessando o menu **'Gestão | Visões de Dados'** e clique no botão Incluir (Ctrl + Ins).

Em seguida, clique em Banco de Dados Externo. Por essa tela é possível gerenciar as conexões externas existentes em Consultas SQL.

Passo 2Passo 2Passo 2

Após acessar a tela de Conexões a banco de dados externos, clique no botão Incluir (Ctrl + Ins) e preencha os principais campos, como demonstrado no exemplo abaixo:

Clique em "String de conexão", selecione o Data Source e Data Provider conforme seu ambiente. No exemplo a seguir, usaremos uma conexão SQL.

Clique em "OK".

Passo 3Passo 3Passo 3

Determine o Servidor (Server Name), Usuário (User Name), Senha (Password) e a Base de Dados (Select or Enter a Database Name).

Clique em "Test Connection" para certificar que a base está acessível e a conexão está funcionando:

Clique em "Ok".

Passo 4Passo 4Passo 4

Na tela de cadastro de Conexões a banco de dados externos, selecione a conexão que foi configurada nos passos anteriores.

Passo 5Passo 5Passo 5

Após configurar e selecionar a conexão de Banco de Dados Externo, cadastre a Consulta SQL desejada, como no exemplo abaixo:

Observação

Para os Data Source de Microsoft ODBC e Microsoft SQL Server utilizando Data Provider OLE DB não será permitido a utilização de parâmetros na consulta SQL (Ex. CODIGOO = @CODIGO) por limitação dos data sources.

# Conexão com Oracle

---

Ao utilizar uma base externa Oracle a conexão será realizada utilizando o provider Devart com a funcionalidade Direct Mode habilitada, este é o modo padrão usado pelo RM.

Veja mais informações em,

Observações

O assistente de conexão apresentado é nativo do Windows, veja imagens dos passos 2 e 3. Sua funcionalidade de teste de conexão neste caso é realizada do lado Client do RM.exe, dessa forma somente será bem sucedido caso o Oracle Client esteja instalado, porém não é necessário, nem obrigatório sua instalação para uso no RM, por padrão. Por este motivo caso não seja possível realizar o teste, não significa que haverá problema de conexão pelo RM.Host

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX ou 12.01.XX

false

**Processo:** Banco de Dados Externo

false

**Subprocesso:** Configuração de Banco de Dados Externo

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
