---
content_hash: cd16afc523737079bb14ccc37655ab4d55d5fb7d28f0f4ca7b589507dbf98b40
fetched_at: '2026-06-29T00:06:30.044345+00:00'
page_id: '235309938'
product: rm
source: tdn-rm
title: TULJMC_DT_Contabilizacao_Novo_Modelo_Com_Contrato_Com_Mais_De_Um_Servico
type: documentation
url: https://tdn.totvs.com/display/LRM/TULJMC_DT_Contabilizacao_Novo_Modelo_Com_Contrato_Com_Mais_De_Um_Servico
version: 119
---

# CONTABILIZAÇÃO NO NOVO MODELO QUANDO O CONTRATO POSSUI PARCELAS COM MAIS DE UM SERVIÇO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Contabilização por Competência* |
| **Situação/Requisito:** | *Sistema gerava contabilizações indevidas de cancelamento ou aumento quando o contrato possuía parcelas com mais de um serviço* |
| **Solução/Implementação:** | Sistema passou a calcular a diferença entre o contábil e o financeiro por serviço a fim de se evitar cancelamentos ou aumentos indevidos para contratos com parcelas financeiras de mais de um serviço.  Alteração ao setar o valor cancelado e valor de aumento de forma que não se gerem contabilizações de cancelamento ou de aumento por diferenças de um centavo (0,01) em parcelas diferentes da última parcela contábil. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUNTA8* |
| **Requisito (ISSUE):** | *N/A* |

divs
