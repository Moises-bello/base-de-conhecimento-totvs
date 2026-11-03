---
content_hash: ba4521a2e69d4f5acbca4af6832de9b30632038b138e7a7032da4c950c297ef1
fetched_at: '2026-06-28T21:35:23.157486+00:00'
page_id: '244423762'
product: fluig
source: tdn-fluig
title: ARQ - Por que a atualização da plataforma em Windows é interrompida pelo antivírus?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244423762
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Ambiente:** Windows

# Ocorrência

Renomeamos a pasta de instalação da plataforma no momento da atualização porém, está ocorrendo erro. Mantemos o nome original e após término da *wizard* de atualização, renomeamos a pasta para o nome que desejamos. Portanto, como proceder para renomear a pasta de instalação no momento da atualização?

# Causa

Durante a atualização da plataforma, o instalador renomeia temporariamente a pasta de instalação no servidor. Ao finalizar a atualização, o nome original da pasta é restaurado. O problema ocorre porque o antivírus varre a pasta de instalação durante este processo, acusando que os arquivos estão sendo utilizados pelo Windows.

# Solução

Adicionar uma exceção para o diretório de instalação da plataforma Fluig nas configurações do programa antivírus.
