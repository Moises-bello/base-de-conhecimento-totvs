---
content_hash: 08731f093181cc0cc032236c1c07e2ea597a1d9d36599824b4468b10f76a813f
fetched_at: '2026-06-29T00:10:29.617755+00:00'
page_id: '518460184'
product: rm
source: tdn-rm
title: Lançamentos Produção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518460184
version: 1
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela inicial**
   1. **Outras Ações / Ações relacionadas**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A produção (menu **Lançamentos/Produção**) consiste em lançamentos das quantidades de produtos ou serviços realizados por um centro de custo produtivo ou auxiliar. Como, por exemplo, centro de custo Maternidade e suas diárias em um determinado período.

## **02. EXEMPLO DE UTILIZAÇÃO**

Gestão de custos > Lançamentos > Quantidades produzidas

## **03. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão de um novo cadastro de produção | 1. Clique em Incluir (Página em branco). 2. No campo Período informe no formato ano/mês (AAAA/MM) o período correspondente à produção que está sendo lançada. Este campo é de preenchimento obrigatório. 3. O campo Tipo Lançamento é preenchido pelo sistema com as opções Digitado ou Automático, onde:     1. Digitado: Inclusão de forma manual de dados pela digitação.    2. Automático: Inclusão automática de dados realizada por meio dos esquemas de apuração. 4. O campo Esquema é preenchido pelo sistema, se a inclusão do lançamento da base de rateio for por meio automático, com o código do esquema de apuração usado na importação dos dados.    1. Clicando no botão 3P “Reticências” a tela abaixo será aberta para atribuir um centro de custo ao lançamento da produção. É possível pesquisar os centros de custos já cadastrados filtrando os registros pelos campos que compõe esse cadastro.    2. Dê um duplo clique no centro de custo desejado para selecioná-lo, ou também é possível cadastrar um novo centro de custo clicando em Incluir (Página em branco).  No campo Código Centro Custo clique em 3P “Reticências” para selecionar uma das opções disponíveis, ou informar manualmente, não sendo necessário realizar a busca por intermédio do botão, se souber o código ou a descrição do centro de custo desejado. Este campo é de preenchimento obrigatório. 5. No campo Código Produto clique em 3P “Reticências” para selecionar uma das opções disponíveis, ou informar manualmente, não sendo necessário realizar a busca por intermédio do botão, se souber o código ou a descrição do produto desejado. Este campo é de preenchimento obrigatório.     1. Clicando no botão 3P “Reticências” a tela abaixo será aberta para atribuir um produto ao lançamento da produção. É possível pesquisar os produtos já cadastrados filtrando os registros pelos campos que compõe esse cadastro.    2. Dê um duplo clique no produto desejado para selecioná-lo, ou também é possível cadastrar um novo produto clicando em Incluir. 6. No campo Total Produzido informe o total da produção no período informado daquele produto para o centro de custo. Este campo é de preenchimento obrigatório. 7. Clique em OK. |

## **04. TABELAS UTILIZADAS**

* Passo a passo com as telas
* Tela do cadastro de quantidades produzidas

* Tela centro de custos

* Tela produto custo

**IMPORTANTE**

---

Para os lançamentos em produção efetuados por meio dos esquemas de apuração, não é possível alterar seus dados ou excluir seus registros. As mesmas precisam ser alteradas na fonte de extração dos dados, e importadas novamente para o sistema TOTVS Gestão de Custo.

Ao informar um Centro de Custo e um Produto no lançamento da Produção, os mesmos devem estar associados no cadastro de Produtos do Centro de Custo. Ao contrário, o seguinte erro será informado em tela ao tentar salvar o lançamento, e será preciso realizar a associação dos mesmos no cadastro de Produtos do Centro de Custo, ou corrigir o Produto e o Centro de Custo informados, respeitando o tipo de lançamento realizado para fazer a alteração.

* **Produção Detalhe**
* Para os lançamentos de produção para centros de custos auxiliares, é preciso associar centros de custos produtivos para absorver o valor total produzido. A partir da tela de lançamento em Produção acesse a opção Anexos/Produtos Detalhe, conforme a imagem abaixo.

Ao acessar a tela serão exibidas as colunas de dados:

* Código Centro Custo.
* Centro de Custo.
* Quantidade Produzida.
* Criado Por.
* Criado Em.
* Modificado Por.
* Modificado Em.

Se houver lançamentos efetuados na tela eles serão listados em uma grid onde cada linha representa um determinado registro. Verifique imagem abaixo a tela que exibe relação de cadastros de Produção Detalhe efetuados.

Para consultar em tela os lançamentos efetuados via esquema de apuração, execute um duplo clique no registro desejado.

* **Cadastrando Centro de Custo na Produção Detalhe**

1. Clique em Incluir (Página em branco).
2. No campo Código Centro Custo clique em 3P “Reticências” para selecionar uma das opções disponíveis, ou informar manualmente, não sendo necessário realizar a busca por intermédio do botão, se souber o código ou a descrição do centro de custo desejado. Este campo é de preenchimento obrigatório.

   1. Clicando no botão 3P “Reticências” a tela abaixo será aberta para atribuir um centro de custo ao lançamento da produção detalhe. É possível pesquisar os centros de custos já cadastrados filtrando os registros pelos campos que compõe esse cadastro.
   2. Dê um duplo clique no centro de custo desejado para selecioná-lo, ou também é possível cadastrar um novo centro de custo clicando no botão Incluir.

   3. No campo Quantidade Produzida informe a quantia do total produzido da produção que será atribuída ao centro de custo informado. Este campo é de preenchimento obrigatório.

   4.Clique em OK.

**IMPORTANTE**

---

Para os lançamentos em produção detalhe efetuados por meio dos esquemas de apuração, não é possível alterar seus dados ou excluir seus registros. As mesmas precisam ser alteradas na fonte de extração dos dados, e importadas novamente para o sistema TOTVS Gestão de Custo.

Pode se associar um ou mais Centros de Custo ao lançamento Produção Detalhe, desde que os valores do campo Quantidade Produzida informado para cada Centro de Custo, quando somados não ultrapassem o valor estipulado no campo Total Produzido da tela de lançamentos Produção. Se o valor total estipulado para a total produzido for ultrapassado, o seguinte erro será informado em tela, e será preciso corrigir a quantidade produzida informada para o centro de custo, ou redefinir o total produzido, respeitando o tipo de lançamento realizado para fazer a alteração.
