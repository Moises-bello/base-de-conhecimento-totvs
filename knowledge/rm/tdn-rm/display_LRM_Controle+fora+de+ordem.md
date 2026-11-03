---
content_hash: c44a2913e5291d3140a7cccec9417264f84914e1388e1262d1c50a1252673cec
fetched_at: '2026-06-29T00:05:51.224374+00:00'
page_id: '1050283593'
product: rm
source: tdn-rm
title: Controle fora de ordem
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+fora+de+ordem
version: 4
---

# Código de Referência

---

false

**control-out-of-order-in-member**

# Contexto

---

Quando um controle faz referência a outro controle, porém na listagem do relatório, os controles estiverem fora de ordem, não será possível obter corretamente os valores de referência.

Para abrir a tela de ordenação de controle, acesse o menu "Inicio" > "Ordenação de controles"

veja na imagem abaixo como identificar que o controle está fora de ordem.

Perceba que por mais que no design do relatório, o controle "Quantidade" esteja antes do controle "Expressão1", na configuração de ordenação dos controles, o controle Expressão1 é o primeiro.

# Solução

---

Antes de avançar com a aceleração do relatório, deve-se alterar a ordem dos controles para que seja possível a correta aceleração do relatório.
