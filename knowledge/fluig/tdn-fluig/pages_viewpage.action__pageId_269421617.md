---
content_hash: 55fb01a52cf2f9c96f95ed98610206ca11cb0c8c126db701ef419684b873210d
fetched_at: '2026-06-28T21:35:24.407121+00:00'
page_id: '269421617'
product: fluig
source: tdn-fluig
title: BPM 084 - Como definir o usuário a ser atribuído ao utilizar um Gateway Paralelo?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269421617
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

# Ocorrência

Tenho um atividade que é enviada para um *Gateway* Paralelo (*Fork*) e o mecanismo de atribuição não está configurado na atividade seguinte. Porém o mesmo não permite escolher o usuário para o envio.

# Solução

Pelo comportamento padrão do produto, ao utilizar um *Gateway* Paralelo e não definir um mecanismo de atribuição na próxima atividade, o fluxo será enviado para o primeiro usuário dentre os possíveis para o processo.

Essa mesma regra é aplicada aos componentes *Join*, Sinal e Envio de Email.
