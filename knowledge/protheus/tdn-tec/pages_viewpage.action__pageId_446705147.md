---
content_hash: 138e82d93e0577edd29b979f89fe4ffa071ee4931261bbd9369399a58adca6d9
fetched_at: '2026-07-02T19:24:23.308152+00:00'
page_id: '446705147'
product: protheus
source: tdn-tec
title: Alteração de comportamento do Console.log
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=446705147
version: 2
---

|  |
| --- |
| A partir das versões  e  o comportamento do arquivo console.log, sofreu as alterações abaixo:   1. Para um melhor desempenho, a operação de gravação do console.log passa a ser assíncrona por padrão (o valor default da chave asyncConsoleLog é 1, habilitado); Para configurar a gravação síncrona, configure o valor 0 (desabilitado) para a chave asyncConsoleLog 2. O arquivo passa a ser criado com o tamanho máximo definido pela chave consoleMaxSize; 3. Ao encerrar o Application Server o arquivo console.log é renomeado automaticamente para console.log.xxxxx.log, onde xxxxx é um número sequencial. |
