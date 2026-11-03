---
article_id: 360039767494
category: ADVPL - Classe e Função
content_hash: 60455fe0e9f20139bc9959f372c92d19bb2ea044b11224fb0b7fc49157cc3423
fetched_at: '2026-06-28T22:40:18.037207+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Sobreposição de
  tela FwBrowse
type: support-article
updated_at: '2024-07-31T21:00:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039767494-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Sobreposi%C3%A7%C3%A3o-de-tela-FwBrowse
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura :**00:02:00 min  
  
Dúvida**Em uma tela MBrowse() onde chamo a FWMBrowse(), está sobrepondo o menu outras ações com o conteúdo da MBrowse().  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.1.17  
  
**Solução**Quando a FwMBrowse() filha é chamada e encontra uma variável privada aRotina, a mesma é utilizada, sendo assim é necessário criar uma variável por exemplo getArotina para receber o conteúdo da variável privada aRotina, limpar da variável privada aRotina e ao fechar o FwMBrowse() retornar o conteúdo armazenado na variável  getArotina.  
Segue abaixo um modelo de exemplo:

```
User Function zMVCMd1()  
  
    Local aArea   := GetArea()  
    Local aGetArotina := aRotina  
    Local oBrowse  
   
    //Instânciando FWMBrowse   
    oBrowse := FWMBrowse():New()  
  
    //Setando a tabela   
    oBrowse:SetAlias("SB1")  
  
    //Setando a descrição da rotina  
    oBrowse:SetDescription(cTitulo)  
  
    //CHAMADA DO MENUDEF   
    aRotina:={} //Limpar arotina PAI  
    oBrowse:SetMenuDef('ZMVCTDN')  
  
    //Ativa a Browse  
    oBrowse:Activate()  
  
    aRotina :=aGetArotina  
    RestArea(aArea)  
  
Return Nil
```
