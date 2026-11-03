---
article_id: 360044422233
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 17556d76633df517258ad204f02c6faf2621aff186e1438716f3282ae67b3cec
fetched_at: '2026-06-28T22:42:42.025082+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como o MRP calcula o saldo inicial
type: support-article
updated_at: '2021-05-13T10:55:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044422233-Manufatura-Linha-Protheus-SIGAPCP-Como-o-MRP-calcula-o-saldo-inicial
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:45 min**  
**Dúvida**Como o **MRP - Material Requiriments Planning**calcula o saldo inicial?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Dos armazéns informados no range o Sistema pode:

* Fazer a leitura do campo **B2\_QATU - Saldo Atual** se o **MRP** estiver parametrizado para **Saldo Atual menos o estoque de segurança**.  
  Ou
* Fazer a leitura das tabelas de movimento se o **MRP** estiver parametrizado para **Saldo por movimento**. Neste caso o Sistema faz a leitura da tabela **SB9 - Saldos Iniciais**, do campo **B9\_QINI - Qtd.Inic.Mes** anterior ao primeiro período. Da tabela **SD1 - Itens das NF de Entrada,**soma **D1\_QUANT - Quantidade,** anterior ao primeiro período, quando **D1\_ORIGLAN - Origem do Lançamento**for diferente de **LF - Despesas NF Livro Fiscal** e **TES - Tipo de Entrada e****Saída** movimentar estoque.

Da tabela **SD2 - Itens de Venda da NF,**subtrai **D2\_QUANT - Quantidade,** anterior ao primeiro período, quando **D2\_ORIGLAN - Origem do Lançamento** for diferente de **LF** e **TES** movimentar estoque.  
Da tabela **SD3 - Movimentações Internas,**subtrai **D3\_QUANT - Quantidade,** anterior ao primeiro período, quando **D3\_TM** **- Tipo de movimento** maior que 500.  
Da tabela **SD3,**soma **D3\_QUANT - Quantidade,** anterior ao primeiro período, quando **D3\_TM** menor que 500.  
Se o parâmetro **MV\_LOTVENC - Indica se devem ser utilizados Lotes/Sub-Lotes com a data de validade vencida**, vai subtrair os lotes vencidos.  
Se o parâmetro **Saldo Rejeitado pelo CQ** estiver como **Subtrai Rejeitado**, fará a leitura da tabela **SD7 - Movimentações de CQ**, descontando do saldo em estoque o que estiver com **D7\_TIPO - Tipo** igual a **6** e no caso de **D7\_TIPO** igual a **2** irá subtrair somente a quantidade que ainda não foi devolvida.  
  
**Importante**  
Considerando o **Poder em/de terceiro** como**Ignora**.
