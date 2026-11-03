---
content_hash: 421113fba863a2aaea9d44dcd4f02f7a65867391f1d7bcce17002b0e3b1e7c8b
fetched_at: '2026-06-29T00:10:27.784663+00:00'
page_id: '516645187'
product: rm
source: tdn-rm
title: Conexão de Origem/Destino Utilizando Banco de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516645187
version: 29
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   O objetivo desse documento é esclarecer o uso de conexões origem/destino usando Banco de Dados.

# Introdução:

---

Os provedores de banco de dados são APIs que promovem conexão direta a uma base de dados, sem necessidade de existir um ERP. O provedor de banco de dados fará conexão direta com um banco específico ou a diversos bancos de forma genérica, sendo assim, é de responsabilidade do usuário escolher o que melhor atenderá sua demanda.

    O principal campo para preenchimento dos dados de um provedor é a **Connection String**. É a partir deste que os outros campos serão preenchidos e, caso alguma alteração ocorra nos outros campos, a mudança será refletida na connection string.

# Conexão:

---

    Após inserir a Connection String e pressionar Enter, a tela irá se expandir, contendo novos campos junto das informações preenchidas na string. Os novos campos exibidos na tela poderão ser alterados, refletindo na connection string.

Dica

Consulte o site [https://www.connectionstrings.com](https://www.google.com/url?q=https://www.connectionstrings.com&sa=D&source=hangouts&ust=1570555394361000&usg=AFQjCNEMViFSZMP5aGaIl_B0oEtQMRpLtQ) para diferentes exemplos de utilização de Connection Strings.

# Provedores:

---

**Novidades!**

* A partir da versão 12.1.28 é possível utilizar a mesma conexão de banco que o host e foi adicionada a configuração para permitir paginação. Veja no tópico: Conexão do Host.

1Conexão do Host

A partir dos patches mais recentes da versão 12.1.28 é possível utilizar a configuração de base do host, sem precisar configurar manualmente a connection string.

Base selecionar a opção **Usa conexão do Rm.Host**. que o conceito usará a conexão do usuário logado.

Os parâmetros **Permitir Paginação** e **Tamanho da página** também estão disponíveis a partir dos patches mais recentes da versão 12.1.28.

Quando estão habilitados, a leitura na base será feita de forma paginada. Ou seja, em vez de fazer a leitura de todos os dados de uma vez, o sistema buscará a quantidade de registros determinado no campo Tamanho da página, podendo ser de 10 em 10, por exemplo.

O uso do recurso de paginação reduzirá a quantidade de memória usada pelo processo de extração de dados pela conexão de origem.

Odbc Data Provider

**Connection String**: Driver={SQL SERVER};server=<servername>;database=<dbname>

Nessa conexão, também é possível informar as tags **User ID** e **Password**

OleDb Data Provider

**Connection String**: Provider=SQLOLEDB;Data Source=<servername>;Password=<password>;User ID=<userid>;Initial Catalog=<dbname>

Para o uso de segurança integrada na conexão, informe a tag **Integrated Security=SSPI** e remova as tags **Password** e **User ID**.

Para conexão a um Provedor OleDb, estão disponibilizadas as seguintes opções, no campo "**Provider**":

OracleClient Data Provider

Para uso da conexão, é necessário instalar Oracle Client acima da versão 8.1.7.

**Connection String**: Data Source="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=<host>)(PORT=<port>))(CONNECT\_DATA=(SERVICE\_NAME=<servicename>)))";User ID=<userid>;Password=<password>

Apenas é aceito privilégio/atribuição "SYS", que é o padrão Oracle. SYSDBA não é suportado.

SqlClient Data Provider

**Connection String**: Server=<servername>;Database=<dbname>;User Id=<userid>;Password=<password>;

Utilize o botão "Testar" para testar sua conexão.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Conexões Origem/Destino Banco de Dados

falsefalse

**Status:** Finalizado

false

**Data:** 07/10/2019

false

**Autores:**
