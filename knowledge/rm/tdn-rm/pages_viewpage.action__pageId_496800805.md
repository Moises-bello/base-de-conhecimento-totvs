---
content_hash: 55d91d54d728db19be8b9bdf51b183e911826a7b85194e5baf9860f2e9e755a5
fetched_at: '2026-06-29T00:10:22.489006+00:00'
page_id: '496800805'
product: rm
source: tdn-rm
title: Configurações Parâmetros Globais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496800805
version: 7
---

Atenção

A partir da versão **12.1.26** foi inserido um mecanismo de cache na camada **Server (RM.Host.exe/RM.Host.Service.exe)** para melhorar a performance do sistema, onde após alterar qualquer parâmetro Global, o mesmo demorará 5 minutos para ser replicado. Caso necessário aplicar a alteração imediatamente será necessário reiniciar todos os serviços do **Host** do ambiente.

Atenção

A partir da versão **12.1.2205** foi inserido um mecanismo de cache na camada **Client (RM.exe)** para melhorar a performance do sistema, onde após alterar qualquer parâmetro Global, o mesmo demorará 30 minutos para ser replicado. Caso necessário aplicar a alteração imediatamente no **Client (RM.exe)**será necessário reiniciar o **RM.exe**.

A partir da versão **12.1.2205** o mecanismo de cache na camada **Server (RM.Host.exe/RM.Host.Service.exe)** **foi alterado** de 5 minutos para 10 minutos para ser replicado. Caso seja utilizado mais de um Host no ambiente e seja necessário aplicar a alteração imediatamente em todos, é necessário reiniciar todos os serviços do **Host** do ambiente. Caso utilize apenas um Host, a alteração é realizada de imediato após salvar as configurações.
