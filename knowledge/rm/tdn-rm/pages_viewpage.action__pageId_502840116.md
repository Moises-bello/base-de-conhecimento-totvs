---
content_hash: f940104d1d05769120cf56ace15fb3463eb92723d62abea2243c5a31202e2314
fetched_at: '2026-06-29T00:10:25.356181+00:00'
page_id: '502840116'
product: rm
source: tdn-rm
title: 6381685 FISCAL01-10166 NF-e 4.0 - Responsável Técnico no envio com Totvs Colaboração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502840116
version: 1
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Fiscal |
| Ticket: | 6381685 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10166 |

**02. SITUAÇÃO/REQUISITO**

O cliente utiliza Totvs Colaboração 2.0 para emissão de nf-e, o mesmo identificou que a Neogrid está rejeitando a Nf-e: "Rejeição Neogrid: O envio do grupo de informações do Resp. Técnico é de responsabilidade da Neogrid. Resp. Técnico é a empresa desenvolvedora responsável tecnicamente pelo sistema de emissão de NF-e/NFC-e utilizado pelo emitente (NT 2018.005).”

O XML gerado pelo RM, preenche as informações do responsável técnico. Em contato com o suporte da Neogrid os mesmos informaram que a tag em questão deverá ser gerada pela Neogrid.

**03. SOLUÇÃO**

Ajuste no envio de NF-e no Totvs Colaboração para que não seja enviado os dados do responsável técnico. Este ajuste foi necessário devido a neogrid ser a responsável pelo envio destes dados.

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
