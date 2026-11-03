---
content_hash: 6f716bebae3d2abf4cb8fbfba84f9de2331d08390f6db5afd3c70811e838f067
fetched_at: '2026-06-29T00:12:15.098006+00:00'
page_id: '969993443'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência de INSS Patronal - Tratativa no movimento financeiro
  de autônomos (cliente/fornecedor)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=969993443
version: 12
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Relatório de Conferência de INSS Patronal - Tratativa no movimento financeiro de autônomos (cliente/fornecedor) |
|  |  |
| Issue: | [DRHROTRM-14305](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14305) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2410.277
* 12.1.2502.180
* 12.1.2506.122 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ao gerar o relatório de conferência de INSS Patronal o valor da base para autônomos do TOTVS Gestão Financeira com múltiplos vínculos não está sendo considerado na parte folha.

## **04. SOLUÇÃO**

Foi realizada uma tratativa no produto para que o movimento financeiro de autônomos (cliente/fornecedor) seja considerado como tomador empresa, desde que o cliente/fornecedor de origem seja igual ao cliente/fornecedor destino.

**Exemplo:**

 Cadastro de múltiplos Vínculos Autônomos em Cliente / Fornecedor | Anexos | Múltiplos Vínculos Autônomos, conforme demonstrado abaixo:
