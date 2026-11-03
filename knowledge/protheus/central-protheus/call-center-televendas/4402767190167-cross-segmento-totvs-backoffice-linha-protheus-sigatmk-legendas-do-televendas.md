---
article_id: 4402767190167
category: Call Center - Televendas
content_hash: 176036c622e15218a1f90d0a760a7c325c7369585fdb6e7de89a95766e3ce056
fetched_at: '2026-06-28T22:41:30.204001+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigatmk - Legendas do
  Televendas
type: support-article
updated_at: '2021-06-17T11:49:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402767190167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigatmk-Legendas-do-Televendas
---

**Dúvida**Qual o significado das legendas exibidas na rotina Televendas do Call Center?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigatmk- Todas as versões  
  
**Solução**

Na rotina Televendas do Call Center (**TMKA271**) os **Status disponíveis** são representados de acordo com as seguintes **legendas**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402766578711/mceclip0.png)- **Marrom** - onde o atendimento não possui cancelamento **(UA\_CANC=Vazio)** e o campo de operação é igual a 3.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402766633111/mceclip1.png)- **Azul** - onde o atendimento não possui cancelamento **(UA\_CANC=Vazio)** e o campo de operação é igual a 2. Nesta fase, ainda pode-se integrar o orçamento para finalização do atendimento nas rotinas de Varejo,  Venda Assistida ou Venda Direta(**Loja701**), habilitando o parâmetro **mv\_tmkloj** ou pode-se efetuar alterações para geração de um pedido de vendas (**MATA410**) para o Faturamento.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402766716695/mceclip2.png)- Verde - onde o atendimento não possui cancelamento **(UA\_CANC=Vazio),**o campo de operação é igual a 1 e ainda não gerou nota fiscal **(UA\_DOC=Vazio**). Essa legenda significa que foi gerado o pedido de venda para o módulo Faturamento e não houve o faturamento direto pelo Call Center, que é habilitado pelo parâmetro **mv\_opfat**, ou houve alguma restrição de bloqueio de regra de negócios (**FATA100**) ou crédito (**MATA450**) ou estoque (**MATA455**) que impediu o faturamento direto pelo Call Center, gerando o pedido de vendas para que seja tratado conforme as regras do módulo Faturamento.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402769817623/mceclip5.png)- Vermelho - onde o atendimento não possui cancelamento **(UA\_CANC=Vazio),**o campo de operação é igual a 1 e ocorreu a geração da nota fiscal para este atendimento **(UA\_DOC=F2\_DOC**).

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402769827863/mceclip8.png) - Preto - Atendimento Cancelado (**UA\_CANC=S).** Significa que foi gerado um pedido de vendas para o módulo faturamento e posteriormente, este pedido foi excluído pela rotina de Exclusão de Pedido **(TMKA150).**
