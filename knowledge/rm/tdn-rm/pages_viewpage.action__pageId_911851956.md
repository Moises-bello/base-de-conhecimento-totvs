---
content_hash: 0ec0c1f274d24640ccb6cca24a385be6a0503ba7ae0fc52b996305f6b482b9de
fetched_at: '2026-06-29T00:12:03.555366+00:00'
page_id: '911851956'
product: rm
source: tdn-rm
title: DT - Lançamento Financeiro e Relatório de INSS Patronal - Passou a considerar
  o Histórico de ocorrência SEFIP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911851956
version: 7
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Lançamento Financeiro e Relatório de INSS Patronal - Passou a considerar o histórico de Ocorrência SEFIP |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-12036](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12036) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.272
* 12.1.2406.232
* 12.1.2410.165 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ao gerar o lançamento financeiro do tipo "25-DCTFWeb Folha" e Relatório de INSS Patronal retroativo, onde o funcionário teve alteração no código da ocorrência do SEFIP,  o sistema não estava considerando o "Histórico de Ocorrência do SEFIP".

04. **SOLUÇÃO**

Realizamos tratativa tanto no **Relatório de INSS Patronal** quanto no **Lançamento Financeiro do tipo "25-DCTFWeb Folha"**, para que, na geração retroativa, passe a considerar o histórico de ocorrência do SEFIP. Caso o histórico não exista, o sistema usará as informações do cadastro do funcionário.

## **05. DEMAIS INFORMAÇÕES**
