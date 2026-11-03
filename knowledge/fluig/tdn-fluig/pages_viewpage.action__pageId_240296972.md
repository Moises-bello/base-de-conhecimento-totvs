---
content_hash: d6a5ff0e0f70dc8da30fb3dc0807d5db7e1af4e802d6bf72cec9065cbb0a1472
fetched_at: '2026-06-28T21:35:22.799024+00:00'
page_id: '240296972'
product: fluig
source: tdn-fluig
title: DES - Erro na busca de bibliotecas disponíveis no ambiente Style Guide
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240296972
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto**: TOTVS Fluig Plataforma

# Ocorrência

Há indisponibilidade no ambiente [style.fluig.com](http://style.fluig.com), assim não estamos conseguindo puxar os arquivos CSS e Javascript oriundos dele, nossos formulários não estão conseguindo abrir por causa disso.

# Solução

Alterar as chamadas de JS e CSS do Style Guide para acessar arquivos locais da própria instalação da plataforma. Abaixo lista de *imports* padrão:

xml

]]>

# Observação

Em termos de performance, ao realizar a chamada das bibliotecas disponibilizadas pela própria plataforma o desempenho será melhor do que chamar uma biblioteca publicada externamente.
