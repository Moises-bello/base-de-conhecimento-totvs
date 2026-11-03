---
content_hash: 1c09e447bdcfecf4392818d604aa288efe216893e032359d1a28e876fcc26b96
fetched_at: '2026-06-29T00:06:28.170330+00:00'
page_id: '233750292'
product: rm
source: tdn-rm
title: TUGUBP_DT_GERACAO_RAIS_TRANSFERENCIA_SEM_ONUS
type: documentation
url: https://tdn.totvs.com/display/LRM/TUGUBP_DT_GERACAO_RAIS_TRANSFERENCIA_SEM_ONUS
version: 121
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | *Ao gerar a RAIS com o parâmetro Projeta aviso prévio indenizado na data de desligamento, o sistema não leva os funcionários demitidos tipo 5 Transferências sem ônus para cedente.* |
| **Solução/Implementação:** | Ajuste na rotina da Rais para considerar demitidos com tipo 5 Transferidos sem onus cedente. Foi tratada condição para campo TEMAVISOPREVIO na tabela PFUNC nulo. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUGUBP TUKYJO |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.10* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
