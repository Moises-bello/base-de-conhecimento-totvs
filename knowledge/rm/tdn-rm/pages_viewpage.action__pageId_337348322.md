---
content_hash: f3af929ee616daecce5b69e6b133dd21c099bc1683e763bedabb249f1974442c
fetched_at: '2026-06-29T00:08:51.549913+00:00'
page_id: '337348322'
product: rm
source: tdn-rm
title: DT Pagamento com cartão de crédito/débito modalidade buypage Cielo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337348322
version: 2
---

# Pagamento com cartão de crédito/débito modalidade buypage Cielo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira. |
| **Função:** | Pagamento com cartão de crédito/débito modalidade buyPage Cielo |
| **Situação/Requisito:** | Quando é feito um pagamento utilizando cartão de crédito/débito na modalidade buyPage Cielo, a informação de código da autorização e NSU não são gravados no sistema. Essas informações são importante caso seja necessário validar a transação junto a Cielo. |
| **Solução/Implementação:** | Foi criado na tabela de transação de cartão e crédito (FINTEGRACAOCARTAO) os campos "NSU" e "CODAUTORIZACAO". Esses campos serão responsável por armazenar as informações de "Cód. de autorização retornado pelo emissor do cartão" e "Num. seq. único retornado pela adquirente (NSU)".  Foi também disponibilizado na visão de histórico de transação, os campos "Id. Boleto", "NSU Adquirente", "Cod. de autorização emissor cartão" e "NSU Sitef" que também poderão ser usado para efetuar filtros |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FINANCEIRO01-2315 |
