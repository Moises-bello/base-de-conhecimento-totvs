---
content_hash: 69358ee1d06b2deb3f5233e1ba35bc7b6c0c2c0dab7dd3e2f3142e13927eed6f
fetched_at: '2026-06-29T00:10:15.137803+00:00'
page_id: '463812567'
product: rm
source: tdn-rm
title: 5055917 FISCAL01-8038 DT Campo TIPO_DOC com valor incorreto na integração RM
  X TAF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463812567
version: 1
---

# Integração RM X TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Integração RM X TAF |
| **Situação/Requisito:** | Ao gerar os registros de integração RM x TAF o registro T013 campo 3 está gerando como 06 para nota complementar de ICMS. |
| **Solução/Implementação:** | O layout de integração com o TAF foi ajustado para calcular corretamente o campo TIPO\_DOC (finalidade do Documento Fiscal) do registro T013 (Documento Fiscal) de acordo com o layout de integração do TAF    Finalidade do documento fiscal: 00 - Emissão Normal; 01 - Documento de Devolução; 02 - Complemento de ICMS; 03 - Complemento de IPI; 04 - Complemento de Frete; 05 - Beneficiamento; **Este tipo não é gerado pelo RM** 06 - Nota Fiscal de Serviço; |
