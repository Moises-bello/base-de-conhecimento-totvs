---
article_id: 360021325912
category: ADVPL - Classe e Função
content_hash: c2b0b7f96171a151a39d5176dea9b95c7fd9c8a54bf2f67f5c2d914a5ab14598
fetched_at: '2026-06-28T22:40:18.228331+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Variável de Memoria
  não disponível ao Utilizar a RunTrigger na rotina Pedido de Venda.
type: support-article
updated_at: '2022-01-06T19:21:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021325912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Vari%C3%A1vel-de-Memoria-n%C3%A3o-dispon%C3%ADvel-ao-Utilizar-a-RunTrigger-na-rotina-Pedido-de-Venda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao utilizar a função RunTrigger no Pedido de Venda, não está disponível o valor de memória porém está preenchido o campo, como pegar esta informação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**Para pegar o valor neste caso é necessário buscar o valor no Acols.

**Exemplo**

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
  
//função do gatilho do campo C6_TES  
user function C6TES()  
   
LOCAL nTESatu := M->C6_TES  
Local nTes := aScan(aHeader,{|x| Trim(x[2])=="C6_TES"} )  
  
  
IF nTESatu == nil  
 nTESatu := aCols[n][nTes]  
ENDIF  
  
if (nTESatu == '520')  
  
nTESatu := '501'  
   
else  
  
nTESatu := '520'  
   
endif  
  
return nTESatu  
  
//Função de gatilho chamando a Runtrigger.  
user function C6PROD()  
   
LOCAL nProduto := M->C6_PRODUTO  
  
If ExistTrigger('C6_TES')   
 RunTrigger(2,n,nil,,'C6_TES')  
Endif  
  
return nProduto
```

**Saiba Mais**

[Runtrigger](http://tdn.totvs.com/pages/releaseview.action?pageId=6815032)

[Gatilhos](http://tdn.totvs.com/display/framework/SX7+-+Gatilhos+de+Campos)
