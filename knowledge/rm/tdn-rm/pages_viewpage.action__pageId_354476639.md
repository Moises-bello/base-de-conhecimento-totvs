---
content_hash: 04c89207a094de285f876b0cc8c47be03d84f289ade14eea90285016012ee4e3
fetched_at: '2026-06-29T00:08:57.778932+00:00'
page_id: '354476639'
product: rm
source: tdn-rm
title: 1760347 FISCAL01-2625 DT Geração do registro registro 0500 campo 08
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354476639
version: 1
---

# Geração do registro registro 0500 campo 08 ( Conta relacionada no plano de contas referenciado da RFB).

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Rotina Federal EFD - Contribuições |
| **Situação/Requisito:** | Geração do registro registro 0500 campo 08 ( Conta relacionada no plano de contas referenciado da RFB). |
| **Solução/Implementação:** | Geração do registro registro 0500 campo 08 ( Conta relacionada no plano de contas referenciado da RFB).  Foi criado um novo parâmetro na tela de geração da rotina EFD - Contribuições conforme imagem abaixo:      Através deste plano de contas referencial que conseguiremos preencher o campo 8 do registro 0500.  Ele será preenchido com a Conta Contábil que foi referenciada la no cadastro do Plano de contas paralelo no módulo Totvs Gestão Contábil.    Exemplo:  Quando eu tiver a conta contábil 2.1.1.1.0002 no campo 06 ( COD\_CTA) do 0500 o campo 8 ( COD\_CTA\_REF) será preenchido com 1.01 ( conta paralela  cadastrada).    Saíra no arquivo da seguinte maneira:  |0500|19042018|02|A|5|2.1.1.1.0002|Conta Default Produto Saida|1.01|| |
