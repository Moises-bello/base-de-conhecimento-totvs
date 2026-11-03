---
content_hash: 408211c296cc7cccd958f544af773b30dc75caaf1d8cc6a20772ba6d32c4e78a
fetched_at: '2026-06-29T00:08:36.233891+00:00'
page_id: '284469148'
product: rm
source: tdn-rm
title: 1036429 EDUCACIONAL01-1471 DT Preparação de dados para o censo escolar e SISTEC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284469148
version: 104
---

# PREPARAÇÃO DE DADOS PARA O CENSO ESCOLAR E SISTEC

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Preparação de dados para o censo escolar e SISTEC* |
| **Situação/Requisito:** | *Ao executar o processo de preparação de dados para o Censo escolar e SISTEC, o sistema apresenta um erro acesso a uma posição inválida.* |
| **Solução/Implementação:** | *Foi detectado que o código da disciplina cadastrado para a turma/disciplina está em minúsculo. Essa diferença de capitalização estava gerando um erro ao tentar localizar a disciplina da Turma/Disciplina.*  *Foi realizado um ajuste no sistema para considerar sempre o código do cadastro da disciplina da busca, evitando erros por diferenças na capitalização da Turma/Disciplina.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
