---
content_hash: aaa3aea45593a486ed338292e6a8bbeef16248941fcaf4dd62a8d9c690610a9a
fetched_at: '2026-06-29T00:11:55.600738+00:00'
page_id: '862592543'
product: rm
source: tdn-rm
title: Atividades.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862592543
version: 28
---

# Índice

## O que são?

Atividade é um programa independente que tem a finalidade de executar alguma tarefa de forma automatizada. Cada atividade pode operar de maneira isolada, mas também pode compartilhar ou utilizar recursos de outras atividades para completar suas funções. A junção dessas atividades cadastradas na aplicação resulta na criação de um Projeto de Teste.

## Para que servem?

As atividades são fundamentais para a automação de processos e testes. No contexto de testes, as atividades desempenham um papel crucial na criação de Projetos de Teste, onde cada atividade executa uma função específica que contribui para a validação do sistema como um todo.

## Exemplo de Uso

Como cadastrarDefinição do Cabeçalho (Nome e Nível de acesso)

O cabeçalho é a seção inicial do cadastro de uma atividade. Nesta etapa, você define o nome da atividade e seu nível de acesso, ou seja, especifica quais grupos podem visualizar a atividade e quais permissões serão concedidas para gerenciá-la.

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

Ícones e Filtros da Tabela

Essa seção tem como objetivo explicar o funcionamento de cada opção disponível nas tabelas de atividades. As ferramentas apresentadas abaixo estão disponíveis em todas as tabelas de qualquer atividade.

ÍconesAdicionar

Essa opção permite iniciar o cadastro de qualquer atividade. Ao clicar, você será direcionado para preencher o cabeçalho correspondente e, em seguida, para completar os campos necessários para a criação da atividade.

Deletar

O botão de deletar permite que os usuários autorizados removam permanentemente uma atividade específica do sistema. Para que ele esteja disponível, deve-se selecionar primeiramente a atividade de interesse.

Duplicar

# 

O processo de duplicação consiste em gerar uma cópia de qualquer atividade. Ele é muito útil para casos em que queremos gerar uma atividade com base em uma outra já existente.

Para que ele esteja disponível, deve-se selecionar primeiramente a atividade de interesse.

## Exemplo De Uso:

Temos o seguinte projeto de teste, sua função é preparar o ambiente de execução e executar o cadastro de um aluno na base via SOAP.

Queremos criar um projeto semelhante a este, mas substituindo a atividade SOAP atual por outra que executa um processo de alteração da situação de matrícula via SOAP. Para isso, selecione a atividade desejada na tabela e clique no ícone **Duplicar**. Uma janela será aberta para confirmar a atividade a ser duplicada e a versão correspondente.

Após confirmar a solicitação, será criada a atividade cópia com todos os aspectos informados anteriormente.

Dessa forma, será possível editar a atividade copiada e inserir a atividade SOAP para alteração de matrícula. Além disso, é possível alterar os demais campos *(Nome, Descrição e etc...),* sem afetar a atividade original.

Replicar

Essa ferramenta tem a função de gerar uma réplica identica da atividade em questão em uma versão diferente. Esse processo é extremamente útil para gerar e controlar o versionamento de uma mesma atividade.

## Exemplo De Uso:

Temos o seguinte projeto de teste, sua função é preparar o ambiente e executar um cadastro de aluno na base via SOAP.  

Na nova versão do produto, quero adicionar um teste para validar um novo fluxo que não existia na versão anterior. Para isso, vamos criar uma réplica da atividade em questão para uma nova versão.

Após confirmar a solicitação, será gerada uma nova versão da atividade em questão.

Ao clicar nessa versão, pode-se atualizar a atividade e adicionar um novo processo.

Ao atualizar a atividade na versão X, as demais versões não serão alteradas.

Pode ser observado o comparativo abaixo, da mesma atividade na *versão 1* e na *versão 2*.

Filtrar

Ao clicar nessa opção, todos os filtros previamente aplicados à tabela são removidos, e a seção de filtros é ocultada.

Selecionar

Essa opção permite selecionar uma ou várias atividades. Após selecioná-las, você pode aplicar outras ações, como deletar, replicar ou duplicar, em todas as atividades escolhidas.

Para selecionar todas as atividades exibidas na tabela, basta clicar na opção correspondente:

Editar

O botão de editar permite que os usuários autorizados modifiquem uma atividade específica.

Logs

Essa opção redireciona para a página de Histórico de Execuções da atividade em questão. Clique [aqui](https://tdn.totvs.com.br/pages/releaseview.action?pageId=687765736) para mais informações sobre essa página.

Filtros da Tabela 

Temos as seguintes opções de filtros:

* **Nome da atividade**: Filtre pelos nomes específicos de suas atividades para encontrar rapidamente um caso particular que você deseja visualizar ou editar.
* **Versão**: Filtre pelas diversas versões de suas atividades.
* **Grupos**: Filtre pelos grupos que associam à sua atividade.

Além disso, é possível filtrar pela quantidade de itens a serem apresentados por página:

 Definição do cabeçalho de uma Atividade

Clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)  para saber mais sobre o cabeçalho que contem em determinadas atividades

Gerenciamento de Recursos nas Atividades

Clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=876227991) para saber mais sobre os recursos (Consumo e disponibilização) que oferecem das Atividades.

---

# Saiba mais

É por meio das atividades, do fluxograma que as conecta e de seus relacionamentos que montamos um Projeto de Teste automatizado.

Ao criar um Projeto de Teste, em cada Atividade será apresentado quais recursos ela necessita e/ou fornece.

As atividades também podem ser utilizadas em agendamentos. No entanto, quando usadas dessa forma, elas não devem depender de recursos de outras atividades incluídas no mesmo agendamento, pois são executadas de forma isolada.

# FAQ

**P: O que significa versionar uma Atividade?**

R: Versionar uma atividade significa criar uma cópia dela associada a uma versão específica do sistema. Isso permite que a atividade seja adaptada e mantida conforme o sistema evolui, sem afetar a versão original.

**P: O que acontece quando duplico uma Atividade?**

R: Ao duplicar uma atividade, uma cópia idêntica é criada na versão padrão, com a palavra "CÓPIA" adicionada à descrição da nova atividade. Isso permite que você trabalhe em uma versão duplicada sem alterar a original.
