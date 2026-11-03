---
content_hash: 287e8e6a28501ba71da8a39a918999d1a3964b24ce8835a27b4be798d921a986
fetched_at: '2026-06-29T00:08:23.171332+00:00'
page_id: '269450684'
product: rm
source: tdn-rm
title: 97616_DT_Listagem_Extratos
type: documentation
url: https://tdn.totvs.com/display/LRM/97616_DT_Listagem_Extratos
version: 114
---

# RM Reports - Listagem de Extratos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Função:** | Listagem de Extratos |
| **Situação/Requisito:** | Ao gerar o relatório padrão (FINREL0020 - Listagem de extrato) do book de relatórios, o mesmo apresenta todos os lançamentos como se fossem de uma unica conta caixa, o que implica no totalizador do saldo ao fim do relatório e gera um valor irreal para a conta caixa. |
| **Solução/Implementação:** | Foi necessário ajustar todo o relatório para que a quebra da conta caixa fosse feita corretamente, além da quebra da conta caixa que foi ajustada no cabeçalho do detalhe,  também foi necessário ajustar o campo de saldo anterior do relatório, o saldo anterior do relatório atual não estava correto, então foi feito também o ajuste deste campo.  OBS: Não houve alteração no código fonte do sistema, apenas ajuste no relatório do RM Reports. O relatório ajustado será publicado oficialmente nos canais de comunicação com o cliente. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *97616* |
| **Requisito (ISSUE):** | *N/A* |

divs
