---
content_hash: 6c06b668fbcfcc6d60dc4f4ee3a7c26d0a8d43440f396f07bc0746443fc9602f
fetched_at: '2026-06-29T00:10:50.857825+00:00'
page_id: '563944212'
product: rm
source: tdn-rm
title: DT - Inclusão de Borderô de Pagamentos em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563944212
version: 19
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Totvs Gestão Financeira |
| Função: | Borderô de Pagamentos |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FINANCEIRO01-16277, FINANCEIRO01-16430, FINANCEIRO01-16509 |

## **02. SITUAÇÃO/REQUISITO**

Facilitar a inclusão de Borderô de pagamentos em situações que temos várias coligadas cadastradas no sistema. Desta forma, o usuário não irá precisar ir em cada coligada para gerar o borderô de pagamento para os lançamentos a pagar.

## **03. SOLUÇÃO**

Criação do processo em lote de inclusão de Borderô de Pagamentos com a utilização de um filtro genérico juntamente com o banco vinculado à conta caixa, que irá permitir ao usuário incluir o borderô de pagamentos para cada coligada e convênio presente nos lançamentos a pagar selecionados. O processo está disponível no menu Movimentações Bancárias → Integração Bancária → Processos em Lote → Borderô de Pagamentos

No campo "**Banco**" o usuário seleciona o banco cadastrado nas contas caixas presentes nos lançamentos a pagar. Vale ressaltar que a conta caixa e o convênio devem está cadastrados previamente no lançamento a pagar.

No campo "**Filtro genérico**" o usuário irá selecionar o filtro desejado para retornar os lançamentos a pagar para a inclusão dos borderôs de pagamentos por coligada e convênio.

É necessário dar permissão ao perfil do usuário para acessar o menu Movimentações Bancárias → Integração Bancária → Processos em Lote → Borderô de Pagamentos

A autorização de Borderô de Pagamentos em lote será realizada pelos campos "**Autorização**" e "**Data de Validade**" presente na tela do processo **somente** quando o usuário tiver **permissão** **de acesso** ao processo de "**Autorização de Borderô de Pagamentos**" na coligada logada.

ATENÇÃO

Na execução do processo de Inclusão de Borderô de Pagamento em Lote quando o campo "Autorização" estiver marcado o sistema irá verificar se o usuário de autorização, usuário logado, tem permissão em todas as coligadas pertencentes ao lançamentos retornados pelo filtro genérico informado na tela do processo. Caso não tiver o sistema irá informar quando coligada do usuário não tem permissão ao processo de "Autorização de Borderô de Pagamentos".

## **04. DEMAIS INFORMAÇÕES**

**Vale ressaltar que o filtro genérico deve considerar os lançamentos a pagar em aberto ou parcialmente baixado, não pode está faturado, não ter cheque emitido, não está bloqueado, o cliente/fornecedor está associado ao dados bancários, a moeda deve ser real, a forma de pagamento não pode ser cartão de crédito, não pode ser de previsão, não ter baixa pendente, o movimento associado não pode está bloqueado, não pode está vinculado em outro borderô de pagamento, não pode ser lançamento de repasse, ter dados bancários de pagamento informado.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**


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
