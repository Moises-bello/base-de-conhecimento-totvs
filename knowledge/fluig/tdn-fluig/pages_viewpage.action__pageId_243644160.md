---
content_hash: 1ede06144b66681fe059b7f8e22c55ba70ddbc1da990c169c60bab7ad6fafa41
fetched_at: '2026-06-28T21:35:23.021705+00:00'
page_id: '243644160'
product: fluig
source: tdn-fluig
title: BPM 048 - Por que o erro "O processo não existe ou não possui nenhuma versão
  ativa" acontece?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243644160
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Ocorre o erro "O processo [nome do processo] não existe ou não possui nenhuma versão ativa" ao tentar iniciar uma solicitação, mesmo tendo liberado versão para o respectivo processo.

# Causa

O processo foi criado utilizando caracteres especiais no código do processo, especificamente o caractere "tabulação" (Tecla "TAB").

# Solução

Neste caso, não é possível utilizar caracteres especiais no código do processo.
