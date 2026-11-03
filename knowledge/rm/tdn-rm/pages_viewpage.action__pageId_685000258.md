---
content_hash: a04b186c06aefe1fd5d033ceaca44d9143dd1143c00f8f74805fb6e04031a840
fetched_at: '2026-06-29T00:11:18.319710+00:00'
page_id: '685000258'
product: rm
source: tdn-rm
title: Liberação de Contas para Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=685000258
version: 10
---

**ÍNDICE**

1. **Visão Geral**
2. **Exemplo de Utilização**

sumarioVisão Geral

**01. VISÃO GERAL**

Essa rotina é responsável por encerrar as parciais em lote.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Informações

Neste processo somente é possível o encerramento em lotes de atendimentos Externos com status em aberto.

A rotina fica localizada no menu em Faturamento > Particular e Convênios > Liberação de Contas para Faturamento

Na primeira etapa, deverão ser informados os filtros de acordo com a necessidade.

Após avançar serão listadas as parciais dos atendimentos Externos que possuem débitos, caso o convênio da Parcial utiliza o padrão TISS, somente serão listados as parciais que tenham Guias com um dos três tipos de guia registradas na tela de Guia / Autorização.

Após executar o processo, o sistema irá retornar um log retornando para cada parcial se ela foi encerrada com sucesso ou se validações impediram o seu encerramento, nesse momento cabe ao faturista analisar cada Parcial e realizar as devidas correções.
