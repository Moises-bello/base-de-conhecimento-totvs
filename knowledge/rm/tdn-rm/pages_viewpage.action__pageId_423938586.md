---
content_hash: 9399d454bbb3db6380cacc44e9e171c01bd25747a79b7361b5a92ff39a539f8f
fetched_at: '2026-06-29T00:09:27.952037+00:00'
page_id: '423938586'
product: rm
source: tdn-rm
title: Tarefas  
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938586
version: 5
---

**Tarefa** é a denominação dada à solicitação para execução de um determinado serviço, solicitada diretamente nos módulos onde os lançamentos contábeis são originados, para que seja executada dentro do próprio TOTVS Gestão Contábil.

Depois que a contabilização gerada por uma operação que teve origem em outro aplicativo, ou seja, em um módulo externo ao da contabilidade, é integrada ao lote zero, estes lançamentos não podem mais ser excluídos da contabilidade. Se por algum motivo for necessário que estes lançamentos não sejam mais considerados na contabilidade, eles deverão ser *Estornados* pelo próprio aplicativo que os originou. Através desta ação, são incluídos no TOTVS Gestão Contábil os lançamentos de *Estorno*, que deverão ser integrados também ao lote zero para que um cancele o efeito contábil do outro. Porém, tanto os lançamentos Estornados quanto os de Estorno ficarão registrados na contabilidade, um anulando o efeito contábil do outro.

Temos, contudo disponíveis no sistema alguns tipos de tarefas que permitem a exclusão de alguns lançamentos que tiveram origem em outros aplicativos, como os citados anteriormente.  Hoje o sistema disponibiliza os seguintes Tipos de Tarefas:

* **Exclusão Contabilidade Lote Zero:** Este tipo de tarefa envia uma solicitação ao TOTVS Gestão Contábil para excluir definitivamente da base de dados toda a contabilização gerada por uma operação, ou seja, solicita a exclusão dos lançamentos contábeis originados pela operação contábil, assim como os respectivos lançamentos de estornos desta operação. Desta forma excluirá toda a contabilização vinculada a determinada operação realizada em módulo externo ao da contabilidade.
* **Exclusão de Lançamentos de Estorno e Estornado:** Este tipo de tarefa envia uma solicitação para o TOTVS Gestão Contábil para excluir definitivamente da base de dados somente os lançamentos de estorno e os estornados que estiverem vinculados a determinada operação realizada em módulo externo ao da contabilidade, mantendo porém os lançamentos vinculados a esta operação que estiverem ativos.

Vale lembrar que as Tarefas devem ser solicitadas diretamente nos módulos onde os lançamentos contábeis são originados e para isto estes módulos deverão estar devidamente preparados para utilizar estes serviços.

As tarefas solicitadas são enviadas para o TOTVS Gestão Contábil e somente poderão ser realizadas por usuários que tenham permissões para gerenciá-las, podendo executar ou cancelar as tarefas solicitadas. Tais permissões devem ser incluídas dentro do próprio cadastro do Tipo de Tarefa disponível no TOTVS Gestão Contábil|Utilitários|Tarefas|Permissões. O gerenciamento deve ser feito em TOTVS Gestão Contábil|Utilitários|Tarefas|Gerenciador.

Para obter informações sobre atribuição de permissões e gerenciamento de tarefas clique abaixo nos respectivos links:

Mais informações

* Permissão para realização de Tarefas
