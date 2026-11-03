---
article_id: 27328347339287
category: Comércio Exterior - Easy Export Control - Siscomex
content_hash: 34fecd7c46ed6d22ef1ed0ff3d0294395edeaca4045db35a47f5327dc0c01bf3
fetched_at: '2026-06-28T22:37:00.587211+00:00'
product: protheus
section_id: 1500001538121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - É possível customizar
  a rotina de manutenção de Produtos (EECAC120)?
type: support-article
updated_at: '2024-10-30T14:07:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27328347339287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-%C3%89-poss%C3%ADvel-customizar-a-rotina-de-manuten%C3%A7%C3%A3o-de-Produtos-EECAC120
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27328347324567) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

É possível customizar a rotina de manutenção de Produtos (EECAC120)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Para essa necessidade existe o ponto de entrada EECAC120, no qual ele deve ser utilizado para customizar a rotina de manutenção de Produtos no módulo Easy Export Control e Easy Drawback Control.

Permitindo a adição de campos da tabela SB1 e a validação se permite a inclusão/alteração.

**Exemplo**

```
User Function EECAC120()  
Local cParam:= ""  
  
Local nOperacao:= 0  
  
  
If ValType(PARAMIXB) == "C"  
cParam := PARAMIXB  
ElseIf ValType(PARAMIXB) == "A"  
cParam := PARAMIXB[1]  
EndIf  
  
If cParam == "ENCHOICE"  
AAdd(aDrwBck, "B1_GRUPO") //Inclusão de campos adicionais para a manutenção no módulo de Drawback  
AAdd(aDrwBck, "B1_CONTA")  
EndIf  
  
iF cParam == "VALID_GRAVACAO"  
  
nOperacao := ParamIxb[2] //4 atera 3 inclui  
  
IF M->B1_PRV1 > 1000 .AND. nOperacao == 4  
lRetPE:=.F.  
  
ENDIF  
  
Endif  
  
Return .T.
```

**Saiba mais:**

[EECAC120](https://tdn.totvs.com/pages/releaseview.action?pageId=286210903)
