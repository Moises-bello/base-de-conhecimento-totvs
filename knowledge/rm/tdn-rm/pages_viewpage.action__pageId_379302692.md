---
content_hash: 241f0df4d7849b8e483c3da5d32a4def56ac2f54b8d44e53f0cec8154007824b
fetched_at: '2026-06-29T00:09:02.327891+00:00'
page_id: '379302692'
product: rm
source: tdn-rm
title: 1682942 FOPCALCULO01-2551 Diferença de Férias por Dissídio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379302692
version: 1
---

# Cálculo da diferença de Férias por Dissídio

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Diferença de Férias |
| **Situação/Requisito:** | Ao executar a diferença de férias por dissídio para férias partidas, o evento de código de cálculo 116 - Estorno Base INSS dissídio Ret. Férias está estornando os valores dos códigos de cálculo 80 - Dif. férias Próx. Mês e 81 - Dif. 1/3 Férias próx. Mês indevidamente, pois estes não possuem incidência em INSS e consequentemente, geram um estorno para a base de INSS da Folha indevidamente. |
| **Solução/Implementação:** | Ajustado o cálculo de diferença de férias, para não considerar o valor das férias próximo mês no evento de Código de Cálculo 116 quando a diferença for calculada por dissídio. |
| **Tickets relacionados:** | 1682942 |
