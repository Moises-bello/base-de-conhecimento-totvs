---
article_id: 21678582446999
category: Faturamento - Cadastros
content_hash: 74a2c30ea6593ec8cf198ac7cabd80c358f382036203d37ea28c3fc7b139e702
fetched_at: '2026-06-28T22:38:36.788916+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da condição de pagamento
  Tipo 8
type: support-article
updated_at: '2024-03-05T12:44:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678582446999-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-8
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21678613961495) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como criar uma condição de pagamento do tipo 8?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Recomendado para condições de complexidade muito alta;

**Exemplo em vídeo de como criar (How To Tutorial):**

Determinado com dois blocos númericos. O primeiro determina a distância de dias para o vencimento das duplicatas (a partir da emissão da nota fiscal, assim como a condição de pagamento do Tipo 1).

O segundo determina a porcentagem de pagamento em relação ao total das duplicatas a ser paga nas respectivas parcelas.

![](https://tdn.totvs.com/download/attachments/240310845/81.png?version=1&modificationDate=1664166127307&api=v2)

**Os blocos devem ser separados por []:**

Primeiro bloco: Vencimento das duplicatas (similar ao da condição de pagamento Tipo 1).

Segundo bloco: Percentuais acumulados (concentrados) em cada duplicata respectiva que está no primeiro bloco.

**Atenção:**

O segundo bloco de números deve possuir em sua soma 100% e deve ter a quantidade de números igual a quantidade de parcelas (do primeiro bloco)

**Porcentagem decimal:**

Caso o número da porcentagem seja “quebrado”, por exemplo a porcentagem “Quinze e meio por cento” deve ser representada como “15.5” (com ponto e não vírgula) e separada por vírgulas para que não afete a contagem das demais parcelas e porcentagens.

**Cadastrando:**

E4\_CODIGO = (critério do usuário)

E4\_TIPO = 8

E4\_COND = [30,60,90],[50,22.5,22.5]

![](https://tdn.totvs.com/download/attachments/240310845/82.png?version=1&modificationDate=1664166140633&api=v2)

**Resultado:**

Supondo que o total das parcelas seja R$1000,00. Os pagamentos serão efetuados da seguinte forma:

* 1ª parcela 30 dias após a emissão com valor de R$550, que é 55% do valor total.
* 2ª parcela 60 dias após a emissão com valor de R$225, que é 22,5% do valor total.
* 3ª parcela 90 dias após a emissão com valor de R$225, que é 25,5% do valor total.

**GIF Exemplo do resultado da simulação utilizando uma condição de pagamento Tipo 8 (Tipo 8 - E4\_TIPO = “8”):**

![](https://tdn.totvs.com/download/attachments/240310845/tipo8.gif?version=1&modificationDate=1656449329730&api=v2)

**Saiba mais:**

[**Todas as Condições de Pagamento (MATA360)**](https://tdn.totvs.com/x/PdpSDg)
