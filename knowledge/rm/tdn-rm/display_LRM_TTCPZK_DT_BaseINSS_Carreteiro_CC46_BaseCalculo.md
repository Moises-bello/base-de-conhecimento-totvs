---
content_hash: 9fffcef15ce3a54da68a5cab4a7a29ce3fe33618f467212f4d21e7b4c5770a03
fetched_at: '2026-06-29T00:06:05.593755+00:00'
page_id: '201725030'
product: rm
source: tdn-rm
title: TTCPZK_DT_BaseINSS_Carreteiro_CC46_BaseCalculo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCPZK_DT_BaseINSS_Carreteiro_CC46_BaseCalculo
version: 1
---

# BASE INSS DE CARRETEIRO COM CC 46 TIPO BASE DE CÁLCULO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Base de INSS* |
| **Situação/Requisito:** | *O evento de CC 46 - Honorários, quando é do tipo Base de Cálculo, não está sendo acumulado na Base de INSS.*  *Entretanto no caso do INSS de Carreteiro, funcionário com Categoria 15 (Transportador autônomo com contribuição sob remuneração), o evento de CC 46 deve compor a Base de INSS, mesmo sendo do tipo Base de Cálculo.* |
| **Solução/Implementação:** | *Tratar na exibição da pasta Incidências do Envelope e na Folha Analítica, para considerar o valor do evento de CC 46 do tipo Base de Cálculo, somente para funcionários com Categoria 15 (Transportador autônomo com contribuição sob remuneração).* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTCPZK* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
