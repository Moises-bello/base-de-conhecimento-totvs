---
content_hash: 379290fff18fffbc874588b01e8be9f26c165c9c570f9510be56bddcb88e2f36
fetched_at: '2026-06-29T00:09:00.969795+00:00'
page_id: '370614825'
product: rm
source: tdn-rm
title: 2928344 DEDUINTEGRACOES-2539 DT Geração Acordo - Integração Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370614825
version: 1
---

# GERAÇÃO DE ACORDO - INTEGRAÇÃO PROTHEUS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de acordo - Integração Protheus |
| **Situação/Requisito:** | Ao gerar um acordo para lançamentos oriundos do TOTVS Gestão Educacional, quando integrado com o Protheus (integração 1021), caso o módulo financeiro não estivesse parametrizado para trabalhar com o rateio de centro de custo / natureza financeira, era levantada uma exceção e a geração do acordo não era finalizada corretamente. |
| **Solução/Implementação:** | A geração de acordo para lançamentos oriundos do TOTVS Educacional irá considerar a natureza financeira parametrizada nos dados de integração com o Protheus através do serviço, caso não seja identificado rateio de centro de custo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
