---
content_hash: 68a6f1d66f00d3ccda8e3e3c3a9979f53f0aa23bb300351c5db3af9a1302cc30
fetched_at: '2026-06-29T00:11:21.558046+00:00'
page_id: '697260353'
product: rm
source: tdn-rm
title: Transferência de Apropriações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=697260353
version: 24
---

O processo Transferência de Apropriações foi disponibilizado a partir da versão 12.1.2209 e possibilita a transferência de apropriações entre tarefas e projetos no TOTVS Construção Obras e Projetos, mantendo sempre o lançamento original, independente da sua origem.  Através da sua execução, é gerado um lançamento negativo no valor total da(s) transferência(s) para a tarefa da apropriação original, e tantos lançamentos positivos quantas forem as tarefas informada no processo.

Permissão de acesso

Para visualização do processo na tela de Visão das Apropriações, é necessário a liberação do acesso no cadastro do perfil.

Acessando o perfil do usuário, na aba Acesso a Menus, selecione: Obras e Projetos>Controle>Básico>Visão das apropriações>Transferência de Apropriação, e clique no botão "Permitir acesso"

Para realizar a transferência de apropriações, selecione a apropriação desejada na tela de Visão das Apropriações e em seguida clique em Processos>Transferência de Apropriações:

Será exibida a tela abaixo para informar o projeto e a(s) tarefa(s) a(s) qual(is) se deseja realizar a transferência da apropriação:

Por default o projeto destino, virá preenchido com o projeto corrente, mas é possível informar outro projeto, inclusive em outra coligada, dentre aqueles projetos que o usuário tiver acesso.

A tarefa de destino, é informada na sequência e a apropriação de transferência poderá ser lançada em uma das três grandezas: percentual, quantidade ou valor.

Na imagem abaixo, foi usada a grandeza percentual, que tem seu valor e quantidade calculados levando em consideração o saldo disponível da apropriação para realização da transferência.

A Data a apropriar, vem por default com a data corrente, mas permite alteração e deverá ser sempre igual ou maior a data da apropriação original, respeitando o cronograma do projeto destino.

Clicando no botão Transferir, é adicionada a linha abaixo conforme o preenchimento feito anteriormente:

É possível transferir para mais de uma tarefa, assim, abaixo demonstramos o preenchimento para outra tarefa, agora em quantidade:

Ao clicar no botão Transferir, uma nova linha é adicionada:

Por fim, foi adicionada mais uma tarefa, agora usando valor como grandeza:

Perceba que o saldo, tanto em quantidade quanto valor, sofre atualização a cada tarefa informada; garantindo com isso que não seja incluída transferência maior que o total da apropriação:

Clicando em executar, o processo de transferência é efetivado, caso não ocorra nenhuma divergência, seu resultado poderá ser visualizado no anexo .

A apropriação fica sinalizada com um "Sim" indicando que Possui Transferência:

Como vimos, a partir da apropriação original, foi gerado um lançamento negativo na sua tarefa no valor total da transferência, e três lançamentos positivos, um para cada tarefa informada no processo de transferência.

O processo de Transferência de Apropriações não poderá ser executado a partir de Apropriações de Devolução ou Apropriações que foram originadas de uma Transferência de Apropriação, e será exibida a mensagem abaixo:

**Inconsistente**

As apropriações Inconsistentes, são apropriações que possuem Transferências, mas tiveram o valor do movimento alterado e depois de importar as movimentações o saldo ficou insuficiente para as transferências que já existiam. Neste caso o usuário deverá excluir as transferências feitas que estão inconsistentes e realizar novamente o processo de Transferência com os valores corretos.

Exemplo:

O movimento 2442 possui quantidade 100 e valor unitário 100 totalizando o movimento em 10.000,00

Foi realizada uma transferência de 50% para uma tarefa no mesmo projeto.

Ao alterar o item do movimento para uma quantidade menor ocorre inconsistência e o sistema exibe tanto no processo quanto no grid informando que ocorreu a mesma , sendo necessário excluir a transferência e realizar o ajuste da inconsistência gerada.

* Quando a transferência de apropriação tiver sua origem no BackOffice, e ocorrer entre projetos de coligadas diferentes, o usuário poderá informar um produto da coligada de destino para apropriação quando o mesmo não for global.
* Quando a transferência de apropriação tiver sua origem em Apontamentos (Equipamento/Mão de obra) ou por inclusão direta na Apropriação de Serviços/Insumos, dependendo do insumo, se não for global, o usuário poderá informar um produto que esteja associado a um insumo do projeto de destino.
* Caso a importação de movimentações do BackOffice for executada mas não trouxer um movimento que havia sido apropriado e cuja apropriação foi transferida, essas transferências serão excluídas (todas as dependências, inclusive em outros projetos/filiais/coligadas).

**TOPREL0068 - Transferências de Apropriação**

Foi disponibilizado juntamente com a nova funcionalidade, o relatório TOPREL0068 - Transferências de Apropriação; que possibilita a conferência das transferências de apropriações feitas, por projeto e em um determinado período. Seu download pode ser feito através do TOTVS Compartilhamento:

O relatório facilita a visualização das transferências feitas no projeto e para o projeto, informado no parâmetro do relatório, listando a apropriação de origem e o(s) destino(s).
