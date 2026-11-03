---
article_id: 360039323514
category: ADVPL - Classe e Função
content_hash: f4b159e7fda4d40693cb0e29d748a409b1ceb29139565d2e9037770f8775fa4f
fetched_at: '2026-06-28T22:40:19.535289+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Gerar senha no
  arquivo PDF
type: support-article
updated_at: '2022-01-11T17:45:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039323514-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Gerar-senha-no-arquivo-PDF
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min****Dúvida**É possível gerar PDF com senha?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17

**Solução**Segue documentação da [Totvs Printer](https://tdn.totvs.com.br/display/tec/Agente+TOTVS+Printer) tem exemplos de como usar o executável com parâmetros para gerar senha no PDF.

```
printer.exe meuexemplo.rel PDF_WITH_PASSWORD senhauser senhaowner
```

Neste caso use a [ShellExecute](https://tdn.totvs.com/display/tec/ShellExecute).  
Observação: É necessário que o arquivo já esteja gerado, exemplo:

```
#Include 'Protheus.ch'  
  
User Function TshellExec()  
  
ShellExecute( "Open", "C:\Protheus12\Protheus12.1.25\protheus\bin\appserver\printer.exe", "C:\01\impressao_pdf.rel PDF_WITH_PASSWORD senhauser senhaowner","C:\01", 1 )  
//ShellExecute( "Open", "C:\Protheus12\Protheus12.1.25\protheus\bin\appserver\printer.exe", "C:\01\"+ cName + "PDF_WITH_PASSWORD senhauser senhaowner","C:\01", 1 )  
 Return
```

Ao executar o arquivo a senha é solicitada

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052686453/mceclip0.png)
