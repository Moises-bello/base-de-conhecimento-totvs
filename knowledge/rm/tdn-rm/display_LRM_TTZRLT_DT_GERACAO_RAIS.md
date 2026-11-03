---
content_hash: 40f2a9869d8406e0e6f12294a5495fb3575f37b27d99a9bbdab77d739d4b1977
fetched_at: '2026-06-29T00:06:23.378710+00:00'
page_id: '224101294'
product: rm
source: tdn-rm
title: TTZRLT_DT_GERACAO_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTZRLT_DT_GERACAO_RAIS
version: 120
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | Campos de horas extras trabalhadas está arredondando diferente entre Delphi.  Tratar o espaçamento após os caracteres. 122 a 126 05 Alfanum CTPS - (série) |
| **Solução/Implementação:** | Ajuste na rotina Rais para arredondar valores de horas extras conforme era arredondado no Delphi.  Ajuste em campo de Série de CTPS para retirar alfabéticos e espaços em branco conforme validador, preenchendo com zeros à esquerda |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTZRLT TUB661 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.9* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
