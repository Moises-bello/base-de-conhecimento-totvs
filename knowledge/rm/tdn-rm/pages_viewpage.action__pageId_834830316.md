---
content_hash: 8ec102188518caa9743610ad67d618b6f17fe025caadccea7204fabdf62623bb
fetched_at: '2026-06-29T00:11:49.572806+00:00'
page_id: '834830316'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência do INSS Patronal - Melhoria na Performance
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=834830316
version: 15
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | Relatório de Conferência do INSS Patronal - Melhora na PerformanceRH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Relatório de Conferência do INSS Patronal- Melhoria na Performance |
| País: | Brasil |
| Ticket: | 18550082 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-8818](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8818) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2306.244
* 12.1.2310.185
* 12.1.2402.120 e superiores

## **03.** **SITUAÇÃO/REQUISITO**

O Relatório de Conferência do INSS Patronalestá com lentidão durante o processo de geração, carregando mas não concluindo.

## **04. SOLUÇÃO**

Implementada melhoria na performance na geração do Relatório de Conferência do INSS Patronal.

Identificado diversos pontos de melhoria nesse processo, cuja recuperação de dados para construção do relatório é onerosa devida quantidade de consultas SQL feitas e massa de dados.

Nesse primeiro momento, foi melhorado as principais consultas que na análise, apresentaram mais lentidão. Implementada uma carga em lote dos dados de funcionários, seções e tomadores diminuindo a quantidade de transações SQL abertas.

Durante os testes em ambiente controlado, observamos uma melhora de aproximadamente 30% (trinta por cento) no desempenho para 84.490 funcionários processados.

É importante destacar que a melhoria do processo é influenciada pela quantidade de dados e pelas características do ambiente, o que significa que os resultados podem variar.

## **05. DEMAIS INFORMAÇÕES**

**[Relatório INSS Patronal](https://tdn.totvs.com/pages/viewpage.action?pageId=714242305)**
