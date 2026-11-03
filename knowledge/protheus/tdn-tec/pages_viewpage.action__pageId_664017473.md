---
content_hash: 9e8f9313d42bbe61b6ca1d3b13d88b450c8abb4d12b92151a51f6c5010ebeae5
fetched_at: '2026-07-02T19:24:27.646335+00:00'
page_id: '664017473'
product: protheus
source: tdn-tec
title: SQLite - Comparação entre strings
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=664017473
version: 7
---

Comparação entre Strings

A partir da versão Harpia do true, a emissão de *queries* deixa de injetar a instrução **RTRIM** nos statements. Contudo, para manter o comportamento esperado de comparação de strings no true (desconsiderando espaços a direita), as tabelas precisam ser recriadas especificando o ***COLLATE RTRIM*** explicitamente (apenas para campos caractere).

Desta forma, ao abrir uma tabela do SQLite, caso a mesma não tenha sido criada com a especificação citada acima, o true finalizará a thread com e emitirá a mensagem de erro abaixo:

As novas tabelas criadas com esta versão do true já assumem a característica apontada nesta documentação.

É possível parametrizar o true para verificar e converter automaticamente as tabelas do database SQLite.

Para isso, deve-se configurar a chave SQLITE\_RebuildTables=1 na seção [general] do appserver.ini do ambiente.

---

## Veja também
