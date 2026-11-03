---
content_hash: cf0399622f22c2207986690268f6205b1a76dcd05c671148fb757306aaed4da6
fetched_at: '2026-06-28T21:35:26.875349+00:00'
page_id: '438298847'
product: fluig
source: tdn-fluig
title: CON - Problema ao buscar texto copiado de célula do Excel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=438298847
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Ao copiar o conteúdo de uma célula de planilha e colar no campo de busca da plataforma, estando com a tela de Documentos aberta, é carregado um arquivo PNG na pasta atual. Conforme demonstrado abaixo:

# Causa

A plataforma tem esse comportamento porque foi copiada a célula da planilha, e não apenas o texto. Com isso, é copiado o texto juntamente com a formatação da célula e, nesta formatação, quando colado ao componente de *upload* existente na tela de Documentos, a plataforma entende como uma imagem.

# Solução

Para realizar a colagem apenas do texto da célula, deve-se utilizar o atalho "**Ctrl + Shift + V**", que cola o texto sem a formatação.
