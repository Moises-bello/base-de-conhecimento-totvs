---
content_hash: 12bb1d0f8857bb28a5043edfc8233ea443d616ba2e313e2566283b8dc3a7d23e
fetched_at: '2026-06-29T00:10:25.352992+00:00'
page_id: '502839700'
product: rm
source: tdn-rm
title: FISCAL01-10134 - Lançamento Fiscal - Coleta/Entrega Não Afeta Seleção de CFOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502839700
version: 7
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10134 |

**02. SITUAÇÃO/REQUISITO**

Criar no Lançamento Fiscal (Dados de Transporte) um campo para que o usuário defina se as informações da Coleta/Entrega irão afetar ou não a seleção do CFOP.

**03. SOLUÇÃO**

Foi criado o campo **Coleta/Entrega Não Afeta a Seleção de CFOP** na pasta Coleta e Entrega do Lançamento Fiscal para Informar se os dados de Coleta/Entrega não devem afetar a regra de seleção de CFOP

#### **04. DEMAIS INFORMAÇÕES**

* No módulo TOTVS Gestão de Estoque, Compras e Faturamento o Tipo de Movimento possui três opções: Não usa, Usa, Usa sem afetar a seleção do CFOP. No caso do Lançamento, como os campos sempre são apresentados e sempre afetam a seleção do CFOP, é necessário apenas um campo para "desativar" esse comportamento. Ou seja, afetar ou não a seleção do CFOP.
* No processo de escrituração caso o parâmetro ""**Usa sem afetar a seleção do CFOP**" estiver selecionado, no processo de escrituração o sistema irá preencher o campo **"Coleta/Entrega Não Afeta a Seleção de CFOP".**
* No Serviço de seleção de Natureza o sistema irá se comportar para buscar as Naturezas de acordo como o preenchimento da Aba Coleta/Entrega e o novo campo criado.

**Este campo está disponível a partir da versão 12.1.26 de forma nativa e 12.1.23 mediante a execução dos scripts LI.2019.07\_03 e LI.2019.07\_04 através do "RM.Atualizador"IMPORTANTE!**

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
