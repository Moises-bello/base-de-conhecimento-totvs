---
content_hash: bc5a986d3f1b32f7249b667c0c7abe93d172011a5ffeda6e064e2b91695c3d9d
fetched_at: '2026-06-29T00:06:22.571891+00:00'
page_id: '223922578'
product: rm
source: tdn-rm
title: TTZDUR_DT_GERACAO_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTZDUR_DT_GERACAO_RAIS
version: 121
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | Ao gerar a RAIS com um perfil que tenha sido convertido do Delphi, quando excluímos algum evento dos parâmetros da coligada, no final da execução ocorre a seguinte mensagem: “Informações sobre a linha excluída não podem ser acessadas através da linha.” |
| **Solução/Implementação:** | Ajuste na rotina Rais para validar linhas excluídas e não tentar acessá-las |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTZDUR TTZSG6 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.9* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
