---
article_id: 360053714313
category: Financeiro - Contas a Receber
content_hash: 6a76c0bdb5bfee619e6181d6431390d8a1c52373f1a664a8af7466e6b120cd16
fetched_at: '2026-06-28T22:38:12.759348+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA040 - É possível
  alterar o campo E1_CCUSTO
type: support-article
updated_at: '2022-06-21T14:35:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053714313-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA040-%C3%89-poss%C3%ADvel-alterar-o-campo-E1-CCUSTO
---

**Dúvida**É possível alterar o campo E1\_CCUSTO?  
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**No módulo **Financeiro** é possível realizar somente no momento da inclusão de um título**.**  
  
Este campo por padrão não permite que seja alterado após a inclusão do título e para manter a integridade das informações (financeiro vs contábil), pois esse campo tem o conceito contábil.   
  
Segue abaixo pontos de entrada que permitem liberar alteração do campo.   
  
**F040CPO** - Manipular campos  
<http://tdn.totvs.com.br/pages/releaseview.action?pageId=6070865>  
  
Exemplo para desbloquear campo:  
  
USER FUNCTION F040CPO()  
local aTeste := paramixb  
AADD(aTeste,"E1\_CAMPO")  
RETURN aTeste  
  
Exemplo para bloquear campo:  
#Include 'Protheus.ch'  
User Function F040CPO()  
LOCAL  aBlock := {}  
LOCAL  NSCAN :=0  
aIto := paramixb    
NSCAN := Ascan(aBlock,"E1\_CAMPO")  
IF NSCAN > 0  
ADEL(aIto,NSCAN)  
ASIZE(aBlock,Len(aBlock)-1)  
ENDIF  
Return aBlock  
  
E para não validar a alteração de dados no **Contas a Receber**, utilize o **PE FA040ALT**, apenas se for necessário.

Para mais informações sobre esse PE,   
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071094>
