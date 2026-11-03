---
content_hash: 827b92e01b4eefc477b4e55887b855a4bbb8077b8268478b8d957b08884520d8
fetched_at: '2026-06-29T00:10:36.389034+00:00'
page_id: '532039887'
product: rm
source: tdn-rm
title: Função GravaCampoPL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532039887
version: 7
---

# Objetivo

---

Esta função de fórmula tem por objetivo gravar o valor do campo informado na tabela SMATRICPL.

# Descrição

---

A função de fórmula GRAVACAMPOPL poderá ser utilizada por todo o sistema, não possuindo restrição de uso. Na validação será considerado o campo ("CODSTATUS", "CODSTATUSRES", "PERIODO", "CODTURMA", "CR") e o valor do campo.

Exemplo: GRAVACAMPOPL("CODSTATUS",1)

Importante

Para alteração dos campos CODSTATUSRES e CR, não será executada validação de inadimplência, em nenhum dos níveis de ensino.

# Retorno da função

---

Esta função de fórmula irá gravar o valor do campo informado.
