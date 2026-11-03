---
content_hash: f2715c00ab779d3982732a3082db30cf09dd6037a27e4fd269ad0946a551bf61
fetched_at: '2026-06-29T00:09:45.821848+00:00'
page_id: '433254067'
product: rm
source: tdn-rm
title: 4314601 EDUCACIONAL01-7116 DT Seleção de habilitação na matrícula de aluno
  - Mensagem de referência de objeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=433254067
version: 72
---

# SELEÇÃO DE HABILITAÇÃO NA MATRÍCULA DE ALUNO - MENSAGEM DE REFERÊNCIA DE OBJETO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Matrícula de aluno no ensino básico* |
| **Situação/Requisito:** | *Ao tentar selecionar a série/habilitação do aluno no processo de matrícula, o sistema está apresentando a mensagem de erro de referência de objeto.* |
| **Solução/Implementação:** | *Foi detectado um efeito colateral no tratamento do tamanho do campo NOMECURSO, que sofreu um ajuste em seu tamanho..*  *Dessa forma, em bases que, ainda, não rodaram o script para o ajuste do tamanho, estão apresentando essa mensagem de erro na tela.*  *Foi realizado um tratamento para que a mensagem seja tratada e não mais exibida.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
