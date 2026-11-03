---
article_id: 1500012788641
category: ADVPL - Classe e Função
content_hash: f9f3028f7cff650f3be267a8885864548ff3575aea1d9d7bc2f0598a8fd47f5b
fetched_at: '2026-06-28T22:40:15.566167+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como quebrar linha
  em um XML gerado pela classe FWMsExcel?
type: support-article
updated_at: '2021-05-31T18:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012788641-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-quebrar-linha-em-um-XML-gerado-pela-classe-FWMsExcel
---

**Dúvida**Como quebrar linha em um XML gerado pela classe **FWMsExcel**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**Na utilização de quebra utilizando a **ASCII**, que seria **CR** + **LF**  (alimentação de linha - **CHR(13)**+**CHR(10)** ) não tem qualquer efeito na leitura/execução do **XML**, alterando apenas a escrita do arquivo de texto extensão .**XML**.

Para execução da "quebra de linha" deve-se passar o comando em ***HTML codes*** junto a *String* que deseja quebrar:

```
&#13;&#10;
```

Conforme tabela:

|  |  |  |
| --- | --- | --- |
| **Code** | **Name** | **Displayed as** |
| &#09; | Horizontal tab | non-printing |
| &#10; | Line feed | non-printing |
| &#13; | Carriage Return | non-printing |
| &#32; | Space | non-printing |
| &#33; | Exclamation mark | ! |
| &#34; | Quotation mark | " |
| &#35; | Number sign | # |
| &#36; | Dollar sign | $ |
| &#37; | Percent sign | % |
| &#38; | Ampersand | & |
| &#39; | Apostrophe | ' |
| &#40; | Left parenthesis | ( |
| &#41; | Right parenthesis | ) |
| &#42; | Asterisk | \* |
| &#43; | Plus sign | + |
| &#44; | Comma | , |
| &#45; | Hyphen | - |
| &#46; | Period | . |
| &#47; | Slash | / |
| &#58; | Colon | : |
| &#59; | Semi-colon | ; |
| &#60; | Less than | < |
| &#61; | Equals sign | = |
| &#62; | Greater than | > |
| &#63; | Question mark | ? |
| &#64; | At | @ |
| &#91; | Left square bracket | [ |
| &#92; | Bbackslash | \ |
| &#93; | Right square bracket | ] |
| &#94; | Caret | ^ |
| &#95; | Underscore | \_ |
| &#96; | Acute accent | ` |
| &#123; | Left curly brace | { |
| &#124; | Vertical bar | | |
| &#125; | Right curly brace | } |
| &#126; | Tilde | ~ |

Exemplo:

```
#include 'totvs.ch'  
  
#DEFINE CRLF "&#13;&#10;"  
  
User Function TSTEXCEL()  
  
    Local oExcel := FWMSEXCEL():New()  
  
    oExcel:AddworkSheet("Teste - 1")  
  
    oExcel:AddTable ("Teste - 1","Titulo de teste 1")  
  
    oExcel:AddColumn("Teste - 1","Titulo de teste 1","Col1",1,1)  
  
    oExcel:AddColumn("Teste - 1","Titulo de teste 1","Col2",2,2)  
  
    oExcel:AddColumn("Teste - 1","Titulo de teste 1","Col3",3,3)  
  
    oExcel:AddColumn("Teste - 1","Titulo de teste 1","Col4",1,1)  
  
    oExcel:SetLineHeight(30.6)  
  
    oExcel:AddRow("Teste - 1","Titulo de teste 1",{"Titulo de teste 1 " +CRLF+" Titulo de teste 2",12,13,14})  
  
    oExcel:AddRow("Teste - 1","Titulo de teste 1",{21,22,23,24})  
  
    oExcel:AddRow("Teste - 1","Titulo de teste 1",{31,32,33,34})  
  
    oExcel:AddRow("Teste - 1","Titulo de teste 1",{41,42,43,44})  
  
    oExcel:Activate()  
  
    oExcel:GetXMLFile("TESTE.xml")  
  
Return
```

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020007541/mceclip1.png)**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020005701/mceclip0.png)**

**Saiba mais**  
[FWMsExcel](https://tdn.totvs.com/display/framework/FWMsExcel%C2%A0)
