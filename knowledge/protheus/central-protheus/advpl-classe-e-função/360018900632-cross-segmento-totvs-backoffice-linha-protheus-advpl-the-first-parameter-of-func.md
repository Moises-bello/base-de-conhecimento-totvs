---
article_id: 360018900632
category: ADVPL - Classe e Função
content_hash: a80a0722a0dc7f363c6dffba2f9183cd6a43c570bee59f980539c8d83746296c
fetched_at: '2026-06-28T22:40:18.084857+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - The first parameter
  of function CpyS2T must not contain the destination drive letter
type: support-article
updated_at: '2021-09-16T17:01:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018900632-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-The-first-parameter-of-function-CpyS2T-must-not-contain-the-destination-drive-letter
---

**Ocorrência**

Ao executar a Fwmsprinter ocorre erro abaixo:

**"O arquivo do relatório não pode ser copiado para o client"**

**"The first parameter of function CpyS2T must not contain the destination drive letter"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014967092/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014967132/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**o caminho **cPathInServer** está incorreto na classe FWMSPRINTER  
  
**Solução**

Verifique o caminho do diretório onde será salvo existe na pasta system e se está correto na customização

```
Private cLocalImp := GetSrvProfString("ROOTPATH","") + "\SPOOL\"  
  
FWMsPrinter():New("FATURA_EMAIL.rel",IMP_PDF,lAdjustToLegacy,cLocalImp,lDisableSetup,,,,.T.,,.F.,.F.)
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015000471/mceclip2.png)

Observação:  
Quando o erro ocorre em uma **estação local** é necessário:

1. Apontar criação do .rel (PDF) para uma pasta local do usuário;
2. Copiar este arquivo da pasta local (Estação) para a pasta protheus\_data\spool do servidor para outras tratativas como envio e-mail.
