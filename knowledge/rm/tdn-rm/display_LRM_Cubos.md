---
content_hash: 4350afcbaeb5958c9874fdc9bf7c8f231beda73b049bc456155042c10366256e
fetched_at: '2026-06-29T00:10:43.112751+00:00'
page_id: '549512880'
product: rm
source: tdn-rm
title: Cubos
type: documentation
url: https://tdn.totvs.com/display/LRM/Cubos
version: 7
---

* **TOPCUB007 - Validação Qtde Consumida-Pedida x Planejamento**

Ao executar esse cubo serão exibidos os contratos e os pedidos com quantidade maior que a quantidade que foi planejada. É recomendado que a curva abc esteja com o cálculo atualizado.

* **TOPCUB010 - Indicador Financeiro**

Neste gráfico será exibida informações financeiras do Empreendimento associado ao Projeto.

| Campo | Descrição |
| --- | --- |
| ANO | Ano do período mensal |
| COD\_PESS\_EMPR | Código do empreendimento |
| CODCOLIGADA | Código da coligada do projeto |
| CODPRJ | Código do projeto |
| DATAPERIODO | Data do período mensal |
| IDPRJ | Identificador do projeto |
| MÊS | Mês do período mensal |
| PERIODO | Período mensal |
| PROJETO | Descrição do projeto |
| VR\_EMPR\_BAIXADO | Valor baixado do empreendimento de todas as vendas efetivadas e quitadas. |
| VR\_EMPR\_BAIXADO\_ACUMULADO | Valor baixado do empreendimento acumulado. |
| VR\_EMPR\_RECEBER | Valor a receber do empreendimento de todas as vendas efetivadas e quitadas. |
| VR\_EMPR\_RECEBER\_ACUMULADO | Valor a receber do empreendimento acumulado. |
| VR\_PLANEJADO | Valor planejado de todas as tarefas com [insumo do tipo receita](https://tdn.totvs.com/display/public/LRM/Insumos#:~:text=Insumo%20Receita%20%2D%20Este%20Insumo%20ser%C3%A1,comporta%20como%20se%20estivesse%20desativada.). |
| VR\_PLANEJADO\_ACUMULADO | Valor planejado acumulado. |
| VR\_PRJ\_PAGO\_ACUMULADO | Valor pago do projeto acumulado. |
| VR\_PRJ\_PEDIDO | Valor pedido do projeto de todas as apropriações. |
| VR\_PRJ\_PEDIDO\_ACUMULADO | Valor pedido do projeto acumulado. |

### Fonte de dados do cubo:

* [Apropriações e Movimentações do Backoffice no TCOP - Totvs Construção Obras e Projetos](https://tdn.totvs.com/pages/viewpage.action?pageId=518472242)
* [Vendas - Contratos - Contratos de Venda (Revitalizado)](https://tdn.totvs.com/pages/viewpage.action?pageId=435105210)
* [Indicadores - Curva S](https://tdn.totvs.com/display/public/LRM/Curva+S)
* [Insumos do tipo receita](https://tdn.totvs.com/display/public/LRM/Insumos#:~:text=Insumo%20Receita%20%2D%20Este%20Insumo%20ser%C3%A1,comporta%20como%20se%20estivesse%20desativada.)

* **TOPCUB011 - Indicador de Custo**

Nesse cubo são exibidas informações de custo do projeto.

| Campo | Descrição |
| --- | --- |
| IDPRJ | Identificador do projeto |
| IDTRF | Identificador da tarefa |
| IDISM | Identificador do insumo. Observação: este campo pode estar vazio. |
| CODPRJ | Código do projeto |
| PROJETO | Nome do projeto |
| CODTRF | Código da tarefa |
| TAREFA | Descrição da tarefa |
| CODISM | Código do insumo |
| INSUMO | Descrição do insumo |
| CODGIS | Código do grupo de custo |
| GRUPOCUSTO | Descrição do grupo de custo |
| DATAPERIODO | Data do período mensal |
| MÊS | Mês do período mensal |
| ANO | Ano do período mensal |
| PERC\_PLANEJADO | Percentual planejado. Origem dos dados: "Curva S" (MCURVASISMTRF). |
| PERC\_REALIZADO | Percentual realizado. Origem dos dados: "Curva S" (MCURVASISMTRF). |
| QTDE\_PLANEJADA | Quantidade planejada. Origem dos dados: "Curva S" (MCURVASISMTRF). |
| QTDE\_REALIZADA | Quantidade realizada. Origem dos dados: "Curva S" (MCURVASISMTRF). |
| VLR\_PLANEJADO | Valor planejado. Origem dos dados: "Curva S" (MCURVASISMTRF). |
| VLR\_REALIZADO | Valor realizado. Origem dos dados: "Curva S" (MCURVASISMTRF). |
| VLR\_APROPRIADO | Valor apropriado. Origem dos dados "Insumos Apropriados" (MISMAPROP). |
| VLR\_PEDIDO | Valor pedido. Origem dos dados: "Movimentações do BackOffice" (MMOV). |
| VLR\_PAGO | Valor pago. Origem dos dados: "Movimentações do BackOffice"(MMOV). |
| VAR\_CUSTO\_APROPRIADO | Valor do custo apropriado. = VLR\_APROPRIADO / VLR\_PLANEJADO \* 100 |
| VAR\_CUSTO\_REALIZADO | Valor do custo realizado = VLR\_REALIZADO / VLR\_PLANEJADO \* 100 |
| PERC\_PLANEJADO\_ACUMULADO | Percentual planejado acumulado considerando a relação Tarefa e Insumo |
| PERC\_REALIZADO\_ACUMULADO | Percentual realizado acumulado considerando a relação Tarefa e Insumo |
| QTDE\_PLANEJADA\_ACUMULADO | Quantidade planejada acumulado considerando a relação Tarefa e Insumo |
| QTDE\_REALIZADA\_ACUMULADO | Quantidade realizada acumulado considerando a relação Tarefa e Insumo |
| VLR\_PLANEJADO\_ACUMULADO | Valor planejado acumulado considerando a relação Tarefa e Insumo |
| VLR\_REALIZADO\_ACUMULADO | Valor realizado acumulado considerando a relação Tarefa e Insumo |
| VLR\_APROPRIADO\_ACUMULADO | Valor apropriado acumulado |
| VLR\_PEDIDO\_ACUMULADO | Valor pedido acumulado |
| VLR\_PAGO\_ACUMULADO | Valor pago acumulado |
| VAR\_CUSTO\_APROPRIADO\_ACUMULADO | Valor do custo apropriado acumulado |
| VAR\_CUSTO\_REALIZADO\_ACUMULADO | Valor do custo realizado |
| QTDE\_A\_PEDIR | Quantidade a Pedir |
| QTDE\_A\_PEDIR\_ACUMULADO | Quantidade a Pedir Acumulada |
| VLR\_TOTAL\_A\_PEDIR | Valor Total a Pedir |
| VLR\_TOTAL\_ORCADO | Valor Total Orçado |
| VAR\_ORCADO\_ATUAL | % Variação Orçada Atual |
| VLR\_TOTAL\_A\_PEDIR | Valor Total a Pedir |
| VLR\_TOTAL\_ORCADO | Valor Total Orçado |
| VAR\_ORCADO\_ATUAL | Valor Orçado Atual |

### Fonte de dados do cubo:

* [Apropriações e Movimentações do Backoffice no TCOP - Totvs Construção Obras e Projetos](https://tdn.totvs.com/pages/viewpage.action?pageId=518472242)
* [Vendas - Contratos - Contratos de Venda (Revitalizado)](https://tdn.totvs.com/pages/viewpage.action?pageId=435105210)
* [Indicadores - Curva S](https://tdn.totvs.com/display/public/LRM/Curva+S)
* [Insumos do tipo receita](https://tdn.totvs.com/display/public/LRM/Insumos#:~:text=Insumo%20Receita%20%2D%20Este%20Insumo%20ser%C3%A1,comporta%20como%20se%20estivesse%20desativada.)
