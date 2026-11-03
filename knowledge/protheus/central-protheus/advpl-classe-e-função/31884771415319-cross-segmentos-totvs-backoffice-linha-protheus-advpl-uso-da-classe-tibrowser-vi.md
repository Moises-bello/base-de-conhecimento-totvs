---
article_id: 31884771415319
category: ADVPL - Classe e Função
content_hash: 40f4c4f3937c55e769eaf4bc15757140e805b3a81f1352f88df478f1a4855b2d
fetched_at: '2026-06-28T22:40:21.573859+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Uso da Classe
  TIBrowser via WebApp
type: support-article
updated_at: '2025-07-30T18:16:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31884771415319-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Uso-da-Classe-TIBrowser-via-WebApp
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31884783314327)*Tempo aproximado para leitura: 00:02:00 min

**Dúvida**  
É possível utilizar a classe TIBrowser no WebApp?

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.2310

**Solução**  
A Classe **TIBrowser** encontra-se descontinuada nas versões WebApp, pois o componente **TIBrowse** não é mais suportado devido a problemas de compatibilidade com Windows 10 e ferramentas **ActiveX** utilizadas em sua construção. Sendo assim, recomendamos o uso da função **TWebEngine** para a abertura da imagem.  
  
**Obs. :** Para uso da função **TWebEngine**é obrigatório o uso do **WebAgent** no ambiente.

**Exemplo**:

```
#include "TOTVS.CH"  
  
User Function TWebEngine()  
  
DEFINE DIALOG oDlg TITLE "Contorno para file://" FROM 0,0 TO 800,1200 PIXEL  
  
// Copia o arquivo da Estacao para o Servidor, retornando seu caminho  
// Este exemplo foi escrito para Linux, ao utilizar em Windows,  
// basta mudar o caminho para o arquivo, ex: "c:/dir/arquivo"  
cFilePath := CpyF2Web("\spool\imagem.jpeg", .T., .F., .F., .F.)  
  
oWebEngine := TWebEngine():New(oDlg, 0, 0, 100, 100,,)  
oWebEngine:Align := CONTROL_ALIGN_ALLCLIENT  
  
// Executa o Navigate para o arquivo temporario no Servidor  
oWebEngine:navigate(cFilePath)  
  
ACTIVATE DIALOG oDlg CENTERED  
Return
```

**Saiba mais**

[TIBrowse não abre pagina na versão Lobo Guara](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027851532-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TIBrowse-n%C3%A3o-abre-pagina-na-vers%C3%A3o-Lobo-Guara)

[TIBrowser](https://tdn.totvs.com/pages/viewpage.action?pageId=6063246)

[TWebEngine](https://tdn.totvs.com/display/tec/TWebEngine)

[WebAgent](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent)
