---
article_id: 40891506765463
category: Financeiro - Compensação Contas a Pagar
content_hash: 5b8707fdc0ec89575a5621b8b4e31aed7ed55c739200feea46730b1b11e16d55
fetched_at: '2026-06-28T22:37:33.659081+00:00'
product: protheus
section_id: 35057559197335
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 - É possível
  compensar títulos de filiais diferentes ?
type: support-article
updated_at: '2026-06-01T20:51:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40891506765463-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-%C3%89-poss%C3%ADvel-compensar-t%C3%ADtulos-de-filiais-diferentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40891506723351) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
O sistema permite realizar a compensação de títulos de filiais diferentes ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da 12.1.2210.  
  
**Solução**  
Para conseguir realizar a compensação de títulos entre filiais:

* Na tela de seleção dos registros, clique no botão filiais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40892178559255)

* Irá apresentar a tela abaixo, devendo clicar em SIM.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40892178564759)

* Após isso, deverá selecionar as filiais nas quais deseja realizar o filtro dos registros.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40892194760343)

* Após escolher as filiais, basta clicar em OK na próxima tela.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40892178568087)

Após clicar em **OK**, pressione **F12** para acessar os parâmetros da rotina. Em seguida, ajuste os seguintes parâmetros:

* considera Loja? "Não"
* Considera Fornecedor? "Não"
* Do Fornecedor? Deixar em branco
* Até o Fornecedor? Adicionar ZZZZZ
* Considera Filiais abaixo? "Sim"
* Da Filial? Deixar em branco
* Até Filial? Adicionar ZZZZZ

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40892178569367)
