---
content_hash: 58442027f4c0302681dc5400fddf71e73a3d920d38f4b79cfc6136d525a5bdf1
fetched_at: '2026-06-29T00:08:40.820955+00:00'
page_id: '286508154'
product: rm
source: tdn-rm
title: '1280726 PORTALMOBILE01-1470 DT Requisito Educacional(Edu): Integração Protheus'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286508154
version: 102
---

# Requisito Educacional(Edu) Integração Protheus - RM.Atualizador.exe

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Educacional |
| **Função:** | Requisito Educacional(Edu) Integração Protheus |
| **Situação/Requisito:** | No RM.Atualizador.exe, ao realizar a verificação de requisitos do educacional (Integração Protheus), o sistema estava apresentando erro ao acessar a classe de parâmetros pela falta da coluna IMAGEM da tabela SPARAM. |
| **Solução/Implementação:** | Realizado ajuste no TOTVS Educacional em relação a validação requisitos do "RM.Atualizador.exe", pois ao realizar a validação do requisito "Integração Protheus" a classe na versão 12.1.17 já está com a coluna SPARAM.IMAGEM, mas nesse momento de validação de requisitos o RM.Atualizador.exe não executou o script de criação dessa coluna na base, ocasionando assim o erro "Invalid column name 'IMAGEM'." Foi realizado ajuste no educacional, para que seja carregado essa coluna apenas se o script "CN.2017.05\_01" esteja executado na base em questão. |
| **Conversores e Parâmetros:** | *N/A* |
| **Issues relacionadas:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
