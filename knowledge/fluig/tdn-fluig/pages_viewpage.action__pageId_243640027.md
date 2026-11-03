---
content_hash: 80bc195b01ba489009c17250a102da1627cb9fbdc92265130634631dc0a51232
fetched_at: '2026-06-28T21:35:23.018516+00:00'
page_id: '243640027'
product: fluig
source: tdn-fluig
title: DES - Alterar dados do formulário de uma solicitação a partir de outro formulário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243640027
version: 3
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Como alterar o valor de um campo de formulário de uma solicitação já aberta a partir de determinada ação em um novo formulário criado?

# Solução

Para alterar um outro formulário, além do formulário do processo atual, a partir da movimentação de uma solicitação, você poderá utilizar o webservice ECMCardService, método updateCardData, conforme documentação . Com este método é possível alterar dados de um formulário diferente do formulário da solicitação aberta em tela. A chamada do webservice deverá estar em um evento do processo que seja executado após o salvamento da alteração do formulário. Para mais informações sobre eventos do processo e desenvolvimento de workflow acesse .
