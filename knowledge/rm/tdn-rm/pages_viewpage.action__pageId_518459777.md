---
content_hash: f017190c749a76293b79dcb1455dee93b6746d45ccbe9cee2f342bf0bbfb9fd6
fetched_at: '2026-06-29T00:10:29.609845+00:00'
page_id: '518459777'
product: rm
source: tdn-rm
title: Lançamento Base de Rateio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518459777
version: 2
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela inicial**
   1. **Outras Ações / Ações relacionadas**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A base de rateio consiste em lançamentos dos critérios de rateio daquele centro de custo com a sua distribuição, ou seja, qual o critério e os centros de custos onde foram executados, por exemplo, para um critério de rateio Horas de Manutenção executado pelo centro de custo Manutenção será informado total de horas e o seu período e em seguida serão informados quais os centros de custos aos quais essas horas foram distribuídas.

## **02. EXEMPLO DE UTILIZAÇÃO**

Gestão de custos > Lançamentos > Base de rateio

## **03. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão de um novo cadastro da base de rateio | 1. Para incluir um novo lançamento de base de rateio manualmente clique no botão Incluir (Página em branco) na barra de ferramentas da tela. 2. No campo Período informe no formato ano/mês (AAAA/MM) o período correspondente à base de rateio que está sendo lançada. Este campo é de preenchimento obrigatório. 3. O campo Tipo Lançamento é preenchido pelo sistema com as opções Digitado ou Automático, onde:     1. Digitado: Inclusão de forma manual de dados pela digitação.    2. Automático: Inclusão automática de dados realizada por meio dos esquemas de apuração. 4. O campo Esquema é preenchido pelo sistema, se a inclusão do lançamento da base de rateio for por meio automático, com o código do esquema de apuração usado na importação dos dados. 5. No campo Código Critério Rateio clique em 3P ‘’Reticências” para selecionar uma das opções disponíveis, ou informar manualmente, não sendo necessário realizar a busca pelo intermédio do botão, se souber o código ou a descrição do critério de rateio que será usado para distribuir os valores aos centros de custo associados. Este campo é de preenchimento obrigatório.     1. Clicando no botão 3P ‘’Reticências” a tela abaixo será aberta para vincular um critério de rateio a um lançamento de base de rateio. É possível pesquisar os critérios de rateio já cadastrados filtrando os registros pelos campos que compõe esse cadastro.    2. Dê um duplo clique no critério de rateio desejado para selecioná-lo, ou também é possível cadastrar um novo critério de rateio clicando em Incluir (Página em branco). 6. No campo Total Base de Rateio informe o valor que será rateado pelo critério de rateio selecionado ao(s) centro(s) de custo. O campo ao lado desse é preenchido pelo sistema com a unidade de rateio correspondente ao critério de rateio selecionado para realizar a base de rateio que está sendo lançada. Este campo é de preenchimento obrigatório. 7. Clique em OK para confirmar a gravação. |

## **04. TABELAS UTILIZADAS**

* Passo a passo com as telas
* Tela do cadastro da base centro de rateio

* Tela critérios de rateio

**IMPORTANTE**

---

Para os lançamentos de base de rateio efetuados por meio dos esquemas de apuração, não é possível alterar seus dados ou excluir seus registros. Os mesmos precisam ser alterados na fonte de extração dos dados, e importados novamente para o sistema TOTVS Gestão de Custos.

Apenas Critérios de Rateio definidos como Variável por Período podem ser informados nos lançamentos de base de rateio, em cada período, pois estes são aqueles em que os valores base variam conforme cada período de apuração.

* #### Base de Rateio Detalhe

Para cada lançamento de Base de Rateio efetuado é preciso associar um ou mais Centros de Custos para absorver o valor de rateio informado através do critério de rateio definido. A partir da tela de cadastro Base de Rateio acesse Anexos/Base de Rateio Detalhe.

Ao acessar a tela serão exibidas as colunas de dados:

* Código Centro Custo.
* Centro de Custo.
* Quantidade Base Rateio.

Se houver centros de custos atribuídos às bases de rateio eles serão listados em uma grid onde cada linha representa um determinado registro. Verifique abaixo imagem da tela que exibe a relação de Lançamentos em Base de Rateio Detalhe efetuados.

Para consultar em tela os lançamentos efetuados via esquema de apuração, execute um duplo clique no registro desejado.

Verifique imagem da tela que permite efetuar o cadastro da Base de Rateio Detalhe.

* **Cadastrando Centro de Custo a Base de Rateio Detalhe**

1. Clique em Incluir (Página em branco).
2. 1. Clicando no botão 3P “Reticências” a tela abaixo será aberta para atribuir um centro de custo a uma base de rateio. É possível pesquisar os centros de custos já cadastrados filtrando os registros pelos campos que compõe esse cadastro.
   2. Dê um duplo clique no centro de custo desejado para selecioná-lo, ou também é possível cadastrar um novo centro de custo clicando em Incluir (Página em branco).

      No campo Código Centro Custo clique em 3P “Reticências” para selecionar uma das opções disponíveis, ou informar manualmente, não sendo necessário realizar a busca por intermédio do botão, se souber o código ou a descrição do(s) centro(s) de custo desejado(s) para absorver o valor do rateio da base de rateio através do critério de rateio definido. Este campo é de preenchimento obrigatório.
3. No campo Quantidade Base Rateio informe a quantidade que o Centro de Custo absorverá do valor de rateio. Este campo é de preenchimento obrigatório.
4. Clique em OK.

**IMPORTANTE**

---

Para as associações dos Centros de Custo à Base de Rateio efetuadas por meio dos esquemas de apuração, não é possível alterar seus dados ou excluir seus registros. As mesmas precisam ser alteradas na fonte de extração dos dados, e importadas novamente para o sistema Gestão de Custo.

Pode-se associar um ou mais Centros de Custo à Base de Rateio, desde que os valores do campo Quantidade Base Rateio informado para cada Centro de Custo, quando somados não ultrapassem o valor estipulado no campo Total Base de Rateio da tela de cadastro Base de Rateio. Se o valor total estipulado para a base de rateio for ultrapassado, o seguinte erro será informado em tela, e será preciso corrigir a quantidade base de rateio informada para o centro de custo, ou redefinir o total da base de rateio, respeitando o tipo de lançamento realizado para fazer a alteração.
