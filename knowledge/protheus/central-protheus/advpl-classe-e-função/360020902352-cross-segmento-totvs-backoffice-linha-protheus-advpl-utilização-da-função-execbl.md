---
article_id: 360020902352
category: ADVPL - Classe e Função
content_hash: cc744a905f4c9f012ebe2f16d736b3ec7b96e705707c73b9695bcdaf615caa49
fetched_at: '2026-06-28T22:40:18.164264+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Utilização da função
  Execblock '
type: support-article
updated_at: '2022-06-14T17:49:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020902352-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utiliza%C3%A7%C3%A3o-da-fun%C3%A7%C3%A3o-Execblock
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Como utilizar a função **Execblock****()**?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**O **Execblock** é uma função que permite a execução de um ponto de entrada ou de uma função de usuário. Ambas são componentes importantes em um processo de customização dentro do Protheus.

Por meio do ponto de entrada, é possível interferir no funcionamento de um processo padrão do Protheus, dentro de certos limites e regras.

Por meio da função de usuário, é possível criar rotinas que serão executadas por outras ou diretamente no menu pelo usuário. Com essas rotinas, criam-se novas funcionalidades ou alteram-se determinados procedimentos do Protheus, dentro dos limites estabelecidos.  
  
**Exemplo**

```
#include "protheus.ch"  
  
User Function Teste20()  
  
Local cNota := "XXX"  
Local cSerie := "01"  
Local cFornece := "000001"  
Local cLoja := "02"  
Local aParam := {cNota, cSerie, cFornece, cLoja}  
  
IF EXISTBLOCK("TESTE21")  
 lGravou := EXECBLOCK("TESTE21",.F.,.F.,aParam)  
ENDIF  
  
RETURN  
  
USER FUNCTION Teste21()  
  
LOCAL cNota := PARAMIXB[1]  
LOCAL cSerie := PARAMIXB[2]  
LOCAL cFornece := PARAMIXB[3]  
LOCAL cLoja := PARAMIXB[4]  
  
ApMsgAlert('Nota: ' +cNota)  
ApMsgAlert('Serie: ' +cSerie)  
ApMsgAlert('Fornece: ' +cFornece)  
ApMsgAlert('Loja: ' +cLoja)  
  
RETURN .T.
```

****Saiba mais****

[**ExecBlock - Execução do ponto de entrada**](http://tdn.totvs.com/pages/releaseview.action?pageId=6814883)  

[**Como utilizá-lo**](http://tdn.totvs.com/pages/viewpage.action?pageId=43550098)  

[**ExistBlock - Verifica ponto de entrada existente**](http://tdn.totvs.com/display/public/PROT/ExistBlock+-+Verifica+ponto+de+entrada+existente)
