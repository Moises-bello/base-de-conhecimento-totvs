---
content_hash: 0b646734a53a231a99776774df3c05e94ec9daf36a8896c3bec15dfa9bbc9d1b
fetched_at: '2026-06-29T00:08:10.471667+00:00'
page_id: '240303752'
product: rm
source: tdn-rm
title: TUWYWH_DT_Lancamento_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TUWYWH_DT_Lancamento_Financeiro
version: 112
---

# Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Lançamento financeiro* |
| **Situação/Requisito:** | Ao gerar lançamento financeiro do tipo 20 - Total de IRRF marcando o parâmetro de rateio por centro de custo, sistema executa com sucesso, porém retorna valor zerado para o funcionário.  Ao gerar o mesmo lançamento desmarcando o parâmetro ou informando um rateio que o lançamento segue na parametrização do rateio ainda que este rateio não possua eventos em sua composição, sistema retorna valor para o lançamento normalmente. |
| **Solução/Implementação:** | Ajuste realizado para que os rateios fixos sejam retornados para a geração os lançamentos financeiros de IRRF |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUWYWH |
| **Requisito (ISSUE):** |  |

divs
