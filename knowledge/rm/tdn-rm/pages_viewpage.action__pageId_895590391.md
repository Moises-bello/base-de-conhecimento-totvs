---
content_hash: 5fa4993c4c5ed122d6cf0183e43efcf98f2cd9c26496182adc0e4ed2d32248c5
fetched_at: '2026-06-29T00:12:01.420137+00:00'
page_id: '895590391'
product: rm
source: tdn-rm
title: DT - Cancelamento de Rescisão - Cancelar período retificado de Restituição
  INSS/IRRF de 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=895590391
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cancelar Rescisão |
| País: | Brasil |
| Issue: | [DRHCALCRM-7135](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7135) |

false

A partir dos patchs/release:

12.1.2402.251

12.1.2406.197

12.1.2410.128

12.1.2502.1

## **02. SITUAÇÃO/REQUISITO**

Quando é feito o cálculo da rescisão e existe a restituição de INSS/IRRF de 13º Salário e o parâmetro 'Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão' está marcado, é gerado o período 10000 automaticamente. Porém ao fazer o cancelamento de rescisão é necessário que o mesmo seja cancelado junto com o período da rescisão automaticamente.

## **03. SOLUÇÃO**

Tratado o processo de cancelamento de rescisão para que o mesmo faça a exclusão do período de 13º Salário retificado criado com os valores de restituição de INSS/IRRF de 13º Salário automaticamente.

## **04. DEMAIS INFORMAÇÕES**

[FAQ - Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão](https://tdn.totvs.com.br/pages/releaseview.action?pageId=873208316)

## **05. ASSUNTOS RELACIONADOS**

[Parametrizador - 13º Salário - Rescisão](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719912&draft=true)

[Cancelar Rescisão](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719736)
