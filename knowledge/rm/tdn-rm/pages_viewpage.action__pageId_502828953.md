---
content_hash: c8c6b39db58b70174023dd908f5ef314571618badde3a9b35bf5b05a8dc29606
fetched_at: '2026-06-29T00:10:25.338628+00:00'
page_id: '502828953'
product: rm
source: tdn-rm
title: FISCAL01-10258 - NFS-e - Parâmetro CNPJ para Assinatura Lote NFS-e.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502828953
version: 1
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Fiscal |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10258 |

**02. SITUAÇÃO/REQUISITO**

As NFS-e são transmitidas em lote para as prefeituras. Cada NFS-e tem sua assinatura digital individual e o lote de NFS-e também tem sua própria assinatura digital (mesmo se o lote tiver apenas uma nota).

O lote de notas pode ser assinado com o CNPJ da Filial Matriz ou CNPJ do certificado digital ou CNPJ da filial remetente ou não ter nenhum CNPJ no lote, esta regra é de cada prefeitura e layout da NFS-e.

Por este motivo foi necessário a criação de um parâmetro de NFS-e para que o usuário informe qual o CNPJ será utilizado para assinatura do lote de NFS-e.

**03. SOLUÇÃO**

Foi criado o parâmetro "CNPJ Assinatura Lote NFS-e", o qual pode ser acessado através do caminho Ambiente | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Filial desejada | Ambiente NF-e:

Este CNPJ será utilizado na assinatura do Lote da NFS-e. O campo deverá ser preenchido se houver necessidade definida pela prefeitura.

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
