---
content_hash: 826c478ad672b4bdff7f3f522f52b764a657d65d6fc25ec3acf60bc23c0f195d
fetched_at: '2026-06-28T21:35:19.518361+00:00'
page_id: '210047041'
product: fluig
source: tdn-fluig
title: ECM - Como herdar os aprovadores de uma pasta pai para as subpastas?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210047041
version: 12
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto**: TOTVS Fluig Plataforma

# Ocorrência

Pastas criadas dentro de uma outra pasta com aprovação, não herdarão os aprovadores da pasta pai. Para atribuir os aprovadores da pasta pai, é necessário atribuí-los manualmente.

# Causa

Hoje esse é o comportamento padrão da plataforma, apenas a segurança é herdada e não os aprovadores.

# Solução

Para este caso, existem duas possibilidades:

* Editar a pasta criada, ir na aba aprovadores e selecionar a opção "Herdar aprovadores do pai". Assim as subpastas herdarão os níveis de aprovação e os respectivos aprovadores da pasta pai.

* Utilizar o evento beforeDocumentPublisher e copiar os aprovadores (quando existir) ao criar novas pastas.

Fique atento!

Para mais detalhes sobre aprovadores confira a documentação [Definir critérios de aprovação para pasta ou para documento](http://tdn.totvs.com/pages/viewpage.action?pageId=243008763).
