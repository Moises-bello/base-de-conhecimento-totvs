---
content_hash: 3c4b1c817abbf13244dd523fadaf8ea2740e5ff919d8f48e4dec6b12766380b8
fetched_at: '2026-06-29T00:09:54.857433+00:00'
page_id: '445652924'
product: rm
source: tdn-rm
title: 4306416 FISCAL01-7096 DT Alterações DAPI-MG
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445652924
version: 1
---

# Alterações DAPI-MG

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Rotina Estadual DAPI-MG |
| **Situação/Requisito:** | Ajuste na geração da DAPI-MG |
| **Solução/Implementação:** | 1 - Quando a Rotina da DAPI foi implementada não existia na Linha 36 o CFOP 3.128,  por este motivo que os lançamentos com este CFOP não são gerados na Rotina. Nesta Linha deve gerar as informações dos Lançamentos de Entrada com o  CFOP 3.101, 3.102, 3.126, 3.127, 3.128, 3.651, 3.652 e 3.653.  2 - Na Rotina da DAPI deve incluir as seguintes informações:  Campo 111 – Exportação Indireta pela Comercial Exportadora / Trading Company - Neste campo deve incluir na consistência atual os novos tipo de "Natureza de Exportação":  Exportação Indireta Simplificada Declaração Unica de Exportação Indireta  Campo 113 - Exportação Direta pelo produtor remetente - Neste campo deve incluir na  consistência atual os novos tipo de "Natureza de Exportação":  Exportação Direta Simplificada Declaração Unica de Exportação Direta |
| **Tickets Relacionados:** | 4306416; 3936193 |
