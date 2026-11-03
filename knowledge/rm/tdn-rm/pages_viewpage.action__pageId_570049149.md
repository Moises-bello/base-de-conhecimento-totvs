---
content_hash: f32e36f92a07768c1233daf136551adb918ba84f4cd8488205422a2e443947ca
fetched_at: '2026-06-29T00:10:52.092735+00:00'
page_id: '570049149'
product: rm
source: tdn-rm
title: DT - MP 927 - Cálculo de médias de férias antecipadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570049149
version: 1
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Parametrizador |
| **Situação/Requisito:** | Cliente informa que sistema está calculando o valor do adicional de férias, referente às férias pagas em 04/2020 da MP 927 mais as médias não estão sendo calculadas até o mês corrente. O sistema está considerando para o cálculo das médias o mesmo período calculado nas férias pagas.  Considerando que é devido conforme entendimento da própria Totvs: <https://tdn.totvs.com/pages/releaseview.action?pageId=544731652> |
| **Solução/Implementação:** | Criados os parâmetros: **Diferença de média de férias antecipadas considera período até o vencimento -** para pagar diferença de média referente a MP 927 de acordo com o período aquisitivo do funcionário.  **Ignora lançamento da média no caso de recálculo com valor de diferença negativo -**para lançar o valor da média mesmo que a diferença seja um valor negativo.  O fato de mudar o período original de apuração da media pode tanto aumentar o valor, quanto pode também diminuir o valor desta media. O que antes era dividido por 8, passa a ser dividido por 12. Aumentar ou diminuir o valor vai depender do número de horas extras feitas depois do retorno das férias.    Foi alterado também a pasta Cálculo no Parametrizador pasta Férias, dividindo os parâmetros em duas pastas: Cálculo 1/2 e Cálculo 2/2. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-12269](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-12269) |
| **Documento de Referência:** | [Cálculo 2/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=570048621) |
| **Pacote:** | N/A |
