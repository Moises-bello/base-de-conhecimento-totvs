---
content_hash: 3be6d6b9cc791c5a1a79a54ac6c1b2e3891b13547846dd0cb8d35f873f901013
fetched_at: '2026-06-29T00:09:58.232928+00:00'
page_id: '451279012'
product: rm
source: tdn-rm
title: Provedor - Etapas de nota e falta do aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/Provedor+-+Etapas+de+nota+e+falta+do+aluno
version: 4
---

# Objetivo

---

Este provedor de dados é utilizado quando se deseja montar um relatório que exibirá as notas/faltas de etapas do aluno.

# Como configurar

---

Ao adicionar este provedor de dados é necessário vincular a um item de "subdetalhe" do relatório conforme é mostrado abaixo:

Além disso é necessário criar um parâmetro não visível de nome CODVAZIO e descrição Vazio, exatamente conforme abaixo. Este parâmetro será vinculado aos parâmetros do provedor que não serão utilizados.

Para fazer o vínculo do parâmetro vazio aos parâmetros do provedor que não serão utilizados, deverá acessar o "detalhe" do "subdetalhe" onde o provedor foi vinculado, acessar a grade de propriedades, localizar o item **Parâmetros da fonte de dados** clicar para alterar, com isso será aberta uma janela com todos os parâmetros da fonte de dados, localize todos os parâmetros que não serão utilizados e informe o parâmetro vazio criado no passo anterior.
