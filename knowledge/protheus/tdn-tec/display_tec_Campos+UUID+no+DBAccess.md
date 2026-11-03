---
content_hash: 34a5d08a506452eeac4cbebe2198c3d41db0fd3d7a9b3c5de57109672dcfca2f
fetched_at: '2026-07-02T19:24:27.691482+00:00'
page_id: '676573696'
product: protheus
source: tdn-tec
title: Campos UUID no DBAccess
type: documentation
url: https://tdn.totvs.com/display/tec/Campos+UUID+no+DBAccess
version: 2
---

A partir do true **Build 20210202 – Build Version 21.1.1.4** foi implementada uma forma de usar o tipo de campo "unique identifier" ou "uuid", para os bancos de dados **MS-SQL Server**, **Oracle** e **PostgreSQL**.

Essa implementação tem o objetivo de criar um identificador único para uma determinada linha de uma tabela, usando um identificador de 16 bytes (128 bits) nativo do Banco de Dados, para identificar um determinado registro, e ser possível manter a sua identificação única desde a criação.

---

## Características

Para cada Banco de Dados, é usado seu tipo nativo para armazenar o valor criado.

* Para o MS-SQL Server: é utilizado o tipo "uniqueidentifier"
* Para o PostgreSQL é utilizado o tipo "uuid"
* Para o Oracle é utilizado o tipo RAW(16)

Cada registro inserido na tabela, caso não seja informado um valor para o campo usado como identificador único, será populado com um valor único obtido pelo SGDB.

* Para o MS-SQL Server, a constraint default do campo usa o valor retornado pela função **NEWID**
* Para o PosgtreSQL é utilizado o valor recuperado através da função **uuid\_generate\_v4**
* Para o Oracle é utilizado o valor recuperado através da função **SYS\_GUID**

***Observação:*** Todas as funções mencionadas acima são nativas de seus respectivos SGDBs.

A estrutura da tabela no Banco de Dados vai utilizar um tipo de dado que consome apenas 16 bytes e a aplicação true pode consultar ou mesmo atribuir um valor ao campo, usando:

* Uma string de 36 caracteres para MS-SQL Server e PostgreSQL (string UUID de 32 caracteres hexadecimais, divididos em 5 blocos com separadores '-' , agrupando 8-4-4-4-12 caracteres nessa ordem)
* Uma string de 32 bytes hexadecimais sem separadores para o Oracle

---

## Uso pela aplicação

A idea de uso deste campo é que cada novo registro criado em uma tabela receba um identificador único, que possa ser lido pela aplicação, possa ser utilizado como chave estrangeira em outra(s) tabela(s), gere um consumo mínimo de armazenamento, e que seja endereçável pela aplicação para leitura e atribuição.

A visibilidade e tratamento do campo na camada de dados do true como uma string permite a visualização e manipulação do campo, bem como manter o seu valor em caso de uma manutenção, alteração estrutural ou cópia da tabela de/para outros formatos e vice-versa.

*Cada tabela criada pelo true possui o campo de controle interno R\_E\_C\_N\_O\_ que emula o numero físico de um registro ISAM.*

*Esse valor, embora seja atribuído uma vez na inserção, não é persistido ou exportado para outros drivers ou formatos de arquivos de dados, e pode ser recriado caso o controle de numeração da tabela seja alterado. ou uma alteração estrutural exija internamente a recriação da tabela.*

Por isso o valor do R\_E\_C\_N\_O\_ não deve ser usado como chave estrangeira.

---

## Referências

* [Wikipedia - Identificador único universal](https://pt.wikipedia.org/wiki/Identificador_%C3%BAnico_universal)
