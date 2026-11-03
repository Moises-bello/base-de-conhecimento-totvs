---
article_id: 360057775514
category: Escrita Fiscal - Impostos - ICMS
content_hash: cb662ce602ffbca34961dcff588caef1a06dce11459604e0037d366233ea82b2
fetched_at: '2026-06-28T22:39:23.982450+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como Configurar
  para o cálculo de ICMS Conforme Decreto 35.679, de 13 de Outubro de 2010?'
type: support-article
updated_at: '2021-07-20T13:06:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057775514--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-Configurar-para-o-c%C3%A1lculo-de-ICMS-Conforme-Decreto-35-679-de-13-de-Outubro-de-2010
---

**Dúvida**Como Configurar para o calculo ICMS Conforme Decreto 35.679, de 13 de Outubro de 2010?

**Ambiente**Protheus - Fiscal -  A partir da versão 11.80  
  
**Solução**MV\_ESTADO = PE  
MV\_FISXMVA = .T.  
MV\_AGRPERC ={7.32,13.41,17.07} 

Precisa calcular o custo na nota fiscal de entradas fornecedor de SP

TES  
Gera duplicata = sim  
Atualiza estoque = sim  
Calcula icms = sim  
L fiscal icms = tributado  
F4\_CUSENTR = sim  
  
Nota fiscal de entradas  
Quantidade = 5  
Valor unitário = 120,00  
  
![](https://ci5.googleusercontent.com/proxy/0y0HLsxQWz4aHZ6XBYsXwZjlnP0rDP-QteWFnJsx_KXBgbMh903R8AsJTtxh9SmTrhWY_cxI1jLM12mPIp1qc3C40qVA6gSwoHkOE2GbSbeK-efOmE6ZEZ765bf04loUha3hPJzZ-XliCHMmbIdUxETvnp-hGM9cb4s=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/9ASVzlFm6O1Z9G9FedOgEGDNA/?name=inline1316059316.png)  
  
Valor do custo  
![](https://ci4.googleusercontent.com/proxy/j_jHgvtxztbf47qLyRlqybzAqd1mgN-zm6BiFjublfgkMsQKg19zTXd4O3wIla57Yqb164R7Q-tTeGU_iOFoJZ5ffQ0XgZI4m3QFgFNlgAfmkfy1HnC-bGGQiCTrIbeYA2Q-v_NXEIXlHqkjBNoK_t9q3yH-dkKds6FU=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/3u4R1OE0MYijFvYtcvB3lVnIU/?name=inline-1166618503.png)  
custo 576,00/5 = 115,20

vendas

Pedido de Vendas  
UF = PE  
  
Gera duplicata = sim  
Atualiza estoque = sim  
Calcula icms = sim  
L fiscal icms = tributado  
F4\_CUSENTR = sim

Valor da base de calculo do icms será composta pelo custo e não pelo valor da venda

![](https://ci6.googleusercontent.com/proxy/Vu03d3GA7gFnhD9Nf5gZlCJIJEOS-zFkABOByDJ1eEBN7GTR2nraYrjFt5GKdJJ3uVySzq-a7hcSh8eoljP16oPBC8tFtUSpiQ6Ld3U_v6H85p3xux2d83uU1VjWe95yTuX2NBZgyGoxDkmSJyqXDIMBhs8RcpNNrA=s0-d-e1-ft#https://totvssuporte.zendesk.com/attachments/token/UMGR6gWSuUm46SEmIyRNQuE16/?name=inline-17660279.png)

Fórmula para Cálculo da Base

***D1\_CUSTO + ( ( D1\_CUSTO  \* Percentual  ) / 100 )***

 Onde o Percentual refere-se a :

* 7,32 % Quando a origem da mercadoria referente à ultima aquisição for da região do Nordeste, Norte, Centro Oeste e Espirito Santo;
* 13,41 % Quando a origem da mercadoria referente à ultima aquisição for da região do Sul e Sudeste (Exceto Espirito Santo).
* 17,07% para mercadorias importadas considerando as origens ( 1,2,3 e 8 )

D1\_custo = 115,20

( 115,20\*12,05% ) = 13,88

Valor da base de calculo do icms = 115,20+13,88 = 129,08

**IMPORTANTE**

          Caso a *Base de Cálculo do ICMS*calculada pelo custo de aquisição (conforme mencionado acima), seja maior que o valor da operação no momento da revenda, será considerada para  cálculo do imposto o valor da operação.

No nosso exemplo valor da mercadoria = 200,00

Boletim

https://tdn.totvs.com/pages/releaseview.action?pageId=187826917
