---
content_hash: 8b6d9b79f89b5e169ea819305ce2b8b07327bdbc3909ac58cab469e5abb6b426
fetched_at: '2026-06-29T00:05:56.955652+00:00'
page_id: '160105537'
product: rm
source: tdn-rm
title: Criação/conexão com banco de dados externo com Microsoft Office Excel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=160105537
version: 17
---

# Índice:

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é auxiliar como configurar uma conexão em Banco de Dados Externo com Microsoft Office Excel e como utilizá-lo em uma Consulta SQL.

# Introdução

---

          O RM permite a utilização de Banco de Dados Externo com o Excel para execução de Consultas SQL. A configuração da Conexão de banco pode ser feita na própria tela de edição da Consulta, em qualquer módulo, menu '**Gestão | Visão de Dados**', ou no módulo '**Serviços Globais**'**,**menu'**Segurança | Conexões a banco de dados externos**'.

          Veja nos passos a seguir como deve ser feito o procedimento para utilização desse recurso.

falsePasso a PassoPasso 1Passo 1Passo 1

Para criar uma conexão, abra a configuração Fonte de dados (ODBC) pelas Ferramentas Administrativas do Windows.

**Obs.:** **Este** **caminho** **pode** **ser** **diferente** **de** **acordo** **com** **seu** **sistema** **operacional. C****aso** **não** **encontre,** **abra o Painel** **de** **Controle/Ferramentas** **administrativas:**

(Acesso ao Painel de Controle / Ferramentas Administrativas)

(Abra a Fonte de Dados ODBC compatível com seu Sistema Operacional. Usaremos o de 64 bits neste exemplo)

Passo 2Passo 2Passo 2

Selecione a aba **DSN de Sistema** e clique em Adicionar:

Passo 3Passo 3Passo 3

Selecione o driver para fonte de dados e clique em **concluir**.

Neste exemplo estamos trabalhando para conexão com **Microsoft** **Office** **Excel.**

Passo 4Passo 4Passo 4

Na tela seguinte, informe o **nome** **da** **fonte** **de** **dados** e sua **descrição**.

A opção **versão** é preenchida automaticamente, como a que está em destaque, mas poderá ser alterada se necessário. Clique em **OK**:

Passo 5Passo 5Passo 5

Crie a sentença SQL desejada, acessando o menu **'Gestão | Visões de Dados'** e clique no botão Incluir (Ctrl + Ins).

Em seguida, clique em **Banco de Dados Externo**, para vincular a Consulta ao Excel.

Por essa tela também é possível gerenciar as conexões externas existentes em Consultas SQL, criar novas ou editar.

Passo 6Passo 6Passo 6

Para cadastrar uma nova conexão, após acessar a tela de Conexões a banco de dados externos, clique no botão Incluir (Ctrl + Ins) e preencha os principais campos, como demonstrado no exemplo abaixo.

Clique em "String de conexão", selecione **Microsoft ODBC Data Source**.

Clique em **OK**.

Passo 7Passo 7Passo 7

Na tela exibida abaixo, na opção **Use** **user** **system****data** **source** **name** selecione o banco de dados que foi criado no ODBC, pelos passos anteriores.

Na opção **Use connection string** clique em **build** e selecione o caminho onde está o arquivo excel, como mostra nas imagens abaixo:

Selecione a aba Fonte de dados de máquina e clique 2 vezes sobre o **nome** **da** **fonte** **de** **dados** criada:

Selecione o arquivo Excel a ser consultado, clicando sobre ele 2 vezes.

 Pressione **OK** e salve todos os processos.

**Clique** **em** **testar** **conexão** para certificar que a base está acessível e a conexão está funcionando:

Clique em **Ok**.

Passo 8Passo 8Passo 8

**Consulta** **SQL**

Após configurar e selecionar a conexão de Banco de Dados Externo, cadastre a Consulta SQL desejada, de acordo com a estrutura de seu arquivo Microsoft Office Excel como no exemplo abaixo:

*****Sintaxe de SQL para consultar dados em arquivos Microsoft Office Excel:*****

**SELECT** \* **FROM** [NOME\_DA\_ABA\_DO\_ARQUIVO\_EXCEL$]

Caso tenha muitas colunas na tabela e queira buscar apenas alguns campos, pode ser feito a sintaxe abaixo:

**SELECT** [CAMPO1], [CAMPO2], [CAMPO\_N] **FROM** [NOME\_DA\_ABA\_DO\_ARQUIVO\_EXCEL$]:

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX ou 12.01.XX

false

**Processo:** Banco de Dados Externo

false

**Subprocesso:** Criação/conexão com banco de dados externo com Microsoft Office Excel 

falsefalse

**Status:** Finalizado

false

**Data:** 04/08/2016

false

**Autores:**
