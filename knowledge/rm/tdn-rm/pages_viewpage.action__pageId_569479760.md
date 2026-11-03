---
content_hash: 762a736bf3e02dbff761b217faa11d8240bb4da873a96ee2052d1bbd2bfda455
fetched_at: '2026-06-29T00:10:51.602822+00:00'
page_id: '569479760'
product: rm
source: tdn-rm
title: Balancete Consolidado (Ernst & Young)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=569479760
version: 4
---

Através desse layout é possível extrair dados consolidados da contabilidade, de duas ou mais empresas, que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

Grupo EmpresarialO relatório gera os valores consolidados de acordo com as coligadas do [Grupo Empresarial](https://tdn.totvs.com/display/LRM/Grupo+Empresarial) informado no plano de contas paralelo e também pelo percentual de consolidação informado no cadastro de .

| ID | Formato | Tamanho | Dec | Descrição | Origem de dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 30 |  | Código da coligada | Código da coligada que deu origem ao saldo da conta. |  |
| 2 | Alfanumérico | 30 |  | Código da conta | Código da conta existente no plano de contas consolidado. |  |
| 3 | Alfanumérico | 30 |  | Segmento da conta | Não aderente ao RM. |  |
| 4 | Alfanumérico | 30 |  | Ano Fiscal | Não aderente ao RM. |  |
| 5 | Alfanumérico | 40 |  | Período Fiscal | Não aderente ao RM. |  |
| 6 | Decimal |  | 2 | Saldo de fechamento na moeda funcional | Saldo consolidado da primeira moeda. | O Saldo devedor deve ser gerado positivo e o Saldo credor negativo. |
| 7 | Alfanumérico | 30 |  | Código da moeda funcional | Moeda corrente existente nos parâmetros do módulo contábil. |  |
| 8 | Decimal |  | 2 | Saldo final na moeda de apresentação | Não aderente ao RM. |  |
| 9 | Alfanumérico | 30 |  | Código da moeda de apresentação | Não aderente ao RM. |  |
