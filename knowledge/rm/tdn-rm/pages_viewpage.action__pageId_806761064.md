---
content_hash: 9bb5e7b4defd574e43d3c16ce125c1cd8f11c69473fba096d5ac85d250181c86
fetched_at: '2026-06-29T00:11:43.417800+00:00'
page_id: '806761064'
product: rm
source: tdn-rm
title: DT - Transferência - Desconsiderar o Período da Ficha Financeira (DIRF/Informe
  de Rendimentos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=806761064
version: 7
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Transferência de funcionários |
| País: | Brasil |
| Epic | [DRHCALCRM-4610](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-4610)  [DRHCALCRM-5660](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5660) |

## **02. SITUAÇÃO/REQUISITO**

Criar o parâmetro **Desconsiderar o período da ficha financeira quando a data de pagamento for igual a data de demissão** na tela de rescisão por transferência de funcionário.

## **03. SOLUÇÃO**

Foi criado o parâmetro **Desconsiderar o período da ficha financeira quando a data de pagamento for igual a data de demissão** na tela de rescisão por transferência de funcionário.

Ao marcar o parâmetro, o sistema irá desconsiderar o período da ficha financeira quando a data de pagamento for igual a data de demissão.

**Observação**

O novo parâmetro criado estará disponível somente quando o parâmetro '**Considera a data de transferência igual a data de demissão na transferência sem ônus',** existente em RH | Folha de Pagamento | Configurações | Parametrizador | Rescisão | Transferência estiver marcado, pois quando o parâmetro está desmarcado, o sistema considera automaticamente a ficha financeira com data de pagamento até a data de demissão.

## **04.****ASSUNTOS RELACIONADOS**

* [Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=807221160)
* [Importação de Dados do Período da Ficha Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=452719264)
