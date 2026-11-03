---
content_hash: 4efa85c96ea634549f9cb32f28d205965bc730037c70ad597f574b9df183d6b8
fetched_at: '2026-06-29T00:06:02.061375+00:00'
page_id: '198942954'
product: rm
source: tdn-rm
title: ER_PCREQ-6705_Gestão por Escala no Ponto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198942954
version: 78
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Automação de Ponto | **Módulo** | Gestão por Escala |
| **Segmento Executor** | Contrução e Projetos | | |
| **Projeto1** | PDR\_RH\_PTO003 | **IRM1** | PCREQ-6703 |
| **Requisito1** | PCREQ-6705 | **Subtarefa1** | PDR\_RH\_PTO003-2 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Permitir que o gestor consiga realizar alterações por escala de horários, abonos e ocorrências para seus subordinados, além de realizar a impressão da escala. Os processos necessários para o gestor são:

* Alteração de Horário: Será possível alterar o horário dos subordinados dentro do período de apuração em uma única tela.
* Lançamento de abonos: Será possível lançar abonos para os subordinados dentro do período de apuração em uma única tela.
* Modificação de ocorrência. Será possível modificar ocorrências dos subordinados dentro do período de apuração em uma única tela.
* Filtro rápido de subordinados: Será possível filtrar os subordinados carregados na grid como na página de subordinados. (Ex: Subordinados Diretos)
* Dias de indisponibilidade: Será possível visualizar os dias de indisponibilidade.
* Filtro avançado: Será possível realizar filtros adicionais, por chapa, função, equipe e seção.

## Definição da Regra de Negócio

Serão listadas a seguir as evoluções que serão necessárias para atender o requisito. Serão realizadas dentro da nova MDI e do Portal:

## **MDI:**

### **Modificação de ocorrências**(**)**

A modificação de ocorrências é um novo cadastro que será incluído no Chronus, para que o usuário possa alterar informações do tipo de ocorrência e atitude das ocorrências calculadas dentro do período de apuração.

Com essa nova funcionalidade, o usuário não perderá as informações originais da ocorrência calculada.

Cadastro

O usuário poderá realizar os seguintes procedimentos:

* Visualizar as modificações de ocorrência cadastradas na visão padrão.
* Edição das modificações de ocorrência (inclusão, alteração e exclusão).

Serão disponibilizados quatro menus para acesso ao cadastro:

* Automação de Ponto > Movimento  > Ocorrências > Modificação de  Ocorrência
* Cadastro de Funcionário > Anexos > Movimento do Ponto > Modificação de Ocorrência
* Cadastro de Funcionário > Espelho .NET > Anexos > Modificação de Ocorrência (dia selecionado no espelho)
* Cadastro de Funcionário > Espelho .NET > Botão de atalho > Modificação de Ocorrência (período)

Serão disponibilizadas tags de permissão para desabilitar as opções :

* .Modificação de ocorrência

  + Incluir Modificação de ocorrência.
  + Excluir Modificação de ocorrência.
  + Editar Modificação de ocorrência.

A modificação de ocorrência terá as seguintes informações:

* Código da coligada.
* Chapa do funcionário.
* Tipo de ocorrência destino.
* Atitude.
* Por intervalo:
  + Início - data e hora.
  + Fim - data e hora.
  + Número de horas - total.
* Por número de horas:
  + Início - data.
  + Fim - data.
  + Número de horas - total por dia.
* Justificativa.
* Comportamento:
  + considera somente interseção com as ocorrências calculadas. (padrão)
  + considera toda a modificação de ocorrência..(**somente para modificação por intervalo**)
* Tipos de ocorrência origem.

Caso o cadastro seja por número de horas, ele irá considerar o número de horas para cada dia do intervalo.

Ex:

Modificação de ocorrência por número de horas

01/08/2015 a 05/08/2015

Núm. Horas: 04:00

Nesse caso ele irá considerar 04:00 para cada um dos dias do período 01/08/2015 a 05/08/2015.

Serão implementados os seguintes componentes para o cadastro:

