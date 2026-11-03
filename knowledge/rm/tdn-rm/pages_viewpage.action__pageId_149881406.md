---
content_hash: 5d73b1a6d1340f189e905ecedfae9f37beb7a4b48844b37c8f38dd41bb02d708
fetched_at: '2026-06-29T00:05:56.286395+00:00'
page_id: '149881406'
product: rm
source: tdn-rm
title: Utilizando a atividade "Criar Conjuntos de Dados"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881406
version: 10
---

# Índice:

---

.\*ndice:

# Objetivo:

---

     Este documento tem por objetivo especificar a atividade “Criar Fonte de Dados (DataSet)” disponível na Fórmula Visual.

# Especificação:

---

     Está atividade busca criar uma fonte dados que seja utilizada internamente na Fórmula Visual. Poderemos conferir esta situação no exemplo abaixo.

false

     O exemplo a seguir tem como objetivo percorrer os valores de uma consulta SQL salvando cada registro dentro da atividade "Criar Fonte de Dados (DataSet)". Para realizar a inserção dos mesmos utilizaremos a atividade "Adicionar Registros na Tabela" e em seguida exibiremos os valores já inserido no conjunto de dados.

Importante

     Todas as atividades abaixo foram renomeadas para melhor interpretação.

Criar Fonte de DadosPasso 1

     Adicionar a atividade "Executar Consulta SQL" e atribuir a ela uma sentença conforme os prints abaixo:

Passo 2

     Adicionar a atividade Criar Fonte de Dados. Em seguida, dentro da propriedade Estrutura das Tabelas clique em Adicionar, em seguida crie a tabela e seus campos:

Passo3

     Adicionar as atividades "Para Cada Interação e Sequência"

     Na propriedade Lista de Itens da atividade "Para Cada Iteração" selecione o caminho abaixo:

     Ou seja, estamos dizendo que a atividade Para Cada Iteração está percorrendo cada linha do resultado do SQL.

Passo 4

     Adicionar a atividade Adicionar Registro na Tabela. Esta é a atividade responsável por inserir os valores do SQL na atividade ConjuntoDados. Na propriedade Tabela selecione o caminho abaixo.

Ou seja, estou informando a tabela para gravar os dados. Após, ira aparecer os campos da tabela do conjunto, em seguida selecione o caminho abaixo.

Passo 5

     Adicionar a atividade "Transformar Registro em Xml" e "Gerar Exceção"

     O intuito das atividades é mostrar os valores na tela. Na atividade Xml selecione o caminho:

     Na atividade Msg selecione o caminho:

Passo 6

     Finalizada a configuração da Fórmula Visual, sua execução retornará a seguinte informação:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.17 ou Superior

false

**Processo:** Atividade "Criar Fonte de Dados (DataSet)" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
