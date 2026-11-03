---
content_hash: 0148e6f0e37a6edad78a58eb4ae47e0cf16a50e1bd7fda6ffe02fdd139d5b5b5
fetched_at: '2026-06-29T00:08:58.786441+00:00'
page_id: '361441331'
product: rm
source: tdn-rm
title: 2290177 FISCAL01-4578 DT Sped Fiscal D197 - Alíquota DIFAL e FECP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361441331
version: 1
---

# Sped Fiscal D197 - Alíquota DIFAL e FECP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Sped Fiscal D197 |
| **Situação/Requisito:** | Ao gerar a rotina SPED FISCAL o sistema apresenta o campo Alíquota do registro D197 incorretamente.  No registro D197 o sistema deve gerar as alíquotas de DIFAL e FECP separadamente uma vez que possui código de ajustes específicos. |
| **Solução/Implementação:** | Foi modificado a geração do registro D197 do SPED Fiscal para gerar as alíquotas de DIFAL e FECP separadamente da mesma forma como é gerado o C197 |
