---
content_hash: deba75b8610ff88e9a360254c2efeffb2a070f5a70ae783bbf2b09ae2f055f69
fetched_at: '2026-06-29T00:12:08.491679+00:00'
page_id: '937244673'
product: rm
source: tdn-rm
title: DT - Folha Analítica - Tratativa para considera envelope de retificação anterior
  à admissão por transferência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=937244673
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Folha Analítica - Tratativa para considera envelope de retificação anterior à admissão por transferência |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11807](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11807 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2406.267
* 12.1.2410.219
* 12.1.2502.135

## **03.****SITUAÇÃO/REQUISITO**

Gerar o relatório da **Folha Analítica** de um período retificado antes da transferência do funcionário.

**04. SOLUÇÃO**

Foi criado o parâmetro **"Considera envelopes de retificação anterior à admissão por transferência"**. Ao habilitar essa opção e ao gerar a folha analítica de competências anteriores, o sistema também passará a considerar os envelopes de retificação lançados para os funcionários que foram admitidos por transferência.

**Exemplo:**

Funcionário com a chapa **99957** foi transferido de filial em **01/03/2025**, passando a ter a nova chapa **91957**.

Na competência **04/2025**, foi realizada uma retificação para o funcionário em uma competência anterior (**12/2024**). O sistema processou corretamente a retificação, gerando o período retificado apenas na nova chapa **91957**, conforme esperado para casos de admissão por transferência.

Ao gerar o relatório da **Folha Analítica** referente à competência **12/2024** para a chapa **91957**, conforme demonstrado abaixo, o sistema considerou corretamente os dados da retificação realizada na competência **04/2025**, apresentando apenas os valores do **envelope de retificação**.

## **05. DOCUMENTAÇÃO**
