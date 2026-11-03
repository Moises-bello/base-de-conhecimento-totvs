---
content_hash: 24443c4822e739921c983c6ed6c97e5ce5cb473272cf965974fa442b09a03758
fetched_at: '2026-06-29T00:08:58.949603+00:00'
page_id: '362449263'
product: rm
source: tdn-rm
title: 2920728 EDUCACIONAL01-5081 DT Cadastro Turmas Predio Bloco Sala Desabilitado
type: documentation
url: https://tdn.totvs.com/display/LRM/2920728+EDUCACIONAL01-5081+DT+Cadastro+Turmas+Predio+Bloco+Sala+Desabilitado
version: 86
---

# TURMAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Turmas |
| **Situação/Requisito:** | Quando o cliente acessa o cadastro de turma, os campos "Bloco" e "Sala" ficam desabilitados mesmo com campo "Prédio" preenchido. Para que os campos "Bloco" e "Sala" sejam habilitados, é necessário clicar no lookup do prédio e selecionar o prédio novamente. |
| **Solução/Implementação:** | Foi feito o ajuste para tratar corretamente a validação dos campos ao iniciar a tela, assim se o campo "Prédio" estiver preenchido o campo "Bloco" ficará habilitado e que habilita o campo "Sala", o campo "Sala" só ficará habilitado se os campos "Prédio" e "Bloco" estiverem preenchidos pois este campo utiliza filtros de Prédio e Bloco para listar as salas. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
