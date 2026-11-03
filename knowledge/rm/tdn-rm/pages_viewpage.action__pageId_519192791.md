---
content_hash: 084782292c33a2d0c30827c8eb2c57f32ae8f469d083fa0afba6b9e6d27e82ee
fetched_at: '2026-06-29T00:10:30.081122+00:00'
page_id: '519192791'
product: rm
source: tdn-rm
title: 5442396 FISCAL01-11119 DT - Emissão da NFS-e do município de Araxá - MG
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519192791
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Emissão da NFS-e através do TSS |
| Ticket: | 5442396 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11119 |

## **02. SITUAÇÃO/REQUISITO**

Liberar o município de Araxá - MG para emissão de NFS-e

## **03. SOLUÇÃO**

* Foi realizado a liberação do município Araxá - MG para emissão da NFS-e através do TSS utilizando o [modelo único do XML do TSS](http://tdn.totvs.com/pages/releaseview.action?pageId=243641191)

Para o município em questão existe uma particularidade do envio da tag **tsCodVer** que é exigida pela prefeitura. 

É necessário a criação de um campo complementar no **movimento** conforme especificações abaixo:

Nome da Coluna: **CODVERIFICACAO**

Tipo: **Alfanumérico**

Tipo de Texto: **Texto**

Tamanho: **10 (Tamanho do campo no layout da prefeitura)**

Após a criação do campo é necessário torna-lo visível nos parâmetros do tipo de movimento:

Ambiente | Parâmetros | Gestão de Estoque , Compras e Faturamento | Parametrizar o tipo de movimento.

Preencher o mesmo no movimento:

Exemplo:

Passo 01, Passo 02, Passo 03, Passo 04passo1,passo2yespasso1

Para utilização do processo é necessário seguir as parametrizações da FAQ: [NFS-e - Parametrizar o sistema para emissão de NFS-e](http://tdn.totvs.com/pages/viewpage.action?pageId=66126311)

nopasso2

Para atualizar a lista de municípios homologados na base é necessário executar o processo de Atualização de Municípios Homologados: [Link da FAQ](http://tdn.totvs.com/pages/releaseview.action?pageId=135496124)

## **04. DEMAIS INFORMAÇÕES**

Este município permite os seguintes processos:

* Enviar: Sim
* Consultar: Sim
* Substituir: Não
* Cancelar: Sim
* Validar Schema: Não
* Gerar Cnae: Sim

**É aconselhável atualizar o TSS com a ultima versão disponível no portalIMPORTANTE!**

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
