---
content_hash: cd38f527c73159cad69726005ab2879d4692f2419b9f0746c4352c2c9076c754
fetched_at: '2026-06-29T00:05:59.857606+00:00'
page_id: '192100191'
product: rm
source: tdn-rm
title: ER_Planejamento_Captacao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Planejamento_Captacao
version: 12
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** | RHU – DESENVOLVIMENTO RHU006 | **IRM1** | PCREQ-1947 |
| **Requisito1** | PCREQ-1948 | **Subtarefa1** | PDR\_RHU\_RHU006-77 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Serão desenvolvidos recursos para possibilitar a utilização de várias etapas simultaneamente numa mesma vaga de seleção. O comportamento do sistema irá refletir essa opção, mudando as ações relacionadas aos candidatos das etapas.Também serão desenvolvidas funcionalidades para transferir candidatos entre vagas/seleções e melhorias na triagem.

## 

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parametrizador | Alteração | Configurações ->Parametrizador | - |
| Perfil de Vagas | Alteração | Seleção -> Perfil de Vagas | - |
| Vagas da Seleção | Alteração | Seleção -> Seleções -> Vagas da Seleção | - |
| Etapas de vagas de seleção | Alteração | Seleção > Seleções > Vagas da Seleção > Etapas do Perfil de Vaga | - |
| Transferir candidatos entre vagas/seleções | Inclusão | Seleção > Seleções > Vagas da Seleção > Etapas do Perfil de Vaga > Processos | - |
| Voltar candidato transferido | Inclusão | Seleção > Seleções > Vagas da Seleção > Etapas do Perfil de Vaga > Candidatos > Processos | - |
| Triagem | Alteração | Seleção > Triagem | - |
| Iniciar processo de seleção | Alteração | Seleção > Seleções > Vagas da Seleção > Etapas do Perfil de Vaga | - |
| Visão de Etapas Paralelas | Inclusão | Seleção > Painel de Seleção | - |

**1 – PERFIS DE VAGAS COM ETAPAS PARALELAS**

Esta funcionalidade está sendo desenvolvida de acordo com as necessidades do processo de Recrutamento e Seleção (R&S) do Grupo Contax. Devido ao dinamismo do processo de R&S e da volumetria de candidatos avaliados por dia, as etapas de um processo seletivo não poderiam ser executadas de forma sequencial (forma padrão), respeitando o encerramento da etapa anterior para só então iniciar a etapa consecutiva. O processo seletivo ocorre duas vezes ao dia em média, com duração de cerca de 4 horas cada um e os comparecimentos espontâneos para o R&S da Contax também são frequentes, ou seja, existem candidatos iniciando e percorrendo as etapas do Processo Seletivo (PS) a todo momento, o que justifica a utilização das Etapas no formato “Etapas Paralelas”.

Para possibilitar que várias etapas de uma mesma vaga possam estar “Em andamento” simultaneamente, será criada no cadastro de Perfis de Vagas uma classificação de “Andamento de etapas”. A forma sequencial que o sistema trabalha atualmente será o andamento padrão, porém será criado o tipo “Etapas Paralelas”. Em perfis de vagas do tipo “Etapas Paralelas” não haverá controle sequencial de etapa. Nesse formato o que se espera é que os candidatos cumpram as etapas, não sendo obrigatório seguir uma ordem predefinida. Nesse caso, os processos de mudança de status de etapas não serão aplicáveis.

Ao criar uma vaga de seleção, as preferências da vaga serão carregadas automaticamente. Antes de iniciar o processo de seleção, o usuário poderá alterar o “Andamento de etapas” da vaga, seja de sequencial para etapas paralelas ou o contrário.

Os candidatos, quando entrarem numa vaga do tipo “Etapas Paralelas”, seja por triagem, transferência ou inclusão manual, serão incluídos automaticamente com o status “Pendente de análise” em todas as etapas. Deverão ser registradas as aprovações, reprovações ou transferências normalmente para os candidatos.

Conclusão de etapas paralelas:

* A conclusão de etapas em vagas com etapas paralelas deve apenas alterar o status da etapa, e não fazer qualquer transferência de candidatos.

Comportamento em etapas pais e filhas:

* Não deve ser permitido transferir candidatos entre etapas filhas se for vaga com etapas paralelas.
* Para etapas pais, ao concluir uma etapa com esta característica, não deve ser feita a inclusão dos candidatos aprovados nas etapas filhas.
* Para etapas filhas, ao concluir uma etapa com esta característica, não deve ser feita a inclusão dos candidatos aprovados na etapa posterior às filhas.

**2 – ETAPAS OBRIGATÓRIAS E PREDECESSORAS**

Tanto para perfis de vagas com etapas sequencias quanto com etapas paralelas, as etapas deverão ter um flag para informar "Etapa obrigatória". Ao tentar incluir candidatos em processo de admissão ou movimentação, o sistema deverá verificar se os candidatos selecionados estão aprovados em todas as etapas obrigatórias. Em caso negativo, o sistema deverá avisar ao usuário através de uma mensagem de alerta que há etapas obrigatórias não aprovadas. Este aviso também deverá informar se o candidato foi transferido para esta vaga a partir de outra vaga existente. Nenhuma das duas informações impedirá a execução do processo.

Para vagas com andamento de etapas do tipo “Etapas paralelas”, será possível identificar etapas Predecessoras. Com esse recurso é possível, mesmo não obedecendo uma ordem de etapas, estabelecer regras de dependência entre as etapas.  
Numa etapa que possua etapas predecessoras, o candidato só poderá ter o status alterado (Aprovar ou Reprovar) caso seu desempenho nas etapas predecessoras já tenha sido devidamente registrado, não estando Pendente de Análise. Caso um usuário tente alterar o status de um candidato numa etapa e o candidato esteja pendente em etapas predecessoras, o sistema não permitirá que a ação seja executada e deverá informar ao usuário o motivo e as etapas que estão bloqueando a ação.

As etapas e obrigatórias predecessoras serão definidas dentro do cadastro de uma etapa pertencente a um perfil de vaga. Quando uma vaga for incluída numa seleção, ao carregar as informações das etapas, serão carregadas também as obrigatoriedades e predecessoras definidas no perfil de vaga. Essas informações poderão ser personalizadas na vaga, incluindo ou excluindo novas dependências e mudando a obrigatoriedade de etapas.  
A alteração dessas informações durante o andamento da seleção é permitida, porém não haverá validação das alterações de status já realizadas. Dessa forma as novas regras serão aplicadas somente às novas alterações de status dos candidatos.

**3 – TRANSFERÊNCIA DE CANDIDATOS**

Será criado um assistente chamado “Transferir candidatos entre vagas/seleções”, que será disponibilizado a partir de **Planejamento e Captação > Seleções > Perfis de Vaga > Etapas > Candidatos.**

O objetivo é permitir a transferência de candidatos entre vagas de seleção distintas para aproveitamento de candidatos que possam participar de outros processos de seleção, e dessa forma otimizar a gerência de informações da tarefa de recrutamento.

Não será permitido transferir candidatos entre etapas de uma mesma vaga, numa mesma seleção (avançar ou retroceder o candidato).

**Regras para transferência de candidatos**:

a. Origem: vagas com etapas sequenciais:  
Os candidatos poderão ser transferidos a partir da última etapa (mais recente) que estejam, podendo ser:

* Etapa com status Em Andamento;
* Qualquer etapa Concluída onde o candidato tenha sido reprovado e esteja com status “Reprovado” ou status “Pendente de Análise” (ou seja, não está em etapas seguintes);
* Etapa final onde o candidato esteja com o status “Aprovado” (ou seja, não está em etapas seguintes).

b. Origem: vagas com etapas paralelas:  
Os candidatos poderão ser transferidos a qualquer momento.

c. Destino: vagas com etapas sequenciais:  
Em vagas sequenciais, a regra de transferência de candidatos será aplicada somente para etapas com status “Em Andamento”, ou seja, as etapas de destino deverão obrigatoriamente possuir o status “Em Andamento”.

d. Destino: vagas com etapas paralelas:  
A transferência para vagas do tipo “Etapas Paralelas”, permitirá que os candidatos sejam inclusos automaticamente em todas as etapas da vaga, com o status “Pendente de análise”.

No momento de transferir um candidato, o usuário terá a opção de mover o candidato na etapa atual (etapa de origem). Caso opte por mover, o candidato será incluído na nova etapa (etapa de destino) e terá o status alterado para “Transferido” na etapa de origem. Candidatos com status “Transferido” não podem ser aprovados, reprovados ou voltar para pendente de análise.

O processo poderá ser acionado com a seleção de um ou mais candidatos, mas no momento da execução poderá não ser efetivado para todos por validações do processo. Um candidato não pode ser movido para uma etapa que ele já esteve anteriormente. Além disso, as regras descritas acima serão verificadas neste momento e somente os candidatos que atendam às regras poderão ser transferidos.

Ao ser acionado o processo, será exibida uma interface para a escolha do destino da transferência. Os seguintes campos deverão ser informados:

* Seleção: Seleção destino da transferência. Não podem ser escolhidas seleções com data de fechamento menor que a data atual. Campo obrigatório.
* Vaga: Perfil de vaga destino da transferência. Serão exibidos perfis de vaga existentes na seleção escolhida no campo anterior. Não podem ser escolhidos perfis de vaga com data de fechamento menor que a data atual. Nunca será exibida a vaga que origina a transferência. Campo obrigatório.
* Etapa: Etapa destino da transferência. Serão exibidas as etapas existentes no perfil de vaga escolhido no campo anterior e que estejam com status “Em andamento”, para o caso de etapas Sequenciais. Não poderão ser escolhidas etapas com data de fechamento menor que a data atual. Campo obrigatório. Esse campo não será informado caso a vaga destino seja do tipo “Etapas Paralelas”.
* Motivo da transferência: Campo onde poderá ser informado um texto para justificar a transferência. Campo opcional.

Ao executar o processo, o sistema irá:

* Se o destino for do tipo sequencial, criar um novo registro de candidato na etapa de destino com o candidato transferido. Se for do tipo “Etapas Paralelas”, o candidato será incluído automaticamente em todas as etapas.
* O status do candidato será “Pendente de análise” e a “Data de Entrada” será a data/hora da execução do processo.
* No campo “Observações” dos registros criados, deverá ser incluído um texto informando que o candidato foi transferido a partir de outra seleção, e informar qual seleção, vaga e etapa origem da transferência. O motivo da transferência, se informado, deverá ser acrescentado a esse texto.
* No registro criado (vários, ser for uma vaga com etapas paralelas), deverá ser gravada a chave que identifica a origem da transferência. Essa informação será necessária para o eventual retorno do candidato à etapa original.
* No campo “Observações” do registro original, deverá ser incluído um texto informando que o candidato foi transferido para outra seleção, e informar qual para qual seleção, vaga e etapa se deu a transferência. O motivo da transferência, se informado, deverá ser acrescentado a esse texto.
* O candidato terá o flag “Transferido” marcado na etapa que originou a transferência. O campo “Data de Saída” deverá ser atualizado com a data/hora da transferência.

O campo “Transferido” deverá ser exibido na visão dos candidatos de etapas e deverá ser possível aplicar filtros com este campo.  
Um candidato transferido não poderá mais ter o status alterado, bem como não será incluído na etapa seguinte, mesmo tendo status aprovado no momento da conclusão da etapa atual.

Se o usuário tentar incluir um candidato transferido em processo de admissão ou de movimentação, o sistema deverá alertar o usuário sobre a transferência para outra vaga. Essa mensagem será informativa e não impossibilitará a continuação do processo.

**4 – VOLTAR CANDIDATO TRANSFERIDO**

Utilizando vagas com etapas do tipo “Sequencial”, se o usuário transferir um candidato por engano, não será possível reativar o candidato na etapa de origem. Por esse motivo, é necessário criar um assistente para desfazer uma transferência feita por engano. Esse assistente deverá ser disponibilizado na visão de candidatos de etapa.

Em vagas com etapas sequenciais, o candidato recém transferido deverá estar na mesma etapa para a qual foi transferido e ainda com o status “pendente de análise”. Se ele avançou para etapas seguintes devido à conclusão de etapas, não será possível desfazer a transferência.

Em vagas com etapas paralelas, o candidato recém transferido possuirá status “pendente de análise” em todas as etapas para que seja possível desfazer a transferência.

O sistema deverá detectar qual foi a última vaga e etapa que o candidato esteve e retorná-lo para esta etapa com o status “pendente de análise”. Para detectar a última vaga e etapa, o sistema verificará os campos que identificam a origem e que foram preenchidos no momento da transferência.

O candidato será removido da etapa atual e será registrado um histórico. Deve ser registrado o histórico deste procedimento no campo de observações do registro original do candidato que havia sido transferido. O campo “Transferido” terá o valor atualizado para null.

**5 – TRIAGEM**

A triagem deverá ser aprimorada e terá as seguintes possibilidades:

* Informar uma lista de Níveis Hierárquicos desejados. Quando informados, os itens desta lista deverão ser utilizados no momento da execução da triagem para buscar candidatos que atendam às preferências definidas no cadastro da triagem. Para ser selecionado na triagem, no currículo do candidato, o nível hierárquico deve estar preenchido com um dos níveis definidos na triagem.
* Lista de competências e as graduações desejadas nos candidatos a serem triados. Além de informar quais competências deseja e as suas respectivas graduações mínimas e máximas, o usuário poderá escolher se deseja triar candidatos que possuam todas ou uma das competências nas graduações informadas.
* Lista de requisitos de acesso desejados nos candidatos a serem triados. Além de informar quais requisitos deseja, o usuário poderá escolher se deseja triar candidatos que possuam todos ou um dos requisitos informados. Também poderá escolher de se deseja considerar como válidos os requisitos de acessos que por ventura estejam expirados na data de execução da triagem.
* Limite de vagas simultâneas que o candidato pode participar: este campo, do tipo numérico, deverá ser informado caso o usuário queira que a triagem verifique se os candidatos triados já estão participando de seleções e estão ativos nelas, e limite a quantidade de seleções nessas condições que um candidato pode estar. Por exemplo: se o candidato já está participante de uma seleção e a triagem limita em 1 (um) o número de vagas simultâneas, esse candidato, mesmo atendendo aos requisitos da triagem, não será incluído na seleção. Considera-se que um candidato encontra-se ativo numa vaga de seleção:
  + Com etapas sequenciais: a vaga está com status “Em Andamento” e o candidato encontra-se com status Aprovado ou Pendente de Análise na etapa que estiver “Em andamento”.
  + Com etapas paralelas: a vaga está com status “Em Andamento” e o candidato não se encontra Eliminado.
* Não triar candidatos que participaram de vagas de seleção concluídas nos últimos X meses ou que ainda estejam abertas. Esta opção deverá permitir que o usuário informe um número (inteiro) de meses e, a partir dessa informação, a triagem irá eliminar candidatos que tenham participado de processos seletivos no intervalo definido.

Na visão de candidatos de uma etapa, deverá ser incluída uma coluna que indica se o candidato se matriculou pelo portal para a vaga.

Atualmente, a Triagem só pode ser executada quando a vaga está na primeira etapa. A partir desta implementação, para vagas do tipo “Etapas Paralelas”, a execução da Triagem será permitida mesmo após os candidatos já estarem sendo movimentados entre das etapas. Neste caso, todos os candidatos que já estão no processo serão mantidos, com os seus respectivos status. e aqueles identificados na triagem que não estejam no processo, serão acrescentados. Para vagas do tipo "Sequencial", o atual comportamento será mantido ("Iniciar Processo de Seleção").

**6 – VISUALIZAÇÃO DE ETAPAS PARALELAS**

Para possibilitar uma visualização consolidada do andamento das etapas dos candidatos de uma vaga de seleção, deverá ser criada uma visão que demonstre para uma determinada vaga, quais etapas cada candidato já cumpriu e qual o status. Dessa forma o usuário conseguirá acompanhar o progresso da seleção de forma facilitada, sem precisar entrar em cada etapa para ver seus candidatos.

Além dos status dos candidatos nas etapas, também será possível visualizar se há transferência e eliminação de candidatos, e a partir de qual etapa foi tomada a ação. No Painel de Seleção, quando uma vaga do tipo “Etapas Paralelas” for selecionada, será exibido um checkbox que, quando marcado, exibirá a visualização de Etapas Paralelas. Protótipo 01.

A partir da visão de Etapas Paralelas, será possível executar as seguintes ações:

**Aprovar/Reprovar/Pendente:**

Este assistente deverá permitir que o usuário, a partir da seleção de candidatos, possa trocar o status dos candidatos para Aprovado, Reprovado ou Pendente de Análise, da seguinte forma:

* Ao acionar o assistente, o usuário escolherá qual dos status acima deseja aplicar aos candidatos.
* Em seguida o usuário poderá escolher para quais etapas ele deseja aplicar o novo status.
* Poderá também incluir um texto explicativo para justificar a alteração proposta.

Todas trocas de status ficarão registradas no campo “Observações” do candidato. Os status escolhidos sobrescreverão os status anteriores das etapas para os candidatos selecionados.

Candidatos transferidos não poderão sofrer alteração de status na etapa de origem.

**Eliminação de candidatos:**

Em vagas com etapas paralelas, nos registros de etapas dos candidatos haverá um flag que indicará que o candidato foi eliminado. Assim será possível identificar a origem da eliminação e manter os status das etapas.

Um candidato será considerado eliminado da vaga se tiver com o flag “Eliminado” marcado para qualquer uma das etapas da vaga. Após ser eliminado, um candidato não poderá ser transferido, aprovado, reprovado ou ainda ser incluído em processo de admissão ou movimentação.

No processo de reprovação de candidatos em vagas com etapas paralelas, o usuário terá a opção de eliminar o candidato, independentemente da etapa ser obrigatória ou não. Neste caso, o usuário deverá informar a etapa que causou a eliminação (Protótipo 02).

Será possível voltar um candidato eliminado para a vaga. Para isso o usuário deverá voltar o candidato para Pendente de Análise na etapa que originou a eliminação. Essa permissão será atribuída de acordo com o Perfil de acesso do usuário.

**Transferir candidato:**

O processo de transferência de candidatos estará disponível e poderá ser utilizado normalmente. O usuário deverá informar a etapa que originou a transferência, pois ela terá o flag “Transferido” marcado.

**7 – SERVIÇOS DE CANDIDATURA**

Deverão ser disponibilizados pelo RM serviços que possam ser acessados pelo Fluig para indicar a candidatura e a desistência de candidatos em vagas de seleção.   
O serviço de candidatura será responsável por identificar dentro do RM que determinado candidato candidatou-se espontaneamente a uma determinada vaga. No caso da Contax isso poderá acontecer com MOI (Mão-de-obra indireta).  
Os serviços deverão receber como parâmetro o código da pessoa e a chave primária da vaga (CODCOLIGADA, CODSELECAO, CODVAGA). Os serviços irão atualizar as informações contidas na tabela VRSSELECOESVAGASCANDIDATOS, que armazena o vínculo entre vagas e candidatos que se inscreveram diretamente à vaga por meio do Portal.

## 

## Protótipos de Tela

**Protótipo 01**

****Protótipo 02****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
