---
content_hash: 3305524830e4e676c47a313ab1f5e2154d37db253227fcee59d120a6525ccd40
fetched_at: '2026-06-29T00:09:55.523419+00:00'
page_id: '447092914'
product: rm
source: tdn-rm
title: 4479369 FISCAL01-7391 DT - Ajuste DAPI-MG
type: documentation
url: https://tdn.totvs.com/display/LRM/4479369+FISCAL01-7391+DT+-+Ajuste+DAPI-MG
version: 3
---

# Ajuste DAPI-MG

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Rotina Estadual DAPI-MG |
| **Situação/Requisito:** | Cliente relata erro ao validar a DAPI:  " [D1D030061] Estorno de Débito Existe duplicidade de notas ficais."  Foi verificado que este erro aparace quando o lançamento fiscal possui duas situações tributárias. |
| **Solução/Implementação:** | Ajuste para que não seja apresentado o erro "[D1D030061] Estorno de Débito Existe duplicidade de notas ficais"  ao vincular nos Lançamentos de Outros Débitos/Créditos do tipo Estorno de Débito um Lançamentos Fiscal com mais de uma Situação Tributária. |
