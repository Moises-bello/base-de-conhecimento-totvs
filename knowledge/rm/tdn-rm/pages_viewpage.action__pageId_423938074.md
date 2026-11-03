---
content_hash: df12fb3f9d2aaa52176cac239855c6439e7ef1c1f64a07b73fd05a831d48aa43
fetched_at: '2026-06-29T00:09:25.245006+00:00'
page_id: '423938074'
product: rm
source: tdn-rm
title: Manutenção de Contratos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938074
version: 42
---

A Gestão de Contratos pelo TOTVS Gestão de Estoques, Compras e Faturamento possibilita um controle total sobre todos os contratos, sejam eles: de fornecimento, aquisição de produtos e/ou serviços entre a empresa e terceiros ou arrendamento mercantil.

Os contratos podem ser do tipo formal ou informal, sendo possível utilizar no sistema o controle para contratos efetuados com fornecedores, contratos efetuados junto à cliente, bem como o controle do tipo "Ambas", no qual as situações de compra e venda podem ser utilizadas no mesmo contrato.

O sistema permite o controle e faturamento de diversos tipos de contratos de forma simples e eficiente.

A utilização desse controle poderá ser utilizada por empresas que periodicamente faturam para o mesmo cliente e/ou fornecedor, dependendo do tipo de contrato realizado, exemplos, comuns utilizados na gestão de contratos são as prestações de serviços como água, luz, telefonia, assinatura de jornais e revistas, prestação de serviços etc.

Através do módulo de Manutenção de Contratos é possível gerar diretamente as notas fiscais, ordens de compra ou qualquer outro documento necessário, reduzindo assim os prazos necessários para a execução dos pagamentos e recebimentos de sua empresa, além de permitir um controle eficiente entre as partes, empresa x fornecedor e empresa x cliente.

Antes de iniciar o uso do módulo de Manutenção de Contratos é importante que o sistema esteja devidamente parametrizado e as tabelas utilizadas na elaboração do contrato sejam cadastradas.

O acesso aos parâmetros do Contrato é feito pelo menu 04.05 – Contratos, bem como as Tabelas de Contrato relacionadas a este processo. [Link para acessar documentação dos Parâmetros do Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=423938209)

---

* **Inclusão de Contratos**

A inclusão de novos contratos é feita pelo pelo menu: "Contratos | Manutenção de Contratos", onde são exigidos informações obrigatórias para a inclusão como: Número do contrato, Data do contrato, Tipo de contrato, Natureza do contrato (Compra, Venda, Ambos ou Arrendamento Mercantil), Status do contrato, Cliente/Fornecedor do contrato.

Os demais campos não são essenciais para a inclusão de um contrato, mas, dependendo da parametrização feita, podem se tornar obrigatórios por fazerem parte de um controle da empresa.

* ***Dica***: em relação a Configurando e Edição do Contrato, na inclusão alguns campos (em negrito) são de preenchimento obrigatório.
  + Os demais campos, mesmo não sendo obrigatórios, podem ser definidos como tal, através do menu de contexto (Botão Direito do mouse), clicando-se no campo que se deseja tornar obrigatório e selecionado a opção: "Preenchimento Obrigatório".
  + Através do menu de contexto (Botão Direito do mouse), também é possível definir valores default para os campos do contrato ou dos itens de contrato. Para isso basta clicar com o botão direito do mouse em cima do campo e na opção "Valor Default" selecionar a opção "Usar como Default".

Tabelas \ FuncionáriosImportante

Recurso disponível a partir da release 12.1.2306

Será possível parametrizar até quatro funcionários por Natureza do Contrato, onde poderemos nomeá-los conforme a necessidade do processo, ou seja, nos contratos de Compras\Arrendamento Mercantil será possível definir quatro nomes e para os contratos de Vendas outros quatro nomes diferentes, conforme os [parâmetros do contrato.](https://tdn.totvs.com/pages/viewpage.action?pageId=423938209)

Possibilitando uma melhor adequação dos cadastros com a regra de negócio.

Por padrão, caso não tenha sido feita nenhuma parametrização dos funcionários, serão exibidos dois campos de funcionários e comissões para preenchimento.

---

* **Inclusão de itens**

As informações definidas no contrato serão carregadas automaticamente para os respectivos campos dos itens do contrato, isso porque funcionam como um default, que será utilizado durante a inclusão dos seus itens.

A geração dos movimentos criados pelo processo de gestão de contratos se baseia nas informações definidas nos itens de contrato, ou seja, os dados definidos nos itens de contrato são os responsáveis pela geração dos movimentos.

É possível gerar um único movimento com todos os itens de contrato, ou então, um movimento para cada item de contrato. Isto é possível através da definição das regras de quebra informadas nos [parâmetros do Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=423938209). De forma semelhante também é possível gerar um único movimento para mais de um contrato com o mesmo Cliente/Fornecedor.

Será permitido selecionar no contrato e item de contrato apenas Natureza Fiscal Ativa.

Outras informações como por exemplo o tipo de faturamento dos itens, aditivos e reajuste de contratos serão explicados em detalhes em seções próprias, que podem ser acessadas através dos links abaixo em "*Informações Complementares"*.

Rateio \ Centro CustoImportante

Recurso disponível a partir da release 12.1.2306

Será possível informar um valor de referência que é utilizado apenas para o cálculo do percentual de rateio do centro de custo.

Caso a conversão de algum valor de referência para percentual gere dízima periódica, pode ser necessário a edição de um dos rateios, informando o percentual que falta para atingir os 100% do rateio.

### Ícones da visão do Contrato

Quando o contrato possui a **Data Fim** anterior à data atual do sistema, será exibido o ícone indicativo de **Vigência expirada** ao lado do contrato.

---

Um contrato é considerado **Ativo** quando a sua vigência é superior ou igual à data atual do sistema, e não se encontra em status de Suspenso ou Cancelado.

---

Para cancelar um contrato, é necessário executar o processo **Cancelar Contrato**.

---

 

Para alterar o status de um contrato para **Suspenso**, é necessário que o contrato esteja previamente com o status **Cancelado**. Em seguida, deve-se executar o processo **Desfazer Cancelamento de Contrato** e escolher a opção de **Novo Status** para **Suspenso**. Caso se opte por **Normal**, o contrato retornará ao status ativo.

### Repositório de Arquivos

A partir da versão 12.1.2402 a visão de Contratos passa a exibir a nova funcionalidade [Repositório de Arquivos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=784778828).

Maiores Informações

* [Como Fazer - Reajuste de Contrato no Faturamento](http://tdn.totvs.com/display/LRM/Reajuste+de+Contrato+por+Faturamento)
* [Como Fazer - Previsão Financeira do Contrato por Medição](http://tdn.totvs.com/pages/viewpage.action?pageId=4813050)
* [Como Fazer - Faturamento de Itens de Contrato sem Vigência Definida](http://tdn.totvs.com/pages/viewpage.action?pageId=4813162)
* [Como Fazer - RSS de Contratos a Vencer nos próximos 30 dias](http://tdn.totvs.com/pages/viewpage.action?pageId=4813114)
* Integração com TOTVS
