---
article_id: 360023084311
category: ADVPL - Rotina Automática
content_hash: 884243dbdc063f7a46541628db3179e200f838f0ce9546bf8f24a35ad2cb2552
fetched_at: '2026-06-28T22:40:24.081072+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - Exemplo de execauto para
  alteração FINA050 '
type: support-article
updated_at: '2021-12-29T15:05:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023084311-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Exemplo-de-execauto-para-altera%C3%A7%C3%A3o-FINA050
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como utilizo a ExecAuto da **FINA050** para realizar uma alteração.  
  
**Ambiente**Protheus – ADVPL – A partir da versão 11.8  
 **Solução**Para alterar um registro via **execauto**, você precisa ter o registro posicionado, caso o registro não esteja posicionado, a **execauto** ira alterar o primeiro registro encontrado na tabela.

Basicamente a alteração via **execauto** é a mesma realizada na rotina padrão, por isso você precisa verificar a regra da rotina, para validar se tal alteração é permitida.

**Exemplo**

```
#Include "protheus.ch"  
#Include "parmtype.ch"  
#Include "tbiconn.ch"  
  
User Function FIN050ALT()  
  
LOCAL aArray := {}  
PRIVATE lMsErroAuto := .F.  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"  
  
DbSelectArea("SE2")  
DbSetOrder(1)  
DbSeek(xFilial("SE2")+"ABC"+"00000027") //Alteração deve ter o registro SE2 posicionado  
  
aArray := {{"E2_PREFIXO" ,SE2->E2_PREFIXO , NIL },;// CAMPO POSICIONADO  
           {"E2_NUM"     ,SE2->E2_NUM     , NIL },;  
           {"E2_VALOR"   ,300             , NIL }} // campo que vai ser alterado  
  
MsExecAuto( { |x,y,z| FINA050(x,y,z)},aArray,, 4) // 3 - Inclusao, 4 - Alteração, 5 - Exclusão  
  
If lMsErroAuto  
   MostraErro()  
Else  
   Alert("Título alterado com sucesso!")  
Endif  
  
RESET ENVIRONMENT  
  
Return
```
