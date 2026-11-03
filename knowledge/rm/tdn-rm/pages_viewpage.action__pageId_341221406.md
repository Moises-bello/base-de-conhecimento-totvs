---
content_hash: 719220ce3f4e05a6e2664bed0b55dffe3b4d5a44719c2bd34befdc8458c16edc
fetched_at: '2026-06-29T00:08:52.579054+00:00'
page_id: '341221406'
product: rm
source: tdn-rm
title: 2109522 FISCAL01-3319 DT Processo de Escrituração Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=341221406
version: 1
---

# Processo de Escrituração Fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Processo de Escrituração Fiscal |
| **Situação/Requisito:** | Ao realizar o Processo de Escrituração Fiscal (.Net) foi apresentado a seguinte mensagem: Erros ao Validar Movimentos Movimento: 195225 Erro: Object reference not set to an instance of an object. |
| **Solução/Implementação:** | Ajuste no Processo de Escrituração para quando a Natureza não tiver regra de ICMS  e no movimento tiver o Tributo de ICMS apenas com Base (sem Alíquota e Valor), o erro "Object reference not set to an instance of an object." não seja apresentado. e o Movimento seja escriturado corrente. |
