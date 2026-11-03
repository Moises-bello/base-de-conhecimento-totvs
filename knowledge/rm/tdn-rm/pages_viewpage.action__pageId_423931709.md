---
content_hash: 8995a6dd688a87b6af2f61274aff1cbd0e0b8ca818247bf284f10e1bf68233a9
fetched_at: '2026-06-29T00:09:24.040024+00:00'
page_id: '423931709'
product: rm
source: tdn-rm
title: CONTROLADORIA01-2103 DT Otimização CtbActionModuleController
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423931709
version: 2
---

# Otimização CtbActionModuleController

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Contábil |
| **Função:** | Mudança de módulos. |
| **Situação/Requisito:** | Identifiquei um problema que acredito ser muito importante e que merece a atenção de todos em todas as versões suportadas.  Muitos produtos, no seu ***ActionModuleController***, assinam o evento ***OnContextPropValueChanged*** do ***RMSContext***, porém não removem a assinatura. Isso gera vazamento de memória e replicação de execuções desnecessárias pois o *ModuleController* é destruído e recriado em vários momentos distintos na manipulação da MDI. |
| **Solução/Implementação:** | Adição e remoção da assinatura do evento OnContextPropValueChanged no CtbActionModuleController. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
