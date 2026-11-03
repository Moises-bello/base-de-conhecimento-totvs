---
content_hash: 591076a9c0b1b0bc013ffc70dc54823cd27a5f5d1ecf0bbb8121f7e3d439336d
fetched_at: '2026-06-28T21:35:19.520655+00:00'
page_id: '210054631'
product: fluig
source: tdn-fluig
title: ARQ - Por que na indexação gera erro no log ao indexar arquivos com extensão
  '.dwg'?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210054631
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Tipo de API:** SOLR

# Ocorrência

Por que ao tentar indexar arquivos com extensão '.dwg', gerados via AutoCAD, ocorre o erro em log abaixo?

javaEclipseArquivo de log

# Causa

A API Tika não dá suporte a este tipo de arquivo (.dwg).

Existe um chamado para o time responsável pela API no Apache, segue o link: <https://issues.apache.org/jira/browse/TIKA-1735>

# Solução

Atualmente não há solução, porém não é um erro impeditivo, pois os metadados do arquivo são indexados.
