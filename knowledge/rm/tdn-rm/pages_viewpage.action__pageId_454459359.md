---
content_hash: e22240a18201c0350963cee09e9987236b4495177a46b6f99ac51a889686fa0c
fetched_at: '2026-06-29T00:10:12.490416+00:00'
page_id: '454459359'
product: rm
source: tdn-rm
title: 3712080 FISCAL01-6258 DT Ajuste na carga dos Lançamentos de integração RM X
  TAF para a geração da REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454459359
version: 4
---

# Integração RM X TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Integração RM X TAF |
| **Situação/Requisito:** | Quando são gerados os registros para integração com o TAF e o parâmetro GERAR SOMENTE REGISTROS PERTINENTES A ROTINA REINF marcado, os lançamentos que contém o tributo Contribuição Previdenciária estão sendo gerados no registro T013, porém as informações para a apuração da Contribuição Previdenciária, já são geradas no registro T082, portanto ficam duplicadas. |
| **Solução/Implementação:** | A Sentença SQL que seleciona os Lançamentos Fiscais para a geração dos registros de integração com o TAF foi alterada para desconsiderar os lançamentos que possuem o tributo Contribuição Previdenciária , quando o parâmetro "GERAR SOMENTE REGISTROS PERTINENTES A ROTINA REINF " estiver marcado.  Adequada também a geração dos registros  T082AB, T001AB e T001AO ao parâmetro. |
