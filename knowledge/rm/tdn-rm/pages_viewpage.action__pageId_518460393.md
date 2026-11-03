---
content_hash: 5af264ec0085a88bc876499ce487c11ec5b73dcf10711463cf844f4da99ccd2a
fetched_at: '2026-06-29T00:10:29.971905+00:00'
page_id: '518460393'
product: rm
source: tdn-rm
title: Lançamentos Conta de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518460393
version: 1
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela inicial**
   1. **Outras Ações / Ações relacionadas**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O lançamento de contas de custo possui quatro destinos, que serão seus agrupadores lógicos:

* Custos Diretos.
* Indiretos.
* Receitas.
* Deduções de Receitas.

Cada tipo de lançamento é responsável por realizar a composição em valores monetários das Contas de Custos com os Centros de Custos em que foram distribuídos, por exemplo, para uma conta de custo Salários do tipo Direto, a contabilização dos salários pagos será informada por meio de um lançamento, informando o código da conta de custo, valor, período e os custos distribuídos por centros de custo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Gestão de custos > Lançamentos > Conta de custo

## **03. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão | 1. Clique em Incluir (Página em branco) para incluir um novo lançamento em conta de custo manualmente. 2. No campo Período informe no formato ano/mês (AAAA/MM) o período correspondente à conta que está sendo lançada. Este campo é de preenchimento obrigatório. 3. O campo Tipo Lançamento é preenchido pelo sistema com as opções Digitado ou Automático:    1. Digitado: Inclusão de forma manual de dados pela digitação.    2. Automático: Inclusão automática de dados realizada por meio dos esquemas de apuração. 4. O campo Data de Lançamento é preenchido pelo sistema com a data e a hora, de acordo com a configuração do servidor da aplicação, correspondente ao lançamento da conta em custo no sistema. 5. O campo Esquema é preenchido pelo sistema, se a inclusão do lançamento da conta em custo for por meio automático, com o código do esquema de apuração usado na importação dos dados. 6. No campo Código Conta Custo clicando em 3P “Reticências” é possível selecionar uma das opções disponíveis, ou informar manualmente, não sendo necessário realizar a busca pelo intermédio do botão, se souber o código ou a descrição da conta de custo desejada. Este campo é de preenchimento obrigatório.     1. Clicando no botão 3P “Reticências” a tela abaixo será aberta para associar uma conta de custo ao lançamento. É possível pesquisar as contas de custo já cadastradas filtrando pelos campos que compõe esse cadastro.    2. Dê um duplo clique no registro da conta de custo desejado para selecioná-lo, ou também é possível cadastrar uma nova conta de custo clicando em Incluir. 7. O campo **Data do Documento** é opcional e referente à conta lançada. 8. O campo **Número do Documento** é opcional e referente à identificação da conta lançada. 9. Clique em **OK**. |

## **04. TABELAS UTILIZADAS**

---

**IMPORTANTE**

---

Para os lançamentos em conta de custo efetuados por meio dos esquemas de apuração, não é possível alterar seus dados ou excluir seus registros. Os mesmos precisam ser alterados na fonte de extração dos dados, e importados novamente para o sistema TOTVS Gestão de Custos.

* Passo a passo com as telas
* Tela do cadastro de  conta de custo

* Tela conta de custo

* #### Lançamento Custo Detalhe

Cada tipo de lançamento é responsável por realizar a composição em valores monetários das Contas de Custos com os Centros de Custos em que foram distribuídos. Para atribuir centros de custos para absorver as contas de custos lançadas, a partir da tela de cadastro Lançamento em Conta de Custo acesse a opção Anexos/Lançamento Custo Detalhe, como na imagem abaixo.

Ao acessar a tela serão exibidas as colunas de dados:

* Código Centro Custo.
* Centro de Custo.
* Valor Lançamento.
* Código do Cenário.

Se houver centros de custos atribuídos às contas de custos eles serão listados em uma grid onde cada linha representa um determinado registro. 

Para consultar em tela os lançamentos efetuados via esquema de apuração, execute um duplo clique no registro desejado.

Verifique imagem da tela que permite efetuar o Lançamento Custo Detalhe.

* **Cadastrando Lançamento Custo Detalhe**

1. Para atribuir centro(s) de custo para absorver o valor da conta de custo lançada clique em Incluir (Página em branco) na barra de ferramentas da tela.
2. No campo Código Centro Custo clique em 3P “Reticências” para selecionar uma das opções disponíveis, ou informar manualmente, não sendo necessário realizar a busca por intermédio do botão, se souber o código ou a descrição do(s) centro(s) de custo desejado(s) para absorver o valor da conta de custo lançada.

   1. Clicando no botão 3P “Reticências” a tela abaixo será aberta para atribuir um centro de custo a uma conta de custo. É possível pesquisar os centros de custos já cadastrados filtrando os registros pelos campos que compõe esse cadastro.
   2. Dê um duplo clique no centro de custo desejado para selecioná-lo, ou também é possível cadastrar um novo clicando em Incluir (Página em branco).

    Verifique abaixo a tela que permite vincular um Centro de Custo ao Lançamento Custo Detalhe.

     3.No campo Valor Lançamento informe o valor da conta de custo que será absorvido pelo centro de custo que está sendo atribuído. Este campo é de preenchimento obrigatório.

    4.No campo Código do Cenário clique em 3P “Reticências” é possível selecionar uma das opções disponíveis, ou informar manualmente, não sendo necessário realizar a busca por intermédio do botão, se souber o código ou a descrição do cenário desejado.

1. Clicando no botão 3P “Reticências” a tela abaixo será aberta para atribuir um cenário ao lançamento de custo detalhe. É possível pesquisar os cenários já cadastrados filtrando os registros pelos campos que compõe esse cadastro. Dê um duplo clique no cenário desejado para selecioná-lo.5.Clique em OK.

Verifique abaixo a tela que permite vincular um Cenário ao Lançamento Custo Detalhe.

**IMPORTANTE**

---

Para os lançamentos em conta de custo detalhe efetuados por meio dos esquemas de apuração, não é possível alterar seus dados ou excluir seus registros. Os mesmos precisam ser alterados na fonte de extração dos dados, e importados novamente para o sistema TOTVS Gestão de Custos.
