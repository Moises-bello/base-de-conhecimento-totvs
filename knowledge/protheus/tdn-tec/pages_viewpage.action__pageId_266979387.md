---
content_hash: b82503ad34d419eaf945683852f7309b08795313c82863cb63501d695c2b404f
fetched_at: '2026-07-02T19:24:21.361585+00:00'
page_id: '266979387'
product: protheus
source: tdn-tec
title: DBAccess - Seção [Environment], chave ConnectionMode
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266979387
version: 4
---

Permite definir o modo de conexão do DBAccess com o SGDB

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (**Padrão**) | Conexão ODBC por DSN. |
| 1 | String de conexão montada internamente pelo DBAccess, usando DSN. |
| 2 | Conexão usando apenas string de conexão (DSN-less)  Para todos os bancos (exceto Oracle) deve ser fornecida a string de conexão no formato ODBC, especificando o nome do Driver utilizado entre chaves, o nome do host onde está o MSSQL Server, e o nome do Database a ser utilizado, vide exemplo abaixo:   ``` ConnectionMode=2 ConnectionString="DRIVER={ODBC Driver 11 for SQL Server};SERVER=TEC-JULIOW-PC;DATABASE=ENVP11;" ```   Para ORACLE, pode ser especificado o Banco no formato **//<ora\_host>:<ora\_port>/<oracle\_service\_name>** |

## Observações

* Especificar a chave na seção de configuração de um banco de dados tem efeito sobre o valor default de todos os ambientes nele configurados.
* Caso seja especificada dentro de uma seção de conexão específica [Banco/ambiente], esta configuração será considerada para o ambiente em questão.
* Esta configuração está disponível e passa a ser considerada a partir do **DBAccess Build 20161016**

## Exemplos

text

## Veja Também
