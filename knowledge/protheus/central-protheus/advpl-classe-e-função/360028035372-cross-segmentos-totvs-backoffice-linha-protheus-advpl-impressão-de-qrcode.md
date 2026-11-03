---
article_id: 360028035372
category: ADVPL - Classe e Função
content_hash: d1e84397e3c94fd75af3b981f7cfb221a220512dc2c5df5cf5f9f7f9cdb82677
fetched_at: '2026-06-28T22:40:20.429556+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Impressão de QRCODE
type: support-article
updated_at: '2024-09-18T11:11:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028035372-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impress%C3%A3o-de-QRCODE
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26452200235671)*Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**O Protheus possui alguma função para impressão do QRCODE ?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para gerar o QRCODE utilizamos a classe [**FwQRCode.**](http://tdn.totvs.com/display/public/PROT/FwQrCode)  
  
A classe [**FwQRCode**](http://tdn.totvs.com/display/public/PROT/FwQrCode) permite que seja adicionado um componente gráfico em vídeo, capaz de exibir um gráfico do tipo **QRCode**. Temos também o método Qrcode na Classe**[FwMsprinter](https://tdn.totvs.com/display/public/framework/FWMsPrinter)**

**Exemplo**

```
#INCLUDE "PROTHEUS.CH"  
  
//Consulte: http://tdn.totvs.com.br/display/mp/FwQrCode  
User Function TstQrCode()  
Local oDLG := Nil  
Local cCodigo := "http://www.totvs.com.br" + Space(60)  
Private oQrCode  
  
//Cria a Dialog  
DEFINE MSDIALOG oDlg TITLE "RDMAKE para teste da classe FwQrCode" FROM 0,0 TO 400,800 PIXEL  
  
//Cria o objeto FwQrCode  
oQrCode := FwQrCode():New({25,25,200,200},oDlg,cCodigo)  
  
//Get com o codigo exibido  
@25,150 GET oGet VAR cCodigo OF oDlg SIZE 200,10 PIXEL  
  
//Botao Gerar  
@45,150 BUTTON "Gerar" SIZE 30,20 PIXEL OF oDlg ACTION MsgRun("Gerando QRCode","Aguarde",{|| U_MyRefresh(cCodigo)}) PIXEL  
  
//Exibe a Dialog em Video  
ACTIVATE MSDIALOG oDlg CENTERED  
  
Return  
  
User Function MyRefresh(cNewCod)  
oQrCode:SetCodeBar(cNewCod)  
oQrCode:Refresh()  
Return
```

![FwQrCode.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26452202820247)
