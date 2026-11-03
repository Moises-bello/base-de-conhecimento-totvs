---
content_hash: b0187a01694645dd8dcc76ac0262c8b6cb1c0f8e8680d77e3a72b46b830eba8d
fetched_at: '2026-06-29T00:10:57.896065+00:00'
page_id: '600309285'
product: rm
source: tdn-rm
title: DT- Parametrizador – Perda de férias devido a faltas não deve afetar avo do
  aviso prévio indenizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=600309285
version: 2
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Parametrizador |
| **Situação/Requisito:** | Para o CC 329 esta sendo considerado 1,5 dias, pois sistema entende que funcionário perdeu 1 dia em cada avo devido faltas, porem isso só deve ser considerado para Ferias proporcionais, a Ferias sobre aviso não devem ter alteração devido falta, ou seja, deve ser calculado 2,5 dias.  Faltas não devem ser consideradas sobre a projeção do aviso conforme a documentação <https://tdn.totvs.com/pages/releaseview.action?pageId=520656576> |
| **Solução/Implementação:** | Criado parâmetro “Perda de férias devido a faltas não deve afetar avo do aviso prévio indenizado” para calcular avos de férias referente ao período do aviso prévio indenizado desconsiderando a proporção perdida pelas faltas e será habilitado somente quando marca para considerar faltas para cálculo de férias.  Os CC's 329, 330 e 331 na rescisão serão calculados de acordo com essa parametrização, ou seja, a parte desconsiderada no avo do CC 329 será acumulada no CC's 330 ou 331, dependendo se o aviso entra nas férias proporcionais ou vencidas. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-10199](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-10199) |
| **Documento de Referência:** | [Parametrizador - Rescisão / Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719504) |
| **Pacote:** | N/A |
