---
content_hash: c15cabfe6622ad9a50445523d3edf9dd546d84b9d731087f8bc40482a1a95f08
fetched_at: '2026-06-29T00:09:02.211130+00:00'
page_id: '379298163'
product: rm
source: tdn-rm
title: 3251025 EDUCACIONAL01-5611 DT Validação entre datas de colação de grau e emissão
  de diploma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379298163
version: 86
---

# VALIDAÇÃO ENTRE DATAS DE COLAÇÃO DE GRAU E EMISSÃO DE DIPLOMA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Matrícula no curso* |
| **Situação/Requisito:** | *Ao tentar alterar informações no cadastro do curso, o sistema está validando a diferença entre as datas de colação e emissão de diploma, mesmo sendo iguais.* |
| **Solução/Implementação:** | *Foi verificado que o sistema estava considerando a parte horária na validação das datas e havia uma diferença de alguns milésimos de segundos entre elas, o que gerava a mensagem de validação.*  *Foi realizada uma alteração para que seja validada apenas a data, ignorando a parte horária.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
