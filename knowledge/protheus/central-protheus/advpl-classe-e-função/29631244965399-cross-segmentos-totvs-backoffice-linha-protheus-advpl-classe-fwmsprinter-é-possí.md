---
article_id: 29631244965399
category: ADVPL - Classe e Função
content_hash: 3f814ce55a9efb567692ee75afc47fe01646aa42e36c5301271a77dcee4e6fe7
fetched_at: '2026-06-28T22:40:21.663695+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL- Classe FWMsPrinter
  - É possível gerar um relatório em formato MSExcel, XLS, XLSX ou XML utilizando
  a Classe FWMsPrinter?
type: support-article
updated_at: '2025-01-30T18:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29631244965399-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FWMsPrinter-%C3%89-poss%C3%ADvel-gerar-um-relat%C3%B3rio-em-formato-MSExcel-XLS-XLSX-ou-XML-utilizando-a-Classe-FWMsPrinter
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29631244947351) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possível gerar um relatório Excel utilizando a **FWMsPrinter**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

A classe **FWMSPrinter** é utilizada para geração de arquivos **PDF** ( **IMP\_PDF**) ou envio para impressora (**IMP\_SPOOL** ).

* **IMP\_SPOOL** -> Envia para impressora.
* **IMP\_PDF** -> Gera arquivo PDF a partir do relatório.

Para a geração de planilhas, pode ser utilizada a classe **[FWMsExcel](https://tdn.totvs.com/display/public/framework/FWMsExcel)**

**Exemplo:**

User Function TESTE()

Local oExcel := FWMSEXCEL():New()

oExcel:AddworkSheet("Teste - 1")  
oExcel:AddTable ("Teste - 1","Titulo de teste 1")  
oExcel:AddColumn("Teste - 1","Titulo de teste 1","Col1",1,1)  
oExcel:AddColumn("Teste - 1","Titulo de teste 1","Col2",2,2)  
oExcel:AddColumn("Teste - 1","Titulo de teste 1","Col3",3,3)  
oExcel:AddColumn("Teste - 1","Titulo de teste 1","Col4",1,1)  
oExcel:AddRow("Teste - 1","Titulo de teste 1",{11,12,13,14})  
oExcel:AddRow("Teste - 1","Titulo de teste 1",{21,22,23,24})  
oExcel:AddRow("Teste - 1","Titulo de teste 1",{31,32,33,34})  
oExcel:AddRow("Teste - 1","Titulo de teste 1",{41,42,43,44})  
oExcel:AddworkSheet("Teste - 2")  
oExcel:AddTable("Teste - 2","Titulo de teste 1")  
oExcel:AddColumn("Teste - 2","Titulo de teste 1","Col1",1)  
oExcel:AddColumn("Teste - 2","Titulo de teste 1","Col2",2)  
oExcel:AddColumn("Teste - 2","Titulo de teste 1","Col3",3)  
oExcel:AddColumn("Teste - 2","Titulo de teste 1","Col4",1)  
oExcel:AddRow("Teste - 2","Titulo de teste 1",{11,12,13,stod("20121212")})  
oExcel:AddRow("Teste - 2","Titulo de teste 1",{21,22,23,stod("20121212")})  
oExcel:AddRow("Teste - 2","Titulo de teste 1",{31,32,33,stod("20121212")})  
oExcel:AddRow("Teste - 2","Titulo de teste 1",{41,42,43,stod("20121212")})  
oExcel:AddRow("Teste - 2","Titulo de teste 1",{51,52,53,stod("20121212")})  
oExcel:Activate()  
oExcel:GetXMLFile("TESTE.xml")

Return

Para gerar uma planilha nativa do **MS Excel**, ou seja, arquivo extensão XLSX, podem ser utilizadas as classes **FwPrinterXlsx** e/ou **FWMsExcelXlsx**

**Saiba Mais:**

[FWMsExcelEx](https://tdn.totvs.com/display/public/framework/FWMsExcelEx)  
[FwPrinterXlsx](https://tdn.totvs.com/display/framework/FwPrinterXlsx)  
[FWMsExcelXlsx](https://tdn.totvs.com/display/public/framework/FWMsExcelXlsx)
