---
content_hash: 75562af907bc8844516b1aa928314e91ba9ae15acba979132906a36d97b3e671
fetched_at: '2026-06-29T00:08:43.901297+00:00'
page_id: '307834297'
product: rm
source: tdn-rm
title: Vantagens em utilizar Direct mode (Oracle)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307834297
version: 23
---

## Introdução

A partir da versão **12.1.18**, os produtos da linha **RM** passarão a utilizar o **"Direct Mode"** do provider de conexão **(Devart)**, utilizado para bases de dados **Oracle**.

O **"Direct Mode"** implementa a conexão da aplicação **RM** sem a necessidade de utilizar **dll's**, **providers** ou outros **artefatos de terceiros** para conexão a base **Oracle**. Antes da implementação, utilizávamos a **Oracle Call Interface (OCI)** para conexão ao banco de dados **Oracle**. Esta configuração exigia a existência do **Client Oracle,** tanto nas máquinas **Client,** quanto nas máquinas **Server,** além de demandar a existência do **Client** em **32 (x86)** e **64 (x64)** bits.

Para saber mais sobre o "**Direct Mode",** acesse o artigo [Oracle Direct Mode](http://tdn.totvs.com/display/public/LRM/ER_FRW_FRW002-370_Oracle_DirectMode).

## Vantagens

As vantagens em se utilizar o **"Direct Mode"** são:

falsePERFORMANCE]]>

| **Este trecho envolve conteúdo extremamente técnico.** |
| --- |

Iremos mostrar abaixo, os resultados dos testes de comparação de performance, realizados pela empresa **Devart**, utilizando o **"dotConnect for Oracle" (DirectMode)** em relação a outros providers ADO .NET, como: **"Oracle Client"**, **"OLE DB"** e **"ODP.NET"**.

* Todos os testes foram realizados em um ambiente que utilizava o Sistema Operacional **Windows 2000 Professional**;
* Servidor: Intel P4 2.4 / 512 Mb RAM, Oracle9i Enterprise Edition Release 9.2.0;
* Estação de Trabalho: Intel P4 2.0 / 512 Mb RAM, Oracle client 9.2.0;

Operações realizadas em banco:

sql1CreatePerftruetrue

Os teste realizados foram:

## 1° Teste - Obtenção dos Dados

Esse teste demonstra a obtenção de várias linhas começando com 1000. Para realizar esse teste a classe DataReader é usada diretamente. Nesse teste o valor padrão do parâmetro Fetch Block Size foi usado.

O comando SQL utilizado nesse teste é:

sql1fetch.testtrue

Resultado:

## 2º Teste - Preechimento dos Dados

Esse teste demonstra o preenchimento de um DataSet por um DataAdapter com várias linhas.

O comando SQL utilizado nesse teste é:

sql1fill.testtrue

Resultado:

## 3º Teste - Execução Múltipla

Executa um número específico **X** de vezes o comando **INSERT**.

O teste usa a tabela **DETAIL**.

Resultado:

## 4º Teste - Chamada a uma Stored Procedure

Esse teste demonstra um número específico **X** de chamadas a uma Stored Procedure com parâmetros. Os Parâmetros são passados cada vez que a Store Procedure é chamada. A Stored Procedure foi criada antes dos testes de Execução (4º Teste)

Nome da Stored Procedure: **Master\_Insert**

Parâmetros a sêr submetidos: **p\_Code**, **p\_Field1**, **p\_Field2**, **p\_Field3**

Resultado:

Caso queira conferir o artigo oficial do teste, acesse [DotConnect for Oracle Performance](https://www.devart.com/dotconnect/oracle/performance.html).

## Links Úteis

Caso tenha algum problema na comunicação entre o AppServer (Host) e o banco de dados, consulte o artigo [CannotConnect ao utilizar Direct mode (Oracle)](http://tdn.totvs.com/pages/viewpage.action?pageId=305930904).
