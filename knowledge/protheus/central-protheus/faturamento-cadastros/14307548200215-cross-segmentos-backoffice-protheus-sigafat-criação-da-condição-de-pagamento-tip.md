---
article_id: 14307548200215
category: Faturamento - Cadastros
content_hash: dc4bdf7222cad0ad02715ea221a139e0e44cc65354ea22a28bd583c33b798c09
fetched_at: '2026-06-28T22:38:36.765033+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da condição de pagamento
  Tipo 3
type: support-article
updated_at: '2024-03-04T18:48:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14307548200215-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-3
---

Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como criar uma condição de pagamento do tipo 3?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

Cada condição de pagamento simboliza como serão gerados as datas de vencimento e valores de cada parcela no módulo financeiro.

A regra de condição e vencimento são definidos no cadastro das condições de pagamento, no campo "Condição [E4\_COND]".

**No caso da condição de pagamento Tipo 3:**

O primeiro espaço entre vírgulas simboliza a quantidade parcelas.

O segundo espaço entre vírgulas simboliza os dias de intervalo até o vencimento da primeira parcela.

O terceiro espaço entre vírgulas para frente simboliza os dias do mês em que o vencimento será reajustado para cair caso naturalmente não caia após o primeiro intervalo.

**Exemplo em vídeo de como criar (How To Tutorial):**

**Exemplo (por escrito):**

"Condição [E4\_COND]" = **2,30,2,22**

* **2 →** 2 Parcelas
* **30 →** 30 dias de intervalo para o primeiro vencimento (da primeira parcela)
* **2 e 22 →** Dias do mês em que os vencimentos poderão ocorrer (ou serão reajustados para cair nesses dias caso não caiam nesses dias (2 ou 22) naturalmente pelo vencimento)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14307262495895)  
  
No cadastro da condição de pagamento no Protheus:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14307349068823)

Resultado (parcelas e vencimento das parcelas) da simulação de um faturamento no dia 01/01/2023, com valor a ser distribuído de R$100:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21797028789527)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14307401046807)

**Saiba mais**

[**FAT0089 - Condições de Pagamento (MATA360)**](https://tdn.totvs.com/x/PdpSDg)
