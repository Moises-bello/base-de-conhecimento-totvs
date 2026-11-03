---
content_hash: 9e475bb012fdf52174015606d3c0d00c577f39011359a73f2df825ced95ef1ac
fetched_at: '2026-06-29T00:09:17.729375+00:00'
page_id: '421388632'
product: rm
source: tdn-rm
title: FIN - Fórmula Visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388632
version: 11
---

O recurso de Fórmula Visual poderá ser usado para criar procedimentos customizados no aplicativo TOTVS Gestão Financeira.

Estão disponíveis na ferramenta as seguintes Atividades:

**Lançamento Financeiro**

Incluir Lançamento Financeiro

* Incluir Contabilização
* Incluir Rateio de Contabilização
* Incluir Rateio por Centro de Custo
* Incluir Rateio por Departamento
* Incluir Retenções do Lançamento
* Incluir Valores da Integração
* Salvar Inclusão de Lançamento

As atividades Incluir Lançamento Financeiro e Salvar Inclusão de Lançamento são complementares, devendo estar em uma mesma fórmula visual. Elas também devem estar em qualquer fórmula visual para as demais atividades de inclusão de detalhes.

Nestas atividades "detalhe", a atividade Incluir Lançamento Financeiro deve ser selecionada na propriedade "Lançamento Referenciado".

Alterar Lançamento Financeiro

* Alterar Contabilização (Inclusão e Baixa)
* Alterar Rateio de Contabilização
* Alterar Rateio por Centro de Custo
* Alterar Rateio por Departamento
* Alterar Retenções do Lançamento
* Salvar Alteração de Lançamento

As atividades Alterar Lançamento Financeiro e Salvar Alteração de Lançamento são complementares, devendo estar em uma mesma fórmula visual. Elas também devem estar em qualquer fórmula visual para as demais atividades de alteração de detalhes.

Nestas atividades "detalhe", a atividade Alterar Lançamento Financeiro deve ser selecionada na propriedade "Lançamento Referenciado".

Cancelar Lançamento

Excluir Lançamento

Gerar Código de Barras do Lançamento

Gerar Nosso Numero do Lançamento

**Extrato de Caixa**

Incluir Extrato de Caixa

* Incluir Contabilização do Extrato
* Salvar Inclusão de Extrato

Alterar Extrato de Caixa

* Alterar Contabilização do Extrato
* Salvar Alteração de Extrato

Cancelar Extrato

Excluir Extrato

Compensar Extrato

Conciliar Extrato

**Fatura**

As três atividades a seguir devem ser utilizadas de forma complementar, em uma mesma fórmula visual.

* Incluir Fatura: onde são preenchidos os parâmetros de inclusão
* Incluir Lançamento na Fatura: onde são preenchidas as informações do lançamento a ser faturado
* Salvar Inclusão de Fatura: onde as informações referenciadas são enviadas ao banco de dados.

Cancelar Fatura

Excluir Fatura

**Cliente/Fornecedor**

Incluir Cliente/Fornecedor

* Incluir Contato do Cliente/Fornecedor
* Incluir Dados Bancários do Cliente/Fornecedor

Alterar Cliente/Fornecedor

* Alterar Contato do Cliente/Fornecedor
* Alterar Dados Bancários do Cliente/Fornecedor
* Alterar Defaults do Cliente/Fornecedor

**Exemplo de utilização de Fórmulas Visuais ao salvar a inclusão de Extrato**

Criar uma Fórmula Visual no TOTVS Gestão Financeira que bloqueie a gravação do extrato, caso o valor da conta caixa esteja menor que o fluxo de caixa definido pela diretoria da empresa.

Observação: atenção ao preenchimento do contexto corrente para os respectivos campos de entrada do serviço, isso não é feito de forma automática. Exemplo, para a inclusão do Cliente/Fornecedor, a "Coligada Corrente" deve ser amarrada com o valor do contexto.
