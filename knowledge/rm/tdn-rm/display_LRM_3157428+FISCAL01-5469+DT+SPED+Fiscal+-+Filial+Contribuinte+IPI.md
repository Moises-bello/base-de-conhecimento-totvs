---
content_hash: 110f3bd81488aa4132ae73847ab3e1658a04dded530bc0985d09589123adb0ce
fetched_at: '2026-06-29T00:09:10.051259+00:00'
page_id: '396658654'
product: rm
source: tdn-rm
title: 3157428 FISCAL01-5469 DT SPED Fiscal - Filial Contribuinte IPI
type: documentation
url: https://tdn.totvs.com/display/LRM/3157428+FISCAL01-5469+DT+SPED+Fiscal+-+Filial+Contribuinte+IPI
version: 3
---

# Gerar campo 20 (C170) apenas quando a filial for contribuinte do IPI

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Sped Fiscal |
| **Situação/Requisito:** | Cliente solicita análise da legislação do SPED FISCAL quanto ao campo 20 do registro C170: CST de IPI. |
| **Solução/Implementação:** | Gerar campo 20 (C170) apenas quando a filial for contribuinte do IPI  Foi criado o campo contribuinte IPI nos dados fiscais da FIlial para informar se a mesma é contribuinte:    Caso a mesma estiver desmarcada, o sistema não preencherá o campo 20 do registro C170 no SPED Fiscal. |