* Lookup para informar a chapa do funcionário - "Chapa". Caso o cadastro seja aberto pelo anexo do funcionário, a chapa será carregada no campo que ficará desabilitado. (**obrigatório**)
* Lookup para informar o tipo de ocorrência destino - "Tipo Ocorrência Destino".
* Combobox para definir a Atitude da ocorrência - "Atitude".
* RadioButton para identificar se a modificação é por intervalo ou por número de horas - "Intervalo/Número de horas" (**obrigatório**)
* DateTimePicker para informar a data de início do intervalo da nova ocorrência - "Início". (**obrigatório**)
* DateTimePicker para informar a data fim do intervalo da nova ocorrência - "Fim". (**obrigatório**)
* Textbox para informar o número de horas- "Número de horas".
* Textbox para informar a justificativa - "Justificativa".
* Checkbox para definir o comportamento da modificação de ocorrência. - "Considera somente interseção com as ocorrências calculadas" (**obrigatório**)
* Lookup multirecord para informar os tipos de ocorrência origem - "Tipo Ocorrência Origem".

As informações serão gravadas nas tabelas **AMODIFICAOCORRENCIA** e **AMODIFICAOCORRENCIAORIGEM**. ()

Processo

Será criado um processo na visão das ocorrências calculadas, para que seja possível realizar modificações a partir das suas informações.

O processo irá carregar as informações comuns das ocorrências calculadas selecionadas na visão para alterar as informações, e terá os seguintes controles:

* Lookup para informar o tipo de ocorrência destino - "Tipo Ocorrência Destino".
* Combobox para definir a Atitude da ocorrência - "Atitude".
* RadioButton para identificar se a modificação é por intervalo ou por número de horas - "Intervalo/Número de horas"
* DateTimePicker para informar a data de início do intervalo da nova ocorrência - "Início".
* DateTimePicker para informar a data fim do intervalo da nova ocorrência - "Fim".
* Textbox para informar o número de horas- "Número de horas".
* Textbox para informar a justificativa - "Justificativa".

Ao alterar as informações e confirmar, o processo irá criar novas modificações de ocorrências, considerando sempre o comportamento "Considera somente interseção com as ocorrências calculadas".

Será disponibilizado dois menus para execução do processo:

* Automação de Ponto  > Movimento > Ocorrências Calculada > Processos > Modificar ocorrências calculadas
* Cadastro de Funcionário > Espelho .NET > Janelas de Informação > Ocorrências Calculada > Processos > Modificar ocorrências calculadas

Serão disponibilizadas tags de permissão para desabilitar a opção :

* .Modificação de ocorrência

  + Incluir Modificação de ocorrência.
  + Excluir Modificação de ocorrência.
  + Editar Modificação de ocorrência.
  + Modificar ocorrências calculadas.

Cálculo

O usuário poderá realizar os seguintes procedimentos:

* Visualizar as modificações de ocorrências calculadas.
* Rastrear as ocorrências calculadas origens e o cadastro de modificação que gerou a nova ocorrência calculada.

Será disponibilizado um menu para acesso as modificações de ocorrência calculadas:

* Automação de Ponto  > Movimento > Ocorrências Calculada > Anexos > Modificação de Ocorrência Calculada

Será disponibilizado um menu para acesso ao cadastro de modificação de ocorrência que gerou a nova ocorrência calculada:

* Automação de Ponto  > Movimento > Ocorrências Calculada > Anexos > Modificação de Ocorrência Calculada  > Modificação de ocorrência

O cálculo ser comportará da seguinte maneira:

* Comportamento: considera somente interseção
  + Caso a modificação não faça interseção com nenhuma ocorrência calculada.
    - Não será criada nenhuma ocorrência calculada modificada.
  + Caso a modificação seja por intervalo, irá buscar diretamente  os intervalos da ocorrência calculada para validar a interseção com o intervalo da modificação de ocorrência.
  + Caso a modificação seja por número de horas, irá buscar as n primeiras horas das ocorrências calculadas para validar a interseção com o número de horas da modificação de ocorrência .
  + Caso a modificação faça interseção com ocorrências calculadas e não tenha tipos de ocorrência origem:
    - Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção.
    - As ocorrências calculadas que fazem interseção serão gravadas na tabela de modificação de ocorrência calculada.
  + Caso a modificação faça interseção com ocorrências calculadas e tenha tipos de ocorrência origem:
    - Serão filtradas as ocorrências calculadas com os tipos de ocorrência origem equivalentes.
    - Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção.
    - As ocorrências calculadas que fazem interseção serão gravadas na tabela de modificação de ocorrência calculada.
