---
article_id: 360027579092
category: BI - Business- Intelligence - Workflow
content_hash: a002241a1369f15525cf5eda93a6da757cef86c925900998a781877acabd6171
fetched_at: '2026-06-28T22:37:03.071477+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Título do e-mail disparado
  através do Workflow não traz "ç" e também palavras com acentos.
type: support-article
updated_at: '2022-02-15T19:06:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027579092-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-T%C3%ADtulo-do-e-mail-disparado-atrav%C3%A9s-do-Workflow-n%C3%A3o-traz-%C3%A7-e-tamb%C3%A9m-palavras-com-acentos
---

**Dúvida**Título do e-mail disparado através do **Workflow** está trazendo caracteres especiais nos lugares de **"ç"** e também **palavras com acentos**.  
  
**Ambiente**Protheus – Workflow – A partir da versão 12  
  
**Solução**Para exibir uma página ou mesmo um título **HTML** corretamente, um navegador da Web deve saber qual conjunto de caracteres (codificação de caracteres) deve ser usado.

Usualmente a codificação **UTF-8** (Unicode) abrange quase todos os personagens e símbolos do mundo.

Tratando agora o fonte do **Workflow**, temos o parâmetro **cSubject:**

**cSubject: É um parãmetro do método SendMail, do tipo caractere que indica o assunto do e-mail. Caso não seja especificado, o assunto será enviado em branco.**

Neste caso o **cSubject** poderá ser tratado com o parâmetro **EncodeUTF8** que converte uma string de origem de um ***encoding*** (code-page) conhecido para a codificação **UTF-8** ( 8-bit Unicode Transformation Format ).

Os valores possíveis para o parâmetro ***encoding*** são aqueles utilizados pela biblioteca *iconv*. Pode-se visualizar o conjunto de valores a partir do executável binário gerado pela biblioteca *iconv* pelo comando: **iconv -l**. Alguns dos valores possíveis são **"cp1252", "cp1251", "iso8859-1"**.

```
//-------------------------------------------------------------------  
 // Informamos o assunto do email.   
 //-------------------------------------------------------------------   
 //oProcess:cSubject := "çççççççççççççç"  
 oProcess:cSubject := EncodeUTF8("çççççççççççççç", "cp1252")
```

**Saiba mais:** **[EncodeUTF8](http://tdn.totvs.com/display/tec/EncodeUTF8)****[TMailManager:SendMail](http://tdn.totvs.com/display/tec/TMailManager%3ASendMail)**
