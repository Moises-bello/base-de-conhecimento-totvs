---
content_hash: 48ce55efc1e5c6a363eb58466a42ce1ab9ed1803df242e36eca66a1f6b3cd14c
fetched_at: '2026-06-29T00:10:46.885362+00:00'
page_id: '556380848'
product: rm
source: tdn-rm
title: Acesso a banco de dados MS Access
type: documentation
url: https://tdn.totvs.com/display/LRM/Acesso+a+banco+de+dados+MS+Access
version: 63
---

## Problema

Ao fazer uma "Conexão a banco de dados externos" e escolher o Datasource "Microsoft Access Database File" e fazer o teste de conexão é apresentado o erro "O provedor 'Microsoft.Jet.OLEDB.4.0' não está registrado não máquina local.".

## Solução

Como o provider JET.OLEDB não é compatível com as versões x64, é necessário utilizar outras formas de acesso ao arquivo.

Você pode fazer a conexão de duas formas diferentes via ACE.OLEDB ou via ODBC segue um detalhamento das opções.

#fffACE.OLEDB

1. Baixe e instale o Microsoft Access Database Engine 2010 Redistributable (<https://www.microsoft.com/en-us/download/details.aspx?id=13255>)
2. No cadastro de "Conexões a bancos de dados externos", ao cadastrar a "String de conexão" selecione conforme abaixo  
   1. Escolha o DataSource: "<other>".
   2. Escolha o DataProvider: ".NET Framework Data Provider for OLE DB".
   4. Escolha o OLE DB Provider: "Microsoft Office 12.0 Access Database Engine OLE DB Provider".
   5. Informe o local do arquivo em "Server or file name"
   6. Clique em "Teste Connection"
#fffODBC

1. Criar uma fonte de Dados ODBC.
2. No cadastro de "Conexões a bancos de dados externos", ao cadastrar a "String de conexão" selecione conforme abaixo  
   1. Escolha o DataSource: "Microsoft ODBC Data Source".
   3. Escolha o Data Source Name (DSN) cadastrado no passo anterior e clique em "Test Connection".

## Artigos relacionados

Os artigos relacionados aparecem aqui baseados nos rótulos que você selecionar. Clique para editar a macro e adicionar ou alterar os rótulos.

false5LRMfalsemodifiedtruepagelabel = "kb-troubleshooting-article" and type = "page" and space = "LRM"kb-troubleshooting-article

true

|  |  |
| --- | --- |
| Ocorrências relacionadas |  |
