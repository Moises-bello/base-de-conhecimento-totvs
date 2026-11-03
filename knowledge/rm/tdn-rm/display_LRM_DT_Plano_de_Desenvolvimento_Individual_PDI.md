---
content_hash: e08753d5bba3943af0da2735ccbb35ab216706cac86b52db12aa4cb7b3436860
fetched_at: '2026-06-29T00:06:27.175577+00:00'
page_id: '231899364'
product: rm
source: tdn-rm
title: DT_Plano_de_Desenvolvimento_Individual_PDI
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Plano_de_Desenvolvimento_Individual_PDI
version: 3
---

# Plano de Desenvolvimento Individual

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | PDI | pdi | |
| **Versões/Release:** | *12.1.4* |

## Descrição

O Plano de Desenvolvimento Individual (PDI) tem como objetivo planejar, executar e acompanhar o desenvolvimento individual de cada profissional, visando atender as necessidades estratégicas internas, de sua função/cargo e do desenvolvimento pessoal/profissional.

Pontos de impacto do PDI:   
1) Gestão de Metas: Utiliza a estrutura de metas e seu acompanhamento para criar as ações e lançamentos de completude.   
2) Requisitos de Acesso: Realiza a concessão de requisitos de acesso, ao realizar o cumprimento de ações.   
3) Levantamento das necessidades de treinamento e desenvolvimento: Utiliza o resultado de uma LNTD para gerar plano de sugestões de ações.  
 4) Mapa de conhecimento: Utiliza o mapa de conhecimento do funcionário para gerar plano de sugestões de ações.   
5) Avaliação de desempenho: Utiliza a estrutura de participantes de uma AD no gerenciamento do PDI.   
6) Questionários da Avaliação de Desempenho: Exibe os questionários respondidos na AD no gerenciamento do PDI.   
7) E-mail Customizado: Utilizado para enviar e-mail para os avaliadores.

## Procedimento para Utilização

**1 – Cadastro**

Acessar Acompanhamento| PDI para criar um novo registro.

Cód. PDI: campo descritivo que contém identificador único;   
Descrição: campo descritivo para nomear o PDI;   
Data Início/Data Fim: campo que controla a data de início e data limite para execução;   
Permitir visualizar próprio PDI: campo que determina se um colaborador pode visualizar o seu próprio PDI na tela de gerenciamento no Totvs Portal;   
Permitir ao próprio avaliado definir seu PDI: campo que determina se um colaborador pode definir/gerenciar o seu próprio PDI na tela de gerenciamento no Totvs Portal.   
Este campo somente será habilitado se o campo “Permitir visualizar próprio PDI” estiver marcado;   
Utiliza metas para o desenvolvimento de requisitos de acesso: campo que determina se o PDI em questão possuirá suporte à utilização de requisitos de acesso nas ações (metas) do PDI, ou seja, se o colaborador avaliado pode receber requisitos de acesso a partir do cumprimento das ações definidas em seu plano de desenvolvimento;  
Preenchimento de requisito de acesso obrigatório: campo que determina se o preenchimento do requisito de acesso ao criar ação no Totvs Portal é obrigatório.   
Este campo só poderá ser marcado, caso o campo "Utilizar metas para o desenvolvimento de requisitos de acesso" esteja marcado;   
Habilitar sugestões de ações para o funcionário: campo que determina que no Totvs Portal o usuário terá acesso a funcionalidade Sugestão de Ação.   
Este campo só poderá ser marcado, caso o campo "Utilizar metas para o desenvolvimento de requisitos de acesso" esteja marcado;   
Tipos de restrição para associação de requisitos à metas: campo que determina o tipo de restrição que o sistema irá realizar nos requisitos de acesso que estarão disponíveis no PDI.   
Este campo só poderá ser marcado, caso o campo "Utilizar metas para o desenvolvimento de requisitos de acesso" esteja marcado;

Uma vez definido que um PDI possuirá suporte à gestão de Requisitos de Acesso, será necessário definir os tipos de requisitos que poderão ser utilizados no processo.   
Para isso o campo “Tipos de restrição para associação de requisitos à Metas” possuirá as opções que restringem à utilização dos requisitos, que são:   
    - Exibir somente requisitos definidos na meta   
    - Exibir somente requisitos definidos no mapa de conhecimento do funcionário   
    - Exibir somente requisitos definidos na meta e que estejam definidos no mapa de conhecimento do funcionário   
    - Sem restrição

Observações: campo descritivo que contém observações gerais sobre o PDI em questão;   
Instruções: campo de texto livre que deve conter informações sobre o PDI e que serão exibidas ao usuário na tela de gerenciamento de PDI no Totvs Portal;   
Gestão de Metas: campo que deve conter uma meta base do tipo “agrupadora” que contém metas associadas para serem a base da criação das ações no PDI para os avaliados;

   Ao acionar o botão “Incluir todas as metas associadas”, serão adicionadas neste campo todas as metas associadas à meta Pai e estas serão a base para criação das ações dos avaliados do PDI através do Totvs Portal;

Avaliação de Desempenho: campo que contém o código de uma Avaliação de Desempenho e realiza o vínculo da mesma com o PDI em questão. Uma vez definido este vínculo, o PDI utilizará a estrutura de participantes existente na Avaliação de Desempenho e criará uma estrutura de participantes idêntica. Contudo, para que esta estrutura seja gerada, o usuário deverá executar o processo "Gerar PDI a partir da AD associada";   
Liberar PDI somente após encerramento da AD: campo que determina que o PDI somente ficará disponível para utilização, no Totvs Portal, após o encerramento da AD vinculada.

**2 – Execução do PDI**   
**2.1 – Com Avaliação de Desempenho associada**

1) Acessar Acompanhamento | PDI e executar o processo "Gerar PDI a partir da AD associada".   
2) Acessar Acompanhamento| PDI, Anexos| Participantes. Todos os participantes da AD associada serão visualizados como participantes do PDI. O anexo de Participantes é um recurso baseado na “Exibição Modularizada de Participantes”, que fornece uma visão da estrutura hierárquica de avaliadores e seus avaliados de um determinado módulo do sistema, com algumas informações sobre estes participantes.   
Neste anexo é possível acessar os dados do cadastro de pessoa de cada participante através dos botões “Dados do avaliador” e “Dados do avaliado”.

     \*\*\*Para saber mais informações sobre as funcionalidades disponibilizadas para as telas que utilizam a exibição modularizada, o documento “Exibição Modularizada de Participantes” deve ser consultado.

3) Alterações pontuais na estrutura de participantes podem ser realizadas através dos processos do anexo de Participantes: Inserir Participantes, Excluir Participantes e Substituir Avaliador.

     Processo Excluir Participantes: se todos os avaliados foram excluídos, automaticamente o avaliador será excluído.  
     Processo Substituir Avaliador: se o campo “Manter respostas do atual avaliador” estiver marcado, e o avaliador que estiver sendo substituído já possuir avaliações respondidas, as respostas serão mantidas no momento da substituição, caso contrário, as respostas serão            removidas. Se o campo “Substituir avaliador atual para todos os seus avaliados” estiver marcado, o avaliador será substituído para todos os avaliados e não somente para o avaliado selecionado.

4) Se desejar encaminhar e-mail para os avaliadores do PDI, com as informações do processo, acessar Acompanhamento| PDI e executar o processo “Enviar e-mail para os avaliadores do PDI”. Nesta tela, se o parâmetro “Enviar somente para PDI’s não iniciados” estiver marcado, os e-mails devem ser enviados a todos os avaliadores que não iniciaram o processo de PDI, caso contrário, se o parâmetro estiver desmarcado, os e-mails devem ser enviados a todos os avaliadores.

   \*\*\*Este processo foi construído baseado no recurso de \*”E-mail Customizado”. Maiores informações podem ser consultadas através do documento “E-mail Customizado”.

5) Acessar Totvs Portal| Recursos Humanos| Gestão por competências| PDI. Respeitando os parâmetros de definição no cadastro do PDI, os usuários avaliadores/avaliados poderão gerenciar o PDI através do Portal.  
O funcionamento da gerência de PDI consiste basicamente na definição de ações que o avaliado deve executar para se desenvolver individualmente em um prazo determinado, assim como o lançamento do percentual de completude de cada ação definida. Sendo assim, tanto a definição das ações quanto a atualização da completude, podem ser realizados pelo avaliador ou pelo avaliado. Contudo, toda alteração realizada por um avaliado é submetida à aprovação de seu avaliador.

   \*\*\*Para saber mais informações sobre as funcionalidades disponibilizadas no Totvs Portal, consulte as informações adicionais deste documento.

6) Se no cadastro do PDI foi marcado o campo “Habilitar sugestões de ações para o funcionário”, no Totvs Portal será habilitado a opção “Carregar sugestões de ação”.  
A sugestão de ação é uma rotina baseada nos requisitos a desenvolver dos avaliados do PDI apontadas através do mapa de conhecimento por requisito de acesso e por competências.   
Quando acionada a opção “Carregar sugestões de ação”, será visualizada uma listagem com os requisitos a desenvolver do colaborador, conforme a regra de exibição de requisitos definidos no cadastro de PDI, campo “Tipos de restrição para associação de requisitos à metas”. Deve ser selecionado um requisito e o tipo de ação para que seja lançado uma ação no PDI. As ações serão criadas com o status “aguardando complemento”, sendo necessário editar a ação criada e preencher as informações obrigatórias faltantes da ação, como: objetivo e prazo de conclusão.

Após o preenchimento completo das ações o sistema irá disponibilizá-las para uso com a possíveis situações:   
-“Ação sem pendências” caso seja o gestor que esteja preenchendo o PDI;  
 - “Inclusão de PDI aguardando aprovação de Gestor”, caso seja o próprio funcionário (avaliado) a preencher as informações.

Observação: Na tela de sugestões de ações, serão listados separadamente os requisitos que deveriam ser sugeridos, mas que não possuem metas definidas para desenvolvimento no PDI. Caso o funcionário já possua ações criadas a partir de requisitos sugeridos, o sistema irá marcar estes requisitos com o caractere \* (asterisco).

A rotina de sugestões de ações possui ainda uma funcionalidade onde o sistema provê sugestões de ação para os colaboradores baseadas nos resultados de um LNTD (Levantamento de Necessidades de Treinamento e Desenvolvimento). Desta forma, ao invés de serem carregadas sugestões baseadas nos itens a se desenvolver do mapa de conhecimento do funcionário, serão apresentadas sugestões baseadas nos resultados de uma LNTD em que o funcionário for indicado.   
Para que as sugestões por LNTD fiquem disponíveis, deve ser executado o processo “Carregar sugestão de ação por LNTD” disponível em Acompanhamento| PDI. Neste processo deve ser informado o LNTD desejado, para que sejam carregadas as sugestões para todos os participantes do PDI.

**2.2 – Sem Avaliação de Desempenho associada**

1) Acessar Acompanhamento| PDI, selecionar um PDI e executar o processo “Configurar Participantes”. Após a execução do processo no anexo “Participantes” serão visualizados todos os participantes do PDI.   
O processo Configurar Participantes é um recurso baseado no “Processo Modularizado de Montagem de Participantes”, que fornece uma infraestrutura para criação e manipulação de estruturas hierárquicas de avaliadores e seus avaliados. Nesta tela de configuração de participantes, poderão ser feitas as operações de adição/exclusão de avaliadores e avaliados respeitando o período de execução do PDI.

   \*\*\*Para saber mais informações sobre as funcionalidades disponibilizadas para as telas que utilizam a montagem modularizada, o documento “Processo Modularizado de Montagem de Participantes” deve ser consultado.

2) Acessar Acompanhamento| PDI, Anexos| Participantes. O anexo de Participantes é um recurso baseado na “Exibição Modularizada de Participantes”, que fornece uma visão da estrutura hierárquica de avaliadores e seus avaliados de um determinado módulo do sistema, com algumas informações sobre estes participantes.   
Neste anexo é possível acessar os dados do cadastro de pessoa de cada participante através dos botões “Dados do avaliador” e “Dados do avaliado”.

   \*\*\*Para saber mais informações sobre as funcionalidades disponibilizadas para as telas que utilizam a exibição modularizada, o documento “Exibição Modularizada de Participantes” deve ser consultado.

3) Alterações pontuais na estrutura de participantes podem ser realizadas através dos processos do anexo de Participantes: Inserir Participantes, Excluir Participantes e Substituir Avaliador.  
     Processo Excluir Participantes: se todos os avaliados foram excluídos, automaticamente o avaliador será excluído.   
     Processo Substituir Avaliador: se o campo “Manter respostas do atual avaliador” estiver marcado, e o avaliador que estiver sendo substituído já possuir avaliações respondidas, as respostas serão mantidas no momento da substituição, caso contrário, as respostas serão removidas. Se o campo “Substituir avaliador atual para todos os seus avaliados” estiver marcado, o avaliador será substituído para todos os avaliados e não somente para o avaliado selecionado.

4) Se desejar encaminhar e-mail para os avaliadores do PDI, com as  informações do processo, acessar Acompanhamento| PDI e executar o processo “Enviar e-mail para os avaliadores do PDI”. Nesta tela, se o parâmetro “Enviar somente para PDI’s não iniciados” estiver marcado, os e-mails devem ser enviados a todos os avaliadores que não iniciaram o processo de PDI, caso contrário, se o parâmetro estiver desmarcado, os e-mails devem ser enviados a todos os avaliadores.

   \*\*\*Este processo foi construído baseado no recurso de \*”E-mail Customizado”. Maiores informações podem ser consultadas através do documento “E-mail Customizado”.

5) Acessar Totvs Portal| Recursos Humanos| Gestão por competências| PDI. Respeitando os parâmetros de definição no cadastro do PDI, os usuários avaliadores/avaliados poderão gerenciar o PDI através do Portal.

O funcionamento da gerência de PDI consiste basicamente na definição de ações que o avaliado deve executar para se desenvolver individualmente em um prazo determinado, assim como o lançamento do percentual de completude de cada ação definida. Sendo assim, tanto a definição das ações quanto a atualização da completude, podem ser realizados pelo avaliador ou pelo avaliado. Contudo, toda alteração realizada por um avaliado é submetida à aprovação de seu avaliador.

    \*\*\*Para saber mais informações sobre as funcionalidades disponibilizadas no Totvs Portal, consulte as informações adicionais deste documento.

6) Se no cadastro do PDI foi marcado o campo “Habilitar sugestões de ações para o funcionário”, no Totvs Portal será habilitado a opção “Carregar sugestões de ação”.   
A sugestão de ação é uma rotina baseada nos requisitos a desenvolver dos avaliados do PDI apontadas através do mapa de conhecimento por requisito de acesso e por competências.   
Quando acionada a opção “Carregar sugestões de ação”, será visualizada uma listagem com os requisitos a desenvolver do colaborador, conforme a regra de exibição de requisitos definidos no cadastro de PDI, campo “Tipos de restrição para associação de requisitos à metas”. Deve ser selecionado um requisito e o tipo de ação para que seja lançado uma ação no PDI. As ações serão criadas com o status “aguardando complemento”, sendo necessário editar a ação criada e preencher as informações obrigatórias faltantes da ação, como: objetivo e prazo de conclusão.

Após o preenchimento completo das ações o sistema irá disponibilizá-las para uso com a possíveis situações:  
 - “Ação sem pendências” caso seja o gestor que esteja preenchendo o PDI;   
- “Inclusão de PDI aguardando aprovação de Gestor”, caso seja o próprio funcionário (avaliado) a preencher as informações.

Observação: Na tela de sugestões de ações, serão listados separadamente os requisitos que deveriam ser sugeridos, mas que não possuem metas definidas para desenvolvimento no PDI. Caso o funcionário já possua ações criadas a partir de requisitos sugeridos, o sistema irá marcar estes requisitos com o caractere \* (asterisco).   
A rotina de sugestões de ações possui ainda uma funcionalidade onde o sistema provê sugestões de ação para os colaboradores baseadas nos resultados de um LNTD (Levantamento de Necessidades de Treinamento e Desenvolvimento). Desta forma, ao invés de serem carregadas sugestões baseadas nos itens a se desenvolver do mapa de conhecimento do funcionário, serão apresentadas sugestões baseadas nos resultados de uma LNTD em que o funcionário for indicado.   
Para que as sugestões por LNTD fiquem disponíveis, deve ser executado o processo “Carregar sugestão de ação por LNTD” disponível em Acompanhamento| PDI. Neste processo deve ser informado o LNTD desejado, para que sejam carregadas as sugestões para todos os participantes do PDI.

**Atenção**

Um aspecto importante que deve ser entendido sobre a tela de gerência de PDI é que todo seu funcionamento é integrado ao módulo de gestão de metas, ou seja, toda ação criada é uma meta do tipo “valor” que é gerada a partir das metas associadas ao PDI. Sendo assim, toda atualização de completude da ação, nada mais é que a atualização dos resultados para cumprimento de uma meta.  
Apesar da relação entre PDI e Metas funcionarem de forma transparente, as metas geradas pelo PDI podem ser visualizadas nos cadastros de metas, contudo estas mesmas metas não podem ser manipuladas ou visualizadas através do Painel de Metas (Totvs Portal).  
 **Em caso de dúvidas consulte o help do aplicativo ou entre em contato pelo Help Desk.**

# Informações Adicionais

Gerenciamento de PDI através do Totvs Portal

Visão geral:

Gerenciar – contém link de acesso para gerenciar o PDI do avaliado;   
Status – indica o status do PDI, que pode ser: Pendente (PDI que ainda não foi definido), Iniciado (PDI definido mas as ações não foram cumpridas) e Concluído (Quando as ações definidas foram todas cumpridas);   
Pendências – indica se o PDI possui pendência de aprovação pelo avaliador de uma nova ação ou lançamento ;   
Descrição – contém a descrição do PDI;   
Chapa – chapa do funcionário avaliado;   
Nome – Nome do funcionário avaliado;   
Avaliação de Desempenho – indica o nome da Avaliação de Desempenho vinculada ao PDI, caso exista;   
Data Início – data inicial do período para execução;   
Data Fim – data final do período para execução.

Tela de gerenciamento:  
 Excluir – Botão para exclusão da ação (Somente poderão ser excluídas ações que não tiveram lançamento e também se o PDI estiver dentro do período de execução);   
Editar – Botão para editar dados da ação (Somente podem ser editados os campos de objetivo da ação e prazo de cumprimento);   
Lançar atualização – Botão para efetuar um novo lançamento de percentual de completude da ação, com possibilidade de incluir um comentário;  
 Status – Informa qual o status da ação, que pode ser: Inclusão aguardando aprovação do avaliador, Ação sem pendências, Sugestões de PDI reprovadas pelo avaliador, Atualização aguardando aprovação do avaliador ou Ação aguardando complemento;   
Tipo de Ação – Informa o tipo de ação a ser desenvolvida pelo avaliado;   
Objetivo da Ação – Descreve o objetivo da ação a ser desenvolvida pelo avaliado;   
Requisito de Acesso – Informa o requisito de acesso associado à ação, ou seja, qual requisito será concedido ao funcionário caso ele cumpra a ação (100% de completude);   
Prazo para cumprimento – Contém a data limite para cumprimento da ação;   
Valor – É o valor percentual de completude da ação. Também é um link de acesso ao histórico de lançamento de completude da ação.

Nova ação - Para se incluir uma nova ação, nesta tela existe o botão Nova Ação onde é necessário informar os seguintes dados:   
Objetivo da ação – Devem ser descritos os objetivos do avaliado para cumprimento da ação;   
Tipo de ação – Deve ser descrito o tipo de ação que o usuário deve desenvolver. Neste campo serão listadas todas as metas filhas cadastradas na tela de definição do PDI;  
 Requisito de Acesso – Caso o parâmetro “Utiliza metas para o desenvolvimento de requisitos de acesso” esteja marcado no cadastro de PDI, esta opção estará disponível na criação da ação. Ao informar o Requisito de Acesso associado à ação, caso avaliado atinja100% nessa ação, o requisito de acesso será concedido ao avaliado. Os requisitos de acesso disponíveis para ação respeitarão o parâmetro “Tipos de restrição para associação de requisitos à Metas”. Se estiver marcado o parâmetro “Preenchimento de requisito de acesso obrigatório”, este campo se torna obrigatório;  
 Prazo para cumprimento - Deve ser informado o período para execução e cumprimento da ação.

“Aprovar/Reprovar Ações” e “Aprovar/Reprovar Atualizações” - Botões para “Aprovar/Reprovar Ações” e “Aprovar/Reprovar Lançamentos”. Contudo estes botões somente são exibidos para avaliadores. Caso seja aprovado um lançamento de 100% e ação criada possua Requisito de Acesso vinculado, este requisito será concedido ao perfil do avaliado no momento da aprovação;   
Para visualizar o histórico de lançamentos (% completude) de cada ação, na listagem existe a coluna valor que armazena um link de acesso ao histórico;  
 Caso o avaliado não necessite da definição de ações, o avaliador pode marcar o checkbox “Não será necessária nenhuma ação”, que seu PDI será considerado como concluído.
