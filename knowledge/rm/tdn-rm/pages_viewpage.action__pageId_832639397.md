---
content_hash: b746638d1f7cd16d75619958d72aa9ea4b4d579bfea5643474a594dfe75abe4c
fetched_at: '2026-06-29T00:11:49.399412+00:00'
page_id: '832639397'
product: rm
source: tdn-rm
title: DT - DIRF - Agrupar as informações de RRA quando essas foram pagas de forma
  parcelada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=832639397
version: 16
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | DIRF - Agrupar as informações de RRA quando essas foram pagas de forma parcelada |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-9450](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9450) |

## **02.** **VERSÕES**

Lembrando que, será a partir dos patches:

* + 12.1.2306.238
  + 12.1.2310.179
  + 12.1.2402.115 e superiores

## **03.** **SITUAÇÃO/REQUISITO**

Quando o RRA é pago em parcelas, ao gerar a DIRF, o sistema estava criando um grupo de RRA para cada mês.

## **04.** **SOLUÇÃO**

Implementamos uma solução para agrupar as informações de RRA na geração da DIRF quando essas foram pagas de forma parcelada. Isso significa que, quando houver mais de um registro na tabela sem a informação do número do processo, o sistema irá agrupar essas informações no ano calendário correspondente.

1) Quando não houver processo no histórico de RRA ou quando o número do processo for o mesmo em todas as parcelas, o sistema irá somar todos os valores, exceto os valores do advogado, que devem ser considerados apenas no último registro.

Exemplo: 

Nesse caso, os valores de RRA serão somados da seguinte forma: R$400,00 + R$200,00=600,00 (processos iguais).

2) Quando o número de processos for diferente, o RRA deve ser dividido por parcelas e não somado.

## **05. DEMAIS INFORMAÇÕES**

**[DIRF- RRA](https://tdn.totvs.com/pages/releaseview.action?pageId=208347807)**
