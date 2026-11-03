---
article_id: 37838757814679
category: Financeiro - Smart View
content_hash: e80acb03b01958b009ef92f173328c9cf7b4367e86a2b64116f82b3a0f9e5506
fetched_at: '2026-06-28T22:37:44.693067+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINSV047 - Previsão de comissões
type: support-article
updated_at: '2026-03-19T12:19:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37838757814679-Cross-Segmentos-Backoffice-Linha-Protheus-FINSV047-Previs%C3%A3o-de-comiss%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37838757806359) Tempo aproximado para leitura: **00:15 min**  
  
**Dúvida**  
Qual o relatório em que é possível visualizar as previsões de comissões?   
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) - Comissão - A partir da release 12.1.33.  
  
**Solução**  
Relatório do Smart View **Previsão de Comissões (FINSV047)** apresenta títulos a receber (em aberto ou baixados) e pedidos de venda configurados para geração de comissão.

Após a execução da rotina [**MATA530 – Atualização de Pagamento de Comissão**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25811305833367-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATA530-Atualiza%C3%A7%C3%A3o-de-Pagamento-de-Comiss%C3%B5es), os registros deixam de ser exibidos no relatório.

Por meio dos parâmetros, é possível filtrar e configurar algumas validações iniciais conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37839594714007)

Após a realização das validações, os relatórios serão exibidos conforme ilustrado na imagem abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37839602834327)

Por meio do ícone localizado no canto superior direito, conforme exemplificado, é possível selecionar ou remover colunas, permitindo a personalização da visualização conforme a necessidade do usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37839594718871)

Por meio do ícone **XLSX**, é possível exportar o relatório para o Excel, conforme ilustrado no exemplo a seguir.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37839602837399)

A seguir, são apresentadas algumas das principais **características e validações referentes aos parâmetros** do relatório:

* Os valores dos pedidos de venda podem sofrer alterações até o momento do faturamento.
* O usuário pode optar por visualizar ou não os pedidos de venda.
* O agrupamento padrão é realizado por **vendedor**, com classificação em **título original**, **título renegociado** e **pedido de venda**.
* O valor previsto da comissão é sempre demonstrado no **título original**, não sendo impactado pelo parâmetro **MV\_COMILIQ**.
* É possível informar a alíquota de **Imposto de Renda**, sendo exibidos o valor do IR calculado e o valor líquido estimado da comissão.
* Títulos de crédito não são apresentados no relatório.
* O objeto de negócio suporta até **cinco vendedores** por pedido de venda ou título a receber.
* Os valores acessórios são considerados no cálculo da comissão, em conformidade com a rotina **FINA440**, sendo títulos e pedidos de venda apresentados de forma independente.

**Saiba mais**

[Smart View - Previsão de comissões](https://tdn.totvs.com/pages/releaseview.action?pageId=815586043)

[Configuração inicial Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=665287989)  
[Requisitos Mínimos](https://tdn.totvs.com/pages/viewpage.action?pageId=678582172)
