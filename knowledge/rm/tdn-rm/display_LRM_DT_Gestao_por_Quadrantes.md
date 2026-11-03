---
content_hash: cd10637e8bd80535b44e702ce5be2b22a3716524b5799870ebc176585acb7ca0
fetched_at: '2026-06-29T00:06:27.147889+00:00'
page_id: '230916649'
product: rm
source: tdn-rm
title: DT_Gestao_por_Quadrantes
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Gestao_por_Quadrantes
version: 1
---

# Gestão por Quadrantes

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Acompanhamento | Gestão | |
| **Versões/Release:** | *12.1.4* |

## Descrição

A Gestão por Quadrantes tem como objetivo fazer a qualificação de colaboradores avaliados no processo de Avaliação de Desempenho – AD utilizando grupos (quadrantes) pré-definidos, agrupando esses avaliados de acordo com o resultado de sua avaliação. Utilizando o Totvs Portal, gestores ou revisores podem qualificar e requalificar todos estes participantes buscando o melhor grupo que enquadre o resultado de cada avaliado. Desta maneira é possível qualificar o perfil dos colaboradores da organização quanto ao potencial e seus resultados efetivos.   
Pontos de impacto da Gestão por Quadrantes:   
1) Avaliação de desempenho: Utiliza a estrutura de participantes de uma AD, para gerar uma estrutura própria.   
2) Filtro Customizado: Utiliza filtros do RM Portal para filtrar visualização da Gestão por Quadrantes no Totvs Portal.

## Procedimento para Utilização

**1 – Cadastro**

Acessar Acompanhamento / Gestão por Quadrantes para criar um novo registro.

Código: campo que contém identificador único;   
Status: campo que conterá o status da Gestão Por Quadrante. Este não é editável e pode conter somente os seguintes valores: Iniciada, Não iniciada ou Finalizada;   
Descrição: campo descritivo para nomear a Gestão Por Quadrante;   
Data de Abertura/Data Limite Execução: campo que controla a data de início/data limite de execução. Se a data limite de execução for menor do que a data de acesso do avaliador no Totvs Portal, o mesmo não poderá fazer mais alterações na gestão por quadrantes, somente visualizar.  
Data de Fechamento: campo que controla a data fechamento da gestão (campo de somente leitura). Se a gestão por quadrantes já tiver sido finalizada, este campo será preenchido e o avaliador não poderá mais fazer alterações na gestão por quadrantes.   
Observação: campo descritivo que contém observações gerais sobre a gestão;   
Tipo de Avaliação: campo que indica qual tipo de filtro estará disponível para gerência de quadrantes no Totvs Portal, sendo eles:   
- Cargo   
- Função   
- Grupo Ocupacional

Seleção de Avaliados: campo que indica que tipo de avaliado os avaliadores da gestão têm permissão de gerenciar através do Totvs Portal, sendo eles:  
- Avaliados diretos  
- Avaliados diretos e indiretos  
  
 Orientado a potencial e resultado: campo que determina se a Gestão por Quadrantes será em um plano cartesiano, destacando-se os eixos Potencial (eixo vertical) e Resultado (eixo horizontal).   
       \*\*\*Este campo somente pode ser marcado ou desmarcado no momento da criação da Gestão por Quadrantes.

Utiliza participantes de Avaliações de Desempenho: campo que determina se a Gestão por Quadrantes será baseada na estrutura de uma avaliação de desempenho, utilizando os seus participantes e resultados para compor a gestão.   
  
Avaliações: aba que informa todas as avaliações de desempenho vinculadas à Gestão por Quadrantes;   
      \*\*\*Este campo somente é habilitado e visível, se o campo “Utiliza participantes de avaliações de desempenho” estiver marcado. Somente poderão ser associadas as avaliações de desempenho encerradas.

Revisores: campo que informa usuários que possuem permissões para gerenciar a Gestão por Quadrantes em nome dos avaliadores cadastrados independente se a gestão estiver finalizada;   
      \*\*\*O revisor deve possuir permissão de acesso ao Totvs Portal, na funcionalidade Gestão por Quadrantes.

Quadrante: anexo responsável pela definição dos quadrantes (grupos) e seus valores para que sejam enquadrados os participantes da gestão. Desta forma, devem ser informados dois pares de valores, para representação de um grupo em um plano cartesiano, ou seja representado coordenadas de eixo X (potencial) e eixo Y (resultado).

- Quadrante Padrão: indica se o quadrante em questão é do tipo padrão, ou seja, caso algum participante não seja incluso nos quadrantes existentes devido aos critérios de valores definidos de cada quadrante, estes serão automaticamente inclusos no quadrante do tipo padrão. O sistema permite a criação de apenas um quadrante padrão.

- Ordenação: campo numérico que informa a ordem em que o quadrante será exibido na tela de gerenciar quadrantes no Totvs Portal;   
      \*\*\*Este campo ficará desabilitado caso a gestão por quadrantes seja do tipo “Orientada a potencial e resultado”.

- % Exigido: campo numérico que informa qual o percentual de participantes que a organização espera que esteja alocado no quadrante. A soma dos % da curva dos quadrantes deve ser igual a 100;

- Intervalo de Pontuação Potencial: campos do tipo numérico que descrevem à coordenada do eixo X (potencial) para definição do quadrante em um plano cartesiano;

- Intervalo de Pontuação Resultado: campos do tipo numérico que descrevem à coordenada do eixo Y (Resultado) para definição do quadrante em um plano cartesiano;

-Tipo de Quadrante: campo que fará uma sugestão para o nome do quadrante, caso a gestão por quadrantes seja do tipo “Orientada a potencial e resultado”. Esta sugestão é feita, pois a abordagem 4Box, trata de apenas 4 quadrantes que podem ser: “Alto Potencial | Baixo Resultado”, “Alto Potencial | Alto Resultado”, “Baixo Potencial | Baixo Resultado” ou “Baixo Potencial | Alto Resultado”. De acordo com os val ores de pontuação digitados o sistema automaticamente fará a sugestão do tipo de quadrante.

Informação Complementar do Participante: anexo que permite cadastrar consultas SQL para que sejam exibidas informações complementares do participante na tela de gerenciamento de quadrantes no Totvs Portal, quando o usuário posicionar o mouse sobre o avaliado. - Cód. Consulta SQL: campo do tipo lookup de consultas SQL que deve ser executado para exibir as informações complementares do participante. Contudo, somente podem ser informados consultas SQL que possuam os campos CHAPA e CODCOLIGADA.

**2 – Execução da Gestão por Quadrantes  
2.1 – Utilizando participantes da Avaliação de Desempenho**

1) Acessar Acompanhamento / Gestão por Quadrantes e executar o processo "Inicializar Gestão por Quadrantes". Este processo tem como objetivo verificar a nota potencial e resultado da avaliação de desempenho de cada avaliado e o colocará no respectivo quadrante de acordo com estas pontuações em relação as definições dos quadrantes. Após sua execução o status da gestão passa de “Não iniciada” para “Iniciada”.

Observações:   
- Caso não tenha sido definido nenhum quadrante padrão para esta Gestão Por Quadrantes e esta gestão seja baseada em uma Avaliação de Desempenho, participantes que não tiveram pontuação ou que tiveram uma pontuação que não se enquadram em nenhum dos quadrantes definidos, estes serão desconsiderados de todo o processo.   
- Durante a execução do processo serão realizadas as seguintes verificações:   
     - Verificar se o somatório do percentual da curva de todos os quadrantes associados à gestão é igual a 100;  
     - Verificar se os intervalos de pontuação de todos os quadrantes associados à gestão não entram em conflito;   
     - Verificar se as ordenações de todos os quadrantes não estão em conflito;   
     - Caso seja definido que a gestão é orientada por potencial e resultado, verifica se os 4 tipos de quadrantes foram definidos corretamente.

Caso não sejam cumpridas todas as consistências, a Gestão Por Quadrantes não será inicializada e disponibilizada para uso no Totvs Portal.

2) Acessar Acompanhamento / Gestão por Quadrantes, Anexos / Participantes. Todos os participantes da AD associada serão visualizados como participantes da gestão.

O anexo de Participantes é um recurso baseado na “Exibição Modularizada de Participantes”, que fornece uma visão da estrutura hierárquica de avaliadores e seus avaliados de um determinado módulo do sistema, com algumas informações sobre estes participantes. Neste anexo é possível acessar os dados do cadastro de pessoa de cada participante através dos botões “Dados do avaliador” e “Dados do avaliado”.   
     \*\*\*Para saber mais informações sobre as funcionalidades disponibilizadas para as telas que utilizam a exibição modularizada, o documento “Exibição Modularizada de Participantes” deve ser consultado.

3) Alterações pontuais na estrutura de participantes podem ser realizadas através dos processos do anexo de Participantes: Excluir Participantes e Substituir Avaliador.

Processo Excluir Participantes: se todos os avaliados foram excluídos, automaticamente o avaliador será excluído.   
Processo Substituir Avaliador: se o campo “Substituir avaliador atual para todos os seus avaliados” estiver marcado, o avaliador será substituído para todos os avaliados e não somente para o avaliado selecionado.

4) Se desejar encaminhar e-mail para os avaliadores da Gestão por Quadrantes, com as informações do processo, acessar Acompanhamento / Gestão por Quadrantes e executar o processo “Envio de E-mail de acesso ao Gestão por Quadrantes”.

O e-mail a ser enviado utilizará a estrutura de “mensagem livre” ou “relatório do sistema (gerador .NET)”, sendo que o relatório pode ser enviado no anexo do email. Nesta tela, se o parâmetro “Enviar somente para avaliadores que ainda não responderam” estiver marcado, os e-mails devem ser enviados a todos os avaliadores que não iniciaram o processo de Gestão por Quadrantes, caso contrário, se o parâmetro estiver desmarcado, os e-mails devem ser enviados a todos os avaliadores.

5) Acessar Totvs Portal / Recursos Humanos / Gestão por Quadrantes. A visão é composta por cabeçalho com filtros, o grid de acompanhamento e os quadrantes com os participantes.

Os participantes da gestão estarão distribuídos nos quadrantes de acordo com a nota obtida na avaliação de desempenho e o valor do intervalo do quadrante, conforme descrito no processo de inicialização. E somente serão exibidos nos quadrantes os participantes que o avaliador for gerir, ou seja, avaliados diretos e/ou indiretos.   
As opções de filtros são:   
- Responsável pela Fase: campo que indica o nome do funcionário avaliador da gestão em questão. Caso o usuário seja um avaliador, o lookup ficará desabilitado, mostrando o nome do mesmo. Caso o usuário logado não seja um avaliador, mas tenha permissão para revisão, o lookup ficará habilitado, onde será permitido selecionar o responsável pela gestão;   
- Filtro de Avaliação: campo que listará as entidades existentes, de acordo com a configuração da Gestão por Quadrante. As entidades poderão ser Função, Cargo ou Grupo Ocupacional. Se a gestão por quadrante foi configurada por função, no lookup serão listadas as funções dos avaliados por exemplo;   
- Filtro de Pessoas por Gestor: campo com os avaliados que são avaliadores (diretos e/ou indiretos) do responsável pela fase selecionado. Ao selecionar uma pessoa por gestor, será exibido os avaliados da gestão a partir da visão deste avaliador selecionado;   
- Filtro customizado: campo que irá listar os filtros do RM Portal configurados para a gestão por quadrantes. Para configurar estes filtros acessar Configurações / Filtros do RM Portal e editar a opção Gestão por Quadrantes;   
- Exibir avaliados diretos: campo que irá restringir a exibição para somente avaliados diretos;   
- Exibir avaliados indiretos: campo que irá restringir a exibição para somente avaliados indiretos.   
    \*\*\*Para saber mais informações sobre as funcionalidades disponibilizadas no Totvs Portal, consulte as informações adicionais deste documento.

6) Se desejar visualizar o histórico de respostas criadas de cada avaliado pelos avaliadores no Totvs Portal, acessar Acompanhamento / Gestão por Quadrantes, anexo “Respostas”.

7) Para finalizar a Gestão por Quadrantes, acessar Acompanhamento / Gestão por Quadrantes e executar o processo “Finalizar Gestão por Quadrantes”.

O processo irá concluir a execução da Gestão por Quadrante no Totvs Portal e disponibilizar o resultado final da gestão no anexo “Resultado final”. Neste anexo vai conter a última resposta realizada na Gestão por Quadrantes. Após sua execução o status da gestão passa de “Iniciada” para “Finalizada” e a data de fechamento e preenchida no cadastro da Gestão por Quadrantes.

**2.2 – Não utilizando participantes da Avaliação de Desempenho**

1) Acessar Acompanhamento / Gestão por Quadrantes e executar o processo "Inicializar Gestão por Quadrantes". Como não há nenhuma avaliação de desempenho associada à gestão, será aberto uma tela de gerência de configuração de participantes. Nesta tela, poderão ser feitas as operações de adição/exclusão de avaliadores e avaliados, antes da execução do processo. Ao terminar a seleção o sistema fará normalmente as consistências que foram explicitadas acima e ao inicializar todos os participantes serão destinados ao quadrante padrão obrigatoriamente.

Após a inicialização da gestão o status da gestão passa de “Não iniciada” para “Iniciada”.

Observações:  
- Durante a execução do processo serão realizadas as seguintes verificações:   
- Verificar se o somatório do percentual da curva de todos os quadrantes associados à gestão é igual a 100;  
 - Verificar se os intervalos de pontuação de todos os quadrantes associados à gestão não entram em conflito;  
 - Verificar se as ordenações de todos os quadrantes não estão em conflito;   
- Caso seja definido que a gestão é orientada por potencial e resultado, verifica se os 5 tipos de quadrantes foram definidos corretamente.

Caso não sejam cumpridas todas as consistências, a Gestão Por Quadrantes não será inicializada e disponibilizada para uso no Totvs Portal. O processo Configurar Participantes é um recurso baseado no “Processo Modularizado de Montagem de Participantes”, que fornece uma infraestrutura para criação e manipulação de estruturas hierárquicas de avaliadores e seus avaliados.

    \*\*\*Para saber mais informações sobre as funcionalidades disponibilizadas para as telas que utilizam a montagem modularizada, o documento “Processo Modularizado de Montagem de Participantes” deve ser consultado

2) Acessar Acompanhamento / Gestão por Quadrantes, Anexos / Participantes. O anexo de Participantes é um recurso baseado na “Exibição Modularizada de Participantes”, que fornece uma visão da estrutura hierárquica de avaliadores e seus avaliados de um determinado módulo do sistema, com algumas informações sobre estes participantes.   
Neste anexo é possível acessar os dados do cadastro de pessoa de cada participante através dos botões “Dados do avaliador” e “Dados do avaliado”.

    \*\*\*Para saber mais informações sobre as funcionalidades disponibilizadas para as telas que utilizam a exibição modularizada, o documento “Exibição Modularizada de Participantes” deve ser consultado.

3) Alterações pontuais na estrutura de participantes podem ser realizadas através dos processos do anexo de Participantes: Excluir Participantes e Substituir Avaliador.   
     Processo Excluir Participantes: se todos os avaliados foram excluídos, automaticamente o avaliador será excluído.   
     Processo Substituir Avaliador: se o campo “Substituir avaliador atual para todos os seus avaliados” estiver marcado, o avaliador será substituído para todos os avaliados e não somente para o avaliado selecionado.

4) Se desejar encaminhar e-mail para os avaliadores da Gestão por Quadrantes, com as informações do processo, acessar Acompanhamento / Gestão por Quadrantes e executar o processo “Envio de E-mail de acesso ao Gestão por Quadrantes”.

O e-mail a ser enviado utilizará a estrutura de “mensagem livre” ou “relatório do sistema (gerador .NET)”, sendo que o relatório pode ser enviado no anexo do email. Nesta tela, se o parâmetro “Enviar somente para avaliadores que ainda não responderam” estiver marcado, os e-mails devem ser enviados a todos os avaliadores que não iniciaram o processo de Gestão por Quadrantes, caso contrário, se o parâmetro estiver desmarcado, os e-mails devem ser enviados a todos os avaliadores.

5) Acessar Totvs Portal / Recursos Humanos / Gestão por Quadrantes. A visão é composta por cabeçalho com filtros, o grid de acompanhamento e os quadrantes com os participantes.

Os participantes da gestão estarão obrigatoriamente no quadrante padrão, conforme descrito no processo de inicialização. E somente serão exibidos nos quadrantes os participantes que o avaliador for gerir, ou seja, avaliados diretos e/ou indiretos.

As opções de filtros são:  
 - Responsável pela Fase: campo que indica o nome do funcionário avaliador da gestão em questão. Caso o usuário seja um avaliador, o lookup ficará desabilitado, mostrando o nome do mesmo. Caso o usuário logado não seja um avaliador, mas tenha permissão para revisão, o lookup ficará habilitado, onde será permitido selecionar o responsável pela gestão;   
- Filtro de Avaliação: campo que listará as entidades existentes, de acordo com a configuração da Gestão por Quadrante. As entidades poderão ser Função, Cargo ou Grupo Ocupacional. Se a gestão por quadrante foi configurada por função, no lookup serão listadas as funções dos avaliados por exemplo;   
- Filtro de Pessoas por Gestor: campo com os avaliados que são avaliadores (diretos e/ou indiretos) do responsável pela fase selecionado. Ao selecionar uma pessoa por gestor, será exibido os avaliados da gestão a partir da visão deste avaliador selecionado;   
- Filtro customizado: campo que irá listar os filtros do RM Portal configurados para a gestão por quadrantes. Para configurar estes filtros acessar Configurações / Filtros do RM Portal e editar a opção Gestão por Quadrantes;   
- Exibir avaliados diretos: campo que irá restringir a exibição para somente avaliados diretos;   
- Exibir avaliados indiretos: campo que irá restringir a exibição para somente avaliados indiretos.

     \*\*\*Para saber mais informações sobre as funcionalidades disponibilizadas no Totvs Portal, consulte as informações adicionais deste documento.

6) Se desejar visualizar o histórico de respostas criadas de cada avaliado pelos avaliadores no Totvs Portal, acessar Acompanhamento / Gestão por Quadrantes, anexo “Respostas”.

7) Para finalizar a Gestão por Quadrantes, acessar Acompanhamento / Gestão por Quadrantes e executar o processo “Finalizar Gestão por Quadrantes”.

O processo irá concluir a execução da Gestão por Quadrante no Totvs Portal e disponibilizar o resultado final da gestão no anexo “Resultado final”. Neste anexo vai conter a última resposta realizada na Gestão por Quadrantes. Após sua execução o status da gestão passa de “Iniciada” para “Finalizada” e a data de fechamento e preenchida no cadastro da Gestão por Quadrantes.

**Atenção**

A descrição da Gestão por Quadrantes pode ser alterada. Para isso deve acessar Configurações / Parametrizador / Gestão por Quadrantes e informar a nova descrição no campo “Descrição para Gestão por Quadrante”. Essa nova descrição será visualizada no Totvs Portal. Em caso de dúvidas consulte o help do aplicativo ou entre em contato pelo Help Desk.

# Informações Adicionais

**Gerenciamento da Gestão por Quadrantes através do Totvs Portal**

Visão geral:   
Gerenciar – contém link de acesso para gerenciar quadrantes;   
Código – código da gestão por quadrantes;  
 Status – indica o status da gestão que pode ser: Pendente ou Finalizada;   
Descrição – contém a descrição da gestão;   
Seleção de Avaliados – informa se a gestão será feita em função de avaliados diretos e/ou indiretos;   
Data da abertura – data da abertura da gestão;   
Data limite execução – data de limite de execução da gestão;   
Data de fechamento – data de fechamento da gestão.

Tela de gerenciamento:   
O quadro de Acompanhamento terá as seguintes informações:  
 - Total de Participantes: quantidade de avaliados do avaliador, de acordo com os filtros realizados;  
 - Análise: coluna com o nome dos quadrantes definidos na configuração da gestão por quadrante;   
- Percentual Exigido: percentual de avaliados que espera-se que esteja alocado no respectivo quadrante, definido na configuração da gestão por quadrante;   
- Exigido: quantidade de avaliados que espera-se que estejam alocados no respectivo quadrante, considerando a quantidade de avaliados e o percentual do quadrante;   
- Atual: quantidade atual de participantes em um quadrante;   
- Percentual Atual: percentual atual de avaliados no quadrante, considerando o total de participantes e a quantidade atual.   
- Ajuste: quantidade de participantes que deverão sofrer alterações de quadrante, de modo que seja respeitada a quantidade máxima/percentual;   
- Percentual de Ajuste: diferença entre o percentual exigido e o percentual atual.

Operações:   
- Por meio do recurso arrastar e soltar poderão ser movimentados os participantes entre quadrantes, atualizando automaticamente o quadro de acompanhamento para o determinado avaliador;   
    - Se o avaliado for alterado para um quadrante de avaliação superior, passará a ter seu nome destacado na cor azul.   
    - Se o avaliado for alterado para um quadrante de avaliação inferior, passará a ter seu nome destacado na cor vermelha.  
 - Visualização de informações complementares do avaliado, ao posicionar o mouse sobre o mesmo, e a possibilidade de realizar a inserção de comentários;   
- Para destacar um quadrante deve clicar no ícone "Destacar quadrante". Ao destacar um determinado quadrante, o “quadrante padrão” (quando houver) ocupará temporariamente a posição do quadrante que irá receber o destaque. Sendo assim, o quadrante padrão irá retornar à posição original no momento em que o quadrante em destaque for restaurado.   
- Finalização da gestão feita pelo avaliador. Este recurso encontra-se presente no botão “Finalizar”, onde cada avaliador após realizar os seus ajustes, fecha a gestão para que o avaliador hierarquicamente acima dele possa efetuar uma gestão sem interferências. Uma vez que um avaliador finaliza a sua gestão, todos os seus avaliados que são avaliadores terão a sua gestão finalizada, ou seja, não poderão realizar nenhuma alteração. Ao acessar o recurso de finalização serão apresentadas algumas informações sobre os avaliados, como Nome, Quadrante Anterior, Quadrante Atual, e um botão para inserir comentário rapidamente.
