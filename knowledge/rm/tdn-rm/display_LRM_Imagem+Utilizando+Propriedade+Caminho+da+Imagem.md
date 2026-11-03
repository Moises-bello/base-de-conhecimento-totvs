---
content_hash: c65db9141a902b1a72efc47d776a6ee913c840d0c5ccbb1c1ff260b9de085e20
fetched_at: '2026-06-29T00:11:51.530954+00:00'
page_id: '848818956'
product: rm
source: tdn-rm
title: Imagem Utilizando Propriedade Caminho da Imagem
type: documentation
url: https://tdn.totvs.com/display/LRM/Imagem+Utilizando+Propriedade+Caminho+da+Imagem
version: 1
---

## Índice:

---

2

# Código de Referência

---

false

**image-using-image-path**

# Contexto

---

Para ser corretamente acelerado, controle Imagem não pode conter sua imagem atrelada à propriedade **'Caminho da Imagem'**, uma vez que o Smart View não é capaz de acessar imagens contidas em caminhos de máquina.

# Solução

---

## Antes da Aceleração, no RM Reports

No RM Reports, é necessário atrelar a imagem do controle Imagem ao campo **Fonte de Imagem**, pois este campo irá enviar corretamente a imagem ao Smart View, durante o processo de aceleração.

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2310

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO
