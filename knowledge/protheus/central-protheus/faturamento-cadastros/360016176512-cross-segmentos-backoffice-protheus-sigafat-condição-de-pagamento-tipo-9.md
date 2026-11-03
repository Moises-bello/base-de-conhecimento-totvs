---
article_id: 360016176512
category: Faturamento - Cadastros
content_hash: 81b31ecea2a5ad524147a2907fdaa7356d0123fac81a50a98fe45b6e1890aaf4
fetched_at: '2026-06-28T22:38:36.752662+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Condição de Pagamento Tipo
  9
type: support-article
updated_at: '2025-04-22T11:10:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016176512-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Condi%C3%A7%C3%A3o-de-Pagamento-Tipo-9
---

**Dúvida**

Como utilizar a condição de pagamento do tipo 9?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - a partir da versão 11.80  
  
**Solução**

A **Condição de Pagamento** do **Tipo 9** é utilizada quando não há um Tipo que automatize a regra do cliente (ou quando não há uma regra pré-definida para geração das duplicatas).

No Tipo 9, o usuário informa manualmente de acordo com sua regra, no próprio Pedido de Venda, o valor e a data que deverá gerar cada duplicata.

**Exemplo em vídeo de como criar (How To Tutorial):**

Para este tipo, deve-se cadastrar uma nova Condição de Pagamento - **MATA360**. Informe no campo Cond. Pagto: zero (0) ou o símbolo percentual (%):

* Zero (0) - para os parcelamentos serem considerados em valor moeda;
* O símbolo de porcentagem (%) - para utilizar os campos Parcelas do arquivo de Pedidos de Vendas como percentuais a serem parcelados.

Assim, o sistema irá "desconsiderar a condição" e considerar os campos registrados no Próprio Pedido.

**Observações:**

* Se no campo Cond.Pagto (**E4\_COND**) for informado parcelas separadas por virgula, exemplo, 0,30,60, o sistema irá exibir o **Help: Cond. Pagto.**
* Pode-se definir a obrigatoriedade de informar os valores das parcelas (não permitir salvar o Pedido sem informar os valores) através do parâmetro **MV\_TIPO9SP = .F.**
* **[MV\_DATAINF - Condição de pagamento](https://tdn.totvs.com/pages/createpage.action?spaceKey=PROT&title=MV_DATAINF+-+Condi%C3%A7%C3%A3o+de+pagamento&linkCreation=true&fromPageId=238034990):** Bloqueia faturamento quando 1o vencto for menor que a data de emissao da NF na cond.pagto.tipo 9(T=Bloqueia /F=Fatura)
* Ao consultar a **Planilha Financeira** (Pedido de Vendas > Ações relacionadas > Planilha > Aba Duplicatas), as datas para respectivas duplicatas **serão exibidas apenas depois de confirmar o Pedido**, ao visualizar. Isto porque não há uma regra automatizada do sistema (como há nos demais tipos) para que seja feita a projeção.

**Saiba mais:**

**[FAT0074 - Condição de Pagamento Tipo 9](http://tdn.totvs.com/pages/releaseview.action?pageId=238034990)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help Cond.Pagto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403752913687-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-Cond-Pagto)**
