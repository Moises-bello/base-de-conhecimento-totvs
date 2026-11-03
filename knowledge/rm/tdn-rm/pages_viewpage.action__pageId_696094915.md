---
content_hash: e564bcc13c904210cc3ce5361885ef62cb434524f8221102b55d821409b49823
fetched_at: '2026-06-29T00:11:21.441797+00:00'
page_id: '696094915'
product: rm
source: tdn-rm
title: DT – Base Anual de Participação no Lucros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=696094915
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Ficha Financeira |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-1923](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-1923)  [DRHCALCRM-1924](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-1924)  [DRHCALCRM-1925](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-1925) |

## **02. SITUAÇÃO/REQUISITO**

Tratar no cálculo para considerar a base de anual no campo PFPERFF.BASEIRRFPARTANUAL.

Alterar telas do Envelope, anexo Ficha Financeira e Ficha Financeira complementar para ter novo campo.

Validar a Transferência Manual dos Registros da Ficha Financeira.

Inserir o novo campo criado no relatório LAB04 do RM Portal e nos relatórios de envelope de pagamento disponíveis no RM Reports.

Inserir o novo campo criado no Layout de Exportação de Dados do período da Ficha Financeira (**FOPLAY0054 - 09.004.028 Exportação de Periodo de Ficha Financeira.TotvsGen**) e no processo de Importação de Dados do período da Ficha Financeira.

## **03. SOLUÇÃO**

Feito o tratamento do cálculo da base anual da participação nos lucros acumulando no período anual de pagamento. Considerado o ano caixa para o acumulo no campo Base Participação Anual.

Foi Inserido o novo campo criado no relatório LAB04 do RM Portal e nos relatórios de envelope de pagamento disponíveis no RM Reports.

## **04. DEMAIS INFORMAÇÕES**

**1) RM Portal  - Envelope de Pagamento (Demonstrativo de Pagamento - Lab04) com o NOVO campo criado:**

**2) Nome dos relatórios de Demonstrativo de Pagamento que sofreram inclusão do NOVO campo no RM Reports:**

FOPREL00015 - Envelope pgto Modelo Extrato (frenteverso).TotvsReport

FOPREL00016 - Envelope pgto Modelo Extrato (frenteverso).TotvsReport

FOPREL00176 - Envelope Pgto Portal Padrão.TotvsReport

FOPREL00177 - Envelope Pgto Portal Personalizado ORACLE.TotvsReport

FOPREL00178 - Envelope Pgto Portal Personalizado SQL.TotvsReport

FOPREL00192 - Envelope pgto Model Extrato (frenteverso).TotvsReport

FOPREL25.0025 - 2.004.101 - Envelope de pagamento - Labo 05.0.TotvsReport
