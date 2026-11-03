---
content_hash: dc9ecc92c164cb9ca7fc6b285623af063fe45458ac2a3f533f560ac218b5d919
fetched_at: '2026-06-29T00:10:45.523594+00:00'
page_id: '553338788'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Como Realizar Check-in no Azure DevOps?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338788
version: 1
---

5%90%10%100%

Ao trabalhar com uma *issue* no Azure Devops, no momento do *commit* é necessário passar o código da *issue* na mensagem para que ocorra a integração do *check-in*. O código da *issue* pode ser incluído em qualquer lugar da mensagem:

Exemplos:   
git commit -m "DTHFM-202"  
git commit -m "DTHFM-202 teste"  
git commit -m "teste DTHFM-202"  
git commit -m "teste DTHFM-202 teste teste"  
  
Após a realização do *Push* ao diretório Remoto, estando tudo ok e após alguns segundos, a informação do campo TFS Checkins será populada com o *changset*.

A visualização do *commit* na *issue* ficará disponível no campo (TFS Check-ins)

5%
div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.expand-control-text {
color: #000000;
font-size: 13px !important;
font-weight:bold !important;
}
.expand-icon, .aui-icon, .aui-icon-small, .aui-iconfont-chevron-right {
color: #FF8000;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
