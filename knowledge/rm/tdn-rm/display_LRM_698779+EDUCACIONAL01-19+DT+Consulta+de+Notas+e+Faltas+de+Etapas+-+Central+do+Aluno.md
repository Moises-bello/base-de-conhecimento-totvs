---
content_hash: 107e87c0e5a7ba60a4d1eb7e9fd7d0863fbf805a5f84cbb78a04394727fa7c18
fetched_at: '2026-06-29T00:08:31.679110+00:00'
page_id: '273305286'
product: rm
source: tdn-rm
title: 698779 EDUCACIONAL01-19 DT Consulta de Notas e Faltas de Etapas - Central do
  Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/698779+EDUCACIONAL01-19+DT+Consulta+de+Notas+e+Faltas+de+Etapas+-+Central+do+Aluno
version: 108
---

# CONSULTA DE NOTAS E FALTAS DE ETAPAS - CENTRAL DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Consulta de Notas e Faltas de Etapas - Central do Aluno* |
| **Situação/Requisito:** | *Ao liberar no perfil o item Matrícula e Avaliação | Notas e faltas | Notas e Faltas da etapa é liberado esta consulta na central do aluno também de notas e faltas, entretanto estas permissões deveriam estar separadas, pois a primeira é referente a digitação de notas e faltas através do menu e a segunda é apenas consulta na central do aluno.* |
| **Solução/Implementação:** | *Ajuste nas permissões de notas e faltas para que seja separado a permissão de consultar notas e faltas de etapa na central do aluno e na digitação de notas e faltas de etapas no menu. Com isso um novo parâmetro, chamado Visualizar consulta de notas e faltas na central do aluno, nos Parâmetros Educacionais | Aba Notas e Faltas foi criado para dar a permissão de Visualizar consulta de notas e faltas na central do aluno, onde este parâmetro nasce com permissão para todos os perfis.* |
| **Conversores e Parâmetros:** | *No cadastro do Perfil do Usuário | Anexo Parâmetros Educacionais | Aba Notas e Faltas:*   * ***Visualizar consulta de notas e faltas na central do aluno,** tem função de permitir a visualização da consulta de notas e faltas de etapas na central do aluno ou não.* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
