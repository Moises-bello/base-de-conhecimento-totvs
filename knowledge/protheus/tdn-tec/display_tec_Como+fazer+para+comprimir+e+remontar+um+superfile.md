---
content_hash: 21109d06a1ca67fe7ed877a1c4730a7033bd02ae80bd8c422bfda7f646d276fe
fetched_at: '2026-07-02T19:24:27.804191+00:00'
page_id: '682061564'
product: protheus
source: tdn-tec
title: Como fazer para comprimir e remontar um superfile
type: documentation
url: https://tdn.totvs.com/display/tec/Como+fazer+para+comprimir+e+remontar+um+superfile
version: 1
---

Como fazer para comprimir e remontar um superfile

**01. SITUAÇÃO/REQUISITO**

Em algumas situações de erros no acesso a arquivos c-tree, pode ser necessário efetuar esse procedimento para remontar um superfile.

Não se esqueça de bloquear previamente o acesso dos demais usuários, esse procedimento deve ser realizado em modo stand-alone pelo Administrador do ambiente.IMPORTANTE!

**02. SOLUÇÃO**

Passo 01, Passo 02, Passo 03passo1,passo2,passo3yespasso1

Interromper o ambiente.

* Interromper o true (primários e secundários), workflow e demais serviços dedicados (caso estejam separados);
* Caso o ambiente utilize o c-tree Server, interromper o c-tree Server.
nopasso2

Execute **ctscmp <superfile> -v11 64**

Exemplo: ctscmp sigahlp.hlp -v11 64

 Opte por realizar o backup antes de processar o arquivo, eles podem ser necessários para análise.

nopasso3

Após a criação dos índices, encerre o sistema, reinicie o ambiente e libere o acesso para todos os usuários.

**03. MAIS INFORMAÇÕES**

* [ctscmp - Superfile Compact Utility. FairCom](https://docs.faircom.com/doc/ctreeplus/31096.htm)

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
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
