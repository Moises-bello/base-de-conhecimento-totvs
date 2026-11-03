---
content_hash: db0563db03ea4b229f0f0dad187e19fa5b9aa63548513e6f56385bdb8281f16f
fetched_at: '2026-06-29T00:08:52.576263+00:00'
page_id: '341221306'
product: rm
source: tdn-rm
title: DT Evolução na frequência diária no Portal do professor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=341221306
version: 1
---

# EVOLUÇÃO NA FREQUÊNCIA DIÁRIA NO PORTAL DO PROFESSOR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Totvs gestão Educacional |
| **Módulo:** | Portal CorporeRM (Portal do Professor) |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Frequência diária | Chamada |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Etapas de falta da turma/disciplina | Etapa de falta | |  |  | |
| **Cadastros Iniciais:** | * Turma/Disciplina * Professor da turma/disciplina * Horário da turma/disciplina * Professor do horário da turma/disciplina * Plano de aula * Etapa de Falta da turma/disciplina |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | Informe o requisito relacionado (Issue). |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | SQL e Oracle |

## Descrição

Ao acessar o **Portal CorporeRM (Portal do professor)**, e selecionar a funcionalidade "**Frequência diária**"  os campos: **Data frequência de** e **Data Frequência até** o portal irá preencher as respectivas datas com a data atual automaticamente (como exemplo a data atual é 27/02/2018 e está compreendida entre as datas início/término da etapa), permitindo maior agilidade na realização da chamada dos alunos.

IMPORTANTE!!!

Caso exista mais de uma etapa de falta que compreenda na data atual ou etapas sem data início/término, o sistema não irá carregar a etapa automaticamente e o usuário deverá selecionar a etapa desejada, mantendo o comportamento anterior do sistema.
