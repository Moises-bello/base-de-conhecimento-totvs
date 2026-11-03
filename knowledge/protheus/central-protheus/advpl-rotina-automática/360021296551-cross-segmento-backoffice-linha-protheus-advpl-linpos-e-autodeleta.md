---
article_id: 360021296551
category: ADVPL - Rotina Automática
content_hash: dd46b5ad755d8b0a8cf297af4a9109e8be2fb97559f65f16cc651371775cf01a
fetched_at: '2026-06-28T22:40:24.124939+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - LINPOS e AUTODELETA '
type: support-article
updated_at: '2023-07-13T20:31:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021296551-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-LINPOS-e-AUTODELETA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como realizar Alteração ou Exclusão na Execauto**.**

**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**

Para Alteração e exclusão de um item da rotina automática deve-se utilizar **LINPOS** e **AUTODELETA**

Quando existir a necessidade de alterar um item especifico da Getdados, existem dois campos que podem ser utilizados, os campos são: LINPOS e AUTDELETA. O primeiro deve ser utilizado para localizar o item do aCols que sofrerá alteração, o segundo instruí a rotina automática para deletar a linha. Caso não seja utilizado o LINPOS esta função irá reconstruir todo o aCols.

```
//aItem:={}  
  
aAdd(aItem,  
  
// Para incluir um único item não é necessário os itens LINPOS e AUTODELETA usa-se somente na Alteração ou exclusão  
  
aAdd(aItem,{"LINPOS","DA1_ITEM" ,'0001'})  
aAdd(aItem,{"AUTDELETA","N" ,Nil})  
  
  
// Para excluir um único item é os itens LINPOS e AUTODELETA sendo que o Autodeleta receberá o valor "N"  
  
aAdd(aItem,{"LINPOS","DA1_ITEM" ,'0002'})  
aAdd(aItem,{"AUTDELETA","S" ,Nil})
```

**Saiba Mais:**

[**MsGetDAuto**](http://tdn.totvs.com/display/public/PROT/MsGetDAuto)
