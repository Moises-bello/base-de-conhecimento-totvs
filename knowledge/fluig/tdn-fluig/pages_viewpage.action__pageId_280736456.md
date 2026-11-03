---
content_hash: 278511dc59f2511451ada3895d2872ce4802181c34a3f2dae6c31b0cef74808a
fetched_at: '2026-06-28T21:35:25.308282+00:00'
page_id: '280736456'
product: fluig
source: tdn-fluig
title: ARQ - Como verificar se o MemCached foi iniciado corretamente e não está populado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=280736456
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.5.x  até 1.6.2

# Ocorrência

Como verificar se o Servidor de Cache (MemCached) do Fluig foi iniciado corretamente e não está populado?

# Solução

Importante

Este procedimento pode ser realizado tanto em sistemas operacionais Windows como em Linux.

No Windows, certifique-se que o recurso Telnet esteja ativado pois, para executar os procedimentos desta FAQ, será necessário este recurso estar ativo.

No Prompt de Comandos ou Console, conectar o telnet e digitar o IP e a porta do servidor de cache (MemCached) configurado na plataforma. Em seguida, execute o comando “stats”. Portanto, siga os passos abaixo:

0.5falsesamplesfadetrue1Passo 1

* Inicie o serviço de MemCached e, antes de iniciar os serviços de RealTime, Indexer (se tiver na versão 1.6 da plataforma) e Fluig, siga os demais passos.

2Passo 2

* Digite no Prompt de Comandos ou Console: **telnet <IP MemCached> <porta MemCached>**. Por padrão o serviço de MemCached vem configurado para utilizar a porta 11211, conforme informado na documentação . Exemplo:

3Passo 3

* Após acessar o recurso de Telnet, digite o comando: '**stats**'

4Passo 4

* Antes do Fluig ser iniciado o valor apresentado na propriedade “**curr\_items**” deve ser igual a zero. Se tiver um valor diferente, o servidor de cache está populado e pode apresentar problemas ao iniciar o Fluig. Estando populado, deve ser reiniciado.
