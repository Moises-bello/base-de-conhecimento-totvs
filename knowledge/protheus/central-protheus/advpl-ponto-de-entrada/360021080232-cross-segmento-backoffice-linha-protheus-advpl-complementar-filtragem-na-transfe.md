---
article_id: 360021080232
category: ADVPL - Ponto de Entrada
content_hash: 6d4ac88d8c43ca7717bf2700891d3f1ef7899d413f99e82db330dc446b9c6f5a
fetched_at: '2026-06-28T22:40:11.522536+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Complementar filtragem
  na transferência de ativos por aquisição
type: support-article
updated_at: '2021-12-21T17:53:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021080232-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Complementar-filtragem-na-transfer%C3%AAncia-de-ativos-por-aquisi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Solicito melhoria de produto para termos um ponto de entrada para adicionar um filtro por campo personalizado no botão transferência, logo após o diálogo de bem.  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para atender essa necessidade, já existe disponível o ponto de entrada **AF251FILTR**. Através deste ponto de entrada é possível complementar a filtragem para itens que serão carregados no *browser* para marcação na opção **Transfere**.  
A seguir um exemplo utilizando um [Parambox](http://tdn.totvs.com/display/public/mp/Parambox) adicional, com opção para filtrar por centro de custo:

```
#Include 'Protheus.ch'  
  
User Function AF251FILTR()  
Local cFiltro := PARAMIXB[1]  
Local aRetPB := {}  
Local aParam := {}  
  
// Parambox PE AF251FILTR  
aAdd(aParam,{1,'Centro de Custo',space(TamSx3("N3_CUSTBEM")[1]),"@!", "","CTT","",50,.F.})  
  
If Parambox(aParam,'CC CONTA BEM',aRetPB,,,.T.,80,3,,"AF251PE",.T.,.T.)  
 cFiltro += ' .AND. N3_CUSTBEM == "' + aRetPB[1] + '"'  
EndIf  
  
Return cFiltro
```

**Saiba mais**  
[AF251FILTR() - Manipula filtro padrão da Transferência de Ativos por Aquisição](https://tdn.totvs.com/pages/releaseview.action?pageId=180584553)
