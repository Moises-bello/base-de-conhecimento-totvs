---
article_id: 22729076180503
category: ADVPL - Classe e Função
content_hash: dcfe90fcfbf09eb54c884e7323e898cb93e635562b68b48cde357d605162d863
fetched_at: '2026-06-28T22:40:20.663937+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Alterar tamanho
  da tela na classe FwMarkBrowse
type: support-article
updated_at: '2024-04-11T12:01:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22729076180503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Alterar-tamanho-da-tela-na-classe-FwMarkBrowse
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22729076172567) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Quais são as funções de criptografia existentes no Protheus?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Pela classe FwMarkBrowse não existe este controle de tamanho da tela. Agora pode-se criar a FwMarkBrowse em uma MsDialog ou TDialog, irá conseguir redimensionar.

**Exemplo:**

```
#include "protheus.ch"  
  
#include "fwmvcdef.ch"  
  
  
function u_tstFwMarkDlg()  
  
            private oMark  
           private oDlg  
           private aRotina := menuDef()  
  
  
           oDlg := msDialog():new(180,180,550,700,'Browse Mark com Dialog',,,,,CLR_BLACK,CLR_WHITE,,,.T.)  
  
            oMark := fwMarkBrowse():new()  
          oMark:setOwner(oDlg)  
        oMark:setAlias('SA1')  
            oMark:setDescription('Alunos')  
        oMark:setFieldMark( 'A1_OK' )  
     oMark:setSeeAll(.T.)   
            oMark:activate()  
  
            // Ativa diálogo centralizado  
  
         oDlg:activate(,,,.t.,{||,.t.},,{||})  
return  
static function menuDef()  
  
            local aRotina := {}  
            ADD OPTION aRotina TITLE 'Visualizar' ACTION 'função de usuário' OPERATION 2 ACCESS 0  
           ADD OPTION aRotina TITLE 'Processar' ACTION 'função de usuário' OPERATION 2 ACCESS 0  
  
return aRotina
```

**Saiba Mais**

[MsDialog](https://tdn.totvs.com/display/tec/MsDialog)

[TDialog](https://tdn.totvs.com/display/tec/TDialog)

[FwMarkBrowse](https://tdn.totvs.com/display/public/framework/FWMarkBrowse)
