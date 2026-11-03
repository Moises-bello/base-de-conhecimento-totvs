---
content_hash: 7a1635abd5516099767d0684908f503f62615718a3f70a4f32cb6764d623a2de
fetched_at: '2026-06-29T00:10:58.952771+00:00'
page_id: '607862931'
product: rm
source: tdn-rm
title: Gráficos - TCOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607862931
version: 15
---

* **TOPGRA003 - Gráfico de informações financeiras do Empreendimento e do Projeto**
* **TOPGRA004 - Gráfico de informações financeiras do Empreendimento e do Projeto - Acumulado**
* **TOPGRA005 - Gráfico de Indicador de Custos do Projeto**
* **TOPGRA006 - Gráfico de Indicador de Custos do Projeto - Acumulado**

### **Gráficos - Informações Financeiras do Empreendimento e do Projeto**

Neste gráfico será exibida informações financeiras do Empreendimento associado ao Projeto:

É possível criar um anexo de gráfico na visão de projetos:

[Como inserir um gráfico como anexo](https://tdn.totvs.com/pages/releaseview.action?pageId=438282349)

[Configuração de gráficos](https://tdn.totvs.com/pages/releaseview.action?pageId=271847659)

Foi criado um Provider "82 - Informações Financeiras do Projeto e do Empreendimento":

Campos do Provider:

1617306319212\_1327986939

| Campo | Descrição |
| --- | --- |
| DATAPERIODO | Data do período mensal |
| CODCOLIGADA | Código da coligada do projeto |
| IDPRJ | Identificador do projeto |
| CODPRJ | Código do projeto |
| PROJETO | Descrição do projeto |
| COD\_PESS\_EMPR | Código do empreendimento |
| ANO | Ano do período mensal |
| MÊS | Mês do período mensal |
| PERIODO | Período mensal |
| VR\_PLANEJADO | Valor planejado de todas as tarefas com [insumo do tipo receita](https://tdn.totvs.com/display/public/LRM/Insumos#:~:text=Insumo%20Receita%20%2D%20Este%20Insumo%20ser%C3%A1,comporta%20como%20se%20estivesse%20desativada.). |
| VR\_EMPR\_RECEBER | Valor a receber do empreendimento de todas as vendas efetivadas e quitadas. |
| VR\_EMPR\_BAIXADO | Valor baixado do empreendimento de todas as vendas efetivadas e quitadas. |
| VR\_PRJ\_PEDIDO | Valor pedido do projeto de todas as apropriações. |
| VR\_PLANEJADO\_ACUMULADO | Valor planejado acumulado. |
| VR\_EMPR\_RECEBER\_ACUMULADO | Valor a receber do empreendimento acumulado. |
| VR\_EMPR\_BAIXADO\_ACUMULADO | Valor baixado do empreendimento acumulado. |
| VR\_PRJ\_PEDIDO\_ACUMULADO | Valor pedido do projeto acumulado. |
| VR\_PRJ\_PAGO\_ACUMULADO | Valor pago do projeto acumulado. |

### **Gráficos - Indicadores de Custo do Projeto**

Foi criado um Provider "83 - Indicadores de Custo do Projeto":

Campos do Provider:

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
| PERC\_PLANEJADO\_ACUMULADO | Percentual planejado acumulado |
| PERC\_REALIZADO\_ACUMULADO | Percentual realizado acumulado |
| QTDE\_PLANEJADA\_ACUMULADO | Quantidade planejada acumulado |
| QTDE\_REALIZADA\_ACUMULADO | Quantidade realizada acumulado |
| VLR\_PLANEJADO\_ACUMULADO | Valor planejado acumulado |
| VLR\_REALIZADO\_ACUMULADO | Valor realizado acumulado |
| VLR\_APROPRIADO\_ACUMULADO | Valor apropriado acumulado |
| VLR\_PEDIDO\_ACUMULADO | Valor pedido acumulado |
| VLR\_PAGO\_ACUMULADO | Valor pago acumulado |
| VAR\_CUSTO\_APROPRIADO\_ACUMULADO | Valor do custo apropriado acumulado |
| VAR\_CUSTO\_REALIZADO\_ACUMULADO | Valor do custo realizado |

**Atenção**: É necessário realizar o vínculo do projeto com o empreendimento através do Gestão de Imóveis:

* Após acessar o empreendimento no Gestão de Imóveis, no menu esquerdo em Integração, acessar a opção "Construção Obras e Projetos" conforme imagem abaixo:

* No Lookup "Projeto" escolher o tipo do projeto para o empreendimento e Salvar (Criar o filtro todos para listagem dos tipos de projeto):

### 

### Fonte de dados dos providers:

* [Apropriações e Movimentações do Backoffice no TCOP - Totvs Construção Obras e Projetos](https://tdn.totvs.com/pages/viewpage.action?pageId=518472242)
* [Vendas - Contratos - Contratos de Venda (Revitalizado)](https://tdn.totvs.com/pages/viewpage.action?pageId=435105210)
* [Indicadores - Curva S](https://tdn.totvs.com/display/public/LRM/Curva+S)
* [Insumos do tipo receita](https://tdn.totvs.com/display/public/LRM/Insumos#:~:text=Insumo%20Receita%20%2D%20Este%20Insumo%20ser%C3%A1,comporta%20como%20se%20estivesse%20desativada.)
