---
content_hash: fb3ea231a169186ad4fe294cfff490e353437f36585780049f62f2dec1bec8e2
fetched_at: '2026-06-29T00:06:12.140787+00:00'
page_id: '204968763'
product: rm
source: tdn-rm
title: DT_Planejamento_Captação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=204968763
version: 8
---

# PLANEJAMENTO E CAPTAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM** |
| **Segmento:** | *CONSTRUÇÃO E PROJETOS* |
| **Módulo:** | **TOTVS GESTÃO DE PESSOAS** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *PLANEJAMENTO E CAPTAÇÃO* | *Planejamento Captação* | |
| **Versões/Release:** | *12.1.9* |

## Descrição

Foram desenvolvidos recursos que possibilitam a utilização de várias etapas simultaneamente numa mesma vaga de seleção. Também foram desenvolvidas funcionalidades para transferir candidatos entre vagas/seleções e melhorias na triagem

## Procedimento para Utilização

#### Rotinas envolvidas:

**Configurações / Parametrizador  
Seleção / Perfil de Vagas**  
**Seleção / Seleções / Vagas da Seleção**  
**Seleção / Seleções / Vagas da Seleção / Etapas do Perfil de Vaga  
Seleção / Seleções / Vagas da Seleção / Etapas do Perfil de Vaga / Processos  
Seleção / Seleções / Vagas da Seleção / Etapas do Perfil de Vaga / Candidatos / Processos  
Seleção / Triagem  
Seleção / Seleções / Vagas da Seleção / Etapas do Perfil de Vaga  
Seleção / Painel de Seleção**

O processo de recrutamento e seleção dos candidatos são avaliados por dia, por isso as etapas de um processo seletivo não poderiam ser executadas de forma sequencial (forma padrão), respeitando o encerramento da etapa anterior para só então iniciar a próxima etapa. O processo seletivo ocorre duas vezes ao dia em média, com duração de cerca de quatro horas cada um e os comparecimentos espontâneos para o recrutamento e seleção da *Contax* também são frequentes, ou seja, existem candidatos iniciando e percorrendo as etapas do Processo Seletivo a todo momento, o que justifica a utilização das Etapas no formato **Etapas Paralelas**.

No cadastro de Perfis de Vagas uma classificação de **Andamento de Etapas** serve para que as etapas de uma mesma vaga estejam em andamento simultaneamente. A do tipo **Etapas Paralelas** não haverá controle sequencial. Nesse formato o que se espera é que os candidatos cumpram as etapas, não sendo obrigado a seguir uma ordem predefinida.

Ao criar uma vaga de seleção, as preferências da vaga serão carregadas automaticamente. Antes de iniciar o processo de seleção, o usuário poderá alterar o Andamento de Etapas da vaga, seja de sequencial para etapas paralelas ou o contrário.

Os candidatos, quando entrarem numa vaga do tipo Etapas Paralelas, seja por triagem, transferência ou inclusão manual, serão incluídos automaticamente com o status Pendente de análise em todas as etapas. Deverão ser registradas as aprovações, reprovações ou transferências normalmente para os candidatos.

▪ A conclusão de etapas em vagas com etapas paralelas deve apenas alterar o status da etapa, e não fazer qualquer transferência de candidatos.  
 ▪ Não deve ser permitido transferir candidatos entre etapas filhas se for vaga com etapas paralelas.  
 ▪ Para etapas pais, ao concluir uma etapa com esta característica, não deve ser feita a inclusão dos candidatos aprovados nas etapas filhas.  
 ▪ Para etapas filhas, ao concluir uma etapa com esta característica, não deve ser feita a inclusão dos candidatos aprovados na etapa posterior às filhas.

As etapas de Perfis de Vagas, Etapas Sequencias e Etapas Paralelas deverão ter um *flag* para informar a etapa obrigatória. Ao tentar incluir candidatos em processo de admissão ou movimentação, o sistema irá verificar se os candidatos selecionados estão aprovados em todas as etapas obrigatórias. Caso contrário, o sistema avisa ao usuário através de uma mensagem de alerta que há etapas obrigatórias não aprovadas. Este aviso também informa se o candidato foi transferido para esta vaga a partir de outra vaga existente. Nenhuma das duas informações impedirá a execução do processo.

Nas vagas com andamento de etapas do tipo Etapas paralelas, é possível identificar etapas Predecessoras. Mesmo não obedecendo uma ordem de etapas, esse recurso possibilita estabelecer regras de dependência entre as etapas.  
Numa etapa que possua etapas predecessoras, o candidato só poderá ter o status alterado (Aprovar ou Reprovar) caso seu desempenho nas etapas predecessoras já tenha sido devidamente registrado, não estando Pendente de Análise. Se um usuário tentar alterar o status de um candidato numa etapa e o candidato estiver pendente em etapas predecessoras, o sistema não permitirá que a ação seja executada e informará ao usuário o motivo e as etapas que estão bloqueando a ação.

As etapas e obrigatórias predecessoras são definidas dentro do cadastro de uma etapa pertencente a um perfil de vaga. Quando uma vaga for incluída numa seleção, ao carregar as informações das etapas, serão carregadas também as obrigatoriedades e predecessoras definidas no perfil de vaga. Essas informações poderão ser personalizadas na vaga, incluindo ou excluindo novas dependências e mudando a obrigatoriedade de etapas.  
 A alteração dessas informações durante o andamento da seleção é permitida, porém não haverá validação das alterações de status já realizadas. Dessa forma as novas regras serão aplicadas somente às novas alterações de status dos candidatos.

Através do caminho **Planejamento e Captação / Seleções / Perfis de Vaga / Etapas / Candidatos podemos** Transferir Candidatos entre vagas/seleções.  
 O sistema permite a transferência de candidatos entre vagas de seleção distintas para aproveitamento de candidatos que possam participar de outros processos de seleção, e dessa forma otimizar a gerência de informações da tarefa de recrutamento.  
Não será permitido transferir candidatos entre etapas de uma mesma vaga, numa mesma seleção (avançar ou retroceder o candidato).

Se tratando de Origem, nas vagas com etapas sequencias, os candidatos poderão ser transferidos somente a partir da última etapa (mais recente) podendo ter a etapa com status Em Andamento, Reprovado ou Aprovado. Nas vagas com etapas paralelas, os candidatos poderão ser transferidos a qualquer momento

Se tratando de Destino, em vagas sequenciais a regra de transferência de candidatos será aplicada somente para etapas com status Em Andamento. A transferência para vagas do tipo Etapas Paralelas permitirá que os candidatos sejam inclusos automaticamente em todas as etapas da vaga, com o status Pendente de análise.

Quando transferir um candidato, o usuário tem a opção de mover o candidato na etapa atual (etapa de origem). Caso opte por mover, o candidato será incluído na nova etapa (etapa de destino) e terá o status alterado para Transferido na etapa de origem. Candidatos com status Transferido não podem ser aprovados, reprovados ou voltar para pendente de análise.

O processo poderá ser acionado com a seleção de um ou mais candidatos, mas no momento da execução poderá não ser efetivado para todos por validações do processo. Um candidato não pode ser movido para uma etapa que ele já esteve anteriormente. Além disso, as regras descritas acima serão verificadas neste momento e somente os candidatos que atendam às regras poderão ser transferidos.

Ao ser acionado o processo, será exibida uma interface para a escolha do destino da transferência. Os seguintes campos deverão ser informados:

*Seleção*: Seleção destino da transferência. Não podem ser escolhidas seleções com data de fechamento menor que a data atual. Campo obrigatório.  
*Vaga*: Perfil de vaga destino da transferência. Serão exibidos perfis de vaga existentes na seleção escolhida no campo anterior. Não podem ser escolhidos perfis de vaga com data de fechamento menor que a data atual. Nunca será exibida a vaga que origina a transferência. Campo obrigatório.  
*Etapa*: Etapa destino da transferência. Serão exibidas as etapas existentes no perfil de vaga escolhido no campo anterior e que estejam com status Em andamento, para o caso de etapas Sequenciais. Não poderão ser escolhidas etapas com data de fechamento menor que a data atual. Campo obrigatório. Esse campo não será informado caso a vaga destino seja do tipo Etapas Paralelas.  
*Motivo da transferência:* Campo onde poderá ser informado um texto para justificar a transferência. Campo opcional.

Ao executar o processo, o sistema irá:  
Se o destino for do tipo sequencial, criar um novo registro de candidato na etapa de destino com o candidato transferido. Se for do tipo Etapas Paralelas, o candidato será incluído automaticamente em todas as etapas.  
O status do candidato será Pendente de análise e a Data de Entrada será a data/hora da execução do processo.  
No campo **Observações** dos registros criados, deverá ser incluído um texto informando que o candidato foi transferido a partir de outra seleção, e informar qual seleção, vaga e etapa origem da transferência. O motivo da transferência, se informado, deverá ser acrescentado a esse texto.  
 No registro criado (vários, ser for uma vaga com etapas paralelas), deverá ser gravada a chave que identifica a origem da transferência. Essa informação será necessária para o eventual retorno do candidato à etapa original.  
O candidato terá o *flag* Transferido marcado na etapa que originou a transferência. O campo **Data de Saída** deverá ser atualizado com a data/hora da transferência.

O campo **Transferido** deverá ser exibido na visão dos candidatos de etapas e deverá ser possível aplicar filtros com este campo.  
Um candidato transferido não poderá mais ter o status alterado, bem como não será incluído na etapa seguinte, mesmo tendo status aprovado no momento da conclusão da etapa atual.  
Se o usuário tentar incluir um candidato transferido em processo de admissão ou de movimentação, o sistema deverá alertar o usuário sobre a transferência para outra vaga. Essa mensagem será informativa e não impossibilitará a continuação do processo.

Utilizando vagas com etapas do tipo “Sequencial”, se o usuário transferir um candidato por engano, não será possível reativar o candidato na etapa de origem. Por esse motivo, é necessário criar um assistente para desfazer uma transferência feita por engano. Esse assistente deverá ser disponibilizado na visão de candidatos de etapa.  
Em vagas com etapas sequenciais, o candidato recém transferido deverá estar na mesma etapa para a qual foi transferido e ainda com o status Pendente de Análise. Se ele avançou para etapas seguintes devido à conclusão de etapas, não será possível desfazer a transferência.  
Em vagas com etapas paralelas, o candidato recém transferido possuirá status Pendente de Análise em todas as etapas para que seja possível desfazer a transferência.  
O sistema deverá detectar qual foi a última vaga e etapa que o candidato esteve e retorná-lo para esta etapa com o status Pendente de Análise. Para detectar a última vaga e etapa, o sistema verificará os campos que identificam a origem e que foram preenchidos no momento da transferência.  
O candidato será removido da etapa atual e será registrado um histórico. Deve ser registrado o histórico deste procedimento no campo de observações do registro original do candidato que havia sido transferido.

A triagem tem as seguintes possibilidades:

Informar uma lista de Níveis Hierárquicos desejados. Quando informados, os itens desta lista deverão ser utilizados no momento da execução da triagem para buscar candidatos que atendam às preferências definidas no cadastro da triagem. Para ser selecionado na triagem, no currículo do candidato, o nível hierárquico deve estar preenchido com um dos níveis definidos na triagem.  
Lista de competências e as graduações desejadas nos candidatos a serem triados. Além de informar quais competências deseja e as suas respectivas graduações mínimas e máximas, o usuário poderá escolher se deseja triar candidatos que possuam todas ou uma das competências nas graduações informadas.  
Lista de requisitos de acesso desejados nos candidatos a serem triados. Além de informar quais requisitos deseja, o usuário poderá escolher se deseja triar candidatos que possuam todos ou um dos requisitos informados. Também poderá escolher de se deseja considerar como válidos os requisitos de acessos que por ventura estejam expirados na data de execução da triagem.  
Limite de vagas simultâneas que o candidato pode participar: este campo, do tipo numérico, deverá ser informado caso o usuário queira que a triagem verifique se os candidatos triados já estão participando de seleções e estão ativos nelas, e limite a quantidade de seleções nessas condições que um candidato pode estar. Por exemplo: se o candidato já está participante de uma seleção e a triagem limita em 1 (um) o número de vagas simultâneas, esse candidato, mesmo atendendo aos requisitos da triagem, não será incluído na seleção.

Considera-se que um candidato encontra-se ativo numa vaga de seleção:

Com etapas sequenciais: a vaga está com status “Em Andamento” e o candidato encontra-se com status Aprovado ou Pendente de Análise na etapa que estiver “Em andamento”.  
Com etapas paralelas: a vaga está com status Em Andamento e o candidato não se encontra Eliminado.  
Não triar candidatos que participaram de vagas de seleção concluídas nos últimos X meses ou que ainda estejam abertas. Esta opção deverá permitir que o usuário informe um número (inteiro) de meses e, a partir dessa informação, a triagem irá eliminar candidatos que tenham participado de processos seletivos no intervalo definido.

Na visão de candidatos de uma etapa, foi incluída uma coluna que indica se o candidato se matriculou pelo portal para a vaga.  
Para vagas do tipo **Etapas Paralelas**, a execução da Triagem é permitida mesmo após os candidatos já estarem sendo movimentados entre das etapas. Neste caso, todos os candidatos que já estão no processo serão mantidos, com os seus respectivos status. E aqueles identificados na triagem que não estejam no processo, serão acrescentados. Para vagas do tipo Sequencial, o atual comportamento será mantido (Iniciar Processo de Seleção).

Para possibilitar uma visualização consolidada do andamento das etapas dos candidatos de uma vaga de seleção, deverá ser criada uma visão que demonstre para uma determinada vaga, quais etapas cada candidato já cumpriu e qual o status. Dessa forma o usuário conseguirá acompanhar o progresso da seleção de forma facilitada, sem precisar entrar em cada etapa para ver seus candidatos.

Além dos status dos candidatos nas etapas, também será possível visualizar se há transferência e eliminação de candidatos, e a partir de qual etapa foi tomada a ação. No Painel de Seleção, quando uma vaga do tipo **Etapas Paralelas** for selecionada, será exibido um *checkbox* que, quando marcado, exibirá a visualização de Etapas Paralelas.

A partir da visão de Etapas Paralelas, será possível executar as seguintes ações:

**Aprovar/Reprovar/Pendente:**

Este assistente deverá permitir que o usuário, a partir da seleção de candidatos, possa trocar o status dos candidatos para Aprovado, Reprovado ou Pendente de Análise, da seguinte forma:  
Ao acionar o assistente, o usuário escolherá qual dos status acima deseja aplicar aos candidatos.   
Em seguida o usuário poderá escolher para quais etapas ele deseja aplicar o novo status.  
Poderá também incluir um texto explicativo para justificar a alteração proposta.  
Todas trocas de status ficarão registradas no campo **Observações** do candidato. Os status escolhidos sobrescreverão os status anteriores das etapas para os candidatos selecionados.  
Candidatos transferidos não poderão sofrer alteração de status na etapa de origem.

Em vagas com etapas paralelas, nos registros de etapas dos candidatos haverá um *Flag* que indicará que o candidato foi eliminado. Assim será possível identificar a origem da eliminação e manter os status das etapas.  
Um candidato será considerado eliminado da vaga se tiver com o *Flag***Eliminado** marcado para qualquer uma das etapas da vaga. Após ser eliminado, um candidato não poderá ser transferido, aprovado, reprovado ou ainda ser incluído em processo de admissão ou movimentação.  
No processo de reprovação de candidatos em vagas com etapas paralelas, o usuário terá a opção de eliminar o candidato, independentemente da etapa ser obrigatória ou não. Neste caso, o usuário deverá informar a etapa que causou a eliminação   
É possível voltar um candidato eliminado para a vaga. Para isso o usuário deverá voltar o candidato para Pendente de Análise na etapa que originou a eliminação. Essa permissão será atribuída de acordo com o perfil de acesso do usuário.  
O processo de transferência de candidatos estará disponível e poderá ser utilizado normalmente. O usuário deverá informar a etapa que originou a transferência, pois ela terá o *Flag* **Transferido** marcado.

Foram disponibilizados pelo RM, serviços que possam ser acessados pelo Fluig para indicar a candidatura e a desistência de candidatos em vagas de seleção.   
 O serviço de candidatura será responsável por identificar dentro do RM que determinado candidato candidatou-se espontaneamente a uma determinada vaga. No caso da Contax isso poderá acontecer com MOI (Mão-de-obra indireta). Os serviços deverão receber como parâmetro o código da pessoa e a chave primária da vaga (CODCOLIGADA, CODSELECAO, CODVAGA). Os serviços irão atualizar as informações contidas na tabela VRSSELECOESVAGASCANDIDATOS, que armazena o vínculo entre vagas e candidatos que se inscreveram diretamente à vaga por meio do Portal.
