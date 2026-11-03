---
content_hash: 2411bb769a938f2f7c2166a3ea7155637fd8f4dbb0085952a155d6b4ca8946a6
fetched_at: '2026-06-29T00:08:43.585312+00:00'
page_id: '305037408'
product: rm
source: tdn-rm
title: 1242494 FINANCEIRO01-2280 Tipo Contábil default em acordo financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=305037408
version: 92
---

# TIPO CONTÁBIL DEFAULT NA GERAÇÃO DE ACORDO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Geração de acordo. |
| **Situação/Requisito:** | Para lançamento origem da geração de acordo com tipo contábil igual a "Contábil" o sistema usa esse valor como default no lançamento gerado (quando nenhum valor informado na tela pelo usuário). |
| **Solução/Implementação:** | Retornamos para o comportamento anterior, quando o lançamento origem possuir o ***Tipo Contábil*** como "Contábil" ou "Baixa Contábil" o default usado no(s) lançamento(s) gerado(s) pelo acordo será "Baixa Contábil". Caso o usuário informe um valor para o campo na tela do processo esse será usado. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1242494. |
| **Requisito:** | FINANCEIRO01-2280. |

divs
