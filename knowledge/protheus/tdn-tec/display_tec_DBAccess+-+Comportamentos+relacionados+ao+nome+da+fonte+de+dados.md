---
content_hash: 2d0bae91aebeeea47893f6e8d9f4ecf0c96b08462013f75c42bb79b39e6d6df8
fetched_at: '2026-07-02T19:24:28.787643+00:00'
page_id: '856454819'
product: protheus
source: tdn-tec
title: DBAccess - Comportamentos relacionados ao nome da fonte de dados
type: documentation
url: https://tdn.totvs.com/display/tec/DBAccess+-+Comportamentos+relacionados+ao+nome+da+fonte+de+dados
version: 3
---

O true estabelece uma conexão com os  através de um driver ODBC, para as plataformas Windows e Linux, sendo que para o ORACLE, normalmente é utilizada uma conexão através de uma biblioteca *client* chamada de OCI (Oracle Client Interface).

Independente do modo de conexão, para todos os casos, é necessário criar uma fonte de dados que precisa ser identificada por um nome distinto.

Este nome da fonte de dados, ou DSN (Data Source Name), preferencialmente, deve iniciar com uma letra e pode ter letras e/ou números.

Evite usar espaços, símbolos e caracteres especiais no nome da fonte de dados.

Ao configurar o true para se conectar com um determinado Banco de Dados, informamos a ele qual o nome do DSN a ser utilizado, que deve ser exatamente o mesmo nome usado na ODBC.

Um true pode usar mais de uma fonte de dados e conectar-se com vários bancos de dados diferentes.

É possível configurar, por exemplo, uma fonte de dados apontando para um *database* de homologação e outra fonte de dados para um database de testes.

A aplicação true acessa o true através do IP e Porta configurados em cada true, e informa o Banco de Dados e o nome da fonte de dados a ser utilizada.

Internamente, o true utiliza o nome da fonte de dados informado para controlar aspectos da emulação ISAM de acesso às tabelas, como o modo de abertura (exclusivo e/ou compartilhado, acesso completo ou somente leitura), bem como o mecanismo de bloqueios de arquivo e registro (bloqueio de registro linha a linha, ou do arquivo inteiro).

Estes controles fazem parte da compatibilidade exigida pelo true, e são feitos pelo true em listas mantidas em memória.

Quando utilizamos o true em uma , o serviço configurado como primário (*master*) fica responsável por esses controles.

Sabendo dessa característica, sempre devemos criar apenas UMA fonte de dados nomeada (DSN/ODBC ) para UMA determinada instância de Banco de Dados.

Quando utilizamos o true em configuração distribuída, em mais de um equipamento, todas as fontes de dados criadas para um determinado *database* devem ter o mesmo nome em todas as máquinas, para que cada true secundário aponte para a fonte de dados de mesmo nome, que aponta para o mesmo Database.

Observe que não deve-se colocar dois serviços distintos de true (stand-alone por exemplo), apontando para o mesmo Banco de Dados.

Caso essas premissas não sejam respeitadas, a integridade dos dados de tabelas acessadas para alteração de dados em modo concorrente é seriamente prejudicada, pois dois programas true podem conseguir ao mesmo tempo um LOCK de registro para alteração, ou mesmo obter sucesso ao tentar abrir uma determinada tabela em modo EXCLUSIVO, nos cenários abaixo:

1. As instruções estão sendo executadas em programas conectando em dois  true stand-alone distintos, que apontam para o mesmo banco de dados.
2. Programas conectando com o mesmo true, usando duas fontes de dados de nomes distintos, que apontam para o mesmo banco de dados.

Caso os programas executados de forma concorrente usem transacionamento (BEGIN TRANSACTION), pode ocorrer deadlock no Banco de Dados.
