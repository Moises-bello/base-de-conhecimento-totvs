---
content_hash: f7be6f797cd918248b0426e3bce694fec6ecc3d464b2eb4596f0dcfba742df99
fetched_at: '2026-06-29T00:09:29.382132+00:00'
page_id: '425441237'
product: rm
source: tdn-rm
title: 3718384 FISCAL01-6826 DT - NF-e Geração da Tag cEAnTrib
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425441237
version: 4
---

Tempo aproximado para leitura:**02 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Envio NF-e 4.0 |

**02. SITUAÇÃO/REQUISITO**

Gerar a tag <cEANTrib> com o código de barras informado para a unidade tributável do cadastro do produto.

**03. SOLUÇÃO**

Foi modificado o processo de montagem do XML da NF-e para utilizar o serviço do estoque na montagem da TAG cEANTrib. Este serviço irá retornar o código de barras da unidade tributável.

Caso a NF-e enviada seja de exportação ou remessa de exportação (CFOP's 1501, 2501, 5501, 5502, 5505 , 6501 , 6502 , 6504 e 6505) para geração da ceantrib, o ERP irá considerar o campo "Unidade Tributável no Comércio Exterior":

Obs:  O ERP irá considerar a unidade base que foi cadastrada na unidade de medida:

Exemplo do XML gerado:

Caso seja uma NF-e de emissão para envio no território Brasileiro e diferente das CFOP's indicadas acima, o ERP irá considerar o preenchimento do campo "Unidade Tributável":

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
