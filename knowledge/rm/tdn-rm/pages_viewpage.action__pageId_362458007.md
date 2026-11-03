---
content_hash: bb6b4f64aea6ca43af43c88856a857c0fd5ed760f9af9b73819b74f530b5f71e
fetched_at: '2026-06-29T00:08:59.475965+00:00'
page_id: '362458007'
product: rm
source: tdn-rm
title: 2777252 FINANCEIRO01-6830 DT Baixa lançamento via webservice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362458007
version: 1
---

# BAIXA DE LANÇAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamento |
| **Situação/Requisito:** | Cliente informa que ao efetuar a baixa de lançamentos financeiros via WebService, observa-se que os campos Alfa Opcionais não estão sendo preenchidos no item de baixa gerado, mesmo existindo a tag no XML utilizado. |
| **Solução/Implementação:** | Ajuste na classe de parametros FinTBCBaixaParamsProc do processo FinTBCBaixaDataProcess para permitir passar os campos alfa opcinais. |
| **Tickets relacionados:** | N/A |
