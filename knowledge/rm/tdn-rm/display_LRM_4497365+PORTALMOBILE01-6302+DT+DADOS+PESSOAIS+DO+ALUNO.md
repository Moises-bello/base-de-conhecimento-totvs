---
content_hash: e559eeaffb95c86749f9cc63cf12fca34c599150e050cc4e54f124cb20614ee4
fetched_at: '2026-06-29T00:09:53.159449+00:00'
page_id: '440839062'
product: rm
source: tdn-rm
title: 4497365 PORTALMOBILE01-6302 DT DADOS PESSOAIS DO ALUNO
type: documentation
url: https://tdn.totvs.com/display/LRM/4497365+PORTALMOBILE01-6302+DT+DADOS+PESSOAIS+DO+ALUNO
version: 1
---

# DADOS PESSOAIS DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Dado pessoais do aluno |
| **Situação/Requisito:** | Ao acessar com um aluno no portal corpore.net que possuí mais de um contexto, é exibido a tela de seleção de contexto e por baixo dessa tela estava sendo exibido os dados pessoais de outro aluno, pois na base existia um aluno com o campo "RA" vazio, assim o portal carregava seus dados quando o aluno logado ainda não tinha selecionado o contexto. |
| **Solução/Implementação:** | Ajuste para que não execute a consulta quando ainda não tenha nenhum RA selecionado. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
