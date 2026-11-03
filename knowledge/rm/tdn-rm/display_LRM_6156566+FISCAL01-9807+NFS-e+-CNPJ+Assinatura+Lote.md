---
content_hash: 76ceb2fa366ecfd606535fb4a2f75fd7840b3c49218a87bc583e413c053ad048
fetched_at: '2026-06-29T00:10:22.737253+00:00'
page_id: '498720246'
product: rm
source: tdn-rm
title: 6156566 FISCAL01-9807 NFS-e -CNPJ Assinatura Lote
type: documentation
url: https://tdn.totvs.com/display/LRM/6156566+FISCAL01-9807+NFS-e+-CNPJ+Assinatura+Lote
version: 1
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | NFS-e Municipal |
| Ticket: | 6156566 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-9807 |

**02. SITUAÇÃO/REQUISITO**

Após a alteração do comportamento do sistema, na qual passou a validar a partir da versão 12.1.23, o CNPJ da Filial Matriz informada nos Parâmetros do RM Liber (Apuração de tributos / Filial Matriz), para assinar a nota. Porém o certificado do cliente não está vinculado a Filial Matriz e sim a Filial que está emitindo a nota. Desta forma ao enviar a NFS-e era apresentado a rejeição:

1428 - Certificado Digital utilizado na assinatura do lote deve ser o mesmo do remetente do lote.

**03. SOLUÇÃO**

Foi criado o parâmetro CNPJ Assinatura Lote NFS-e, o qual pode ser acessado através dos parâmetros fiscais por filial. Este CNPJ será utilizado na assinatura do Lote da NFS-e. O campo deverá ser preenchido se houver necessidade definida pela prefeitura. Para as versões de mercado quando não possuir o preenchimento deste novo campo, o sistema irá continuar com o comportamento anterior, assinar a NFS-e com o CNPJ da Filial Matriz.

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
