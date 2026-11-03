---
content_hash: 7e80751c0759a59e6cded23562d3da5f2c8a2939086cd9d7a4500aba7986a445
fetched_at: '2026-06-29T00:10:52.153515+00:00'
page_id: '570361124'
product: rm
source: tdn-rm
title: Plano de Contas Consolidado (Ernst & Young)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570361124
version: 7
---

Listagem das contas consolidadas que foram exibidas no arquivo CTB - Consolidation trial balance.

| ID | Formato | Tamanho | Dec | Descrição | Origem de Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Numérico |  | 2 | Código da Conta Consolidada | Código da conta do plano de contas paralelo. | Código da conta consolidada que está sendo consolidada. Esse código será referenciado no arquivo "Consolidation trial balance (Consolidação do Balancete)". |
| 2 | Alfanumérico | 30 |  | Segmento da Conta | Não aderente ao RM. |  |
| 3 | Alfanumérico | 30 |  | Nome da Conta | Nome da conta no plano de contas paralelo. |  |
| 4 | Alfanumérico | 30 |  | Tipo da Conta | Natureza da conta para emissão do sped e natureza da conta (credora ou devedora). | Se a Natureza do SPED for "Conta de Ativo", então "Assets".  Se a Natureza do SPED for "Conta de Passivo", então "Liabilities".  Se a Natureza do SPED for "Patrimônio Liquido", então "Equity".  Se a Natureza do SPED for "Conta de Resultado" e a Natureza for Credora, então "Revenue".  Se a Natureza do SPED for "Conta de Resultado" e a Natureza for Devedora, então "Expenses" Caso contrário, será gerado vazio. |
| 5 | Alfanumérico | 30 |  | Subtipo | Não aderente ao RM. |  |
| 6 | Alfanumérico | 30 |  | Classe | Não aderente ao RM. |  |
| 7 | Alfanumérico | 30 |  | SubClasse | Não aderente ao RM. |  |
