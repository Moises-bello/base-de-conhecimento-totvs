---
content_hash: 6a4426dbe1d31decbd4e0f8a8ccd50f353e5ab3b9e8e875a4c50fab515dc8a84
fetched_at: '2026-06-29T00:08:33.022385+00:00'
page_id: '274002142'
product: rm
source: tdn-rm
title: 707787 FINANCEIRO01-529 DT ACORDO GERADORES DE IRRF
type: documentation
url: https://tdn.totvs.com/display/LRM/707787+FINANCEIRO01-529+DT+ACORDO+GERADORES+DE+IRRF
version: 107
---

# Acordo de acordo de lançamentos geradores de IRRF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Inclusão de Acordo |
| **Situação/Requisito:** | Cliente gerou um acordo de Lançamento que gera IRRF, com uma Parcela que possui o mesmo tipo de documento (Gera IR). Após a geração selecionou esta parcela, com outro lançamento que Gera IRRF. Ao gerar um novo acordo para a Parcela mais esse terceiro lançamento o sistema bloqueia a geração pois as classificações são distintas. (15 - Gerado Por Acordo Versus 5 - Gera IR) |
| **Solução/Implementação:** | Adicionada a validação da database de geração do Imposto de Renda para os lançamentos selecionados para geração do acordo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000084 |

divs
