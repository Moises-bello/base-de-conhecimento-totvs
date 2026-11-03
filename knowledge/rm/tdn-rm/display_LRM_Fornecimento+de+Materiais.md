---
content_hash: 459926b9e490c2edcf544e51c3bf2f4d2849b204d315a107b9aee5ac53cb5ff4
fetched_at: '2026-06-29T00:09:14.763200+00:00'
page_id: '421385250'
product: rm
source: tdn-rm
title: Fornecimento de Materiais
type: documentation
url: https://tdn.totvs.com/display/LRM/Fornecimento+de+Materiais
version: 4
---

---

Para cadastrar um **Contrato de Fornecimento de Materiais** é necessário selecionar a finalidade do contrato, dentro da opção de inclusão de novos contratos. Sendo que tais contratos serão sempre do tipo A pagar.   
  
 Devido a sua forma de utilização, as informações de fórmula e reajuste não serão utilizadas e por isso, o acesso às telas de cadastro de tais informações não é permitido. É exibida uma mensagem informando que não será possível a sua utilização.  
  
 Os períodos do Contrato de Fornecimento de Materiais, bem como suas medições e liberações, são gerados automaticamente através da funcionalidade  ou  . De forma semelhante, os períodos serão apagados caso o pedido de material que os originaram sejam excluídos.  
 A associação de objetos (itens) é feita através do processo "Associar objetos ao Contrato de Fornecimento de Material". Através deste processo é possível selecionar insumos que estejam associados às tarefas ativas do projeto e vinculá-los ao contrato.   
  
 Apenas insumos ligados ao grupo DNIT "Materiais" e com unidade diferente de Percentual poderão ser vinculados ao contrato de fornecimento de material.   
  
 Na associação de objetos, foi incluído o conceito prioridade de Consumo. A informação de prioridade de consumo dos objetos será considerada no momento da requisição de materiais. Caso os materiais requisitados estejam contratados, eles serão consumidos do contrato. Caso um material esteja vinculado a mais de um contrato, ele será consumido do contrato que possuir a menor prioridade.  
  
 Um objeto não pode ser associado mais de uma vez com um mesmo valor de prioridade de consumo. Caso tente fazê-lo, será informado que aquele objeto já esta associado com tal prioridade. Caso escolha prosseguir com a associação, o objeto na associação feita anteriormente terá a sua prioridade de consumo alterada. Esta regra é válida tanto na associação diretamente ao contrato quanto a um aditivo contratual.       
  
 No momento da associação de objetos, é possível editar a quantidade contratada e o preço unitário contratado conforme desejado. No processo, os objetos já associados ao contrato corrente serão exibidos em cor azul.

Após já ter sido vinculado, não é possível alterar as informações de quantidade e valor do objeto. Apenas é possível atualizar a sua prioridade de consumo.

Através do anexo  é possível visualizar todos os objetos que estão associados ao contrato. Os objetos poderão ser excluídos do contrato também através desta funcionalidade, desde que não tenham sido consumidos.    
 O **Contrato de Fornecimento de Materiais** utiliza o anexo  . É possível criar um aditivo apenas de data ou também de valor, associando objetos ao aditivo. Para cada aditivo, apenas um novo objeto poderá ser vinculado.

Os anexos Departamentos do Contrato, Centros de Custo do Contrato, Itens do Contrato, Retenções Contratuais e Adiantamento de Contrato, bem como os processos Associação de Itens ao Contrato, Associar Períodos do Contrato à Períodos do Cronograma, Atualiza Cronograma pelos Lançamentos de Medição, Geração de Períodos, Renumerar Períodos Principais, Renumerar Períodos Complementares e Renumerar Períodos Estorno não são utilizados por **Contratos de Fornecimento de Materiais**. Assim, o acesso à tais funcionalidades não é permitido. De forma semelhante, o campo "Periodicidade Medida" é omitido da tela de inclusão/edição de contratos quando trata-se de um contrato desta finalidade.
