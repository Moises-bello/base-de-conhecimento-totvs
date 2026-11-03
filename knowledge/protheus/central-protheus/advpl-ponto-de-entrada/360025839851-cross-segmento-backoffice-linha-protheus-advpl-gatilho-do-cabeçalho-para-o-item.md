---
article_id: 360025839851
category: ADVPL - Ponto de Entrada
content_hash: f223c60b53d92e9af1dcd53a742c5b4b61b2cc005db0f22aa9ff7b99724f3fbe
fetched_at: '2026-06-28T22:40:11.556219+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Gatilho do cabeçalho para
  o item na rotina MATA415
type: support-article
updated_at: '2021-12-21T21:01:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025839851-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Gatilho-do-cabe%C3%A7alho-para-o-item-na-rotina-MATA415
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:04:00 min  
  
Dúvida**Preciso fazer um gatilho disparado do cabeçalho para o item do *acols*, na rotina MATA415 mas o sistema não está atualizando, como resolver?  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para atender essa necessidade, que seria disparar um gatilho da tabela **SCJ** para a **SCK**, é necessário criar uma função de usuário para que possibilite atualizar corretamente todos os itens.  
No caso da rotina em questão, a variável *aCols* não está disponível para ser utilizada em customização, desta forma será necessário atualizar diretamente o alias temporário responsável por controlar o grid de itens, que seria o **TMP1**.  
A seguir um exemplo em que quando é alterado o campo do cabeçalho Cliente(**CJ\_CLIENTE**), uma informação é inserida no campo descrição do item(**CK\_DESCRI**):

```
#Include 'Protheus.ch'  
  
User Function gatCJ()  
Local cRet := M->CJ_CLIENTE  
  
If CJ_CLIENTE == '000001'  
 TMP1->(dbGotop())  
 While TMP1->( !Eof() )  
 TMP1->CK_DESCRI := 'CLIENTE 1'  
 TMP1->(dbSkip())  
 EndDo  
Else  
 TMP1->(dbGotop())  
 While TMP1->( !Eof() )  
 TMP1->CK_DESCRI := ''  
 TMP1->(dbSkip())  
 EndDo  
EndIf  
  
TMP1->(dbGotop())  
  
oGetDad:oBrowse:Refresh()  
  
Return cRet
```

A função pode ser inserida no gatilho da seguinte forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024714131/mceclip1.png)

O campo contra domínio é indiferente para essa necessidade, neste caso defini o próprio campo e consequentemente utilizo a variável de memória deste campo como retorno.

**Atenção**Quando o campo a ser atualizado realiza a atualização de outros campos no processo, como é o caso da TES(**CK\_TES**) por exemplo, é preciso tratar o restante dos campo que ele irá atualizar ou podem ocorrer erros ou não conformidade do dado.  
  
**Saiba mais**  
[RUNTRIGGER - Execução de gatilhos](http://tdn.totvs.com/pages/releaseview.action?pageId=6815032)
