---
content_hash: 3469478ed70c8d9e30a67f0fd5b7ca139f4144c78a12cf1d34b71cdc20bc2da3
fetched_at: '2026-06-29T00:06:27.379554+00:00'
page_id: '232820852'
product: rm
source: tdn-rm
title: TUJ225_DT_GERACAO_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TUJ225_DT_GERACAO_RAIS
version: 121
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | Erro no validador da RAIS para funcionário demitido no ano anterior ao ano base e projetado para o ano seguinte: Validador aponta erro indicando que funcionário não possui remuneração no ano base. |
| **Solução/Implementação:** | Foi incluído o parâmetro "Limitar data projetada para janeiro do ano seguinte" na tela de Geração da RAIS para casos de demissão no ano anterior ao ano base e que a projeção de dias de aviso prévio somado à essa data ultrapassa o mês de janeiro do ano base, evitando assim erro no validador da RAIS que entende que o funcionário deveria ter remuneração no ano base. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUJ225 TUJGUI TUJTH4 TUJRBJ |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.10* |

divs
