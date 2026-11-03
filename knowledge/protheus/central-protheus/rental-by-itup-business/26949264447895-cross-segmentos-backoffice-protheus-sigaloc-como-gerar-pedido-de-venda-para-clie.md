---
article_id: 26949264447895
category: Rental by ItUp Business
content_hash: 95f2a27bcc2fe80d5e08ef55cf9fa54e7cde0bdcd076e6989333d63f5bfe73dc
fetched_at: '2026-06-28T22:36:20.561725+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como gerar pedido de venda
  para clientes diferentes que estão no Orçamento LOCA001
type: support-article
updated_at: '2026-04-09T12:59:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26949264447895-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-gerar-pedido-de-venda-para-clientes-diferentes-que-est%C3%A3o-no-Or%C3%A7amento-LOCA001
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26949287735447) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Dúvida**  
Como gerar um pedido de venda no faturamento automático para um cliente diferente daquele inserido no campo "Cliente (FP0\_CLI)" no Orçamento LOCA001?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Solução**  
Para realizar o faturamento automático de um pedido para um cliente diferente, siga os passos abaixo:

1. Verifique o campo ***"Cliente FAT (FPA\_CLIFAT)"*** na aba "**LOCAÇÃO**",

* Se o campo ***"Cli. FAT (FPA\_CLIFAT)"*** estiver preenchido, o sistema utilizará esse cliente para gerar o pedido de venda.

2. Verifique o campo ***"Cliente Fat. (FP1\_CLIDES)"*** na aba "**LOCALIDADES**"

* Caso o campo **"FPA\_CLIFAT"** esteja vazio, o sistema buscará o cliente no campo ***"Cliente Fat. (FP1\_CLIDES)"***, localizado na aba **"LOCALIDADES"**para gerar o pedido de venda.

3. Verifique o campo ***"Cliente (FP0\_CLI)"*** na aba **"DADOS DO PROJETO"**

* Se nenhum dos campos anteriores estiver preenchido, o sistema utilizará o cliente inserido no campo ***"Cliente (FP0\_CLI)"*** na aba "**DADOS DO PROJETO**" para gerar o pedido de venda.

**Saiba Mais:** [***Faturamento com múltiplos clientes***](https://tdn.totvs.com/display/public/PROT/Faturamento+com+multiplos+clientes)
