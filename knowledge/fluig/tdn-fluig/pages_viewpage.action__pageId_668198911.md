---
content_hash: 0c86ab0ce850887b7655073bc470422fccbbb4479006a3782c023fd28470e8c7
fetched_at: '2026-06-28T21:35:28.670317+00:00'
page_id: '668198911'
product: fluig
source: tdn-fluig
title: Desenvolvimento de Formulários - Editor WEB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=668198911
version: 1
---

# Índice

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é descrever o desenvolvimento de formulários pelo editor web no fluig.

# Pré-requisitos

---

Antes de iniciar o desenvolvimento de formulários entenda como .

# Regras de formulário

---

No editor web de formulário é possível criar validações avançadas para os campos, dependendo da atividade.

Para isso, no editor, clique em “Regras de formulário”, Adicionar, selecione o campo e a atividade e em ação, escolha “Validar”. Clique na lupinha.

Essa validação serve para **bloquear** alguns valores. O usuário não vai informar quais são os valores permitidos, pelo contrário, ele vai configurar quais os valores **proibidos**.

Por exemplo, se quiser configurar para que um campo **idade** só permita valores maiores que **18**, a configuração deve ser: **idade menor 18**. Ou seja, é uma validação **restritiva** e não **permissiva**.

No caso de uma combinação de fatores, como idade entre 12 e 18 anos:

Ou então, caso queira excluir um determinado grupo intermediário, ou seja, ninguém com idades entre 18 e 60:
