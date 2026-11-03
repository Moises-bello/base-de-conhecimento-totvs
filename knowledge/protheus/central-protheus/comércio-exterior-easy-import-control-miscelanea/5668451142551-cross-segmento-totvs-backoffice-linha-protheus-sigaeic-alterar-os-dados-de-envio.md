---
article_id: 5668451142551
category: Comércio Exterior - Easy Import Control - Miscelanea
content_hash: 66a471ae3296415198047415af2ebaa972bce674c511bfcba42c677258d21575
fetched_at: '2026-06-28T22:39:42.053308+00:00'
product: protheus
section_id: 1500001549702
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Alterar os dados
  de envio de e-mail na integração com despachante
type: support-article
updated_at: '2022-04-25T15:02:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5668451142551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Alterar-os-dados-de-envio-de-e-mail-na-integra%C3%A7%C3%A3o-com-despachante
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Temos algum ponto de entrada  que seja possível alterar alguns parâmetros do envio de e-mail na integração com despachante (**EICEI100**)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Hoje temos o ponto de entrada **ENVIAREMAIL** que possibilita customizar as variáveis para o envio de e-mail.

```
User Function EICEI100()  
  
Local cParam:= ""  
IF Type("ParamIXB") == "C"  
cParam:= PARAMIXB  
Else  
cParam:= PARAMIXB[1]  
Endif  
  
IF cParam == "ADICIONA_ACOES"  
msginfo("Entrou no ponto de entrada 'ADICIONA_ACOES'")  
//aActions := {}  
  
ElseIf cParam == "ENVIAREMAIL"  
cSmtpServer := 'servidor'  
cAccount := 'email@email.com'  
cPassword := 'senha'  
lAutentica := .T.  
nTryConnection:= ''  
nTimeout := 120  
cUserAuth := 'email@email.com'  
cPswAuth := 'senha'  
cSmtpPort := 123  
MsgInfo("Entrei no Ponto de Entrada ENVIAREMAIL","Ponto de Entrada")  
Endif  
  
Return Nil
```

**Saiba mais**[PE EICEI100 Alteração de dados para rotina de integração com despachante](https://tdn.totvs.com/pages/releaseview.action?pageId=680245029)
