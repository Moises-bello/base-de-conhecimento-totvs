---
content_hash: ed0a8516ec69daf916ba9bab529f305daffb148686b2ee05883599910fc8db8d
fetched_at: '2026-06-29T00:06:26.524010+00:00'
page_id: '225950920'
product: rm
source: tdn-rm
title: Arquitetura homologada, preparação da base e configurações do BDE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=225950920
version: 10
---

As ferramentas para execução da conversão (CLConversor e Analisa Conversão) foram homologadas somente no Sistema Operacional Windows Server 2008 R2. Demais Sistemas Operacionais podem não funcionar corretamente.

Recomendamos a execução do manual abaixo, para atualização de estatísticas e reindexação dos índices:

<http://tdn.totvs.com.br/pages/viewpage.action?pageId=61935061>

É obrigatório desabilitar todas as triggers da base de dados, para realizar a Conversão

|  |
| --- |
| **Produto:**Banco de dados homologados e configuração do BDE |
| **SGBD Homologados**  SQL 2008 Server, Oracle 10 e 11 G. |

Existe um recurso no SQL Server chamado “***Recovery model***”. Ele é responsável por determinar como será tratado o log das transações, entre outras coisas.

Recomendamos que antes de iniciar uma conversão este parâmetro seja marcado com a opção “***Simple***”.

1) ***Simple***. Quando o Recovery está simples, o SQL faz um TRUNCATE LOG ON CHECKPOINT, ou seja, o log é zerado a cada checkpoint. Isso significa que seu log não cresce, mas você não consegue recuperar o banco no momento da falha, pois não há log para backup (está sempre ZERADO).

2) ***Full***. Nesse caso tudo é gravado. Inclusive o Checkpoint fica registrado no log. Você poderá fazer backup do log e ainda recuperar o servidor no momento de uma falha. O problema é que o Log cresce muito e você deve monitorar esse crescimento para não consumir seu disco e parar o banco.

3) ***BULK-LOGGED*** é um intermediário. Esse é usado quando vamos inserir registros em lotes e que não precisa de muita informação no log pois os dados vem de fontes externas como TXT, XML ou outro banco. Esse também não te dá suporte a restore no ponto de falha. Lembra do comando BULK INSERT ? Então, é para esse tipo de operação.

**Configurações do BDE**

É recomendado que os valores sejam alterados.

CONFIGURATION > DRIVERS > NATIVE > MSSQL > CONNECT TIMEOUT para 900 e TIMEOUT para 210000.

O alias do BDE deve ser criado **sem a utilização** do ODBC, conforme o print abaixo:
