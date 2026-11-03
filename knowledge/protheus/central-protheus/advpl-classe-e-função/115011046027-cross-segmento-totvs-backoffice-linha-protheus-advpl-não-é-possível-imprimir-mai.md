---
article_id: 115011046027
category: ADVPL - Classe e Função
content_hash: 7a882929bf7672b9f27cc60599d0601dd89302bb937667c7e78b1751c5a35a5b
fetched_at: '2026-06-28T22:40:14.204494+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Não é possível
  imprimir mais de 99 paginas na classe Fwmsprinter
type: support-article
updated_at: '2021-09-01T14:25:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011046027-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-N%C3%A3o-%C3%A9-poss%C3%ADvel-imprimir-mais-de-99-paginas-na-classe-Fwmsprinter
---

**Dúvida**Não é possível imprimir mais de 99 paginas na classe **Fwmsprinter**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**

A Classe **Fwmsprinter** com a opção de apresentação da tela do Setup tem a limitação de 99 paginas, mas é possível imprimir mas que 99 paginas utilizando o 13º parâmetro "**nQtdCopy"**  da classe Fwmsprinter sem apresentação de tela

![](https://tdn.totvs.com/download/attachments/274304747/image2017-5-9%2018%3A20%3A4.png?version=1&modificationDate=1494365462000&api=v2)

Exemplo

```
local nQtdCopy:= "150"  
  
oPrint:= FWMSPrinter():New(cFilePrint, IMP_SPOOL , lAdjustToLegacy, cLocal, .T.,.f., , , .t., , ,,nQtdCopy )  
oPrint:StartPage()  
oPrint:lserver:=.T.  
oPrint:linjob:=.T.  
oPrint:cSession :=""  
oPrint:cPrinter := "\\printserver-02\SPCloudPrinter-Color" // nome da impressora  
oPrint:Box(10, 10, 110, 110)  
oPrint:Say(10, 10, "TESTANDO")  
oPrint:nPageCount:=2  
oPrint:EndPage()  
oPrint:Print()
```

**Saiba mais**  
[ADV0018 Impressão FWMSPRINTER](http://tdn.totvs.com/display/PROT/ADV0018_IMP_IMPRESSAO_FWMSPRINTER)
