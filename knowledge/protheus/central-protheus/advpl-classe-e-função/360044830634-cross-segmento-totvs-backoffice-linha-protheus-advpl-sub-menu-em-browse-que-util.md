---
article_id: 360044830634
category: ADVPL - Classe e Função
content_hash: a977acacb84adfe1b087628d73680ca70906bc4074444255334ce64b0416e92f
fetched_at: '2026-06-28T22:40:18.051690+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Sub Menu em browse
  que utiliza rotina padrão MVC
type: support-article
updated_at: '2023-07-27T12:44:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044830634-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Sub-Menu-em-browse-que-utiliza-rotina-padr%C3%A3o-MVC
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Existe alguma forma de colocar um Submenus em MVC utilizando o formato que o manual da totvs recomenda ?  
 **Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Exemplo

```
Static Function MenuDef()  
  
Local aRotina := {}  
Local aSubMnu := {}  
  
// Menu   
ADD OPTION aRotina TITLE 'Visualizar' ACTION 'VIEWDEF.MVC01' OPERATION 2 ACCESS 0  
ADD OPTION aRotina TITLE 'Incluir'    ACTION 'VIEWDEF.MVC01' OPERATION 3 ACCESS 0  
ADD OPTION aRotina TITLE 'Alterar'    ACTION 'VIEWDEF.MVC01' OPERATION 4 ACCESS 0  
ADD OPTION aRotina TITLE 'Excluir'    ACTION 'VIEWDEF.MVC01' OPERATION 5 ACCESS 0  
ADD OPTION aRotina TITLE 'Imprimir'   ACTION 'VIEWDEF.MVC01' OPERATION 8 ACCESS 0  
ADD OPTION aRotina TITLE 'Copiar'     ACTION 'VIEWDEF.MVC01' OPERATION 9 ACCESS 0  
  
//Adiciona o arrya do submenu a opção do menu  
ADD OPTION aRotina TITLE 'SubMenu'    ACTION aSubMnu         OPERATION 9 ACCESS 0  
  
// adiciona opções no submenu  
ADD OPTION aSubMnu TITLE 'Sub Menu 01'    ACTION 'Alert("Sub menu 01")'  OPERATION 4 ACCESS 0   
ADD OPTION aSubMnu TITLE 'Sub Menu 02'    ACTION 'Alert("Sub menu 02")'  OPERATION 4 ACCESS 0   
  
Return aRotina
```

Funcionamento **![20200320_160200.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360062607553/20200320_160200.gif)**

**Saiba mais  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como utilizar MVC (Model View Controller)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017512652)**
