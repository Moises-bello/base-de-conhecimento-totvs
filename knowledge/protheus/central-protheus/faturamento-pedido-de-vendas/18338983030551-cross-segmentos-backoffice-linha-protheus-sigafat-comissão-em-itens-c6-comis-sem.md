---
article_id: 18338983030551
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: e550a55ffa1b4a5e3580a793864012589b5984f118b7778ce860fd9be66ce5f7
fetched_at: '2026-06-28T22:38:42.488742+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Comissão em itens
  (C6_COMIS) sem porcentagem informada
type: support-article
updated_at: '2023-10-19T19:07:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18338983030551-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Comiss%C3%A3o-em-itens-C6-COMIS-sem-porcentagem-informada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18338946707223) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como o sistema calcula comissões em itens com e sem porcentagem informadas no item?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**O sistema gera a comissão única com essa hierarquia:

[1] C6\_COMIS1 -> [2] B1\_COMIS -> [3] C5\_COMIS1 ->[4] A1\_COMIS -> [5] A3\_COMIS

Caso o campo mais a esquerda seja preenchido, é ignorado a comissão preenchido nos campos mais para direita, exemplo: Preenchido comissão nos campos A3\_COMIS e B1\_COMIS, é respeitado a comissão informada no campo B1\_COMIS.

Como o sistema trata a comissão tendo itens com comissão informada e itens sem comissão ([1] C6\_COMIS) informada?

O sistema irá considerar para o item sem comissão informada, a comissão informada nos passos anteriores ([2] B1\_COMIS -> [3] C5\_COMIS1 -> [4] A1\_COMIS -> [5] A3\_COMIS).

**Exemplo de faturamento do pedido de venda:**

C5\_COMIS1 = 5% (cabeçalho do pedido de venda)

Item 1 | Valor total R$100 | C6\_COMIS1 = 2%

Item 2 | Valor total R$100 | C6\_COMIS1 = 0%

Ao faturar o pedido de venda, será levado ao financeiro, a comissão de 3,5%.

Comissão sobre o item 1: 2% de R$100 = R$2

Comissão sobre o item 2: 5% (cabeçalho) de R$100 = R$5

Comissão total tem de ser R$7. (R$7 é 3,5% de R$200 que é o total do pedido de venda)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18338826055191)

**OBSERVAÇÃO:** Caso não queira a junção das comissões, ou seja, que sobre o item sem comissão informada não tenha realmente nenhuma comissão gerada, em todos os passos anteriores não deve ter a comissão preenchida (B1\_COMIS/C5\_COMIS1/A1\_COMIS/A3\_COMIS).
