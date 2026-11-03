---
content_hash: 831e2681a258bc73b899a112e39dc2611a301eba494c536971609a2b1aa513c0
fetched_at: '2026-06-29T00:09:52.358662+00:00'
page_id: '439356461'
product: rm
source: tdn-rm
title: 5231742 FISCAL01-8515 e FISCAL01-7054 DT Alterações Registros C170 e C176
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439356461
version: 3
---

# Alterações Registros C170 e C176

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Geração do Sped Fiscal Layout 2019 |
| **Situação/Requisito:** | Adequação das Alterações dos Registros C170 e C176 para o Layout 2019. |
| **Solução/Implementação:** | Registro C170: ITENS DO DOCUMENTO (CÓDIGO 01, 1B, 04 e 55).  Inclusão do campo 38 - VL\_ABAT\_NT (Valor do abatimento não tributado e não comercial).  Este campo será gerado com o valor do campo "ICMS Desonerado" do Item quando a flag  "ICMS Deson. Não afeta Valor Contábil" não estiver marcada.  Obs.: Mesma Regra para preenchimento do campo no Registro C100.  Registro C176: RESSARCIMENTO DE ICMS E FUNDO DE COMBATE À POBREZA (FCP) EM OPERAÇÕES COM SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 55)  Incluída a opção "6 – Venda interna para Simples Nacional" no campo 19 - COD\_MOT\_RES  (Código do motivo do ressarcimento).  Inclusão do campo 27 VL\_UNIT\_RES\_FCP\_ST (Valor unitário do ressarcimento (parcial ou completo) de FCP decorrente da quebra da ST).  Campo gerado de acordo com o campo VlrICMSItemFCPEstDEST do Item do Lançamento Fiscal. |
