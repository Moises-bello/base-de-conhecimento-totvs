---
article_id: 360053164873
category: ADVPL - Classe e Função
content_hash: 34f5b5199b6a3666dbf7b866ca7829f193407212138e19940eadcc5cd5cc452a
fetched_at: '2026-06-28T22:40:18.144420+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TSVG: Usar imagens
  grandes'
type: support-article
updated_at: '2022-06-14T17:34:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053164873-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TSVG-Usar-imagens-grandes
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como usar uma arquivos grandes na classe TSVG()?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P12  
  
**Solução**Sugestão para uso de uma imagens grandes com a classe TSVG().

```
#include "totvs.ch"  
  
user function tsvg()   
  local textSVG := retSVG()   
  
  DEFINE DIALOG oDlg TITLE "Exemplo TSVG" FROM 180,180 TO 550, 700 PIXEL    
  
    // Cria o objeto e define os eventos do mouse  
    oSVG := TSVG():New(01,01,oDlg,200,200,textSVG)  
    oSVG:BLCLICKED := {|| alert("BLCLICKED") }  
    oSVG:BRCLICKED := {|| alert("BRCLICKED") }  
    oSVG:align := CONTROL_ALIGN_TOP     
  
  ACTIVATE MSDIALOG oDlg CENTERED    
  
return nil  
static function retSVG()  
  
  local textSVG := ""  
  
  // https://tdn.totvs.com/display/tec/FSeek  
  IF (nHandle := FOPEN("C:\Dir\imagem.svg")) >= 0  
  
    // Posiciona no fim do arquivo, retornando o tamanho do mesmo  
    nLength := FSEEK(nHandle, 0, 2) // 2=FS_END (fileio.ch)  
  
    // Posiciona no início do arquivo  
    FSEEK(nHandle, 0)  
  
    // Le arquivo até o final  
    textSVG := FReadStr( nHandle, nLength )  
  
    // Fecha arquivo  
    FCLOSE(nHandle)    
  
  endif  
return textSVG
```

**Saiba mais**

**[Classe TSVG](https://tdn.totvs.com/display/tec/TSVG)**
