---
article_id: 7327950018839
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a2af891cb35ffaf9e036d6516943efb74b4a3f9eee2d6ba7355f83756aa88572
fetched_at: '2026-06-28T22:38:42.395127+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M410STTS
type: support-article
updated_at: '2022-07-25T12:28:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7327950018839-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M410STTS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M410STTS - Alterações no Pedido de Venda**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Este ponto de entrada pertence à rotina de pedidos de venda, MATA410().

Está em todas as rotinas de inclusão, alteração, exclusão, cópia e devolução de compras.

Executado após todas as alterações no arquivo de pedidos terem sido feitas.

Parâmetros:  
nOper --> Tipo: Numérico - Descrição: Operação que está sendo executada, sendo:

3 - Inclusão  
4 - Alteração  
5 - Exclusão  
6 - Cópia  
7 - Devolução de Compras  
  
**Exemplo**

```
User Function M410STTS()  
  
    Local _nOper := PARAMIXB[1]  
  
    If _nOper == 3 //Inclusao  
        Alert("Passou pelo Ponto de Entrada M410STTS - Inclusao")  
    ElseIf _nOper == 4 //Alteracao  
        Alert("Passou pelo Ponto de Entrada M410STTS - Alteracao")  
    ElseIf _nOper == 5 //Exclusao  
        Alert("Passou pelo Ponto de Entrada M410STTS - Exclusao")  
    ElseIf _nOper == 6 //Copia  
        Alert("Passou pelo Ponto de Entrada M410STTS - Copia")  
    ElseIf _nOper == 7 //Devolucao de Compras  
        Alert("Passou pelo Ponto de Entrada M410STTS - Devolucao de Compras")  
    EndIf  
  
Return Nil
```

**Saiba Mais**

**[M410STTS - Alterações no Pedido de Venda](https://tdn.totvs.com/x/m4Rn)**
