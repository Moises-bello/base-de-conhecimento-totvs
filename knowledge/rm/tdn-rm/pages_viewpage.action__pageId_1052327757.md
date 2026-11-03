---
content_hash: b6205f1943759dae25cbd8fdaa3fd79566c38da11376167222e053c5cfec8a84
fetched_at: '2026-06-29T00:05:51.591609+00:00'
page_id: '1052327757'
product: rm
source: tdn-rm
title: DT - Importação de Batidas - Agendamento Por Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1052327757
version: 23
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Permitir realizar a Importação de batidas |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-9294](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2121) |

## **02. REQUISITO**

Permitir a configuração automática de importação de batidas com datas dinâmicas , com isso o usuário não irá precisar editar o agendamento **manualmente a cada virada de período .**

## **03. SOLUÇÃO:**

Implementada a  funcionalidade de **Agendamento Dinâmico de Importação de Batidas** . Essa melhoria permite configurar uma rotina automática de importação com datas flexíveis, baseadas em periodicidades pré-definidas: **Semanal**, **Quinzenal**, **Mensal** ou **Últimos [x] Dias.**

Importante

* As opções para a seleção das datas de Início e Fim do período de importação das batidas serão mantidas, oferecendo flexibilidade para o usuário.
* Quando o período de importação não tiver selecionado Por Intervalo de Datas ou Por Período, será demonstrada uma mensagem para o usuário.
* Será permitido no campo Últimos dias apenas o valor igual a 31
Por Intervalo de DatasImportante:

A funcionalidade segue o comportamento já estabelecido no sistema.

Por PeríodoSemanal

Será considerado exatos 7 dias retroativos à execução

Exemplo: Período 01/04/2026 a 30/04/2026

                Data execução: 06/04/2026

                Será considerado para importação - 30/03/2026 a 06/04/2026

Quinzenal

Será considerado exatos 15 dias retroativos à execução

Exemplo: Período 01/04/2026 a 30/04/2026

                Data execução: 06/04/2026

                Será considerado para importação - 22/03/2026 a 06/04/2026

Mensal

Utiliza as datas do período de ponto vigente no sistema.

Exemplo: Período 01/04/2026 a 30/04/2026

                Data execução: 06/04/2026

                Será considerado para importação - 01/04/2026 a 06/04/2026 (Período Ativo até a data atual)

ùltimos X Dias

Essa configuração busca os registros dos últimos X dias completos, retroagindo a partir da data de execução atual do processo.

Exemplo: Período 01/04/2026 a 30/04/2026

                Data execução: 06/04/2026  informado 3 dias

                Será considerado para importação - 03/04/2026 a 06/04/2026

## **04. VERSÕES**

A partir 12.1.2606

* **05. DEMAIS INFORMAÇÕES**

**[Importação de batidas](https://tdn.totvs.com/pages/releaseview.action?pageId=452719301)**
