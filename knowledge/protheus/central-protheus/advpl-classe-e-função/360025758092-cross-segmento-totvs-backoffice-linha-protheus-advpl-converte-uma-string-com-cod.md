---
article_id: 360025758092
category: ADVPL - Classe e Função
content_hash: 8b5725f90cf2b21b130e8fc55d547477e17f180f9db38e7e69ab94570f0b26bf
fetched_at: '2026-06-28T22:40:15.686760+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Converte uma string
  com codificação UTF-8
type: support-article
updated_at: '2024-12-23T13:14:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025758092-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Converte-uma-string-com-codifica%C3%A7%C3%A3o-UTF-8
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28732732982039)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Preciso utilizar na formação dos e-mails enviados pelo Protheus, o formato UTF-8, pois todos os e-mails que o Protheus envia e tem caracteres especiais estão indo para caixa de span. O provedor informou que precisamos formatar esses e-mails com o padrão UTF-8.

Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025100972)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para tratamento com textos do tipo **UTF-8**, temos as funções **EncodeUTF8** (Converte uma string de origem de um *encoding* (code-page) conhecido para a codificação UTF-8) e função **DecodeUTF8** (Converte uma string **UTF-8** para um buffer com *encoding* especificado em cEncoding).

**Exemplo**:

```
#define CRLF Chr(13) + Chr(10)  
  
User Function Exemplo()  
  
Local cTexto := ""  
Local cEncodeUTF8 := ""  
Local cDecodeUTF8 := ""  
Local cMensagem := ""  
  
cTexto := "à noite, vovô kowalsky vê o ímã cair no pé do pingüim "  
cTexto += "queixoso e vovó põe açúcar no chá de tâmaras do jabuti feliz."  
cEncodeUTF8 := EncodeUTF8(cTexto, "cp1252")  
cDecodeUTF8 := DecodeUTF8(cEncodeUTF8, "cp1252")  
cMensagem := "Pangrama origem: [" + cTexto + "]"  
cMensagem += CRLF + "Texto -> UTF8: [" + cEncodeUTF8 + "]"  
cMensagem += CRLF + "UTF8 -> Texto: [" + cDecodeUTF8 + "]"  
MsgInfo(cMensagem, "Exemplo")  
  
// Brasil em Russo  
cTexto := chr(193)+chr(240)+chr(224)+chr(231)+chr(232)+chr(235)+chr(201)+chr(235)+chr(255)  
cEncodeUTF8 := EncodeUTF8(cTexto, "cp1251")  
cDecodeUTF8 := DecodeUTF8(cEncodeUTF8, "cp1251")  
cMensagem := "Pangrama origem: [" + cTexto + "]"  
cMensagem += CRLF + "Texto -> UTF8: [" + cEncodeUTF8 + "]"  
cMensagem += CRLF + "UTF8 -> Texto: [" + cDecodeUTF8 + "]"  
MsgInfo(cMensagem, "Exemplo")  
  
Return
```

**Saiba mais**

[Função EncodeUTF8](https://tdn.totvs.com/display/tec/EncodeUTF8)

[Função DecodeUTF8](https://tdn.totvs.com/display/tec/DecodeUTF8)
