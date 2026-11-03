---
article_id: 360027260391
category: ADVPL - Classe e Função
content_hash: 3d08e924f93f9cd5585f151d62df8456a5a50923e0c17ef8e36f0e5981dfe374
fetched_at: '2026-06-28T22:40:15.487434+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Códigos de Cor TCBROWSE
type: support-article
updated_at: '2022-01-04T20:19:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027260391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-C%C3%B3digos-de-Cor-TCBROWSE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Estou utilizando a modificação de cores de linha em um TCBrowse, porém não consegui identificar qual a metodologia para obtenção dos códigos de cores.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**O método [SetBlkBackColor](http://tdn.totvs.com/display/tec/TCBrowse%3ASetBlkBackColor) permite alterar a cor da linha do grid. Para isso, é possível definir um bloco de código que permite condicionar as cores de acordo com a regra específica. Os códigos seguem a tabela padrão de cores ADVPL, que seguem:

**Tabela de cores**CLR\_BLACK         // RGB( 0, 0, 0 )  
CLR\_BLUE           // RGB( 0, 0, 128 )  
CLR\_GREEN        // RGB( 0, 128, 0 )  
CLR\_CYAN          // RGB( 0, 128, 128 )  
CLR\_RED            // RGB( 128, 0, 0 )  
CLR\_MAGENTA    // RGB( 128, 0, 128 )  
CLR\_BROWN       // RGB( 128, 128, 0 )  
CLR\_HGRAY        // RGB( 192, 192, 192 )  
CLR\_LIGHTGRAY // RGB( 192, 192, 192 )  
CLR\_GRAY          // RGB( 128, 128, 128 )  
CLR\_HBLUE        // RGB( 0, 0, 255 )  
CLR\_HGREEN      // RGB( 0, 255, 0 )  
CLR\_HCYAN        // RGB( 0, 255, 255 )  
CLR\_HRED          // RGB( 255, 0, 0 )  
CLR\_HMAGENTA  // RGB( 255, 0, 255 )  
CLR\_YELLOW      // RGB( 255, 255, 0 )  
CLR\_WHITE        // RGB( 255, 255, 255 )

Segue exemplo básico de utilização:

```
#Include 'Protheus.ch'  
#Include 'tbiconn.ch'  
  
User Function TcBrCor()  
Local oDlg  
  
PREPARE ENVIRONMENT EMPRESA '99' FILIAL '01'  
  
DEFINE DIALOG oDlg TITLE "Exemplo SetBlkBackColor" FROM 180,180 TO 550,700 PIXEL   
   
 // Cria browse que receberá as colunas   
 DbSelectArea("SA1")   
 oBrowse:=TCBrowse():New(1,1,260,184,,,,oDlg,,,,,,,,,,,,.F.,"SA1",.T.,,.F.,,,)  
   
 // Cria colunas   
 oBrowse:AddColumn(TCColumn():New("Codigo",{||SA1->A1_COD },,,,"LEFT",,.F.,.F.,,,,,))   
 oBrowse:AddColumn(TCColumn():New("Loja" ,{||SA1->A1_LOJA},,,,"LEFT",,.F.,.F.,,,,,))   
 oBrowse:AddColumn(TCColumn():New("Nome" ,{||SA1->A1_NOME},,,,"LEFT",,.F.,.F.,,,,,))  
  
oBrowse:lUseDefaultColors := .F.   
   
   
 // Muda a cor da linha do browser   
 oBrowse:SetBlkBackColor({|| IIf(SA1->A1_COD == "000001" .AND. SA1->A1_LOJA == '01' , CLR_HMAGENTA , Nil )})  
  
oBrowse:Align := CONTROL_ALIGN_ALLCLIENT  
   
 ACTIVATE DIALOG oDlg CENTERED  
   
Return
```

A rotina acima irá listar os clientes em um grid [TCBrowse](http://tdn.totvs.com/display/tec/TCBrowse), e definirá a cor **CLR\_HMAGENTA** somente para o cliente de código '000001' e loja '01'.   
  
O seguinte grid será exibido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026773232/mceclip0.png)

Observação: Caso o recurso não atenda a sua necessidade, é possível também realizar outras mudanças no estilo do componente utilizando CSS, conforme documentação [SetCSS.](http://tdn.totvs.com.br/display/tec/SetCSS)
