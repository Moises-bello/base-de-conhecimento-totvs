---
content_hash: 9ab4f947f881eece26d6401fa57f2579da7b1c5358f47bde59ee960cea03b242
fetched_at: '2026-06-29T00:11:42.710370+00:00'
page_id: '795905097'
product: rm
source: tdn-rm
title: Regerar plano(s) de aula(s) existente(s)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795905097
version: 17
---

O processo de Regerar plano(s) de aula(s) existente(s) tem como objetivo, regerar os plano(s) de aula(s) pra que a Instituição possa realizar alguma manutenção, e consiste na exclusão dos planos existentes no período, seguido da geração de novos planos de aula.

Este processo é recomendado apenas para as Turmas/disciplinas que possuírem Planos de Aula **previamente gerados** e a**data final** informadadeverá ser a **última data do plano de aula gerado**.

Validações realizadas no processo

A partir da versão 12.1.2302.224

Ao executar o processo para regerar o plano de aula, o sistema **não irá regerar os planos de aula para**:

* Planos de Aula com **arquivo em anexo;**
* Planos de Aula com **frequência lançada;**
* Planos de Aula com **frequência liberada;**

Caso o período informado tenha algum plano de aula que se encaixe em algum dos critérios acima, será apresentado o detalhamento no log, contendo a informação da Turma/disciplina, Aula, Data e Código do horário.
