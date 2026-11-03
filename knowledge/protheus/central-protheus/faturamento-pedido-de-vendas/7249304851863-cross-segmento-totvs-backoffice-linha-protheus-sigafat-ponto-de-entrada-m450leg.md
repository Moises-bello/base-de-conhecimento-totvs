---
article_id: 7249304851863
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 89c9f9b9b4bd55dc627218c0722f9197acde9144768714e123e43ba623cdf8b1
fetched_at: '2026-06-28T22:38:42.401607+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M450LEG
type: support-article
updated_at: '2022-07-25T12:27:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7249304851863-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M450LEG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M450LEG - Alteração de cores.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Este ponto de entrada pertence à rotina de **Liberação de Crédito (MATA450)**. Usado para **alterar cores** do “browse” do cadastro, que representam o “status” do pedido.  
  
**Exemplo**

```
#INCLUDE 'protheus.ch'  
  
User Function M450LEG()  
  
    Local aCores := {}  
  
    //Formato do item do array de cores {"condição", 'cor'}.   
    aCores := { {"C9_BLCRED == '  '"                     ,'ENABLE' },;  //Item Liberado (verde)  
                {"C9_BLCRED == '10' .And. C9_BLEST=='10'",'DISABLE'},;  //Item Faturado (vermelho)  
                {"C9_BLCRED == '01'"                     ,'BR_PINK'} }  //Item Bloqueado - Credito (rosa)  
  
Return(aCores)
```

**Saiba Mais:**

**[M450LEG - Alteração de cores](https://tdn.totvs.com/x/qoRn)**
