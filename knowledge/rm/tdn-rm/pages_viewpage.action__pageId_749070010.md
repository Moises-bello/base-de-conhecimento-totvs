---
content_hash: 13869826adaf540320014f99c602536c4e78ea1c5a6f713cafa0299d87f65c5f
fetched_at: '2026-06-29T00:11:32.796608+00:00'
page_id: '749070010'
product: rm
source: tdn-rm
title: Dimensões Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=749070010
version: 28
---

### Conceito

Dimensão contábil é um recurso utilizado pela contabilidade para fragmentar os registros contábeis de forma analítica utilizando elementos como departamentos, projetos, produtos, clientes, fornecedores, centros de custos, imóveis e outras.

### Objetivo da contabilidade por Dimensões Contábeis

Ao  realizar a contabilização utilizando os elementos mencionados, o gestor consegue ter uma visão mais detalhada do seu departamento ou empresa pelas diferentes dimensões e assim interpretar e analisar o impacto de cada dimensão nos dados financeiros e contábeis através de relatórios de demonstração de resultados, balancetes e balanço possibilitando ao gestor perceber as forças e fraquezas das diferentes dimensões por área da empresa e definindo assim as melhores estratégias para o desempenho da organização.

### Dimensões contábeis nos lançamentos contábeis

As dimensões contábeis poderão ser visualizadas nos Lançamentos Contábeis na aba "**Dimensão Contábil**" e serão contabilizadas a partir da vinculação da Dimensão ao Evento Contábil.

Temos também os facilitadores de cópia das Dimensões Contábeis entre Coligadas e Associação da Dimensão ao Evento Contábil, facilitando assim a utilização em diversas coligadas.

Para saber mais acesse os itens de processos.

Processos

* [Processo de Cópia de Dimensões Contábeis](https://tdn.totvs.com.br/pages/viewpage.action?pageId=749072442)
* [Processo de Associação Dimensão entre Evento Contábil](https://tdn.totvs.com.br/pages/viewpage.action?pageId=786546265)

---

# **Cadastro**

Cadastro Dimensões Contábeis

60%VídeosleftfadeGlobal1. GlobalGlobal

O campo **Global** é utilizado para sinalizar se a Dimensão será utilizada por todas as Coligadas.

Coligada2. ColigadaColigada

O campo **Coligada**é utilizado para selecionar a Coligada que terá acesso à Dimensão.

Entidade3. EntidadeEntidade

O campo**Entidade** apresenta uma lista de Entidades pré-definidas que podem ser utilizadas como Dimensões.  
Inicialmente, estão disponíveis as Entidades:

* "**Cliente/Fornecedor**" (FCFO), com integração a partir dos módulos Financeiro e Compras/Faturamento;
* "**Produto**" (TPRODUTO), com integração a partir do módulo de Compras/Faturamento (*somente a partir da 12.1.2310!*)
Descrição4. DescriçãoDescrição

O campo **Descrição** permite que o usuário digite uma Descrição para a Dimensão. É um campo de preenchimento livre e pode ser utilizado para descrever a finalidade da Dimensão.

40%Observações

Todos os campos são obrigatórios, exceto o campo de **Coligada**, quando a Dimensão for cadastrada como **Global**.

As informações cadastradas nesta tela serão utilizadas em outras áreas do sistema. Por isso, é importante preencher corretamente os campos para garantir que as informações seja utilizadas de forma correta.

| Regras | Descrição |
| --- | --- |
| **Inclusão:** | * Ao marcar a opção "**Global**", o campo "**Coligada**" é suprimido. * **Não** é permitida a inclusão de Dimensões com Entidades que já existem na Coligada selecionada. |
| **Edição:** | * Após incluída, o único campo permitido para Edição é o de **Descrição.** |
| **Exclusão:** | * **Não** é permitida a exclusão de Dimensões Contábeis em casos onde a Dimensão já foi utilizada em um Lançamento Contábil. |

---

# **Informações complementares**
