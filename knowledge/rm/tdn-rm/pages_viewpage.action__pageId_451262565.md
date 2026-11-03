---
content_hash: 5682c9926c80797a97ed9fc4b2aa1160592b8854c0ca6708d886a4639bef5a5c
fetched_at: '2026-06-29T00:09:58.141693+00:00'
page_id: '451262565'
product: rm
source: tdn-rm
title: 4786431 EDUCACIONAL01-7923 DT Matrícula de aluno básico com mensagem de violação
  de chave primária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451262565
version: 77
---

# MATRÍCULA DE ALUNO NO BÁSICO APRESENTANDO MENSAGEM DE VALIDAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Matrícula de alunos no ensino básico* |
| **Situação/Requisito:** | *Ao tentar matricular um aluno que foi reprovado em um período letivo anterior, o sistema apresenta uma mensagem de violação de chave primária.* |
| **Solução/Implementação:** | ***Foi identificado que o registro do aluno na tabela SHABILITACAOALUNO foi gravado com espaços no final do código RA. Dessa forma, não estava sendo possível identificar a matrícula existente do período anterior e o sistema estava tentando realizar a inclusão de novo registro na tabela SHABILITACAOALUNO e gerava a mensagem apresentada.***  ***Foi realizado um tratamento no sistema para que os caracteres de espaço antes e depois do código RA sejam ignorados, ao realizar a busca de matrículas existentes dos alunos.*** |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
