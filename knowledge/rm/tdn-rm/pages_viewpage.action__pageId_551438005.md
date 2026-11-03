---
content_hash: 3d9e6762f812b7e2be7aed316174cc964d62c77d25966305c03a8fea7da8dd0f
fetched_at: '2026-06-29T00:10:43.974309+00:00'
page_id: '551438005'
product: rm
source: tdn-rm
title: ADRC-ST - Bloco 0 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=551438005
version: 23
---

Este Bloco é composto pelos registros:

BLOCO0left0000Registro 0000

**Registro de abertura e identificação do contribuinte**

Identifica o período de apuração e o contribuinte substituído.

As informações para geração desse registro provém do Cadastro de Filial e da própria tela de geração da rotina.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| A01 | REG | Registro 0000 | Texto fixo contendo 0000 |
| A02 | COD\_VERSAO | Código da versão do leiaute do arquivo | Versão atual desse Manual é 100 |
| A03 | MES\_ANO | Mês e Ano de referência do arquivo - Formato: MMAAAA | Mês e ano do período seleciona para geração do arquivo |
| A04 | CNPJ | CNPJ do estabelecimento declarante | CNPJ da Filial selecionada para geração do arquivo  GFILIAL.CGC |
| A05 | IE | Inscrição Estadual do estabelecimento | Inscrição Estadual da Filial selecionada para geração do arquivo  GFILIAL.INSCRICAOESTADUAL |
| A06 | NOME | Nome empresarial | Razão Social da Filial selecionada para geração do arquivo  GFILIAL.NOME |
| A07 | CD\_FIN | Código da finalidade do arquivo:  0 – Arquivo original 1 – Arquivo substituto | Opção a ser selecionada para geração do arquivo |
| A08 | N\_REG\_ESPECIAL | Número do regime especial | Opção a ser informada na tela de geração do arquivo |
| A09 | CNPJ\_CD | Informar o CNPJ do estabelecimento que centraliza as aquisições dos produtos sujeitos à substituição tributária | Neste campo deve ser informado o CNPJ do Estabelecimento que Centraliza as aquisições dos Produtos Sujeitos a Substituição Tributária e caso não existir Centro de Distribuição, **deve informar neste campo o próprio CNPJ**.  Atualmente não temos cadastro para buscar o Centro de Distribuição vinculado ao lançamento, sendo assim está sendo preenchido com os dados da Filial. |
| A10 | IE\_CD | Informar a Inscrição Estadual do estabelecimento que centraliza as aquisições dos produtos sujeitos à substituição tributária | Neste campo deve ser informado a Inscrição Estadual do Estabelecimento que Centraliza as aquisições dos Produtos Sujeitos a Substituição Tributária e caso não existir Centro de Distribuição, **deve informar neste campo a própria Instrução Estadual.**  Atualmente não temos cadastro para buscar o Centro de Distribuição vinculado ao lançamento, sendo assim está sendo preenchido com os dados da Filial. |
| A11 | OPÇÃO\_R1200 | Código para reaver ou recolher o imposto nas saídas para consumidor final (R1200)  0 – Recuperação em conta gráfica 1 – Ressarcimento para fornecedor 2 – Complementação do Imposto | Opção a ser informada na tela de geração do arquivo.  Se não tiver registro 1200 no arquivo o campo será gerado em branco, conforme as regras de validação do Manual. |
| A12 | OPÇÃO\_R1300 | Código para reaver o imposto nas saídas interestaduais (R1300)  0 – Recuperação em conta gráfica 1 – Ressarcimento para fornecedor | Opção a ser informada na tela de geração do arquivo.  Se não tiver registro 1300 no arquivo o campo será gerado em branco, conforme as regras de validação do Manual. |
| A13 | OPÇÃO\_R1400 | Código para reaver o imposto nas saídas de que trata o art.119 do Anexo IX do RICMS/17 (R1400)  0 – Recuperação em conta gráfica 1 – Ressarcimento para fornecedor | Opção a ser informada na tela de geração do arquivo.  Se não tiver registro 1400 no arquivo o campo será gerado em branco, conforme as regras de validação do Manual. |
| A14 | OPÇÃO\_R1500 | Código para reaver o imposto nas saídas destinadas ao Simples Nacional (R1500)  0 – Recuperação em conta gráfica 1 – Ressarcimento para fornecedor | Opção a ser informada na tela de geração do arquivo.  Se não tiver registro 1500 no arquivo o campo será gerado em branco, conforme as regras de validação do Manual. |

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
