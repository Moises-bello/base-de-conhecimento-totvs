---
article_id: 360048690813
category: ADVPL - Rotina Automática
content_hash: 9f2a4a58b690784702dc8ff029529d6a8c85917b73ec23edf40f54e7cb72258c
fetched_at: '2026-06-28T22:40:24.085278+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Exemplo de ganho de produção
  por ExecAuto
type: support-article
updated_at: '2021-12-29T15:06:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048690813-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Exemplo-de-ganho-de-produ%C3%A7%C3%A3o-por-ExecAuto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Tem um exemplo de ganho de produção por ExecAuto()?  
  
**Ambiente**  
Protheus – ADVPL – A partir da versão P12  
  
**Solução**Parametrização de produção a maior e ganho de produção por **ExecAuto**() **MATA250**

Parametrização:  
**MV\_GANHOPR = .T.**  
**MV\_PERCPRM= 100**  
Como no **ExecAuto**() não abre tela para classificar a quantidade excedente, deve ser passado via **ExecAuto**() a classificação da quantidade excedente nos campos **D3\_QTGANHO** e **D3\_QTMAIOR**.  
Conforme exemplo a seguir: A **OP** tem a quantidade planejada de 5 e estou apontando quantidade 8.  
Neste exemplo excedi 3 e classifiquei 2 como ganho e 1 como produção a maior.  
Exemplo:

```
User Function MYMATA250()  
  
Local aVetor  
Local dData  
Local nOpc := 3 //-Opção de execução da rotina,  
  
prepare environment empresa "99" filial "01" modulo "est"  
  
lMsErroAuto := .F.  
aVetor := {}  
dData:=dDataBase  
  
aVetor := { {"D3_OP" ,"33707401001 " ,NIL},;  
{"D3_COD" ,"TT-PA " ,NIL},;  
{"D3_QUANT" ,8 ,NIL},;   
{"D3_PARCTOT" , "T" ,NIL},;  
{"D3_TM" ,"010" ,NIL},;  
{"D3_QTGANHO" ,2 ,NIL},;  
{"D3_QTMAIOR" , 1 ,NIL}}  
  
MSExecAuto({|x, y| mata250(x, y)},aVetor, nOpc )  
  
If lMsErroAuto  
CONOUT("Erro")  
mostraerro()  
Else  
CONOUT("Incluido com sucesso")  
Endif  
  
return nil
```

**Saiba Mais;  
[MATA250 - Produção](https://tdn.totvs.com/pages/releaseview.action?pageId=6087461)**
