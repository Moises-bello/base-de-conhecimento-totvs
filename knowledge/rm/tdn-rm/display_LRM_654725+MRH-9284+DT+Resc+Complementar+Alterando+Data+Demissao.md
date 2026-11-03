---
content_hash: 25149c82b5f3a4e42c5f801ee6e7cfa8d798fdc2fbc84932e892c3bf154b3d4e
fetched_at: '2026-06-29T00:08:31.852210+00:00'
page_id: '273313682'
product: rm
source: tdn-rm
title: 654725 MRH-9284 DT Resc Complementar Alterando Data Demissao
type: documentation
url: https://tdn.totvs.com/display/LRM/654725+MRH-9284+DT+Resc+Complementar+Alterando+Data+Demissao
version: 110
---

# RESCISÃO COMPLEMENTAR COM MUDANÇA DE DATA DE DEMISSÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Rescisão Complementar |
| **Situação/Requisito:** | Foi calculada a rescisão de um funcionário com uma data de demissão, e no mês seguinte o usuário verificou que o dia estava incorreto.  Foi alterada a data da demissão para um dia a mais. Ao calcular a rescisão complementar o evento de saldo salário continua considerando a data da demissão utilizada na rescisão original. |
| **Solução/Implementação:** | Ajuste no cálculo da rescisão complementar para aceitar alteração na data da demissão da rescisão original, e alterar os dias trabalhados pagos no evento de saldo salário. |
| **Tickets relacionados:** | MRH-9284 |

divs
