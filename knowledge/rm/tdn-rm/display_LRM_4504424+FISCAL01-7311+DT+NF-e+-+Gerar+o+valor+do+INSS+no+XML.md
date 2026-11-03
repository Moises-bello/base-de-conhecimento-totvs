---
content_hash: 98915589135945c0993c24a8701e10d2d8e8879fdab83c7d26d7e3b31385db2f
fetched_at: '2026-06-29T00:09:53.539905+00:00'
page_id: '440841313'
product: rm
source: tdn-rm
title: 4504424 FISCAL01-7311 DT NF-e - Gerar o valor do INSS no XML
type: documentation
url: https://tdn.totvs.com/display/LRM/4504424+FISCAL01-7311+DT+NF-e+-+Gerar+o+valor+do+INSS+no+XML
version: 2
---

# Enviar NF-e

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Enviar NF-e |
| **Situação/Requisito:** | Ao preencher o INSS no Item do Movimento o valor do tributo não é carregado para NF-e e nem para o XML, nesse caso a informação vai apenas para o REINF corretamente. As tags e não são geradas quando o INSS está no Item, são geradas apenas quando o tributo está no Movimento. |
| **Solução/Implementação:** | Foi modificado a montagem do XML da Nota Fiscal Eletrônica para permitir a utilização dos tributos do tipo INSS ou FUNRURAL no Item ou no Movimento. Sendo que se for informado nos dois os valores serão somados. |
