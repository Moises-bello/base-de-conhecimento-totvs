---
content_hash: 3357f18d82ea52ab8702ec8e1d9d49a5475724f5afc84af63f28a5fb575d529a
fetched_at: '2026-06-29T00:10:16.522991+00:00'
page_id: '471939083'
product: rm
source: tdn-rm
title: FISCAL01-7864 DT Contas LALUR Parte B - Campo Código da Tabela Padrão RFB -
  Parte B
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=471939083
version: 3
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro de Contas da Parte B |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-7864 |

**02. SITUAÇÃO/REQUISITO**

No cadastro da Conta do Lalur Parte B (Obrigações Principais | Lalur Parte B  | Contas | Aba Tributos):

Criar o campo “Código da Tabela Padrão RFB - Parte B” que buscará os Códigos da tabela padrão importados no menu ECF - Tabela Dinâmica.

Só devem aparecer para seleção os Códigos associados ao Grupo "Lalur Parte B".

Este campo será utilizado na geração do campo 5- COD\_PB\_RFB do Registro M010.

**03. SOLUÇÃO**

Foi adicionado o campo "Código da Tabela Padrão RFB - Parte B" no cadastro dos tributos da conta da Parte B do LALUR

Serão exibidos somente os códigos referente ao M010

**Implementação realizada oficialmente na versão 12.1.25 e disponível nas versões 12.1.22 e superiores mediante a execução do script de marcação LI.2019.04\_01 IMPORTANTE!**

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
