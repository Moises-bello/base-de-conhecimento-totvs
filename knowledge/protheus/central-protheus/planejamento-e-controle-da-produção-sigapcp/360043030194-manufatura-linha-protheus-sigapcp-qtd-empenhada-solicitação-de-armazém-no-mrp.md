---
article_id: 360043030194
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 53cef944460580e8baadd515c39feb00c25fe83af8070f68146d61c315106c4c
fetched_at: '2026-06-28T22:42:45.772691+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Qtd. Empenhada Solicitação de Armazém
  no MRP
type: support-article
updated_at: '2025-09-15T12:02:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043030194-Manufatura-Linha-Protheus-SIGAPCP-Qtd-Empenhada-Solicita%C3%A7%C3%A3o-de-Armaz%C3%A9m-no-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34942816493079)***Tempo aproximado para leitura: **00:01:18 min**  
  
**Dúvida**  
Por que o **MRP - Manufacturing Resource Planning** não considera a **Qtd. Empenhada S.A.**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Para o **Protheus**, as pré-requisições pendentes de estoque, não são tratadas como demandas para o **MRP**, pois ele verifica basicamente: ordens de produção, solicitações de compra e pedido de venda.  
Outros tipos de movimentação dentro do suprimentos como requisição, reserva, empenho de solicitação de armazém por exemplo, o **MRP** não verifica.  
  
Referente ao saldo no **MRP** quando possui **Qtd. Empenhada S.A**:

* Se no **MRP** é selecionada a opção **Saldo Atual** o Sistema verificará o campo **B2\_QATU - Saldo Atual**;
* Se considerar por **Movimento** o Sistema verifica as tabelas **SD3 - Movimentações internas**, **SD2 - Itens de venda da NF**, **SD1 - Itens da NF de entrada**, **SB9 - Saldos iniciais**. Ou seja, não é verificado a informação do campo **B2\_QEMPSA - Quantidade Empenhada Prev,** já que o mesmo não atualiza a **SD3**.
