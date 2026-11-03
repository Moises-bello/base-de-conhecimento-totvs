---
content_hash: b4bd243e8a9a011c04e07eecd74ec68333263945586b59227857fdd6e55b699e
fetched_at: '2026-06-29T00:06:18.259671+00:00'
page_id: '215483105'
product: rm
source: tdn-rm
title: TTRSST_DT_Avaliacao_De_Desempenho
type: documentation
url: https://tdn.totvs.com/display/LRM/TTRSST_DT_Avaliacao_De_Desempenho
version: 1
---

# AVALIAÇÃO DE DESEMPENHO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Função:** | *Avaliação de Desempenho* |
| **Situação/Requisito:** | *Avaliação de desempenho não configurada, mesmo após a execução do processo de configuração.* |
| **Solução/Implementação:** | *No processo de configuração da AD, os avaliados selecionados que não possuem nada a ser avaliado são removidos da avaliação. Portanto, caso sejam selecionados somente avaliados sem nada a avaliar, esses são removidos e quando a AD não possui nenhum participante, o processo é concluído mas ela não é configurada. Foi feito um ajuste no log do processo, que não conta esses participantes removidos como incluídos.* |
| **Conversores e Parâmetros:** | *Informe os conversores/parâmetros.* |
| **Chamados relacionados:** | *TTRSST* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.9* |

divs
