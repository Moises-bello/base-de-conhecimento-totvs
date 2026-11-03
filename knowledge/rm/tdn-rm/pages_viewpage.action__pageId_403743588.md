---
content_hash: 479899c40f56af82f44fe3e5ef12ac6710c6a9539e6768258954c709722f8a16
fetched_at: '2026-06-29T00:09:11.280672+00:00'
page_id: '403743588'
product: rm
source: tdn-rm
title: FISCAL01-4516 DT TAF - Registro T010 Campo 8 - "COD_CTA_REF"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403743588
version: 2
---

# TAF - Registro T010 Campo 8 - "COD\_CTA\_REF"

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração dos Registros TAF |
| **Situação/Requisito:** | Revisar Layout do TAF com relação às alterações feitas para a "Conta Contábil Referenciada". Verificar alterações feitas para Conta Contábil no SPED e EFD Contribuições e verificar  se é necessário alterar no Layout de Integração com o TAF o Registro T010. |
| **Solução/Implementação:** | Realizado o preenchimento do campo 8 - "COD\_CTA\_REF" do Registro T010 com a Conta Referenciada  conforme feito na EFD Pis/Cofins. Para o preenchimento deste campo e necessário informar o novo parâmetro criado no Layout, "Plano de Contas Referencial" na geração dos Registros TAF - Parâmetro localizado na última aba do Processo. |
