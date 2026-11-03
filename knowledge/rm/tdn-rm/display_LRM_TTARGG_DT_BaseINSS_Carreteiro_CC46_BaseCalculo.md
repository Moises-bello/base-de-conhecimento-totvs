---
content_hash: d04ff03ae3d494ec3b76b58cb259dd7ba0c53c9b8fb214e44b3a84cbeee0d9d6
fetched_at: '2026-06-29T00:06:05.589863+00:00'
page_id: '201724883'
product: rm
source: tdn-rm
title: TTARGG_DT_BaseINSS_Carreteiro_CC46_BaseCalculo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTARGG_DT_BaseINSS_Carreteiro_CC46_BaseCalculo
version: 2
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
| **Chamados relacionados:** | *TTARGG* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
