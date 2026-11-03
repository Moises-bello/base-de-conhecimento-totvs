---
content_hash: 1d9580ef4c960b9e5b83f48b9a759de50ea2e2dc06594af0be91d72a38bffce6
fetched_at: '2026-06-29T00:09:01.023001+00:00'
page_id: '370620973'
product: rm
source: tdn-rm
title: 2862047 FISCAL01-4663 DT Impressão do DANFE da NFC-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370620973
version: 3
---

# Impressão dos dados de Forma de Pagamento da NFC-e

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Impressão do DANFE da NFC-e |
| **Situação/Requisito:** | Ao efetuar a impressão da DANFE NFC-e não está sendo apresentado o campo Forma de Pagamento.  Conforme o Manual\_de\_Especificações\_Técnicas\_do\_DANFE\_NFC-e\_QR\_Code - versão 5.0 , página 9 é necessário que este campo esteja presente na DANFE. |
| **Solução/Implementação:** | Alteração no processo de impressão do DANFE da NFC-e para com as informações de Pagamento, pois para as versões 3.10 e 4.00 o grupo é montado de forma diferente no XML. |
