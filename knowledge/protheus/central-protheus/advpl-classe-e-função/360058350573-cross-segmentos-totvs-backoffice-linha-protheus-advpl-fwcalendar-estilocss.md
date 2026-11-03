---
article_id: 360058350573
category: ADVPL - Classe e Função
content_hash: 35e3d13c7d4a966ea8e5cef76a8c9ab5a78de0d66082f094faae11c80fdbc166
fetched_at: '2026-06-28T22:40:19.486266+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - FWCALENDAR estilo.CSS
type: support-article
updated_at: '2022-01-10T22:25:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058350573-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-FWCALENDAR-estilo-CSS
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como definir estilo .css no conteúdo das celulas do ***FwCalendar()?***  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - AdvPL - A parti da versão 12.1.17.

**Solução**Segue abaixo um modelo de exemplo para auxiliar em suas customizações:

```
#include 'TOTVS.CH'  
//-------------------------------------------------------------------  
/*/{Protheus.doc} @author Eduardo Paro de Simoni  
    Exemplo de FwCalendar  
-------------------------------------------------------------------*/  
function U_zFwCalendar()  
        local oDlg      := nil  
        local oCalend   := nil  
        local aCoors    := FwGetDialogSize()  
        local cTxtCel   :=''  
        Define MsDialog oDlg Title 'Calendário de Edu' From aCoors[1], aCoors[2] To aCoors[3], aCoors[4] Pixel  
  
        cTxtCel:= '<h3>Teste de Estilo .css </h3> '  
        cTxtCel+= '<font color="red">Este texto é vermelho!</font> <br> '  
        cTxtCel+= '<font color="blue">Este texto é azul!</font><br>     '  
        cTxtCel+= '<font color="yellow">Este texto é amarelo!</font><br> '  
        cTxtCel+= '<font color="green">Este texto é verde!</font>'  
  
        oCalend := FwCalendar():New(Month(dDataBase), Year(dDataBase))  
        oCalend:aNomeCol := {'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Semana'}  
        oCalend:lWeekColumn := .F.  
        oCalend:lFooterLine := .F.  
        oCalend:Activate( oDlg )   
          
        For nI := 1 To Len( oCalend:aCell )   
                If oCalend:aCell[nI][4]   
                        //oCalend:SetInfo( oCalend:aCell[nI][1], '<h1 style="background:red">Eduardo</h1>' )  
                        oCalend:SetInfo( oCalend:aCell[nI][1], cTxtCel )  
                endif              
        Next  
        Activate MsDialog oDlg Centered  
Return
```

Observação:Ao passar a string no ***setInfo*** ela é informada diretamente no componente visual. Os componentes do ***Protheus*** conseguem verificar se o texto informado é um ***html/css*** e conseguem realizar a aplicação.  
Ao informar um array é utilizado um componente do tipo ***listbox***, que não faz essa conversão para acatar um ***css***.  
Desta maneira, o utilizar um (array) ***listbox*** o ***css*** não será acatado.  
  
**Saiba mais**  
[FWCalendar](https://tdn.totvs.com/display/public/PROT/FWCalendar)
