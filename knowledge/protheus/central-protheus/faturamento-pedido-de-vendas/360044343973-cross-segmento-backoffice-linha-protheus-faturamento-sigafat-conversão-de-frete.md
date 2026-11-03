---
article_id: 360044343973
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3c62046ebbc1787fbed78128461e507515523edaf667a75e79ce81a0f4541095
fetched_at: '2026-06-28T22:38:38.360546+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Conversão
  de frete e despesas acessórias no faturamento
type: support-article
updated_at: '2023-11-29T13:30:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044343973-Cross-Segmento-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Convers%C3%A3o-de-frete-e-despesas-acess%C3%B3rias-no-faturamento
---

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7435849218839) Tempo aproximado para leitura: 00:00:30 min**

**Dúvida**

Como proceder para que o frete, seguro e despesas acessórias sejam convertidos quando o pedido de venda (**MATA410**) está com a moeda igual a 2?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento – Todas as versões

**Solução**

Ao entrar na rotina cheque e averigue a configuração dos perguntes da rotina:

Para definição a cerca de valor de **FRETE**/**SEGURO**/**DESPESAS**/**INDENIZAÇÃO** verifique o parâmetro **MV\_FRETMOE**.

**MV\_FRETMOE** = Respeita a moeda do Pedido de Venda para Frete/Seguro/Despesas?

**Exemplos:**

**MV\_FRETMOE** = **S** (Converte o Frete em Reais (R$) de acordo com a taxa da moeda cadastrada)

Taxa da Moeda cadastrada (MATA090): 5,0000

Valor do Frete informado no Pedido de Venda: 10,00 [C5\_FRETE]

Valor do Frete gravado na nota fiscal gerada: 50,00 [F2\_FRETE]

**MV\_FRETMOE** = **N** (Grava o Frete na Moeda informada no Pedido de Vendas)

Taxa da Moeda cadastrada (MATA090): 5,0000

Valor do Frete informado no Pedido de Venda: 10,00 [C5\_FRETE]

Valor do Frete gravado na nota fiscal gerada: 10,00 [F2\_FRETE]

**Saiba mais:**

**[FAT0082 Despesas acessórias no faturamento (Frete,Seguro,Despesas)](https://tdn.totvs.com/pages/viewpage.action?pageId=239024024)  
[FAT0096\_Uso\_Moeda\_Modulo\_Faturamento](https://tdn.totvs.com/display/public/PROT/FAT0096_Uso_Moeda_Modulo_Faturamento)**

**[FAT0028\_Msg:\_Alguns\_pedidos\_não\_foram\_gerados,\_pois\_não\_existe\_taxa\_para\_a\_moeda](https://tdn.totvs.com/pages/viewpage.action?pageId=225950405)**

**[FAT0096\_Uso\_Moeda\_Modulo\_Faturamento](https://tdn.totvs.com/display/PROT/FAT0096_Uso_Moeda_Modulo_Faturamento)**