* Comportamento: considera toda a modificação de ocorrência
  + Caso a modificação não faça interseção com nenhuma ocorrência calculada.
    - Será criada uma nova ocorrência calculada modificada.
  + Caso a modificação seja por intervalo, irá buscar diretamente  os intervalos da ocorrência calculada para validar a interseção com o intervalo da modificação de ocorrência.
  + Caso a modificação seja por número de horas, irá buscar as n primeiras horas das ocorrências calculadas para validar a interseção com o número de horas da modificação de ocorrência .
  + Caso a modificação faça interseção com ocorrências calculadas e não tenha tipos de ocorrência origem:
    - Serão geradas novas ocorrências calculadas com os intervalos que não fazem interseção.
    - Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção.
    - As ocorrências calculadas que foram geradas serão gravadas na tabela de modificação de ocorrência calculada.
  + Caso a modificação faça interseção com ocorrências calculadas e tenha tipos de ocorrência origem:
    - Serão filtradas as ocorrências calculadas com os tipos de ocorrência origem equivalentes.
    - Serão geradas novas ocorrências calculadas com os intervalos que não fazem interseção.
    - Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção.
    - As ocorrências calculadas que foram geradas serão gravadas na tabela de modificação de ocorrência calculada.

 As informações serão gravadas na tabela **AMODIFICAOCORRENCIACALCULADA**. ()

## **RM Portal:**

**Menu equipe ()**

O menu equipe será evoluído para ter acesso para a nova funcionalidade “Gestão por Escala”.

Será criado um perfil de segurança para que apenas os usuários autorizados façam o acesso.

Também serão criados sub-tags de segurança para cada um dos processos:

* Gestão por Escala
  + Alteração de Horário
  + Lançamento de Abono
  + Modificação de Ocorrência

Com essas sub-tags será possível criar perfis de segurança, e definir acesso por grupo de usuários para cada uma das três funcionalidades acima.

**Página da Gestão por Escala ()**

Ao acessar o menu, irá exibir um controle semelhante ao processo de alteração por escala da nova MDI, contendo os seguintes componentes:

* Controle para montagem de filtros de subordinados.
* Controle para definir o período carregado na grid. Por padrão será definido o período ativo e o gestor poderá alterar para períodos posteriores.
* Grid representando o período de apuração do ponto com os subordinados (diretos e indiretos) filtrados.
* Controles acima da grid para realizar a gestão da equipe para o período carregado.

A grid será carregada com a escala de horário e indisponibilidade atual dos funcionários.

Os horários serão apresentados da seguinte maneira:  Código do horário - índice e Tipo da jornada. (0001 - 1T) .

O tipo da jornada será conforme legenda abaixo:

* T: Trabalho:
* C: Compensado
* D: Descanso
* E: Extra Normal

A descrição de cada horário será exibida como hint, ao passar o mouse por cima.

Para identificação das alterações realizadas na grid, as células alteradas ficarão com o fundo vermelho claro.

A seguir cada um dos controles serão abordados e especificados.

**Validação do período de alteração****()**

Será criada uma opção dentro da configuração do grupo de acesso ao portal (Automação de Ponto > Configurações > Parametrizador > RM Portal), para validar o período que o usuário poderá alterar as informações na Grid:

* Período para alterações:
  + A partir da data atual (padrão): Irá considerar a data atual e as datas futuras.
  + A partir do período atual: Irá considerar o período atual e os períodos futuros.

Ao realizar alterações na Grid, o sistema irá validar essa parametrização.

**Dias de indisponibilidade **()****

O gestor poderá visualizar os dias de indisponibilidade através de imagens, onde cada imagem corresponderá a um tipo de indisponibilidade. Será disponibilizado uma legenda mapeando a imagem a sua respectiva indisponibilidade:

* - Abono/Atestado.
* - Descanso (Grupo de descanso).
* - Feriado.
* - Férias.
* - Afastamento.
* - Sem ponto.

Além disso, será possível destacar os dias através do controle “Visualizar dias de indisponibilidade”.

O controle possui as seguintes opções:

* Todos.
* Indisponibilidade parcial.
* Indisponibilidade completa.

Ao selecionar a opção, os dias que forem filtrados serão marcados de cinza claro, para melhor visualização. Ao passar o mouse por cima da imagem da indisponibilidade, será apresentado um hint com a informação da indisponibilidade.

 Ex:

 Abono futuro: 08:00 – 10:00

 Descanso: O dia inteiro

****Horário**()**

Serão implementados os seguintes componentes para alteração do horário:

* RadioButton para definir o tipo do horário- "Tipo do Horário". (**obrigatório**)
* Lookup para informar o código do horário - "Horário". (**obrigatório**)
* Combobox para selecionar o comportamento do horário anterior - "Comportamento Horário Anterior". (**obrigatório**)
* Combobox para selecionar o comportamento do horário atual - "Comportamento Horário Atual". (**obrigatório**)
* Lookup para informar o índice da data de mudança do horário - "Índice Data Mudança".  (**obrigatório, caso o índice da data base não estiver preenchido**)
* Lookup para informar o índice da data base do horário - "Índice Data base".  (**obrigatório, caso o índice da data mudança não estiver preenchido**)
* Textbox para definir por quantos dias o horário será mantido - "Manter horário por (x) dia(s)"
* Botão para alicar a alteração do horário na seleção da grid - "Aplicar na seleção".
* Checkbox para visualizar somente os horários da escala - "Visualizar somente os horários da escala".
* Botão para visualizar o  horário planejado do subordinado selecionado no período de apuração - "Visualizar Horário Planejado"(Hint).
* Botão para visualizar o histórico de horário do subordinado selecionado- "Visualizar Histórico do Funcionário"(Hint).
* Botão para excluir os horários aplicados na grid - "Excluir horários alterados na grid"(Hint).

O gestor poderá realizar alteração do horário por intervalo ou por jornada, passando as seguintes informações:

* Caso o tipo do horário seja Horário por intervalo:
  + Código do Horário por intervalo.
* Caso o tipo do horário seja Horário por jornada:
  + Código do Horário por jornada.
* Comportamento Horário Anterior
* Comportamento Horário Atual
* Índice Data Mudança
* Índice Data Base
* Manter horário por (x) dia(s) - irá aplicar a alteração de horário na grid para a quantidade de dias definido.

Caso algum dia na grid esteja selecionado, ao selecionar o índice da data mudança automaticamente irá selecionar o índice da data base

Ao marcar a opção "Visualizar apenas horários da escala", o lookup de horário irá carregar somente os horários que possuem o parâmetro "Horário da escala" marcado.

Ao clicar no botão "Aplicar na seleção", será feita validação se a data é igual ou posterior a data atual. Caso passe na validação, a grid será atualizada com as novas informações.

Será apresentado o código do horário e o índice alterado para identificação na grid. (0001-1).

Ao clicar no botão "Visualizar Horário Planejado", abrirá a visualização dos horários do período do subordinado selecionado considerando as alterações de horário já realizadas na sessão corrente.  Serão exibidas as seguintes informações:

* Cabeçalho:
  + Chapa.
* Colunas:
  + Data.
  + Código do horário.
  + Índice.
  + Id da jornada.
  + Dia da semana.
  + Entrada X - será conforme número de entradas.
  + Saída X - será conforme número de saídas.
* Rodapé:
  + Período da grid.

Ao clicar no botão "Visualizar Histórico do Funcionário", abrirá a visão do histórico de horário do subordinado selecionado.

Ao clicar no botão "Excluir horários alterados na grid", todos os horários que foram adicionados pelo gestor na seção corrente e estiverem selecionados, serão removidos da grid.

**Abono **()****

Serão implementados os seguintes componentes para lançamento de abono:

* Lookup para informar o código do abono - "Abono". (**obrigatório**)
* Textbox para informar o início do intervalo de abono - "Início". (**obrigatório caso abono por intervalo**)
* Textbox para informar o fim do intervalo de abono - "Fim". (**obrigatório caso abono por intervalo**)
* Textbox para informar o número de horas de abono - "Núm. horas". (**obrigatório caso abono por número de horas**)
* Checkbox para definir se é abono futuro - "Considera atrasos e faltas calculadas".
* Checkbox para definir se abona até o fim da jornada - "Abona até o fim da jornada".
* Botão para alicar o abono na seleção da grid - "Aplicar na seleção".
* Botão para excluir os abonos aplicados na grid - "Excluir abonos alterados na grid"(Hint).

O gestor poderá realizar lançamento de abono, passando as seguintes informações:

* Código do abono
* Caso a configuração do sistema seja para abono por intervalo:
  + Hora início do abono
  + Hora fim do abono
  + Número de horas ficará desabilitado e apresentará o número de horas do intervalo.
* Caso a configuração do sistema seja para abono por número de horas:
  + Número de horas do abono
  + Hora início não ficará visível
  + Hora fim não ficará visível
* Se irá considerar atrasos e faltas calculadas. Caso não considere ou caso a data seja posterior a data atual, será lançado como abono futuro.
* Se abona até o fim da jornada.

Ao clicar no botão "Aplicar na seleção", será feita validação se a data é igual ou posterior a data atual. Caso passe na validação a grid será atualizada com as novas informações. Será apresentado o ícone de indisponibilidade do abono para identificação na grid.

Ao clicar no botão "Excluir abonos lançados na grid", todos os abonos que foram adicionados pelo gestor na seção corrente e estiverem selecionados, serão removidos da grid.

### **Modificação de ocorrências ****()******

Serão implementados os seguintes componentes para lançamento das modificações de ocorrências:

* Lookup para informar o tipo de ocorrência destino - "Tipo Ocorrência Destino".
* Combobox para definir a Atitude da ocorrência - "Atitude".
* RadioButton para identificar se a modificação é por intervalo ou por número de horas - "Intervalo/Número de horas" (**obrigatório**)
* Textbox para informar o início do intervalo da modificação de ocorrência - "Início". (**obrigatório**)
* Textbox para informar o fim do intervalo da modificação de ocorrência - "Fim". (**obrigatório**)
* Textbox para informar o número de horas da modificação de ocorrência - "Núm. horas".
* Textbox para informar a justificativa - "Justificativa".
* Checkbox para definir o comportamento da modificação de ocorrência. - "Considera somente interseção com as ocorrências calculadas". (**obrigatório**)
* Lookup multirecord para informar os tipos de ocorrência origem - "Tipo Ocorrência Origem".
* Botão para aplicar a modificação de ocorrência  na seleção da grid - "Aplicar na seleção".
* Botão para excluir as modificações de ocorrência aplicadas na grid - "Excluir abonos lançados na grid"(Hint).

O gestor poderá realizar lançamento das modificações de ocorrência, passando as seguintes informações:

* Código do tipo de ocorrência destino.
* Atitude da ocorrência (PagarDescontar/Compensar).
* Caso a modificação seja por intervalo:
  + Hora início da modificação de ocorrência.
  + Hora fim da modificação de ocorrência.
* Caso a modificação seja por numero de horas:
  + Número de horas da modificação de ocorrência.
* Justificativa da modificação de ocorrência.
* Comportamento da modificação de ocorrência:
  + considera somente interseção com a ocorrência calculada. (padrão)
  + considera toda a modificação de ocorrência..
* Código dos tipos de ocorrência origem. Neste caso irá modificar a ocorrência somente se o tipo de ocorrência que faz interseção for o mesmo de um dos tipos de ocorrência origem.

Ao clicar no botão "Aplicar na seleção", será feita validação se a data é igual ou posterior a data atual. Caso passe na validação, a grid será atualizada com as novas informações. Será apresentada a sigla "M.O" para identificação na grid.

Ao clicar no botão "Excluir modificações de ocorrências lançadas na grid", todas as modificações de ocorrência que foram adicionadas pelo gestor na seção corrente e estiverem selecionadas, serão removidas da grid.

### **Impressão da escala********()******

### 

Será disponibilizado opção para impressão da escala dos subordinados; A impressão poderá ser realizada através do botão "Imprimir".

Ao mandar imprimir a escala, será aberto o preview de impressão com a grid na página e a legenda da escala.

### **Exportação para excel********()******

Será disponibilizado opção para exportar a grid para excel. A exportação poderá ser realizada através do botão "Exportar".

Ao mandar exportar, será feito download do arquivo excel contendo as informações da grid. As imagens serão representadas por texto:

* : ABONO.
* : DESCANSO.
* : FERIADO.
* **:** FÉRIAS.
* : AFASTAMENTO.
* : SEM PONTO.

### Filtros avançados ******()******

### 

 O gestor terá um controle de filtros avançados a disposição, semelhante ao de gestão de férias. Será possível executar os seguintes filtros:

* Filtro de seção.
* Filtro de subordinados diretos.
* Filtro de equipe.
* Filtro de chapa.
* Filtro de função.

O controle de filtros ficará disponível ao lado esquerdo da página de Gestão por Escala, conforme protótipo.

### Solicitação de abono ******()******

### 

O processo de solicitação de abono do portal será evoluído para que seja possível definir se o abono é futuro. Em algumas situações, pode ser necessário tirar a permissão somente de solicitar abono comum ou somente de solicitar abono futuro.

Portanto serão disponibilizadas tags de permissão para desabilitar a solicitação de abono e abono futuro no portal:

* Solicitar abono.
* Solicitar abono futuro.

Será implementado o seguinte componente para esta definição:

* Checkbox para definir se considera atrasos e faltas calculadas - "Considera atrasos e faltas calculadas".

O perfil de segurança será validado na solicitação de abono do portal:

* Caso as tags "Solicitar abono" e "Solicitar abono futuro" estejam sem permissão, não será possível solicitar abono.
* Caso a tag "Solicitar abono" esteja sem permissão:

  + O checkbox "Considera atrasos e faltas calculadas" ficará desmarcado e desabilitado.
* Caso a tag "Solicitar abono futuro" esteja sem permissão:
  + O checkbox "Considera atrasos e faltas calculadas" ficará marcado e desabilitado.
  + Só poderá solicitar abonos até o dia atual.

## Regras de Integridade

 

## **MDI:**

 

### **Modificação de ocorrências**

Cadastro

1. O cadastro deve respeitar corretamente todas as tags do perfil de segurança.
2. O cadastro deve validar se o fim da modificação de ocorrência é posterior ou igual ao início. Caso não passe pela validação o sistema não irá gravar e irá dar feedback ao usuário.
3. Caso a modificação seja por intervalo, não poderá salvar a informação do número de horas.
4. Caso a modificação seja por número de horas, não poderá exibir e nem gravar a hora da data início e a hora da data fim.
5. O cadastro deve permitir que nenhum tipo de ocorrência origem seja informado. Nesse caso a modificação será realizada considerando qualquer tipo de ocorrência.
6. Caso a modificação seja por número de horas, deve desabilitar e desmarcar o parâmetro "considera somente interseção com as ocorrências calculadas".

Processo

1. O processo deve carregar somente as informações em comum das ocorrências calculadas selecionadas. Os outros campos ficarão desabilitados.
2. O processo irá sempre considerar o comportamento "Considera somente interseção com as ocorrências calculadas".
3. Para cada ocorrência calculada selecionada, deverá gerar uma nova modificação de ocorrência.

Cálculo

1. O cálculo deverá gerar um registro na tabela **AMODIFICAOCORRENCIACALCULADA** para toda modificação de ocorrência aplicada, tendo interseção ou não..

## **RM Portal:**

**Página da Gestão por Escala**

1. O controle de definição do período da grid deverá respeitar as regras de integridade relacionadas ao período ativo, ou seja, não poderá permitir alterações em datas anteriores ao período ativo.

**Filtro de subordinados**

1. O filtro selecionado deve ser aplicado aos subordinados da grid respeitando as mesmas regras do filtro existente na página de subordinados.

**Dias de indisponibilidade**

1. O sistema deve garantir que a indisponibilidade esteja vinculada corretamente a sua respectiva cor.
2. No caso de mais de uma indisponibilidade coincidir no mesmo dia (férias com sem ponto, por exemplo), ?
3. Ao visualizar os dias de indisponibilidade, onde o fundo das células ficarão em cinza claro, o sistema deve garantir a boa visualização das legendas.

******Horário******

1. O controle deve respeitar corretamente a tag do perfil de segurança, e ficar desabilitado caso o usuário não tenha permissão.
2. O sistema deve garantir a alteração do horário conforme seu tipo. Caso seja horário por jornada, ao confirmar deverá gravar a alteração no histórico do horário por jornada, caso contrário, deverá gravar no histórico do horário por intervalo.

****Abono****

1. O controle deve respeitar corretamente a tag do perfil de segurança, e ficar desabilitado caso o usuário não tenha permissão.
2. O lookup de abono deve considerar somente abonos disponíveis no Portal.
3. O processo deve validar se o fim do abono é posterior ou igual ao início. Caso não passe pela validação o sistema não irá gravar e irá dar feedback ao usuário.

### **Modificação de ocorrências**

1. O controle deve respeitar corretamente a tag do perfil de segurança, e ficar desabilitado caso o usuário não tenha permissão.
2. O processo deve validar se o fim da modificação de ocorrência é posterior ou igual ao início. Caso não passe pela validação o sistema não irá gravar e irá dar feedback ao usuário.
3. O processo deve permitir que nenhum tipo de ocorrência origem seja informado. Nesse caso a modificação será realizada considerando qualquer tipo de ocorrência.

## Protótipo de Tela

*prototipo01*

**********************************Protótipo 01**********************************

**prototipo02**

**Protótipo 02**

**prototipo03**

****Protótipo 03****

**Visualização do horário**

**Histórico do horário**

**prototipo04**

**Protótipo 04**

**prototipo05**

**Protótipo 05**

**prototipo06**

**Protótipo 06**

**prototipo07**

**Protótipo 07**

**prototipo08**

**Protótipo 08**

**prototipo09**

**Protótipo 09**

prototipo10

**Protótipo 10**

****dicionariodedados****

## Dicionário de Dados

### **Modificação de ocorrências**

| **Tabela** | AMODIFICAOCORRENCIA |
| --- | --- |
| **Chave primária** | CODCOLIGADA; CHAPA; IDMODIFICACAO |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIA |
| **Campo** | CODCOLIGADA |
| **Tipo** | SMALLINT |
| **Tamanho** | - |
| **Descrição** | Código da coligada |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIA |
| **Campo** | CHAPA |
| **Tipo** | VARCHAR |
| **Tamanho** | 16 |
| **Descrição** | Chapa do funcionário |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIA |
| **Campo** | IDMODIFICACAO |
| **Tipo** | INT (GAUTOINC) |
| **Tamanho** | - |
| **Descrição** | Id da modificação |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIA |
| **Campo** | TIPOOCORRENCIADESTINO |
| **Tipo** | VARCHAR |
| **Tamanho** | 5 |
| **Descrição** | Tipo de ocorrência destino |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIA |
| **Campo** | DATAINICIO |
| **Tipo** | DATETIME |
| **Tamanho** | - |
| **Descrição** | Data e hora início da modificação |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIA |
| **Campo** | DATAFIM |
| **Tipo** | DATETIME |
| **Tamanho** | - |
| **Descrição** | Data e hora fim da modificação |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIA |
| **Campo** | NUMHORAS |
| **Tipo** | INT |
| **Tamanho** | - |
| **Descrição** | Número de horas |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIA |
| **Campo** | ATITUDE |
| **Tipo** | SMALLINT |
| **Tamanho** | - |
| **Descrição** | Atitude da modificação (Pagar/Descontar/Compensar) |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIA |
| **Campo** | JUSTIFICATIVA |
| **Tipo** | VARCHAR(200) |
| **Tamanho** | - |
| **Descrição** | Justificativa |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIA |
| **Campo** | COMPORTAMENTO |
| **Tipo** | SMALLINT |
| **Tamanho** | - |
| **Descrição** | Comportamento para o cálculo:   * considera somente interseção com a ocorrência calculada. (padrão) * considera toda a modificação de ocorrência.. |
| **Obrigatório** | Sim |

