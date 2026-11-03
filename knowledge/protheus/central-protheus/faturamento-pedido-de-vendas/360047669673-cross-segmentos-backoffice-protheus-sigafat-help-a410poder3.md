---
article_id: 360047669673
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: e5cc3125fde73c5dfa5c9e1ffa73ae278d882039f3598b391333a042b071649b
fetched_at: '2026-06-28T22:38:39.815593+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help A410PODER3
type: support-article
updated_at: '2025-01-27T16:57:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047669673-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A410PODER3
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29526018337303) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**

Quando efetuo um pedido de remessa de poder terceiros, ocorre o **Help** **A410PODER3**, o que fazer?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

Primeiramente, para que o sistema consiga gerar os controles de poder de/em terceiros, precisamos de TES devidamente configurados para tal.

Sendo assim, toda Remessa Geradora de Controle de/em Terceiros, independentemente de entrada ou saída, deve conter "R" (remessa) no campo **SF4->F4\_PODER3.**

E toda Devolução de Remessa Geradora de Poder de/em Terceiros, independentemente de entrada ou saída, deve conter "D" (devolução) no campo **SF4->F4\_PODER3.**

Quando o Help **A410PODER3** é apresentado, significa que a nota de saída não corresponde ao utilizado no controle de poder de terceiro Remessa. Nesse caso, para que não ocorra o processo deve atender às seguintes premissas:

1 - "Tipo da Nota de entrada" **(F1\_TIPO)** diferente de "Normal";  
2 - Verificar se campo "Tes de Devolução" **(F4\_TESDV)** esta preenchido;  
3 - Se o campo "Poder Terc." **(****F4\_PODER3)** for "**R - Remessa" ou "D - Devolução"** e **C5\_TIPO** diferente de **"D"** - Devolução, gera o Help.

**Saiba Mais:**

**[Nota de Devolução de Poder de Terceiro / Nota de Retorno](https://tdn.totvs.com/x/nKkXDg)**

**[Poder de Terceiros - Correta configuração do cadastro de TES](https://tdn.totvs.com/x/eSswDg)**
