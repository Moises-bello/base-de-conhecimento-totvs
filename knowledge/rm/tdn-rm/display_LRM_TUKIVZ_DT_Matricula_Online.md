---
content_hash: 829b85fe04eaee554aa962bfa2d490cce6d3ef07a895a8ab47159f676df47ca9
fetched_at: '2026-06-29T00:06:28.214370+00:00'
page_id: '233752415'
product: rm
source: tdn-rm
title: TUKIVZ_DT_Matricula_Online
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKIVZ_DT_Matricula_Online
version: 118
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Educacional* |
| **Função:** | *Matricula On-line* |
| **Situação/Requisito:** | *No momento em que o usuário clica no menu "Matrícula online" no portal esucacional acontece um erro e a tela inicial de matricula não é exibida. Esse erro acontece porque nesse momento o sistema tenta acessar a propriedade "length" de um objeto nulo.* |
| **Solução/Implementação:** | *Foi incluída uma validação para que no momento da exibição da tela inicial da matrícula online, o objeto chamado "valores" seja validado antes da utilização de sua propriedade "length" para que não aconteça erro caso ele esteja nulo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
