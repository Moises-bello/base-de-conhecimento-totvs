---
content_hash: e2527c8fc4ba6e0176ab9b160c1d970abb71a922ebb093fa4400d07cd5438a58
fetched_at: '2026-06-29T00:08:36.478255+00:00'
page_id: '284475919'
product: rm
source: tdn-rm
title: 924244 EDUCACIONAL01-1509 DT Geracao de lancamento
type: documentation
url: https://tdn.totvs.com/display/LRM/924244+EDUCACIONAL01-1509+DT+Geracao+de+lancamento
version: 100
---

# GERAÇÃO DE LANÇAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Geração de Lançamento |
| **Situação/Requisito:** | Ao gerar lançamentos para várias parcelas, com o sistema parametrizado para utilizar agrupamento de lançamentos, caso as informações das parcelas (registro acadêmico, responsável financeiro, data de vencimento e código do serviço) fossem iguais, a referência dos lançamentos gerados não respeitava a ordem dos identificadores das parcelas. |
| **Solução/Implementação:** | Ajustes para considerar o identificador da parcela nos diversos tipos de agrupamento de boletos do sistema (aluno, contrato, responsável financeiro) quando todos os dados das parcelas forem iguais, respeitando dessa forma a ordenação das parcelas por seus identificadores. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 924244 |
| **Requisito:** | N/A |

divs
