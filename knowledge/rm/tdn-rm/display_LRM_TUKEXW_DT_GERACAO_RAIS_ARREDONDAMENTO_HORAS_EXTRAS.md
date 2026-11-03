---
content_hash: 1e84535443738a0c48eea0708de6d5b9ddcfc98e8ee60ebab3198f8ea73cfa15
fetched_at: '2026-06-29T00:06:28.242039+00:00'
page_id: '233752869'
product: rm
source: tdn-rm
title: TUKEXW_DT_GERACAO_RAIS_ARREDONDAMENTO_HORAS_EXTRAS
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKEXW_DT_GERACAO_RAIS_ARREDONDAMENTO_HORAS_EXTRAS
version: 118
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | No caso de horas fracionadas, arredondar os valores até 30 minutos para um número inteiro inferior, e valores que excedem 30 minutos arredondar para um número inteiro superior. Exemplo: 1h30min=1h e 1h35min=2h. |
|  | Ajuste na rotina RAIS para alterar forma de arredondamento das horas extras. O sistema arredondava horas extras parciais e ao final realizava o somatório, perdendo assim frações de horas no arredondamento. Agora o sistema realiza o somatório e ao final realiza o realiza o arredondamento sobre o total, evitando assim perda de frações. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUKEXW TULCY2 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.11* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
