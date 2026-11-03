---
content_hash: 51ba999a07c3fc084af96fda770c680446163a6a87282c1561dcc1a432935e09
fetched_at: '2026-06-29T00:10:21.263699+00:00'
page_id: '490973734'
product: rm
source: tdn-rm
title: 5256984 FISCAL01-8305 DT - Alteração de contexto do fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490973734
version: 5
---

****01.********DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | C&P |
| Módulo: | Gestão Fiscal |
| Função: | Alteração de contexto |
| Ticket: | 5256984 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8305 |

**02. SITUAÇÃO/REQUISITO**

          Ao gerar a guia do DIFAL o sistema está considerando a filial corrente no contexto, porém a tela do período foi aberta através de outro contexto.

**03. SOLUÇÃO**

O módulo fiscal tem o contexto por filial e neste caso ao alterar a filial corrente o usuário precisa encerrar as telas abertas no contexto anterior.   
  
Foi modificado o processo de alteração de contexto para não permitir alterar a Coligada, a Filial e o Exercícios Fiscal com telas do fiscal em aberto.   
Será exibido uma mensagem ao usuário solicitando encerramento das telas que poderá ser de forma manual ou automática.

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
