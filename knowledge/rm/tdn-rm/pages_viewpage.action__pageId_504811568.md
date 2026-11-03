---
content_hash: 1e777927b9e4ef48a51ea81c3d701d69376eba972c7a9f2947249176412c165c
fetched_at: '2026-06-29T00:10:25.409194+00:00'
page_id: '504811568'
product: rm
source: tdn-rm
title: FISCAL01-10224 DT - SPED - Alteração do menu do SPED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=504811568
version: 1
---

**01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10224 |

**02. SITUAÇÃO/REQUISITO**

Alterar o menu SPED na MDI .Net

O menu atual do SPED Fiscal deve passar a ser um submenu do menu principal "SPED".

**03. SOLUÇÃO**

Foi ajustado o Menu SPED adicionando um "dropdownlist" com a criação de um Submenu com o nome de SPED Fiscal.

Antes do ajuste:

**Menu:**

**Permissões:**

Após o ajuste:

**Menu:**

**Permissões:**

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
