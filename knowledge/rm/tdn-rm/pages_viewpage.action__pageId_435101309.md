---
content_hash: 316da543b804ef9600c474bc9a0a29ae4e234c4f1fb969aa20325e3104351207
fetched_at: '2026-06-29T00:09:45.914075+00:00'
page_id: '435101309'
product: rm
source: tdn-rm
title: 3893031 FISCAL01-6737 DT - O valor do IPI não está sendo considerado mesmo
  quando marcado que o IPI afeta de base
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435101309
version: 1
---

# Cadastro de Lançamento Fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Escrituração |
| **Situação/Requisito:** | Quando a parametrização do CFOP é Outros com redução de base e o IPI afeta a base do ICMS a redução não está sendo calculado em cima de Outros + IPI. |
| **Solução/Implementação:** | Foi feito acerto para que seja considerado o valor de IPI no cálculo da Redução quando a Regra de ICMS estiver parametrizada com IPI Afeta a Base.  Foi Feito acerto no Recálculo do Lançamento fiscal para que também considere o valor de IPI no cálculo da Redução quando a Regra de ICMS estiver parametrizada com IPI Afeta a Base. |
| **Requisito:** | FIS000062 |
