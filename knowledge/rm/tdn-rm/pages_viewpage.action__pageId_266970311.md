---
content_hash: 1d45036fd51625ee78d4eb7b0c75f4b8882abbe931bb0095c63763771803add1
fetched_at: '2026-06-29T00:08:18.822981+00:00'
page_id: '266970311'
product: rm
source: tdn-rm
title: Limitando o Tamanho de Imagens no Cadastro de Produtos com Fórmula Visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266970311
version: 18
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Este documento tem por objetivo exemplificar a utilização de uma fórmula visual para limitar o tamanho de imagens no cadastro de produtos.

# Introdução:

---

      Para se limitar o tamanho de uma imagem a ser salva nas telas de cadastros do sistema, é necessário a utilização de uma Fórmula Visual. Abaixo exemplo da criação e associação desta Fórmula Visual que limitará o tamanho de uma imagem no cadastro de produtos.

# Criando a Fórmula Visual:

---

      Para acessar a janela de criação de Fórmulas Visuais, depois de selecionado qualquer produto, acesse o menu "Gestão | Ferramentas de Análise | Fórmula Visual"

falseCriando a Fórmula VisualCriação do Registro

Para criar uma nova Fórmula Visual, após carregada a visão, é necessário clicar em "Novo" e informar no mínimo os campos obrigatórios "Identificador da Fórmula Visual", "Ativo" e "Categoria" para salvar o registro.

Estrutura de Edição

Selecionar com um duplo clique o registro criado anteriormente para que a estrutura de edição da Fórmula Visual seja aberta.

Tela de edição da Fórmula Visual:

Informando o Contexto

É necessário informar um contexto para que a Fórmula Visual reconheça os campos utilizados em sua estrutura. Neste exemplo, será utilizado o contexto de "Produtos"

Adicionando as Atividades

Para limitar o tamanho da imagem a ser salva no cadastro de produtos é necessário que a Fórmula Visual possua as atividades "Se/Senão" e "Gerar Exceção". A seguir será explicado o passo a passo de como estas atividades deverão ser inseridas:

* Arraste a atividade "Se/Senão" para o fluxo de trabalho da Fórmula Visual:

* Neste não será necessário a utilização de uma clausula "Senão". Selecione então a atividade "ifElseBranchActivity**2**" e remova a mesma utilizando a tecla "Delete" de seu teclado.

|  |  |
| --- | --- |

* Agora, nas propriedades da atividade "ifElseBranchActivity**1**" selecione como parâmetro para o campo "Condition" a opção "Condição de Regra Declarativa". Em seguida, expanda as opções e informe um nome para condição:

|  |  |
| --- | --- |

* Agora, clique no lookup do campo "Expression" e insira como condição a seguinte expressão: **!this.Fields["IMAGEM"].IsNull && this.Fields["IMAGEM"].AsBytes.Length > 1024000** . Esta expressão irá limitar que a imagem carregada não seja salva caso está seja maior 1024000 Kbytes ou seja, nenhuma imagem acima de 1 Mega Bytes poderá ser salva no registro. Caso queira diminuir ou aumentar o tamanho das imagens a serem salvas, basta alterar o numeral expresso na fórmula como desejar.

Observação

A grandeza das imagens na fórmula é expressa em Bytes.

|  |  |
| --- | --- |

* Em seguida, adicione a atividade "Gerar Exceção" dentro da atividade "Se/Senão":

* Nas Propriedades da atividade "Gerar Exceção", informe a mensagem que deverá ser apresentada ao usuário quando o mesmo for tentar salvar uma imagem no produto que possua o tamanho acima do limite definido.

* Salve a Fórmula Visual

Executando a Fórmula Visual

Para acessar a janela de Produtos, depois de selecionado o módulo "BackOffice | Gestão de Estoque, Compras e Faturamento", acesse o menu "Cadastro | Estoque, Compras e Faturamento | Produto"

* Para inserir a Fórmula Visual, selecione a opção "Processos | Fórmula Visual | Gerenciar":

* Após, adicione a Fórmula Visual anteriormente criada, ao gatilho "Antes de Salvar o Registro":

* Feito isso, edite um produto e carregue uma imagem de tamanho superior ao limite informado na Fórmula Visual (no caso do exemplo criado, 1 Mb). Ao tentar salvar o registro, a mensagem criada na Fórmula Visual será apresentada impedindo que o usuário salve o registro com está imagem. Entretanto, caso o usuário adicione uma imagem de tamanho inferior ao tamanho definido na Fórmula, o registro será salvo com sucesso:

| Exemplo de Registro com imagem superior  ao que foi definido na Fórmula Visual | Exemplo de Registro com imagem inferior  ao que foi definido na Fórmula Visual |
| --- | --- |
|  |  |

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.12 ou Superiores

false

**Processo:** Utilização de fórmula visual para limitar o tamanho de imagens no cadastro de produtos

falsefalse

**Status:** Finalizado

false

**Data:** 04/10/2016

false

**Autores:**
