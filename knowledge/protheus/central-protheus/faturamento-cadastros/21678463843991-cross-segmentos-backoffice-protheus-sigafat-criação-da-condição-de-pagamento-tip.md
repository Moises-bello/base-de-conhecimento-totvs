---
article_id: 21678463843991
category: Faturamento - Cadastros
content_hash: a6853425184afe6369748953ddec3557af9e4ea50c1af3f42e9696841d3f085e
fetched_at: '2026-06-28T22:38:36.783944+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da condição de pagamento
  Tipo 7
type: support-article
updated_at: '2024-03-05T12:47:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678463843991-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-7
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21678477320471) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como criar uma condição de pagamento do tipo 7?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Recomendado para condições de complexidade muito alta;

**Exemplo em vídeo de como criar (How To Tutorial):**

O primeiro algarismo simboliza a quantidade de parcelas, seguido dos dias do mês de cada mês que as parcelas cairão (Somente um dia fixo no ano (independente da emissão))

**Exemplo 1:** Vencimento no dia 10/07

Criar uma condição de pagamento Tipo = 7 e Condição: 1,0,0,0,0,0,0,10,0,0,0,0,0 , onde o primeiro digito corresponde ao numero de parcelas e depois cada zero como corresponde a um mês do ano.

No sétimo zero foi inserido o dia do vencimento. Ao incluir uma nota na data de hoje, o vencimento ficará para 10/07.

![](https://tdn.totvs.com/download/attachments/240310845/71.png?version=1&modificationDate=1664166097940&api=v2)

**Cadastrando:**

E4\_CODIGO = (critério do usuário)

E4\_TIPO = 7

E4\_COND = 03,05,10,15,20,25,30,05,10,15,20,25,30

![](https://tdn.totvs.com/download/attachments/240310845/72.png?version=1&modificationDate=1664166115423&api=v2)

**Resultado:**

Supondo que a emissão da nota fiscal de saída da compra foi emitida dia 01/01. Os pagamentos serão efetuados da seguinte forma:

* 1ª parcela paga dia 5 de janeiro.
* 2ª parcela paga dia 10 de fevereiro.
* 3ª parcela paga dia 15 de março.

**OBS:** O sistema não retrocede o mês para cálculo do vencimento.

**Exemplo 2:**

Se a Emissão: 10/01/22

O primeiro vencimento (janeiro) seria no dia 5 de janeiro, como foi emitido a nota fiscal em uma data superior a da primeira parcela, ele não retrocede e sim avança para a próxima, que é dia 10 de fevereiro.

**GIF Exemplo do resultado da simulação utilizando uma condição de pagamento Tipo 7 (Tipo 7 - E4\_TIPO = “7”):**

![](https://tdn.totvs.com/download/attachments/240310845/tipo7.gif?version=1&modificationDate=1656449265037&api=v2)

**Saiba mais:**

[**Todas as Condições de Pagamento (MATA360)**](https://tdn.totvs.com/x/PdpSDg)
