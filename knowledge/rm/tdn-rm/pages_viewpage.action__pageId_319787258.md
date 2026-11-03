---
content_hash: 56aae33eb4521cbb7190919620287d665e7dd9ae8cd046237c5c3d54cf468f84
fetched_at: '2026-06-29T00:08:47.187016+00:00'
page_id: '319787258'
product: rm
source: tdn-rm
title: Manual - Introdução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787258
version: 3
---

### O que é o Gerador de Saídas?

O Gerador de saídas é uma ferramenta especializada para a geração de um ou mais arquivo(s) texto para que seja feita o intercambio eletrônico de informações. Os arquivos podem ser gerados em vários formatos baseados em texto, como por exemplo texto puro ou CSV.

Sua arquitetura está foi preparada e testada tendo em vista a geração otimizada de Layouts de grande complexidade, o seu mecanismo de geração está baseado na implementação do SPED Fiscal RM, que contém mais de 150 tipos de registros diferentes e que gera arquivos de mais de 500 MB.

Para ter mais flexibilidade e desempenho máximo, toda a geração dos arquivos é baseada em código fonte gerado (C#) e compilado. O mecanismo de geração é capaz de utilizar várias fontes de dados na geração como por exemplo consultas SQL e classes .NET além de poder ser estendido para suportar outras fontes de dados como bases NoSQL.

### O que é um Layout do Gerador de Saídas?

O Layout do gerador de saídas é a base para criação do arquivo de saída. Ele é divido em Registros e Contextos. Os registros definem como será o arquivo de saída e cada registro possui um configuração específica de campos, que podem ser gerados baseados em uma ou mais listas dos contextos.

Os Contextos do Layout contém as configurações de como o gerador irá buscar os dados para geração dos registros, existem vários tipos de contextos diferentes, entre eles o contexto de Conjunto de Dados (baseado em bases de dados relacionais) e o contexto de Biblioteca .NET (baseado em código C# que retornem lista de objetos).

### O que é o Gerador de Saídas Core?

O Gerador de Saídas Core é uma ferramenta que foi criada baseada no Gerador de Saídas RM. Ele possui funcionalidades extras para conectar a outros bancos de dados não suportados pelo RM, além de permitir a geração dos arquivos em outros sistemas operacionais suportados pela plataforma .NET Core.

Atualmente os bancos de dados suportados são:

* SQL Server
* Oracle
* MySQL
* Postgress SQL
* Firebird
* DB2

Os sistemas operacionais homologados para geração são:

* Windows 7 ou superiores
* Windows 2003 R2 ou superiores
* Red Hat Enterprise Linux
* Ubuntu 16.04.3
