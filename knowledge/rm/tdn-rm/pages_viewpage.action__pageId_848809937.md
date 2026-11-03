---
content_hash: a31cc6a32ecfe3d2de14b13579f38c74d23d61a8906e5b81a36b7756c56b0980
fetched_at: '2026-06-29T00:11:51.491066+00:00'
page_id: '848809937'
product: rm
source: tdn-rm
title: Mais de uma Regra de Formatação atrelada ao Controle
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=848809937
version: 3
---

## Índice:

---

2

# Código de Referência

---

false

**control-with-more-than-one-conditional-formatting**

# Contexto

---

Atualmente não é possível acelerar um relatório para o **Smart View** com controles que possuam múltiplas formatações condicionais.

No Exemplo Abaixo, existem duas regras de formatação:

A primeira pinta o fundo e a fonte de verde e coloca as bordas pontilhadas quando o estado for igual a MG.

A primeira pinta o fundo e a fonte de vermelho e coloca as bordas pontilhadas quando a cidade for diferente de Salvador

Quando fizer a conversão para o Smart View, iremos enviar apenas a primeira regra.

Sendo assim, o resultado fica diferente do esperado.

# Possíveis Soluções

---

## Após aceleração para o **Smart View.**

No **Smart View**, vamos alterar as regras de formatação para atender as duas formatações

No design do relatório, editar a expressão "Nome do estilo", para podermos atualizar a mesma

Inserir a nova regra de formatação com duas condicionais, para assim conseguirmos utilizar as duas regras de formatação.

Após inserirmos corretamente a condicional, o relatório passa a funcionar com a formatação correta.

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2310

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO
