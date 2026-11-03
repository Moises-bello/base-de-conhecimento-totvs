---
content_hash: a8bc2750948e96933097af85f67933fbbb88a27b42558b2873e652980f953e9f
fetched_at: '2026-06-29T00:09:26.499132+00:00'
page_id: '423938304'
product: rm
source: tdn-rm
title: Aprovação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938304
version: 6
---

O processo de Aprovações por Tipo de Movimento deve ser utilizado para aprovar faturamento/recebimento de movimentos, bem como permitir a utilização destes movimentos/itens no processo de Cotação.  
Para este processo, devem ser feitas parametrizações específicas no Perfil associado aos Usuários que deverão aprovar (ou não) os movimentos.

**Parametrização**

Para a correta utilização do processo de Aprovação de Movimentos, alguns passos devem ser seguidos:

* Cadastrar uma fórmula, que irá verificar dados do movimento a ser aprovado, e permitir sua aprovação. Esta fórmula deverá conter, em seu texto, as validações necessárias para efetuar o processo Aprovação, como validação de valores do movimento, usuários que podem ou não efetuar a Aprovação, data e hora em que este movimento poderá ser aprovado, entre outros. A lógica a ser utilizada depende da necessidade da restrição/permissão de Aprovação. Esta fórmula deverá retornar valor '0', quando não aprovar, e '1' para aprovar;
* Associar esta fórmula ao Perfil desejado, informando a qual Processo de Aprovação e qual Tipo de Movimento será utilizado para tal;
* Após a criação da fórmula, deverá ser editado o Perfil o qual conterá a permissão/alteração e, no Anexo 'Aprovações por Tipo de Movimento', incluir uma nova Aprovação, informando qual o Tipo de Movimento e qual o Processo. Estes processos têm funções específicas, as quais serão explanadas abaixo com mais detalhes;
* Associar o Perfil aos Usuários que conterão as mesmas permissões;
* Associar os Usuários ao Perfil parametrizado quer seja para permitir aprovação ou não. Usualmente, são criados Perfis que podem efetuar a Aprovação, e outros que não podem efetuar esta Aprovação, ficando mais fácil esta associação;
* Parametrizar o tipo de movimento para utilização de Aprovação. Esta parametrização está disponível nos parâmetros do Tipo de Movimento | etapa 'Mov – Outros Dados', onde deve ser alterado o campo 'Aprovação' para 'Usa'.

**Informações dos Tipos de Processos Disponíveis**

**Tolerância no Recebimento:** Este tipo de Aprovação é utilizado para o recebimento de Itens, mesmo se seus valores estiverem fora dos limites de tolerância informados na pasta Preço do cadastro de Produtos, desde que a fórmula retorne um valor permitindo a Aprovação.  
Quando selecionado este tipo de Aprovação, será apresentada uma tela com todos os Itens do (s) Movimento (s) selecionado (s) e se já estão aprovados ou dependem de aprovação, permitindo a escolha (aprovação) de determinados Itens especificamente. Para a execução do processo, deverão ser marcados os Itens desejados. Ao finalizar a seleção, o sistema executa a Aprovação/Desaprovação de acordo com o status atual. Exemplo,  
Se um determinado Item já se encontra com o status 'Aprovado', ao executar o processo, este status será invertido, ou seja, será alterado para 'Desaprovado'.  
***Observação***: Este processo é executado desta forma somente para a 'Tolerância no Recebimento'.

**Aprovação no Faturamento**: Este tipo de Aprovação é utilizado para o recebimento de Movimentos, desde que a fórmula definida retorne um valor permitindo a Aprovação. Caso a fórmula retorne um valor permitindo a Aprovação deste movimento, o sistema permitirá que este movimento seja faturado/recebido para outros movimentos.  
Se houver a tentativa de Faturamento/Recebimento deste movimento e a fórmula retorne um valor permitindo a Aprovação deste movimento, o sistema efetuará a Aprovação Automática deste movimento, não havendo necessidade de executar o processo de Aprovação pela visão de movimentos.  
Uma vez aprovado o movimento, qualquer usuário poderá recebê-lo para outro movimento.  
***Observação***: Caso queira retornar o movimento que tenha sido Aprovado para o status 'Não Aprovado', utilize o Menu Movimentos | Desaprovação.  
Quando se reabre um movimento que tenha sido aprovado e faturado, essa aprovação não será excluída, não sendo necessário aprová-lo novamente.

**Aprovação por item de Movimento no Faturamento**: Este tipo de Aprovação é utilizado para o recebimento de itens do Movimento, desde que a fórmula definida retorne um valor permitindo a Aprovação. Caso a fórmula retorne um valor permitindo a Aprovação do item de movimento, o sistema permitirá que este item seja aprovado, caso contrário será apresentado mensagem de que o item não pode ser aprovado. Ao faturar movimento com este tipo de aprovação, só serão apresentados no movimento de destino, os itens que possam ser aprovados pela formula.

***Observação***: Mesmo que não tenha realizado a aprovação de todos os itens (mas que a formula permita a aprovação), ao faturar o movimento, os itens que não foram "pré-aprovados" também serão apresentados no movimento de destino. Uma vez, que a permissão de aprovação é do perfil do usuário.

ImportanteDepois de aprovado o movimento “qualquer” usuário que tenha permissão a “faturar” poderá recebê-lo. O usuário associado a um perfil que “permite aprovação” poderá faturar x receber pedido sem que o processo de aprovação seja realizado, de forma que, ao concluir o faturamento os dados de aprovação serão gravados automaticamente na tabela **TMOVAPROVA.**

**Aprovação de Solicitação de Compras para Cotação**: Este tipo de Aprovação é utilizado para aprovar Solicitações de Compra, de modo a permitir que estas façam parte do processo de Cotação, desde que a fórmula definida retorne um valor permitindo a Aprovação. Neste caso, o sistema permitirá que este movimento participe do processo de Cotação, de modo a efetuar os processos de Compras relacionados ao processo de Cotação. Se houver a tentativa de inclusão de uma Cotação, o assistente não apresentará o movimento, caso o mesmo não esteja Aprovado.  
Diferentemente do processo de Aprovação no Faturamento, mesmo que a fórmula contemple a aprovação deste movimento, é imprescindível que este seja aprovado antes da execução do processo de Cotações.  
***Observação***: Caso queira retornar o movimento que tenha sido Aprovado para o status 'Não Aprovado', utilize o Menu Movimentos | Desaprovação.  
Aprovação por Item de Movimento para Cotação. Este tipo de Aprovação deve ser utilizado para permitir/restringir a inclusão de itens no processo de Cotação. Quando for selecionada será apresentada uma tela que exibirá os itens do movimento. Apenas os itens que passarem na validação da fórmula cadastrada serão aprovados, e poderão ser utilizados na cotação.

**Processo de Desaprovação**

Caso queira retornar um item de movimento que tenha sido Aprovado para o status 'Não Aprovado', utilize o processo Desaprovação. Os itens desaprovados não serão exibidos no Filtro de Produto na cotação.  
***Observações***: Os itens de movimento que estejam participando de algum processo de cotação não poderão sofrer a Desaprovação.  
Apenas itens já aprovados podem ser desaprovados.  
Os itens de movimento só podem ser desaprovados pelo usuário que tiver permissão de acesso ao processo, se for o mesmo que aprovou ou por um supervisor.  
A lógica da fórmula a ser utilizada depende da necessidade da restrição/permissão de Aprovação por Item de Movimento para Cotação. Neste caso, o contexto de utilização da fórmula será o de item de movimento.

Informações Adicionais

* [Aprovação de Itens de Movimento por Tolerância](http://tdn.totvs.com/pages/viewpage.action?pageId=4812986)
* [Aprovação de Movimentos no Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=42043642)
* [RSS - Movimentos que Necessitam de Aprovação](http://tdn.totvs.com/pages/viewpage.action?pageId=4813120)
