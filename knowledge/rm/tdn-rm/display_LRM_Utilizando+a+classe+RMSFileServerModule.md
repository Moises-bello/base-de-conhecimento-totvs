---
content_hash: 0d3a3e4869f5e776a289e4afcf44e1df1f882d77d786907fe46db880f0a245c7
fetched_at: '2026-06-29T00:11:12.495926+00:00'
page_id: '653835523'
product: rm
source: tdn-rm
title: Utilizando a classe RMSFileServerModule
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+a+classe+RMSFileServerModule
version: 24
---

# Objetivo

Para as versões anteriores já existia uma indicação de quando fizer o uso de arquivos no Server é recomendando utilizar a IRMSFileServer.

A partir da versão **12.1.34**, foi criada a interface **IRMSFileServerModule**, um formato mais adequado entre Servers, passando a tenantizar internamente.

Quando houver uma funcionalidade que precise realizar acesso ao disco, para Leitura ou Gravação será necessário usar a classe RMSFileServerModule, este formato visa garantir questões de segurança e funcionalidade em 3 camadas, fazendo a tenantização quando a Tag estiver habilitada, [TenantPathEnabled](https://tdn.totvs.com/pages/viewpage.action?pageId=653574360).

# Implementação

No lado server, para utilizar os métodos da classe, deve-se Instanciar um objeto da interface IRMSFileServerModule no Broker.

Exemplo:

c#DJangotrue();
var filePath = fileServer.GetFilePath(tempFile, false);]]>Classes para manipulação de acesso ao disco

Veja mais informações aqui, para utilização das classes para acesso ao disco.

<https://tdn.totvs.com/pages/viewpage.action?pageId=668179383>

Atenção

Ja existia uma indicação de uso anterior para o FileServer. Mais informações em:
