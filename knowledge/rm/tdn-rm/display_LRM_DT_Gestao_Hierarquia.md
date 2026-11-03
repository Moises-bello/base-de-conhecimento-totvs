---
content_hash: 1320f04f64fbc7e595de1cb1e9b2b125de8783512ca35738419cc6ff787da930
fetched_at: '2026-06-29T00:08:07.623403+00:00'
page_id: '237383163'
product: rm
source: tdn-rm
title: DT_Gestao_Hierarquia
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Gestao_Hierarquia
version: 114
---

# GESTÃO DE HIERARQUIA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Pessoas** |
| **Rotina:** | | **Rotina** | **Nome Técnico** | | --- | --- | | Gestão de Hierarquia | Hierarquia | |
| **Versões/Release:** | *12.1.11* |

## Descrição

O objetivo deste projeto é definir um novo modelo de hierarquia a ser utilizado pelos sistemas de Recursos Humanos da Linha RM.  
O modelo tem como base a hierarquia de seções, porém permite maior flexibilidade para os clientes e melhor usabilidade para os usuários.  
A definição de chefes/subordinados utilizada pelos sistemas de RH passa a respeitar o modelo de posições.

## Procedimento para Utilização

**Gestão de Hierarquia por Posição**

O TOTVS Gestão de Pessoas possibilita que o Analista de RH cadastre a gestões de hierarquia definindo nome, descrição e visualizando se a gestão está ativa para poder aplicar uma gestão à empresa e assim definir as regras de hierarquia que serão utilizadas.

O sistema permite o cadastro, a edição da gestão de hierarquia e a exclusão de gestão que não estejam ativas. Ao cadastrar uma Gestão de Hierarquia, o usuário pode escolher se deseja utilizar a estrutura de seções atuais ou se deseja utilizar uma Proposta de Reestruturação de Seções. Se utilizar Proposta de Reestruturação, será obrigado informar qual proposta. Somente poderão ser utilizadas propostas do tipo “Reimplantação da Estrutura de Seções” e que estejam com o status “Definida”.

**Times de Gestões de Hierarquia por Posições**

Dentro de uma gestão por posições, o Analista de RH pode que cadastrar times e seus participantes (funcionários e externos) para agrupar de maneira flexível e rápida, funcionários e externos de acordo com os critérios que a empresa quiser levar em conta.

O sistema permite cadastrar, editar e excluir times, sendo que para excluir, os times não podem ter vinculo com alguma posição. Também é possível excluir participantes de um time.

Não pode ser incluído num time um participante que esteja ocupando uma posição na gestão. Auxiliares podem ser incluídos normalmente.

O processo para inclusão de funcionários ou externos contém apenas uma etapa, onde o usuário escolhe se quer incluir funcionário ou externo e uma listagem para escolher as pessoas

  

**Painel de Hierarquia**

O analista pode acessar um painel que possua quatro áreas para exibição de informações e que no 1º quadrante possui um campo para escolher uma gestão de hierarquia e então escolher a gestão de hierarquia que deseja visualizar

**Árvore de Posições de Hierarquia no Painel de Hierarquia**

O analista pode visualizar no Painel de Hierarquia (no 2º quadrante) uma árvore de posições que represente a estrutura hierárquica de posições da Gestão de Hierarquia que estiver selecionada no 1º quadrante e ter uma visão rápida e centralizada da hierarquia de posições.

**Opções de visualização da árvore de posições**

O analista tem a opção de visualizar na árvore de posições os nomes dos líderes das posições que tem também os botões para expandir e recolher a árvore de posições.

**Legenda e Formatação da Árvore de Posições**

Para entender o que está sendo demonstrado na árvore de posições, tem no sistema uma legenda que explique as cores de fontes e ícones usados na árvore de posições.

A árvore de posições representa corretamente ícones e fontes esperados.

**Informações do Líder**

Para obter detalhes do participante, o sistema permite visualização da foto e as informações do líder de uma posição.

**Detalhes da Posição**

O sistema permite a visualização de informações de uma posição.

**Times da Posição**

Visualização dos times vinculados a uma posição, incluir e excluir vínculos, e incluir e editar times existente.

**Liderança da Posição**

Visualizar os líderes das posições hierárquicas através de uma lista de participantes que exercem liderança na posição escolhida.

*Cadastro de líder:* Ao incluir um participante numa posição, é necessário estabelecer:

Coligada: coligada do participante.

Chapa: chapa do funcionário que ocupa a posição, se for funcionário.

Código de externo: código do externo que ocupa a posição, se for externo.

Data inicial: data inicial da ocupação da posição pelo funcionário. Campo obrigatório.

Data final: data final da ocupação da posição pelo funcionário. Se não informada, entende-se que não há data final de vigência dessa ocupação.

Tipo: direta ou indireta.

Auxiliar/Temporário: indica se é um ocupante auxiliar ou temporário.

Somente participantes que não participam de um time podem ocupar posições de liderança. Ao tentar vincular um participante a uma posição, se ele pertencer a um time, será perguntado ao usuário se ele deseja remover o participante do time e alocá-lo na posição. Neste caso o participante é removido do time que pertence e passa a ocupar a posição.

*Editar líder*: Ao clicar no botão “Editar”, se não houver um, e apenas um líder selecionado, será exibida a mensagem “Por favor selecione o líder que deseja editar”.

Ao clicar no botão “Editar”, se só tiver um líder selecionado, será exibida a tela de edição de líderes, descrita na história “Liderança da posição – Incluir novo líder”. O líder que estava selecionado será carregado para edição.

Não é permitido alterar o participante após salvar o registro. Este campo passa a ser somente para leitura.

*Excluir líder:*Ao clicar no botão irá aparecer uma mensagem de confirmação da ação solicitada.

*Regras da Tela:*

* Na Inclusão de líder a data final não fica disponível.
* Na Inclusão de auxiliar a data final fica disponível e é obrigatória.
* Ao preencher a data final de vigência de um chefe e salvar, deve ser dada uma mensagem de confirmação "Ao salvar você estará finalizando a vigência. Deseja prosseguir?". Se o usuário confirmar a data final será gravada no banco.
* É possível editar o registro de um líder apagando sua data final de vigência, desde que não haja outro chefe com a data final não preenchida.
* Para auxiliares, não pode ser informado o Tipo de ligação (direta/indireta) com posição acima. Esta informação deverá ficar desabilitada e desmarcada.
* Para auxiliares, não pode haver validação de interseção de períodos. Data de início e fim são sempre obrigatórias. Consequentemente, ao validar a vigência, só devem ser considerados os líderes que não são auxiliares.
* Não pode ser incluído num time um participante que seja chefe vigente numa posição.

  

**Validação de Vigência de Liderança**

O Analista consegue a integridade na definição de líderes através regras de consistência de vigência de liderança.

**Validação de Liderança Direta e Indireta**

O Sistema permite que o usuário consiga identificar quem é o chefe direto de um participante que ocupe mais de uma posição na hierarquia da empresa.

**Cadastro de Posições**

O usuário pode incluir e editar as posições que formam a hierarquia organizacional de uma empresa para representar no sistema a hierarquia de chefia.

**Excluir Posição**

Para revisar a hierarquia que foi definida previamente o usuário tem que excluir uma posição da gestão de hierarquia.

**Alertas da Gestão**

O sistema permite a funcionalidade que me mostra o total de alertas de inconsistência de uma gestão de hierarquia para o usuário estar ciente e agir nas inconsistências, eliminando-as.

**Ativar Gestão de Posição e Histórico**

No sistema tem um assistente que me permite ativar uma gestão de posição. Ao ativar uma gestão, se houver outra ativa, ela irá ser desativada. Este assistente valida a gestão escolhida e exibe uma lista das possíveis inconsistências (reutilizando rotinas da visão de alertas). Será informado um motivo para ativar uma gestão, e gerar histórico, tanto da ativação da gestão quanto da possível desativação de uma gestão que estava ativa para que o usuário tenha a garantia de ter apenas uma gestão ativa, válida e devidamente registrado o motivo e o responsável pela ativação.

**Histórico de Ativação**

Para visualizar o histórico das ativações gestões, o analista precisa de um histórico, tanto da ativação da gestão quanto da desativação de uma gestão que estava ativa.

Os registros de histórico contém informações que identifiquem a gestão, ação realizada (ativação/desativação), motivo, usuário responsável, data e hora. Essas informações podem ser visualizadas em **Gestões de Hierarquia / Anexos / Histórico de Ativação/Desativação.**

**Assistente de Montagem de Gestão de Hierarquia a Partir da Estrutura de Seções**

O sistema permite montar com facilidade e fidelidade a hierarquia através de um assistente que pode ser utilizado para uma gestão de hierarquia, que auxilie o usuário a montar uma estrutura hierárquica a partir da estrutura de seções existente no sistema.

**Parametrização de Tipo de Hierarquia**

O Administrador do sistema tem a funcionalidade de de parametrizar no sistema (Parametrizador / Configurações / Gerais / Preferências) se deseja utilizar hierarquia de gestão de posição ou hierarquia de seção. Isso reflete em todo o sistema a forma de buscar chefes e subordinados. Só é possível parametrizar a hierarquia para gestão por posição se houver uma gestão ativa cadastrada. Feito isso ele escolhe o tipo de sistema de hierarquia e ativa a gestão por posição

**Gestão de Hierarquia para Proposta de Reestruturação de Seções**

O sistema permite que o analista monte uma Gestão de Hierarquia a partir de uma estrutura de seções que esteja sendo proposta por meio de uma “Proposta de reestruturação de seções” ou a partir da estrutura de seções atual da coligada para planejar hierarquia conforme uma proposta de reestruturação de seções para aplicação futura na empresa.

**Aplicar Proposta de Reestruturação de Seção**

O sistema permite aplicar uma proposta de reestruturação vinculada a uma gestão de hierarquia para aplicar todo o planejamento realizado e ver toda a estrutura atual ser atualizada.

**Assistente de Montagem de Hierarquia de Proposta de Reestruturação**

Para ter a hierarquia que respeite o que já foi definido anteriormente em seções físicas numa proposta de reimplantação, precisa montar uma hierarquia a partir de uma proposta de reestruturação de seção definida no Labore.

**Listagem de auxiliares no Portal**

No sistema contém uma lista de auxiliares ativos para as posições que um chefe ocupa que possibilita visualizar e tomar ações relacionadas a auxiliares.

**Definição de auxiliar no Portal**

O sistema permite que o chefe de uma posição tenha a possibilidade de definir e editar auxiliares (funcionário ou externo), que poderão atuar como chefes auxiliares de minhas posições. E escolher para quais posições deseja atribuir o auxiliar e para qual período podendo então delegar tarefas para auxiliares executarem na sua ausência ou simplesmente o auxiliando em suas tarefas.

**Gerar Cópia de Gestões por Posição**

O usuário tem um assistente que permite criar cópias de uma Gestão por Posições e seu conteúdo.

Criando uma cópia de gestão ele pode iniciar um planejamento ou revisão da nova gestão sem impactar a gestão oficial. Em outro momento, se necessário, a nova gestão poderá tornar-se a gestão ativa. Nisso, ele irá conseguir planejar uma Gestão por Posições antes de colocá-la em prática.

**Processo de Exclusão de Gestão de Hierarquia**

Para remover completamente e rapidamente uma gestão não utilizada o usuário irá excluir uma gestão de hierarquia não ativa independente se a mesma possui posições, times, lideres e etc vinculadas a ela.

**Gestão de Hierarquia Multi-Coligada**

O usuário precisa definir gestões de hierarquia que se relacionam entre as coligadas existentes para gerar a hierarquia de toda a empresa.

No cadastro de líder é possível cadastrar líderes de qualquer coligada.

****Impactos em Funcionalidades****

As seguintes funcionalidades dos produtos de RH foram adaptadas para, de acordo com a parametrização, utilizar a regra de hierarquia correta para a coligada:

* Processo de criação de atendente no RM Agilis
* Análise Salarial
* Inclusão de Metas no Portal
* Avaliação de Desempenho por Competências
* Organograma
* Envio de e-mail para Gestor no Mapa de Conhecimento e Análise de Potencial
* Visão de Subordinados
* Fluxo padrão de requisições
* Requisições – Winforms
* Requisições – Portal
* Cadastro de Anotação Pessoal - Winforms
* Aprovação de Batidas
* Saldo de Banco de Horas
* Aprovação de Batidas em Grupo
* Aprovar Abonos
* Encerrar liderança de um funcionário ao demitir o funcionário
* Gestão de Ferias
* Anexo de Funcionários Lotados na Seção
* Rotinas de chefia do Agilis (CRM)

 Em todos os pontos citados acima, o sistema irá validar se deve exibir chefe/subordinado de acordo com a regra de hierarquia por posições ou por seções, de acordo com a parametrização.

O comportamento interno dos itens não foi alterado.

divs
