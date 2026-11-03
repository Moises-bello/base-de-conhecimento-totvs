---
content_hash: 52a252fcebab2b789306ea4862007c26bcce944cd645c8b53a0d7b1720b6e7f5
fetched_at: '2026-06-29T00:08:50.829413+00:00'
page_id: '334341454'
product: rm
source: tdn-rm
title: 877892 FISCAL01-429 DT Geração da DIRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334341454
version: 1
---

# Registro VRPDE sendo gerado agrupado incorretamente apenas pelo Código da Receita

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Geração da DIRF |
| **Situação/Requisito:** | Solicita que na geração da DIRF p registro VRPDE não seja agrupado apenas por código de receita, pois o tipo de rendimento e forma de tributação são diferentes. |
| **Solução/Implementação:** | Alteração na geração da DIRF para que o registro VRPDE seja gerado agrupado seguindo a seguinte ordem de campos: DATA\_PAGAMENTO, COD\_RECEITA, TIPO\_RENDIMENTO e FORMA\_TRIBUTACAO |
