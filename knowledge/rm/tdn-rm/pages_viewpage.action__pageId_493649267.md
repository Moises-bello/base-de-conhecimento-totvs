---
content_hash: 8bf0e1df2f6ac632e21ca883d4f86b73b7292c0e8da2c91968c1fe6cd8e1a2a5
fetched_at: '2026-06-29T00:10:21.845258+00:00'
page_id: '493649267'
product: rm
source: tdn-rm
title: '5617592 - FISCAL01-9233 -  NFS-e - Boa Vista/RR: O país Brasil não pode ser
  selecionado quando a natureza da operação (Exigibilidade do ISS) for exportação'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493649267
version: 1
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Fiscal |
| Ticket: | 5617592 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FISCAL01-9233](http://jiraproducao.totvs.com.br/browse/FISCAL01-9233) |

**02. SITUAÇÃO/REQUISITO**

Quando é emitido uma NFS-e (Boa Vista/RR), onde o tomador é de nacionalidade Estrangeira e o endereço é brasileiro ocorre a seguinte rejeição:

25 - O RPS número 547 e série 1 foi processado com seguinte erro: Erro na gravação do registro. O país Brasil não pode ser selecionado quando a natureza da operação (Exigibilidade do ISS) for exportação.

Este problema ocorre , pois estamos enviando os dados do endereço como estrangeiro, porém o tomador reside no Brasil e possui CPF.

**03. SOLUÇÃO**

Foi efetuado uma tratativa quando o tomador residir no Brasil, a tag de estrangeiro seja enviada como não (Entendimento alinhado com a equipe de TSS ). Essa tratativa foi efetuada de forma pontual para o município de Boa Vista.

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
