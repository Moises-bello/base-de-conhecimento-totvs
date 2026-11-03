---
content_hash: 3c473d8e90b06838bf97a60027403a28c3483213a030255bbdc893811df7b6eb
fetched_at: '2026-06-29T00:08:33.909378+00:00'
page_id: '274629386'
product: rm
source: tdn-rm
title: Financeiro01-694 Boletos
type: documentation
url: https://tdn.totvs.com/display/LRM/Financeiro01-694+Boletos
version: 98
---

# Lançamentos-Boletos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Boletos |
| **Situação/Requisito:** | Ao desvincular um lançamento de um boleto que possui valores nos campos Multa ao Dia, Juros ao dia e Desconto, o sistema está alterando os valores desses campos para valores diferentes do que estavam antes do lançamento ser vinculado. |
| **Solução/Implementação:** | Ajustado o cálculo dos valores de desconto, juros e multa do boleto, utilizado pela execução dos processos de Vincular e Desvincular lançamentos do boleto. Estes processos terão o mesmo comportamento do cálculo de desconto, juros e multa do processo de geração de boleto. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000268 |

divs
