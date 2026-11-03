---
content_hash: 24a68f9a172945fbbc77775d65df07fe794fc2693b5b1bf9596e19a46ee80665
fetched_at: '2026-06-28T21:35:24.438890+00:00'
page_id: '269436043'
product: fluig
source: tdn-fluig
title: ARQ - Por que está ocorrendo o aviso "Diretório Físico não é um diretório válido!"
  ao alterar diretório do volume?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269436043
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Por que ao tentar editar o caminho do volume na plataforma, ocorre o aviso "Diretório Físico não é um diretório válido!"?

# Causa

A pasta do novo diretório não está vazia. Conforme erro demonstrado no arquivo de log:

xmlEclipse1024Arquivo de logtrue

# Solução

Para solucionar este problema, a pasta do diretório que está sendo informado deverá estar vazia. Após informar o novo diretório do volume no painel administrativo, os arquivos referentes ao volume da plataforma deverão ser copiados para esta pasta.
