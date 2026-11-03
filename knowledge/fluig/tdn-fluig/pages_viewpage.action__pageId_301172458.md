---
content_hash: 257006c923473bb7797744d05c14ff417da8fa866f956c8608ca80b290b1820f
fetched_at: '2026-06-28T21:35:25.708233+00:00'
page_id: '301172458'
product: fluig
source: tdn-fluig
title: ARQ - Por que o erro "fluig.foundation.service" está ocorrendo ao subir a plataforma?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301172458
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.6.2

# Ocorrência

Ao subir a plataforma na atualização 1.6.2 está ocorrendo o erro abaixo, o que devo fazer?

javaEclipseArquivo de logtrue

# Causa

Provavelmente a plataforma foi parada de forma inesperada fazendo com que os arquivos da pasta 'data' não fossem apagados de forma automática.

# Solução

**01.** **Parar os serviços** do fluig;

**02.** **Apagar o conteúdo** da pasta '**data**' localizado em [diretório\_instalação]/appserver/domain/servers/[nome do servidor]/data

**03.** **Inciar os serviços** em sua ordem correta.
