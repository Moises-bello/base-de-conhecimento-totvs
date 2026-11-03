---
content_hash: 939bb68d27fb9d3206c4515c8b0263fd7e38324dd0dbea2fa6ed288a43f6ecbe
fetched_at: '2026-06-29T00:11:22.177105+00:00'
page_id: '700489729'
product: rm
source: tdn-rm
title: Paradigma - Mapeamento Campos
type: documentation
url: https://tdn.totvs.com/display/LRM/Paradigma+-+Mapeamento+Campos
version: 12
---

Este documento tem como objetivo demonstrar todas as informações enviadas para o Portal de Compras Paradigma, baseado nos serviços de webservice disponibilizados pelo parceiro.

Clique sobre a descrição das entidade abaixo, para ter acesso ao mapeamento de campos do RM que são enviados para o Paradigma.

| Entidade | Descrição | Fluxo de Dados | WebMethod(\*1) |
| --- | --- | --- | --- |
| Cadastro | [Coligada](https://tdn.totvs.com/display/LRM/Paradigma+-+Coligada) | RM → Paradigma | ProcessarEmpresa |
| Cadastro | [Filial](https://tdn.totvs.com/display/LRM/Paradigma+-+Filial) | RM → Paradigma | ProcessarEmpresa |
| Cadastro | [Unidade de Medida](https://tdn.totvs.com/display/LRM/Paradigma+-+Unidade+de+Medida) | RM → Paradigma | ProcessarUnidadeMedida |
| Cadastro | [Moeda](https://tdn.totvs.com/display/LRM/Paradigma+-+Moeda) | RM → Paradigma | ProcessarMoeda |
| Cadastro | [Condição de Pagamento](https://tdn.totvs.com/pages/viewpage.action?pageId=700490089) | RM → Paradigma | ProcessarCondicaoPagamento |
| Cadastro | [Centro de Custo](https://tdn.totvs.com/display/LRM/Paradigma+-+Centro+de+Custo) | RM → Paradigma | ProcessarCentroCusto |
| Cadastro | [Departmento](https://tdn.totvs.com/display/LRM/Paradigma+-+Departamento) | RM → Paradigma | ProcessarDepartamento |
| Cadastro | [Transportadora](https://tdn.totvs.com/display/LRM/Paradigma+-+Transportadora) | RM → Paradigma | ProcessarEmpresa |
| Cadastro | [Fornecedor](https://tdn.totvs.com/display/LRM/Paradigma+-+Fornecedor) | RM → Paradigma | ProcessarEmpresa |
| Cadastro | Consultar e Inserir no Backoffice, fornecedores inseridos no Paradigma **(\*2)** | RM → Paradigma | RetornarEmpresaVencedoraSemDePara |
| Cadastro | [Categoria de Produto](https://tdn.totvs.com/display/LRM/Paradigma+-+Categoria+do+Produto) | RM → Paradigma | ProcessarCategoriaProduto |
| Cadastro | [Produto](https://tdn.totvs.com/display/LRM/Paradigma+-+Produto) | RM → Paradigma | ProcessarProduto |
| Cadastro | [Produto x Fornecedor](https://tdn.totvs.com/display/LRM/Paradigma+-+Empresa+Produto) | RM → Paradigma | ProcessarEmpresaProduto |
| Cadastro | [Usuário](https://tdn.totvs.com/display/LRM/Paradigma+-+Usuario) | RM → Paradigma | ProcessarUsuario |
| Cadastro | Natureza de Operação (CFOP) | RM → Paradigma | ProcessarCfop |
| Processos | [Envio de requisição](https://tdn.totvs.com/pages/viewpage.action?pageId=700491669) | RM → Paradigma | ProcessarRequisicao |
| Processos | Cancelar requisição | RM → Paradigma | ProcessarRequisicaoCancelamento |
| Processos | Consultar requisições canceladas | RM → Paradigma | RetornarRequisicaoCancelamento |
| Processos | Consultar orçamentos vencedores | RM → Paradigma | RetornarCotacaoItem |
| Processos | [Envio de Pedido de Compra](https://tdn.totvs.com/display/LRM/Paradigma+-+Pedido) | RM → Paradigma | ProcessarPedido |
| Processos | Cancelamento de Pedido de Compra | RM → Paradigma | ProcessarPedidoCancelamento |
| Processos | Consultar aceite de pedido por fornecedor | RM → Paradigma | RetornarPedidoAceite |

**(\*1)** Nome dos métodos de webservice que foram disponibilizados pelo Paradigma

Exemplo de consumo: https://{domínio}/services/servicos/operacao?nomeServico=Empresa&nomeOperacao=ProcessarEmpresa

**(\*2)** Este consumo é executado automaticamente durante a execução do processo de Consultar orçamentos vencedores. O mesmo realiza o cadastro de fornecedores vencedores ganhadores no Backoffice, que foram cadastrados apenas no Paradigma.

Importante

Como a integração dos registros (exceto Fornecedor) não irá ocorrer no sentido Paradigma → RM, é **aconselhável** que os cadastros sincronizados sejam **bloqueados** no **Paradigma** para que não haja incompatibilidade nos dados.

Na concepção do projeto de integração, foram definidos que apenas os campos obrigatórios e necessários para identificação da entidade seriam integrados.

Solicitação de envio de novos campos, se caracteriza uma evolução da integração e devem ser solicitados via [Central Colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics), descrevendo o contexto da solicitação de acordo com a regra de negócio.

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
