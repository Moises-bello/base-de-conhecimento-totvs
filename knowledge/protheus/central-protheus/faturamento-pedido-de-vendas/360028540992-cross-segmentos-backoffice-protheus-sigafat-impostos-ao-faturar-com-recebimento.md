---
article_id: 360028540992
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f2a34856f9addc803133485065cf8800188595e1f22101129fb869f307b01639
fetched_at: '2026-06-28T22:38:39.870710+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Impostos ao faturar com recebimento
  adiantado (RA)
type: support-article
updated_at: '2026-05-13T21:18:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028540992-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Impostos-ao-faturar-com-recebimento-adiantado-RA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27918253222807) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Realizar a associação de um recebimento antecipado ao pedido de venda (**MATA410**) do faturamento, porém, o sistema não está considerando os valores de impostos na compensação?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT -  A partir da release 12.

**Solução**

Através da configuração do parâmetro "MV\_CMP330", pode definir se compensação automática, será  usada no faturamento da nota de saída **".T."**, ao realizar a preparação do documento de saída.

Caso tenha impostos e o valor do RA compõem o valor do Pedido e Impostos na compensação o sistema vai realizar abaixa do titulo no Financeiro.

Exemplo: (**MV\_CMP330 = .T.**)

- Pedido de Venda no valor de $ 1.000,00 que calcule um **IPI** ou **ICMS ST** de 10%.  
- Planilha Financeira irá demonstrar um valor total de $ 1.100,00  
- Incluiremos um RA no valor total do pedido de $ 1.100,00 para o cliente do pedido.  
- Ao relacionarmos o RA ao pedido, informaremos o valor de $ 1.000,00, pois a rotina não permite um valor maior que o do pedido, e com isso, ficará com um saldo de $ 100,00.  
- Salvamos o pedido.  
- Preparamos o Documento de Saída.  
- Ao consultar os títulos de RA e da NF no Financeiro, verifique que foi feita a compensação total dos títulos.

**Saiba mais:**

[**Recebimento Antecipado (Adiantamento) MATA410 Pedido de Vendas**](https://tdn.totvs.com/x/GkD2Dw)
