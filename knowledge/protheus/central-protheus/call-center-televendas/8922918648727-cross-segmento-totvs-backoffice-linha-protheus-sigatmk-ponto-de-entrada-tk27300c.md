---
article_id: 8922918648727
category: Call Center - Televendas
content_hash: 4fc9361128f57411d70be435bd4e885494fd78480959502e1db4b2d8aa5d1c00
fetched_at: '2026-06-28T22:41:30.360447+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Ponto de Entrada
  TK27300C
type: support-article
updated_at: '2022-09-16T15:20:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8922918648727-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ponto-de-Entrada-TK27300C
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **TK27300C - Validação do Preço Unitário dos itens do Televendas.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - A partir da release 12.  
  
**Solução**

O ponto de entrada TK27300C é executado no momento da **digitação do preço unitário** (UB\_VRUNIT) do item no atendimento do Televendas, e é utilizado para v**alidar o preço unitário** antes da atualização dos valores do **rodapé do atendimento**.

  
****Exemplo****

```
#Include 'Protheus.ch'  
#Include 'Totvs.ch'  
  
User Function TK27300C()  
  
Local lRet := .T.  
Local nLinha := N //Linha da linha da grid de produtos  
Local nPosProd := Ascan(aHeader, {|x|AllTrim(x[2]) == "UB_PRODUTO"}) //Posição do campo de produto na grid  
Local nPosQtd := Ascan(aHeader, {|x|AllTrim(x[2]) == "UB_QUANT"}) //Posição do campo de quantidade na grid  
Local nVrUnit := M->UB_VRUNIT //Valor do preço unitário que foi digitado pelo operador  
  
//Não permite que o operador digite um valor menor que R$10,00, se a quantidade do produto "000001" for maior que 1.  
If AllTrim(aCols[nLinha][nPosProd]) == "000001" .And. aCols[nLinha][nPosQtd] > 1 .And. nVrUnit < 10  
    lRet := .F.  
EndIf  
  
Return lRet
```

 **Saiba Mais**

**[DT PE TK27300C Validação do Preço Unitário dos itens do Televendas](https://tdn.totvs.com/x/yrdAKg)**
