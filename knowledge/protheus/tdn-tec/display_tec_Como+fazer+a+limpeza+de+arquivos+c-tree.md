---
content_hash: d0daf51cc177c3a3d00e6015970e1ba78a19ce42bb6708c4bcd4efa8fcf672e7
fetched_at: '2026-07-02T19:24:22.349821+00:00'
page_id: '269425777'
product: protheus
source: tdn-tec
title: Como fazer a limpeza de arquivos c-tree
type: documentation
url: https://tdn.totvs.com/display/tec/Como+fazer+a+limpeza+de+arquivos+c-tree
version: 5
---

Como fazer a limpeza dos arquivos c-tree

**01. SITUAÇÃO/REQUISITO**

Em algumas situações de erros no acesso a arquivos c-tree na inicialização do sistema, pode ser necessário efetuar uma limpeza do ambiente c-tree.

Não se esqueça de bloquear previamente o acesso dos demais usuários, esse procedimento deve ser realizado em modo stand-alone pelo Administrador do ambiente.IMPORTANTE!

**02. SOLUÇÃO**

Passo 01, Passo 02, Passo 03, Passo 04, Passo 05passo1,passo2,passo3,passo4,passo5yespasso1

Interromper o ambiente.

* Interromper o true (primários e secundários), workflow e demais serviços dedicados (caso estejam separados);
* Caso o ambiente utilize o c-tree Server, interromper o c-tree Server.
nopasso2

Se estiver usando c-tree Server, apagar os arquivos \*.FCS

Opte por realizar o backup desses arquivos, eles podem ser necessários para análise.

nopasso3

* Apagar os arquivos de índices (\*.CDX, .IDX e \*.IND), na pasta SYSTEM (o nome da pasta usualmente SYSTEM e corresponde àquele definido em STARTPATH);
* Apagar o conteúdo (\*.CDX) da pasta PROFILE (localizada a partir de ROOTPATH);
* Apagar o conteúdo da pasta CTREEINT (localizada no ROOTPATH, na pasta PROFILE e em STARTPATH);
nopasso4

Reinicialize o ambiente e faça o acesso *stand-alone* (somente um usuário).

* Caso o ambiente utilize o c-tree Server, inicie uma nova instância do c-tree Server;
* Inicie uma nova instância do true;
* Acesse o sistema para que sejam recriados os índices.

Caso existam mais empresas/filiais, esse passo deve ser realizado para cada uma das empresas/filiais.

O módulo SIGACFG pode ser utilizado para agilizar o processo de criação dos índices.

nopasso5

Após a criação dos índices, encerre o sistema, reinicie o ambiente e libere o acesso para todos os usuários.

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
