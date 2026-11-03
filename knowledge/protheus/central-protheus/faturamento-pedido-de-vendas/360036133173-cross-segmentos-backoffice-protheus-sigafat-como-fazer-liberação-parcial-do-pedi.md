---
article_id: 360036133173
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a9c9ab12fafa85ce5fa49bd76b7922123a58ce97bf8e368f5410dc8a2267f3c4
fetched_at: '2026-06-28T22:38:39.706290+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como fazer liberação parcial
  do pedido de venda para faturamento
type: support-article
updated_at: '2026-03-10T11:58:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036133173-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-fazer-libera%C3%A7%C3%A3o-parcial-do-pedido-de-venda-para-faturamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38929466402455)** **Tempo aproximado para leitura:****00:02:00 min**

**Dúvida**

Como fazer liberação parcial do pedido de venda para faturamento?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O processo pode ser feito de duas maneiras:

**1º** Na própria rotina **MATA410 (Pedido de Venda)**é só preencher o campo **C6\_QTDLIB (Qtd. Liberada)** informado a quantidade que deseja faturar de pois só acessar a rotina **MATA460A (Documento de Saída)** caso não haja bloqueio e finalizar gerando a Nota Fiscal.

**2º** Acessando a rotina **MATA440 (Liberação de Pedido de Venda)** clina no botão LIBERAR, altere o campo **C6\_QTDLIB (Qtd. Liberada)** e salva, de pois só acessar a rotina **MATA460A (Documento de Saida)** caso não haja bloqueio e finalizar gerando a Nota Fiscal.

**Observação:** Nos processo de liberação parcial do pedido de venda o sistema ainda vai manter esse pedido na rotina MATA410 (Pedido de Venda) com o status em aberto.

Para mais informações acessar as documentações abaixo:

* [Liberação dos itens do Pedido de Vendas conforme o Saldo Disponível em Estoque](https://tdn.totvs.com/x/gE5tDQ)
* [Cross Segmentos - BackOffice Protheus - SIGAFAT - Restrição de Liberação Manual de Pedidos para evitar Estoque Negativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000659308-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Impedir-estoque-negativo-pelo-Faturamento-Libera%C3%A7%C3%A3o-manual-de-Pedidos)
* Assista nosso vídeo [How To | MP - SIGAFAT - Pedidos de venda aptos a faturar](https://www.youtube.com/watch?v=5E08tiWORdA)
