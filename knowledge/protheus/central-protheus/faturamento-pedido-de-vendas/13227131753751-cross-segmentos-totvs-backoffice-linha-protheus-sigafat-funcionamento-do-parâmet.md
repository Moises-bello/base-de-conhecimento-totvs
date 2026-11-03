---
article_id: 13227131753751
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 50ab83c52a51aca360723aad8ecec6ed05253aac7909d11549354b627248fae0
fetched_at: '2026-06-28T22:38:42.739544+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Funcionamento
  do parâmetro MV_TIPO9SP
type: support-article
updated_at: '2023-03-20T18:32:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13227131753751-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-TIPO9SP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual o conceito e como utilizar o parâmetro MV\_TIPO9SP?   
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**Esse parâmetro tem de ser criado com essa estrutura:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13226841456535)

Uma vez criado, ele não deixa salvar o pedido de vendas se no pedido estiver uma condição do tipo 9 e as parcelas e datas não estiverem informadas nos campos **C5\_PARCn** e **C5\_DATAn**.

* **MV\_TIPO9SP = .F.**

**(Não deixa salvar se o valor das parcelas "C5\_PARCn" seja nulo ou menor que o total das linhas de item "C6\_VALOR")**

"Condição de pagamento (**C5\_CONDPAG**)" = "009" (Condição de pagamento do tipo 9)

"Valor da parcela 1 (**C5\_PARC1**)" = "0,00" ou "100,0"

"Vencimento da parcela 1 (**C5\_DATA1**)" = "Vazio" ou "12/12/2023"

"Valor total do pedido (**C6\_VALOR**)" = "1000,00"

**Não é possível salvar o pedido de vendas pois aparece o Help A410TIPO9:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13226965536023)

* **MV\_TIPO9SP = .T.**

**(Deixa salvar o pedido de venda mesmo se o valor das parcelas "C5\_PARCn" seja nulo ou menor que o total das linhas de item "C6\_VALOR")**

"Condição de pagamento **(C5\_CONDPAG**)" = "009" (Condição de pagamento do tipo 9)

"Valor da parcela 1 **(C5\_PARC1)**" = "0,00" ou "100,0"

"Vencimento da parcela 1 **(C5\_DATA1)**" = "Vazio" ou "12/12/2023"

"Valor total do pedido **(C6\_VALOR)**" = "1000,00"

**É possível salvar o pedido de vendas pois aparece o Help A410TIPO9 de maneira informativa:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13226965536023)**

**Em seguida aparece este Help e é possível voltar para acertar os valores ou salvar o pedido de venda:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13227028869783)**

**Saiba Mais**

Compreenda as regras e características gerais das Condições de Pagamento disponíveis no Protheus: **[FAT0089 - Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)**
