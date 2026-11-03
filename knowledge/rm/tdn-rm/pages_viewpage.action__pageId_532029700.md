---
content_hash: dfb0948c570b0a6bf0df39fa50f19fc82600718e44c2667c4641eba6c66a08c5
fetched_at: '2026-06-29T00:10:36.267833+00:00'
page_id: '532029700'
product: rm
source: tdn-rm
title: 7857917 FISCAL01-12044 DT - Obrigatoriedade de geração do Registro 0210 - Bloco
  K
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532029700
version: 1
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12044 |

**02. SITUAÇÃO/REQUISITO**

A geração do registro 0210 do SPED Fiscal não é obrigatória. Essa obrigatoriedade fica a cargo de cada UF. Usuário deseja ter a possibilidade de não gerar este registro.

**03. SOLUÇÃO**

        Possibilitar ao usuário a escolha para gerar ou não o registro 0210 do SPED Fiscal. Para tanto foi criado um Flag na tela de geração do SPED Fiscal. Quando este Flag for desmarcado, o registro não será gerado. 

O campo será visível somente se estiver marcada a geração do Bloco K (Gerar Bloco K diferente de **Não Gerar**) e será apresentado por default como Marcado, para mantermos o comportamento atual.

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
