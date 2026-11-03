---
article_id: 14191561177879
category: Faturamento - Cadastros
content_hash: e27f94c1741719f7f232ea8a9b0cd33ca2c165dcfbbd44485e23b80a8e429b67
fetched_at: '2026-06-28T22:38:36.761183+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da condição de pagamento
  Tipo 2
type: support-article
updated_at: '2024-03-04T18:47:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14191561177879-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-2
---

Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como criar uma condição de pagamento do tipo 2?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

Nessa condição, o conteúdo código da condição de pagamento (E4\_CODIGO) ajuda na montagem da regra, juntamente com o conteúdo da regra da condição (E4\_COND).

O campo da regra [E4\_COND] é o multiplicador do primeiro e terceiros número do código.

**Exemplo em vídeo de como criar (How To Tutorial):**

**Exemplo (por escrito):**

"Código da condição [E4\_CODIGO]" = **321**

Condição [E4\_COND]" = **10**

* **3** x **10** (E4\_COND) = 30 dias para o primeiro vencimento da primeira parcela
* **2** = 2 Parcelas (não é multiplicado)
* **1** x **10** (E4\_COND) = 10 dias de intervalo entre cada parcela

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14191470928279)  
  
No cadastro da condição de pagamento no Protheus:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14191519649303)

Resultado da simulação de um faturamento no dia 01/01/2023, com valor a ser distribuído de R$100:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21796957980823)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14191557612055)

**Saiba mais**

[**FAT0089 - Condições de Pagamento (MATA360)**](https://tdn.totvs.com/x/PdpSDg)
