---
content_hash: b05b9225c292128671b78bcf9a54f9e8955ada95ffbd649834835bb5b665c439
fetched_at: '2026-06-29T00:10:30.922410+00:00'
page_id: '520121235'
product: rm
source: tdn-rm
title: 7132592 FISCAL01-11231 DT - NFS-e -  Gerar a tag valfoncartri quando houver
  dois serviços na nota fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520121235
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Envio de NFS-e |
| Ticket: | 7132592 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11231 |

## **02. SITUAÇÃO/REQUISITO**

Ao emitir uma NFS-e para a prefeitura de São Paulo, a tag não está sendo gerada.

Quando a NFS-e contém 1 serviço a tag é gerada com a informação IBPT.

Se a NFS-e contém 2 itens a tag não é gerada.

## **03. SOLUÇÃO**

 Foi efetuado um ajuste para geração das tags abaixo no sistema quando possuir mais de um item no movimento. 

**<valcartri></valcartri>** → Será efetuado a soma do "Valor Total dos Tributos" de cada item:

**<valpercartri></valpercartri>** → Será considerado os dados do cadastro do produto | Anexos | Dados Fiscais Por UF | UF da Filial de emissão | Aba IBPT - Lei Transparência, somente do primeiro item do movimento.

**<valfoncartri></valfoncartri>** → Valor Fixo - **IBPT**

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
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
