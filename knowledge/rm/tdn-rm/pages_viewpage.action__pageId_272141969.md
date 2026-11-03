---
content_hash: 41838471cbbe548a675ae62bc8b9676ad4a0946dbc9d3430d9dc167dd8a7f120
fetched_at: '2026-06-29T00:08:29.036279+00:00'
page_id: '272141969'
product: rm
source: tdn-rm
title: 514671 MEDU-2903 DT Bolsas com códigos alfanuméricos na geração de lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272141969
version: 109
---

# BOLSAS COM CÓDIGOS ALFANUMÉRICOS NA GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Geração de lançamentos* |
| **Situação/Requisito:** | *Erro na geração de lançamentos ao tentar gerar um lançamento com bolsa de crédito com código alfanumérico.*  *Erro na criação do lançamento. Mensagem: Cannot perform '=' operation on System.String and System.Int32.* |
| **Solução/Implementação:** | *Ajuste na query de filtro no cálculo de valores de bolsas de crédito para considerar o código da bolsa como alfanumérico.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
