---
content_hash: 36a0b82ae852b8ea7eaaacf6d64040c506566821e86ff56a655128a159d0f457
fetched_at: '2026-06-29T00:10:59.218844+00:00'
page_id: '614372026'
product: rm
source: tdn-rm
title: Função QtdCoEmCurso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=614372026
version: 2
---

# Objetivo

---

Esta função de fórmula tem por objetivo informar o nº de créditos ou de disciplinas ou carga horária em curso e/ou disciplinas a serem matriculadas pelo aluno até um determinado período, ou de um período específico, de acordo com o operador. Ou seja, esta fórmula consegue somar em seu calculo as disciplinas selecionadas no momento da matrícula, função que a  não faz.

# Descrição

---

A função de fórmula QtdCoEmCurso somente poderá ser utilizada em fórmulas que estão vinculadas a um correquisito da disciplina na matriz curricular conforme é mostrado no cadastro abaixo. Caso não esteja vinculado a este cadastro, esta função não irá funcionar.

Na validação serão considerados o período, o operador("=", "<=", ">=", ">", "<") e o tipo ("C", "D", "CH") como parâmetro.

Ex: QtdCoEmCurso('1',"=","C");

# Retorno da função

---

Esta função de fórmula retornará o nº de créditos ou de disciplinas ou carga horária em curso e/ou disciplinas a serem matriculadas pelo aluno até um determinado período, ou de um período específico, de acordo com o operador.
