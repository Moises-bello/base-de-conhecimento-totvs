---
content_hash: a72a4fa667e53a6a10b5ba480c3accc77b5d3278f058397a7c4abcaeacf52a73
fetched_at: '2026-06-29T00:09:58.302657+00:00'
page_id: '452415795'
product: rm
source: tdn-rm
title: Função DiscEmCurso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452415795
version: 1
---

# Objetivo

---

Esta função de fórmula tem por objetivo validar se uma disciplina está ou não em curso no momento da matrícula ou na sugestão de disciplinas.

# Descrição

---

A função de fórmula DiscEmCurso somente poderá ser utilizada em fórmulas que estão vinculadas a um pré-requisito ou correquisito da disciplina na matriz curricular conforme é mostrado no cadastro abaixo. Caso não esteja vinculado a este cadastro, esta função não irá funcionar. O único parâmetro que esta função precisa é o código da disciplina, sendo que este deverá ser igual ao que foi cadastrado, ou seja, respeitando as letras em maiúsculo e minúsculo.

Na validação serão consideradas as disciplinas que estão sendo matriculadas e as que já estão em curso pelo aluno no momento da matrícula. Outro ponto que é feita a validação é na sugestão de disciplinas, ou seja, ao abrir a sugestão o sistema também irá executar as fórmulas que estão vinculadas neste cadastro para exibir ou não a disciplina a ser sugerida.

# Retorno da função

---

Esta função de fórmula irá retornar "S", caso a disciplina estiver em curso ou "N" caso não estiver em curso.
