---
content_hash: e0c28d0c69c8e47cd659b558cefe0de91390c7d3fe4a819735f057bfb0636843
fetched_at: '2026-06-29T00:08:40.833996+00:00'
page_id: '286509563'
product: rm
source: tdn-rm
title: 1244202 EDUCACIONAL01-2152 Digitação de Nota e Faltas Etapas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286509563
version: 102
---

# Digitação de Nota e Faltas Etapas

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Digitar notas e faltas da etapa por aluno* |
| **Situação/Requisito:** | *O sistema não esta respeitando as regras de seguranças informadas para os campos da* *tabela SNOTAETAPA* *na tela de digitação de nota e falta para o aluno.* |
| **Solução/Implementação:** | *Foi corrigido o erro para que a tela de digitação do aluno respeite as normas de segurança informadas para a tabela SNOTAETAPA.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs

Ao acessar o Menu de "Digitação de Notas e Faltas de etapa por aluno", o sistema bloqueia a digitação das Notas mas permite a digitação das faltas e aulas dadas.

Sendo que este dado é gravado na tabela SNOTAETAPA que está, neste perfil, bloqueada para alteração logo não deveria ser possível realizar esta ação
