---
content_hash: 74997451c260bc22483383c74c7ca3ccce5f1d9158f3ab7c518ad4f1f285d23b
fetched_at: '2026-06-29T00:11:56.638527+00:00'
page_id: '867812494'
product: rm
source: tdn-rm
title: DT - S-1200 - Tratativa na geração do XML para diferença de férias retroativa
  e férias partidas com eventos adicionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867812494
version: 4
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1200 - Tratativa na geração do XML para diferença de férias retroativa e férias partidas com eventos adicionais |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-11294](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11294 "View this issue") |

## **02.** **VERSÕES**

Lembrando que, será a partir dos patches:

* 12.1.2310.255
* 12.1.2402.224
* 12.1.2406.151 e superiores

## **03.** **SITUAÇÃO/REQUISITO**

Em uma situação específica, quando o funcionário usufrui de férias divididas entre dois meses,  e possui eventos adicionais de férias, pode ocorrer um dissídio em parte do período, enquanto a outra parte do gozo de férias não sofre o impacto do dissídio.

**EXEMPLO:**O funcionário possui férias partidas, sendo:

* + **Gozo de férias:** 20/05/2024 a 08/06/2024 = 20 dias
  + **Competência atual:** 06/2024
  + **Diferença Dissídio Retroativa**: 01/05/2024

**Na competência de 06/2024**

Ao calcular a diferença de férias retroativa, o sistema lançará os valores da diferença em um único evento adicional, que agrupa tanto os valores com dissídio quanto sem dissídio. Esses valores serão registrados no Evento de Diferença de Salário. No exemplo abaixo, temos dois eventos adicionais que ilustram essa situação.

Na competência de 06/2024, foi calculada a diferença retroativa, resultando no lançamento de duas verbas adicionais de diferença. A verba 0301 inclui valores referentes a verbas que possuem dissídio sim (0178) e dissídio não (0177), enquanto a verba 0075 contempla valores de verbas com dissídio sim (0095) e dissídio não (0189).

## **04.** **SOLUÇÃO**

Realizamos uma melhoria na geração do XML para solucionar o problema de duplicidade de dados em casos de divergências de férias (dissídio sim e não). Agora, ao identificar o código de cálculo 116 na tabela PFFINANC, o sistema faz uma consulta à tabela PGADICFER para verificar os eventos adicionais. Para cada evento adicional, é feita uma verificação na tabela PFVERBASDISFER, identificando os eventos relacionados aos valores de dissídio que devem ser excluídos da verba enviada no período atual.

**Eventos adicionais (****PGADICFER)**

**Eventos de diferença de férias (PFVERBASDISFER)**

Na geração do XML, foram identificados dois eventos adicionais:

* **Verba 0301**: O valor da verba 0178, que possui dissídio sim, foi retirado. O valor total de R$ 200,00 foi ajustado com a exclusão de R$ 120,00, correspondente ao dissídio sim, resultando no valor correto de R$ 80,00 (referente ao dissídio não).
* **Verba 0075**: O valor da verba 0095, que também possui dissídio sim, foi retirado. O valor total de R$ 200,00 foi ajustado com a exclusão de R$ 120,00, resultando em R$ 80,00 (referente ao dissídio não).

Esses ajustes garantem a correção nos valores referentes ao dissídio na geração do XML.
