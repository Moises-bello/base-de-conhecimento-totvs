---
content_hash: caaa0931f0cd877b0bcac7f66268a037543d0f07a855ae66358fc5a22a5d0791
fetched_at: '2026-06-29T00:12:13.417813+00:00'
page_id: '954104813'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência de INSS e Relatório de Conferência de INSS Patronal
  - Diferença de centavos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=954104813
version: 6
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **TOTVS - Folha de Pagamento** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Relatório de Conferência de INSS e Relatório de Conferência de INSS Patronal - Diferença de centavos |
| País: | Brasil |
| Ticket: |  |
| Issue (informe o requisito relacionado) : | [DRHROTRM-13861](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13861 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410.256
* 12.1.2502.160
* 12.1.2506.104 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Ao gerar o lançamento financeiro do tipo **"25 - Total Guia INSS DCTFWeb"**, o sistema apresenta diferença de centavos entre o valor lançado e os valores exibidos noRelatório de Conferência do INSS Patronal e no Relatório de Conferência de INSS.

**04. SOLUÇÃO**

Identificamos que, na geração do **Relatório de Conferência do INSS Patronal** e do **Relatório de Conferência de INSS**, havia uma tratativa para que, caso existisse uma diferença de até R$ 0,09 (nove centavos) entre o valor do segurado calculado pela folha e o valor calculado pelo governo, o sistema considerasse automaticamente o valor do governo.

Essa lógica resultava em divergências de centavos entre os relatórios e o lançamento financeiro.

Com o ajuste realizado, as diferenças em centavos entre os valores dos segurados passam a ser exibidas nos relatórios, facilitando a identificação de eventuais discrepâncias no lançamento financeiro e proporcionando uma conferência mais precisa e eficiente.

**1)** Geração do Relatório de Conferência de INSS

**2)** Geração do Relatório de Conferência de INSS Patronal

**3)** Geração do Lançamento Financeiro

Cálculo: R$23.638,02 (liquido folha) – R$77,00 (PIS filial 1) - R$124,74 (PIS filial 2) – R$75,00 (PIS filial 3) = **R$23.361,28**

## **05. DOCUMENTAÇÃO**

[Lançamento Financeiro](https://tdn.totvs.com.br/display/public/LRM/Cadastros+Financeiros)
