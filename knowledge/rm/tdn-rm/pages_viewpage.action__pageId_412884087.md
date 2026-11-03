---
content_hash: 6c0b5d075ec1e835d282c03e070255b5ac6ab4c63d5a1c76126a98298affeb22
fetched_at: '2026-06-29T00:09:11.606725+00:00'
page_id: '412884087'
product: rm
source: tdn-rm
title: BD0022_CONFIGURAÇÃO_ODBC_SQL_SERVER_2012/2014/2016
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=412884087
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões:** | Todas - SQL Server |
| **Ocorrência:** | Configuração da conexão ODBC no BDE (SQL Server 2012, 2014, 2016) |
| **Ambiente:** | DELPHI - RM - BDE |
| **Passo a passo:** | 1.Abrir o BDE e configurar o ODBC, conforme abaixo:    2. Ir em “Fonte de dados de sistema” e clicar em ADICIONAR:    3. Selecionar o drive “SQL Server Native Client 11.0 ”:    4. Informar um alias e o nome do servidor que está a base de dados:      5. Clicar em AVANÇAR e realizar a conexão com o banco:      6. Selecionar a base:    7. Avançar até finalizar o processo:    8. Verifique as informações do alias criado e clique em "Testar Fonte de dados...":    9. Verifique se o teste de conexão com a Base foi realizado com sucesso:    8. Acessar o BDE após as configurações acima e editar os campos "BlobSize" (999) e "Blob To Cache" (64000) para os valores indicados. |
| **Observações:** | * A conexão deve ser criada na guia ‘DSN System’ ou ‘Fonte de Dados de Sistema’ as guias de usuários não devem ser utilizadas.  * Na seleção do Drive do ODBC deve-se utilizar a opção SQL NATIVE CLIENT 10/11 ou SQL Server; * No campo Description favor informar o nome do Base de Dados que consta no SQL Server; * Atenção: A conexão de ser criada na guia de sistema. Não deve-se utilizar a guia de usuário. * No campo Server favor informar o valor apresentado no resultado da seguinte consulta SQL; select SERVERPROPERTY ('Servername') * No campo Change the default database to: selecione a Base de Dados em questão. * Verifique também se o método de autenticação da instância SQL está definido como SQL Server and Windows Authentication Mode.    Somente o Alias iniciados com ‘CorporeRM’ serão apresentados na aplicação Delphi, sendo assim, o campo Nome da configuração ODBC deverá ser iniciado com CorporeRM.  A nova configuração pode entrar em conflito com a configuração existente anteriormente. Ou seja, pode existir um Alias com nome CorporeRM do tipo MSSQL e pode ser criado um alias com o mesmo nome para a conexão ODBC. Sendo assim, realize uma das opções abaixo:  a)      Exclua a conexão MSSQL e feche o BDE, mantendo somente a conexão ODBC;  b)      Crie a conexão ODBC com um nome distinto das conexões já criadas na guia Database    Atenciosamente, |