| **Tabela** | AMODIFICAOCORRENCIAORIGEM |
| --- | --- |
| **Chave primária** | CODCOLIGADA;CHAPA;IDMODIFICACAO;TIPOOCORRENCIAORIGEM |

| **Tabela** | AMODIFICAOCORRENCIAORIGEM |
| --- | --- |
| **Chave estrangeira - Tabela** | AMODIFICAOCORRENCIA |
| **Chave estrangeira - Campos** | CODCOLIGADA;CHAPA;IDMODIFICACAO |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIAORIGEM |
| **Campo** | CODCOLIGADA |
| **Tipo** | SMALLINT |
| **Tamanho** | - |
| **Descrição** | Código da coligada |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIAORIGEM |
| **Campo** | CHAPA |
| **Tipo** | VARCHAR |
| **Tamanho** | 16 |
| **Descrição** | Chapa do funcionário |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIAORIGEM |
| **Campo** | IDMODIFICACAO |
| **Tipo** | INT |
| **Tamanho** | - |
| **Descrição** | Id da modificação |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIAORIGEM |
| **Campo** | TIPOOCORRENCIAORIGEM |
| **Tipo** | VARCHAR |
| **Tamanho** | 5 |
| **Descrição** | Tipo de ocorrência origem |
| **Obrigatório** | Sim |

| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| --- | --- |
| **Chave primária** | CODCOLIGADA, CHAPA, DATAREFERENCIA, IDJORNADA, TIPOOCORRENCIA, INICIO; IDMODIFICACAO |

| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| --- | --- |
| **Chave estrangeira - Tabela** | AOCORRENCIACALCULADA |
| **Chave estrangeira - Campos** | CODCOLIGADA, CHAPA, DATAREFERENCIA, IDJORNADA, TIPOOCORRENCIA, INICIO |

| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| --- | --- |
| **Chave estrangeira - Tabela** | AMODIFICAOCORRENCIA |
| **Chave estrangeira - Campos** | CODCOLIGADA;CHAPA;IDMODIFICACAO; |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| **Campo** | CODCOLIGADA |
| **Tipo** | SMALLINT |
| **Tamanho** | - |
| **Descrição** | Código da coligada |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| **Campo** | CHAPA |
| **Tipo** | VARCHAR |
| **Tamanho** | 16 |
| **Descrição** | Chapa do funcionário |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIAORIGEM |
| **Campo** | DATAREFERENCIA |
| **Tipo** | DATETIME |
| **Tamanho** | - |
| **Descrição** | Data referência |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| **Campo** | IDJORNADA |
| **Tipo** | INT |
| **Tamanho** | - |
| **Descrição** | Id da jornada |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| **Campo** | TIPOOCORRENCIA |
| **Tipo** | VARCHAR |
| **Tamanho** | 5 |
| **Descrição** | Tipo de ocorrência |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| **Campo** | INICIO |
| **Tipo** | DATETIME |
| **Tamanho** | - |
| **Descrição** | Data e hora início da modificação |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| **Campo** | IDMODIFICACAO |
| **Tipo** | INT |
| **Tamanho** | - |
| **Descrição** | Id da modificação |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| **Campo** | TIPOOCORRENCIAORIGEM |
| **Tipo** | VARCHAR |
| **Tamanho** | 5 |
| **Descrição** | Tipo de ocorrência da ocorrência calculada modificada |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| **Campo** | INICIOORIGEM |
| **Tipo** | DATETIME |
| **Tamanho** | - |
| **Descrição** | Data e hora início da ocorrência calculada modificada |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| **Campo** | FIMORIGEM |
| **Tipo** | DATETIME |
| **Tamanho** | - |
| **Descrição** | Data e hora fim da ocorrência calculada modificada |
| **Obrigatório** | Sim |

|  |  |
| --- | --- |
| **Tabela** | AMODIFICAOCORRENCIACALCULADA |
| **Campo** | ATITUDEORIGEM |
| **Tipo** | SMALLINT |
| **Tamanho** | - |
| **Descrição** | Atitude da ocorrência calculada modificada (Pagar/Descontar/Compensar) |
| **Obrigatório** | Sim |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
