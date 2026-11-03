---
article_id: 14178272061463
category: Faturamento - Cadastros
content_hash: dc9c1325335c471d0c38bb24febadd3cf58e2a5a6331867c7529db17b1276587
fetched_at: '2026-06-28T22:38:36.756937+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da condição de pagamento
  Tipo 1
type: support-article
updated_at: '2024-03-04T18:47:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14178272061463-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21796758226455) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como criar uma condição de pagamento do tipo 1?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

Cada espaço entre as vírgulas da estruturação, representa as parcelas e os dias para o vencimento de cada parcela, após a emissão.

**Exemplo em vídeo de como criar (How To Tutorial):**

**Exemplo 1:**

"Condição [E4\_COND]" = 5, 10

* 2 parcelas (5 e 10)
* Parcela 1: (5 dias após emissão) - "Vencimento [E1\_VENCTO]: 06/01/2023"
* Parcela 2: (10 dias após emissão) - "Vencimento [E1\_VENCTO]: 11/01/2023"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14178358281367)  
  
No cadastro da condição de pagamento no Protheus:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14178112811927)

Resultado da simulação de um faturamento no dia 01/01/2023, com valor a ser distribuído de R$100:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14178146924183)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14178171395223)

**Exemplo 2: A vista**

"Condição [E4\_COND]" = 0

* 1 parcela (0)
* Parcela 1: (0 dias após emissão, ou seja, no própria dia de emissão) - "Vencimento [E1\_VENCTO]: 01/01/2023"

No cadastro da condição de pagamento no Protheus:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14178225651095)

Resultado da simulação de um faturamento no dia 01/01/2023, com valor a ser distribuído de R$100:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14178224928535)

**Saiba mais**

[**FAT0089 - Condições de Pagamento (MATA360)**](https://tdn.totvs.com/x/PdpSDg)
