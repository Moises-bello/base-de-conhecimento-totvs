---
content_hash: caecb06558bb714b9de44dbd36a66a3679cdd6741443fd15eb32a26fea47a8c2
fetched_at: '2026-06-29T00:10:27.122344+00:00'
page_id: '516223263'
product: rm
source: tdn-rm
title: DT Tela de Carteira Digital
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Tela+de+Carteira+Digital
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | eduConnect |
| Função: | Carteira Digital |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-62](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-62 "Tela exibição da carteira Digital e opção de pagamento no eduCONNECT ") |

## **02. SITUAÇÃO/REQUISITO**

Exibir a listagem de cartões de crédito e débito do responsável pelo pagamento (aluno, responsável financeiro, responsável acadêmico, pai ou mãe) quando o usuário selecionar algum boleto para pagamento.

Opção de inclusão de um cartão na carteira do aluno.

Opção de pagamento através do cartão selecionado.

Opção de pagamento através de um outro cartão.

## **03. SOLUÇÃO**

Criação da tela de listagem da carteira digital do usuário logado.

Serão exibidos os cartões de acordo com a bandeira (Visa, Mastercard, American Express, Dinners, JCB). Qualquer outra bandeira será exibida com a cor do tema parametrizado pelo usuário e imagem de um chip conforme exemplo abaixo:

Após salvar o cartão o sistema volta para a tela de carteira digital.

A tela será exibida após o usuário selecionar um boleto para pagamento, visualizar os valores do boleto e selecionar a opção de pagamento por "Cartão".

Possui três funcionalidades:

1. **Inclusão de cartão**: Poderá ser incluído um cartão a partir do clique no cartão com um "+" no centro da imagem do cartão ou clicando no ícone abaixo do carrossel de imagens de cartões.
2. **Pagamento com o cartão selecionado**: Poderá ser feito um pagamento com o cartão selecionado. Botão somente ficará habilitado se o cartão selecionado não for o cartão com o ícone de "+". Nesse caso, após clicar em "Pagar", o pagamento será feito imediatamente caso seja autorizado.
3. **Pagamento com outro cartão**: Poderá ser feito um pagamento com um outro cartão sem ser cartão da carteira. Nesse caso o usuário deverá preencher os dados do cartão bem alguns dados pessoais como seu endereço, email, telefone, dentre outros.

Mais detalhes, consulte o documento de referência: [10.2 Listagem da Carteira Digital](https://tdn.totvs.com/display/LRM/10.2+-+Listagem+da+Carteira+Digital)

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
