---
content_hash: ef672166a5ec5c746024219b4172fe3aeeb7540404b7b65e73ecd47215ac32b6
fetched_at: '2026-06-29T00:12:09.194601+00:00'
page_id: '942050717'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência INSS Patronal - PIS/PASEP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=942050717
version: 12
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Relatório de Conferência INSS Patronal - PIS/PASEP |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-13151](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13151) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2406.275
* 12.1.2410.226
* 12.1.2502.142 e posteriores

## **03.** **SITUAÇÃO/REQUISITO**

Implementar no **Relatório de Conferencia INSS Patronal** a possibilidade de comparar o valor e a base de cálculo do PIS/PASEP informada no evento S-5011 com a base de cálculo do PIS/PASEP apurada pelo sistema TOTVS Folha de Pagamento, facilitando a conferência e validação dos dados.

## **04. SOLUÇÃO**

Implementada o valor e a base de cálculo do PIS/PASEP  no  **Relatório de Conferência INSS Patronal.**

Após atualizações das versões, é necessário a execução do RM.Atualizador.exe para a criação dos campos referente a conferência.

| Coluna | Valor Folha | Valor RET |
| --- | --- | --- |
| Base de Cálculo do PIS/Pasep | Retorna a soma  dos eventos/verbas com Incidência em PIS/PASEP Mensal  com os Códigos 11 e 12, menos os eventos de estorno com incidência em PIS/PASEP com os Códigos 11 e 12. Tabela (PEVENTO.INCPISPASEP). | Retorna o valor da tag <vrBcPisPasep> do S-5011. |
| PIS - FOLHA DE SALÁRIOS | Será realizado o cálculo de 1% sobre o campo Base de Cálculo do PIS/Pasep (Folha). | Retorna o valor da tag <tpCR> com o código de receita 830102  do S-5011. |

**ATENÇÃO:** A base de cálculo do PIS/PASEP (tag `<vrBcPisPasep>` do S-5011) é retornada por filial, e não por lotação tributária. Diante disso, foi necessário criar uma aba separada no relatório especificamente para o PIS/PASEP.

## **05. DEMAIS INFORMAÇÕES**

**[Relatório de Conferência INSS Patronal](https://tdn.totvs.com/pages/viewpage.action?pageId=714242305)**
