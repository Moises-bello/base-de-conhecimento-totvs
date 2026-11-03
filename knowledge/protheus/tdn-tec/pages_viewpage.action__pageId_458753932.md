---
content_hash: 956a1d2df636167c7ea22ea4961bf1785541a3eca66677253c310f2d56d09319
fetched_at: '2026-07-02T19:24:24.133460+00:00'
page_id: '458753932'
product: protheus
source: tdn-tec
title: Posicionamento incorreto de caracteres em relatório TRCT (Rescisão) no módulo
  SIGAGPE.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458753932
version: 1
---

Ocorrência de posicionamento incorreto de alguns caracteres por problema de cálculo de tamanho de caractere

|  |  |
| --- | --- |
| Situação | O posicionamento de caracteres de algumas colunas do relatório TRCT (Rescisão), no módulo SIGAGPE, estava incorreto. |
| Correção | Foi implementado novo cálculo de tamanho de caractere, baseado na média da fonte utilizada no relatório, para que não haja erro no posicionamento inicial da impressão de caracteres das colunas do relatório em questão. |
| Informações adicionais | * Referente ao chamado: Não há ticket associado * Referente à ocorrência: SCHTML-867 * Disponível a partir da build 7.00.131227A - 4.2.3 |
