---
article_id: 29985051241111
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 831e1efe5e9db0b9ab8e94300ec9b33aafcc90c2b85e5fe4a78c514a22da70ba
fetched_at: '2026-06-28T22:38:40.011559+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Qual tipo (C5_TIPO) usar
  em devoluções pelo pedido de venda
type: support-article
updated_at: '2025-02-17T11:18:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29985051241111-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Qual-tipo-C5-TIPO-usar-em-devolu%C3%A7%C3%B5es-pelo-pedido-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29985051236247) Tempo aproximado para leitura: **00:10:30 min** **Dúvida**Se eu quiser devolver pelo pedido de venda, qual tipo de pedido de venda (C5\_TIPO) usar?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Cenário 1:  
Caso sua nota fiscal de entrada tenha sido do tipo (F1\_TIPO) "Normal" com uma TES sem poder de/em terceiros ("Poder terc. (F4\_PODER3)" = 'N - Não controla'), o seu pedido de venda deve ser do tipo (C5\_TIPO) "D - Devolução" e não pode controlar poder de/em terceiros a TES.

**OBS 1:** Para localizar a NF origem para retorno nesse cenário, aperte F4 no campo "NF Origem (C6\_NFORI)"

Cenário 2:

Caso sua nota fiscal de entrada tenha sido do tipo (F1\_TIPO) "Normal" com uma TES com poder de/em terceiros ("Poder terc. (F4\_PODER3)" diferente de 'N - Não controla'), o seu pedido de venda deve ser do tipo (C5\_TIPO) "B - Utiliza fornecedor" e tem de controlar poder de/em terceiros a TES ("Poder terc. (F4\_PODER3)" diferente de 'N - Não controla').

**OBS 2:** Para localizar a NF origem para retorno nesse cenário, aperte F4 no campo "Quantidade (C6\_QTDVEN)"

Cenário 3:

Caso sua nota fiscal de entrada tenha sido do tipo (F1\_TIPO) "Beneficiamento" obrigatoriamente a TES deve ser de poder de/em terceiros  e o seu pedido de venda deve ser do tipo (C5\_TIPO) "N - Normal" e assim como a entrada a TES deve controlar poder de/em terceiros.

**OBS 3:** Para localizar a NF origem para retorno nesse cenário, aperte F4 no campo "Quantidade (C6\_QTDVEN)"

**Saiba mais:**

[FAT0285 - Poder DE/EM Terceiro](https://tdn.totvs.com/x/xyCgGg)
