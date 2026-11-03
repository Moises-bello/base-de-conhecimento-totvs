---
article_id: 16137270982935
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f60728dc630f9c6091c46a07a454183275eb95b6fe6fb0adf19c506cb0875bd2
fetched_at: '2026-06-28T22:38:42.775668+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  A410VTIP
type: support-article
updated_at: '2023-07-19T14:05:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16137270982935-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-A410VTIP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16137284067863) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **A410VTIP - Validação em Pedido de Vendas - Condição de Pagamento tipo 9**.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

O ponto de entrada **A410VTIP** será acionado no momento da **gravação do pedido** de vendas que possuam **condição de pagamento tipo 9**. Utilizado para que o usuário possa realizar **validações** em pedidos de venda que possuam condição de pagamento do tipo 9. Possui **retorno lógico**, onde **.T.** realiza a gravação do pedido de vendas e **.F.** não permite a gravação.  
  
**Exemplo**

```
#INCLUDE 'PROTHEUS.CH'  
  
User Function A410VTIP()  
  
    Local lRet := .F.  
  
    If MsgYesNo("Confirma a gravacao do pedido?", "PE A410VTIP")  
        lRet := .T.  
        Alert("Passou pelo Ponto de Entrada A410VTIP, o pedido sera gravado") //Clicou no Sim  
    Else  
        lRet := .F.  
        Alert("Passou pelo Ponto de Entrada A410VTIP, o pedido nao sera gravado") //Clicou no Não  
    EndIf  
  
Return(lRet)
```

**Saiba Mais**

**[A410VTIP - Validação em Pedido de Vendas - condição de pagamento tipo 9](https://tdn.totvs.com/x/HIZn)**
