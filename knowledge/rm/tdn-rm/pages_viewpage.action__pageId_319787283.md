---
content_hash: 2e0cfddab1655db68ab9a181916f7a140c4d262a12c3b8a0a50bf0ad1e871c81
fetched_at: '2026-06-29T00:08:47.255861+00:00'
page_id: '319787283'
product: rm
source: tdn-rm
title: Manual - Fórmula (RM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787283
version: 3
---

A ligação de fórmula RM permite associar o resultado da execução de uma fórmula RM ao valor do campo. A ligação de fórmula só pode ser utilizada quando o registro estiver ligado a um contexto de Conjunto de Dados, Stored Procedure, Data Server (RM), Consulta SQL (RM) pois os dados da lista do contexto serão utilizados como contexto de execução da fórmula.

\* Esta opção só está disponível no Gerador RM.

![](/download/attachments/319787283/formula_rm.png?version=1&modificationDate=1512921866000&api=v2)

1Fórmula

Selecione a Fórmula RM que será executada para cálculo do valor do campo do registro.

Atenção

A utilização deste tipo de ligação deve ser evitada pois a execução da Fórmula RM tem um alto custo de processamento. Ao utilizar esta ligação a fórmula será executada uma vez para cada registro, o que pode impactar no tempo de geração e no alto consumo de recursos de banco e do servidor de aplicação.
