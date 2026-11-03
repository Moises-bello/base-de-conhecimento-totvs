---
content_hash: 53d576a6d9389ac27252d007aec940464a6b4efb0fa4202d4bc8b5248e86b465
fetched_at: '2026-06-29T00:09:58.047301+00:00'
page_id: '450158402'
product: rm
source: tdn-rm
title: FISCAL01-7084 DT Lançamento Fiscal - Campo Tipo CT-e / BP-e / CT-e OS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450158402
version: 3
---

# Tipo CT-e / BP-e / CT-e OS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Lançamento Fiscal |
| **Situação/Requisito:** | Implementação do Tipo de CT-e no TOTVS Gestão Fiscal |
| **Solução/Implementação:** | Criação do campo "Tipo CT-e / BP-e / CT-e OS" na Sub Pasta Transporte\Remetente-Destinatario. Este campo será habilitado no agrupador de Lançamentos Fiscais para o Tipo de Documento “57 - CT-e”, “63- BP-e” ou “67 - CT-e OS”. |

**Escrituração**

Caso o campo seja do tipo de documento 57 ou 67, o mesmo recuperará a informação do campo TIPOCTE da TMOVTRANSP.  
Caso o campo seja do tipo de documento 63, o mesmo recuperará a informação  do campo TIPOBPE da TMOVTRANSP.

Caso o movimento seja criado a partir da cópia por referência, com motivos:

16 - Conhecimento Transporte Eletrônico (CT-e) – Anulação  
17 - Conhecimento Transporte Eletrônico (CT-e) – Substituição

O sistema escriturará com a referência.

**EFD-Contribuições**

Layout do EFD-Contribuições atualizado para levar em conta o campo Tipo CT-e no registro D100, campo 13.

****Integração com o TAF****

Layout de integração RM x TAF atualizado para levar em conta o campo Tipo CT-e no registro T013, campo 23.
