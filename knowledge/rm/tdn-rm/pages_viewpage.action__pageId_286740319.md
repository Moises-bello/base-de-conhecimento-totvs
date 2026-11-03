---
content_hash: fa05fbb136c68b3e192592aa1a79eb49b577969eaaefe1fa0d120feb2c0acf49
fetched_at: '2026-06-29T00:08:41.623421+00:00'
page_id: '286740319'
product: rm
source: tdn-rm
title: 1245307 DEDUINTEGRACOES-229 DT Cancelamento de Lançamento originado de bolsa
  de crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286740319
version: 101
---

# Cancelamento de Lançamento Originado do Educacional

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Cancelamento de Lançamento |
| **Situação/Requisito:** | Geramos lançamentos para parcelas contendo uma bolsa de Crédito de 50%. Após a geração, o sistema gerou 2 lançamentos, um para o aluno e outro para o responsável pelo pagamento da bolsa de crédito. O sistema permitiu o Cancelamento e Exclusão do lançamento referente a bolsa de crédito, mesmo com o lançamento do aluno ainda em aberto.  Sistema deveria bloquear a exclusão do lançamento em questão. |
| **Solução/Implementação:** | Melhoria na validação do cancelamento de lançamentos provenientes do TOTVS Educacional para que não seja possível cancelar um lançamento originado de uma bolsa de crédito.  Melhoria para que ao cancelar um lançamentos provenientes do TOTVS Educacional que tenha lançamentos financeiro provenientes de bolsa de crédito vinculado, o lançamento de bolsa de crédito será cancelado automaticamente. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
