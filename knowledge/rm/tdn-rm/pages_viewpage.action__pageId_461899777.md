---
content_hash: 6a53b1bf3908ce6302ec09a63d2d33ffc99b163ac15fc24e8f439bc4c433c5ea
fetched_at: '2026-06-29T00:10:14.437205+00:00'
page_id: '461899777'
product: rm
source: tdn-rm
title: 5121133 FISCAL01-8099 DT DIRF - Data de Geração IRRF-PJ
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461899777
version: 1
---

# Geração do Arquivo - DIRF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Backoffice RM |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração do Arquivo - DIRF |
| **Situação/Requisito:** | Ao gerar a rotina DIRF 2018/2019 foi identificado que o sistema considerou a  data de entrada para lançamentos de IRRF PJ, porém cliente solicita que seja  considerado a data de Emissão, ou data base parametrizada para o IRRF,  assim como é realizado na apuração do imposto. |
| **Solução/Implementação:** | Na geração da DIRF o tributo IRRF-PJ será gerado com Data de Emissão ou  Vencimento conforme parametrização do tributo no Financeiro.  Observação: Se a parametrização do Financeiro for diferente de data de emissão ou  vencimento a Data considerada será a data do lançamento. |
| **Requisito:** | FIS000307 - Rotina Federal DIRF |
