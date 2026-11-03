---
content_hash: da3b9b42d2c4f73f9e9116da497637f1ed8661fbd629b8776373efdd8b10b0a5
fetched_at: '2026-06-29T00:06:18.838510+00:00'
page_id: '219686833'
product: rm
source: tdn-rm
title: DT_PCREQ-6705_Gestão_por_Escala_no_Ponto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219686833
version: 5
---

# GESTÃO POR ESCALA NO PONTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Automação de Ponto* | *Escala no ponto* | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Chamados Relacionados** |  |
| **Requisito (ISSUE):** |  |
| **País(es):** |  |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

## Descrição

O Totvs Automação de Ponto permite que o gestor consiga realizar alteração por escalas de horários, abonos e ocorrência para seus subordinados, além de realizar a impressão da escala.  
 O gestor pode alterar o horário, lançar abonos e modificar ocorrências dos subordinados em uma única tela dentro do período de apuração. É possível filtrar os subordinados carregados na grid como na página de subordinados (ex: Subordinados Diretos) e também realizar filtros adicionais por chapa, função, equipe e seção.

## Procedimento para Utilização

 

**MDI**

**Modificação de Ocorrências**

A modificação de ocorrências é um cadastro incluído no Chronus e serve para que o usuário possa alterar informações do tipo de ocorrência e atitude das ocorrências calculadas dentro do período de apuração. Com essa funcionalidade, o usuário não perderá as informações originais da ocorrência calculada.

 

Cadastro

O usuário pode visualizar as modificações de ocorrências cadastradas na visão padrão e também editar as modificações (inclusão, alteração e exclusão).

Para tal processo estão disponíveis quatro menus:   
 • Automação de ponto/ Movimento / Ocorrências / Modificação de Ocorrência;   
 • Cadastro de Funcionário /  Anexos / Movimento do Ponto / Modificação de Ocorrência;  
 • Cadastro de Funcionário / Espelho .NET / Anexos / Modificação de Ocorrência (dia selecionado no espelho);  
 • Cadastro de Funcionário / Espelho .NET / Botão de atalho / Modificação de Ocorrência (período)

Estão disponíveis tags de permissão para desabilitar as opções de Incluir, Excluir e Editar a Modificação de Ocorrência.

A modificação de ocorrência tem as seguintes informações:  
 • Código da coligada  
 • Chapa do funcionário  
 • Tipo de ocorrência destino   
 • Atitude.  
 • Por intervalo: Início – data e hora; Fim – data e hora; Número de horas – total.  
 • Por número de horas: Início – data; Fim – data; Número de horas – total por dia.   
 • Justificativa   
 • Comportamento: considera somente interseção com as ocorrências calculadas. (Padrão); considera toda a modificação de ocorrência. (Somente para modificação por intervalo).  
 • Tipos de ocorrência origem.  
   
 Caso o cadastro seja por número de horas, ele considera o número de horas para cada dia do intervalo.  
 Ex: Modificação de ocorrência por número de horas  
 01/05/2015 a 05/08/2015  
 Núm. Horas: 04:00  
 Nesse caso ele irá considerar 04:00 para cada período 01/08/2015 a 05/08/2015

   
Segue os seguintes componentes para o cadastro:  
 

• Lookup para informar a chapa do funcionário - "Chapa". Caso o cadastro seja aberto pelo anexo do funcionário, a chapa será carregada no campo que ficará desabilitado. (**Obrigatório**)  
• Lookup para informar o tipo de ocorrência destino - "Tipo Ocorrência Destino".  
• Combobox para definir a Atitude da ocorrência - "Atitude".   
• RadioButton para identificar se a modificação é por intervalo ou por número de horas - "Intervalo/Número de horas" (**Obrigatório**)  
• DateTimePicker para informar a data de início do intervalo da nova ocorrência - "Início". (**Obrigatório**)  
• DateTimePicker para informar a data fim do intervalo da nova ocorrência - "Fim". (**Obrigatório**)  
• Textbox para informar o número de horas- "Número de horas".  
• Textbox para informar a justificativa - "Justificativa".  
• Checkbox para definir o comportamento da modificação de ocorrência. - "Considera somente interseção com as ocorrências calculadas" (**O****brigatório**)  
• Lookup multirecord para informar os tipos de ocorrência origem - "Tipo Ocorrência Origem".

 

As informações serão gravadas nas tabelas **AMODIFICAOCORRENCIA** e **AMODIFICAOCORRENCIAORIGEM**

 

 

Processo

Na visão das ocorrências calculadas tem um processo que é possível realizar modificações a partir das suas informações. Esse processo carrega as informações comuns das ocorrências calculadas selecionadas na visão para alterar as informações e tem os seguintes controles:

• Lookup para informar o tipo de ocorrência destino - "Tipo Ocorrência Destino".  
 • Combobox para definir a Atitude da ocorrência - "Atitude".   
 • RadioButton para identificar se a modificação é por intervalo ou por número de horas - "Intervalo/Número de horas"  
 • DateTimePicker para informar a data de início do intervalo da nova ocorrência - "Início".   
 • DateTimePicker para informar a data fim do intervalo da nova ocorrência - "Fim".   
 • Textbox para informar o número de horas- "Número de horas".  
 • Textbox para informar a justificativa - "Justificativa".

Ao alterar as informações e confirmar, o processo cria novas modificações de ocorrências, considerando sempre o comportamento "Considera somente interseção com as ocorrências calculadas".

Para a execução do processo temos dois processos:   
 • **Automação de Ponto / Movimento / Ocorrências Calculada / Processos / Modificar ocorrências calculadas**  
 **• Cadastro de Funcionário / Espelho .NET / Janelas de Informação / Ocorrências Calculada / Processos / Modificar ocorrências calculadas**

Estão disponíveis tags de permissão para desabilitar a opção de Incluir, Excluir, Editar e modificar a Modificação de Ocorrência

 

Cálculo

O usuário pode visualizar as modificações de ocorrências calculadas e rastrear tais ocorrências.  
Para o acesso às modificações de ocorrência calculadas, segue o caminho: **Automação de Ponto / Movimento / Ocorrências Calculada / Anexos / Modificação de Ocorrência Calculada**Para o acesso ao cadastro de modificação de ocorrência que gerou a nova ocorrência calculada, segue o caminho: **Automação de Ponto / Movimento / Ocorrências Calculada / Anexos / Modificação de Ocorrência Calculada / Modificação de ocorrência**

O cálculo ser comportará da seguinte maneira: 

***Comportamento: considera somente interseção***

• Caso a modificação não faça interseção com nenhuma ocorrência calculada, não será criada nenhuma ocorrência calculada modificada.  
• Caso a modificação seja por intervalo, irá buscar diretamente  os intervalos da ocorrência calculada para validar a interseção com o intervalo da modificação de ocorrência.  
• Caso a modificação seja por número de horas, irá buscar as n primeiras horas das ocorrências calculadas para validar a interseção com o número de horas da modificação de ocorrência .   
• Caso a modificação faça interseção com ocorrências calculadas e não tenha tipos de ocorrência origem, será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção. As ocorrências calculadas que fazem interseção serão gravadas na tabela de modificação de ocorrência calculada.  
• Caso a modificação faça interseção com ocorrências calculadas e tenha tipos de ocorrência origem, serão filtradas as ocorrências calculadas com os tipos de ocorrência origem equivalentes. Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção. As ocorrências calculadas que fazem interseção serão gravadas na tabela de modificação de ocorrência calculada.

 

***Comportamento: considera toda a modificação de ocorrência***

• Caso a modificação não faça interseção com nenhuma ocorrência calculada, será criada uma nova ocorrência calculada modificada.  
• Caso a modificação seja por intervalo, irá buscar diretamente  os intervalos da ocorrência calculada para validar a interseção com o intervalo da modificação de ocorrência.  
• Caso a modificação seja por número de horas, irá buscar as n primeiras horas das ocorrências calculadas para validar a interseção com o número de horas da modificação de ocorrência.  
• Caso a modificação faça interseção com ocorrências calculadas e não tenha tipos de ocorrência origem serão geradas novas ocorrências calculadas com os intervalos que não fazem interseção. Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção.

As ocorrências calculadas que foram geradas serão gravadas na tabela de modificação de ocorrência calculada.  
 • Caso a modificação faça interseção com ocorrências calculadas e tenha tipos de ocorrência origem, serão filtradas as ocorrências calculadas com os tipos de ocorrência origem equivalentes. Serão geradas novas ocorrências calculadas com os intervalos que não fazem interseção. Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção.  
 As ocorrências calculadas que foram geradas serão gravadas na tabela de modificação de ocorrência calculada.

 As informações serão gravadas na tabela **AMODIFICAOCORRENCIACALCULADA**.

 

**RM PORTAL**

Menu Equipe

O menu equipe tem a funcionalidade ‘’Gestão por Escala’’. Nela, somente usuários autorizados fazem o acesso.

Foram criados sub – tags de segurança para cada um dos processos:  
   
 • Gestão por escala:   
  
     Alteração de Horário  
     Lançamento de Abono  
     Modificação de Ocorrência

Com essas sub-tags é possível criar perfis de segurança e definir acesso por gripo de usuários para cada uma das três funcionalidades acima.

Página da Gestão por Escala

Ao acessar o menu, será exibido um controle semelhante ao processo de alteração por escala da nova MDI, contendo os seguintes componentes: 

• Controle para montagem de filtros de subordinados.  
 • Controle para definir o período carregado na grid. Por padrão será definido o período ativo e o gestor pode alterar para períodos posteriores.  
 • Grid representando o período de apuração do ponto com os subordinados (diretos e indiretos) filtrados.  
 • Controles acima da grid para realizar a gestão da equipe para o período carregado.

A grid é carregada com a escala de horário e indisponibilidade atual dos funcionários.  
 Os horários são apresentados da seguinte maneira:  Código do horário - índice e Tipo da jornada. (0001 - 1T).

O tipo da jornada será conforme legenda abaixo: 

T: Trabalho  
 C: Compensado  
 D: Descanso  
 E: Extra Normal

A descrição de cada horário será exibida como hint, ao passar o mouse por cima.  
Para identificação das alterações realizadas na grid, as células alteradas ficarão com o fundo vermelho claro.  
A seguir cada um dos controles serão abordados e especificados.

Validação do Período de alteração

 caminho **Automação de Ponto / Configurações / Parametrizador / RM Portal** serve para validar o período que o usuário pode alterar as informações na Grid:

• Período para alterações: 

A partir da data atual (padrão): Irá considerar a data atual e as datas futuras.  
 A partir do período atual: Irá considerar o período atual e os períodos futuros.

Ao realizar alterações na Grid, o sistema valida essa parametrização.

 

Dias de indisponibilidade

O gestor pode visualizar os dias de indisponibilidade através de imagens, onde cada imagem corresponde a um tipo de indisponibilidade. Está disponibilizado uma legenda mapeando a imagem a sua respectiva indisponibilidade:

  Abono/Atestado.      
  Descanso (Grupo de descanso).    
  Feriado  
  Férias  
 Afastamento  
 Sem ponto

Além disso é possível destacar os dias através do controle “Visualizar dias de indisponibilidade”.

O controle possui as seguintes opções:

• Todos.  
 • Indisponibilidade parcial.  
 • Indisponibilidade completa.

 Ao selecionar a opção, os dias que forem filtrados serão marcados de cinza claro, para melhor visualização. Ao passar o mouse por cima da imagem da indisponibilidade, será apresentado um hint com a informação da indisponibilidade.

 Ex: Abono futuro: 08:00 – 10:00

 Descanso: O dia inteiro

Horário

Para alteração do horário segue os seguintes componentes:

• RadioButton para definir o tipo do horário- "Tipo do Horário". (**Obrigatório**)  
 • Lookup para informar o código do horário - "Horário". (**Obrigatório**)  
 • Combobox para selecionar o comportamento do horário anterior - "Comportamento Horário Anterior". (**Obrigatório**)  
 • Combobox para selecionar o comportamento do horário atual - "Comportamento Horário Atual". (**Obrigatório**)  
 • Lookup para informar o índice da data de mudança do horário - "Índice Data Mudança".  (**Obrigatório, caso o índice da data base não estiver preenchido**)

• Lookup para informar o índice da data base do horário - "Índice Data base".  (**Obrigatório, caso o índice da data mudança não estiver preenchido**)  
 • Textbox para definir por quantos dias o horário será mantido - "Manter horário por (x) dia(s)"  
 • Botão para aplicar a alteração do horário na seleção da grid - "Aplicar".  
 • Checkbox para visualizar somente os horários da escala - "Visualizar somente os horários da escala".  
 • Botão para visualizar o  horário planejado do subordinado selecionado no período de apuração - "Visualizar Horário Planejado"(Hint).  
 • Botão para visualizar o histórico de horário do subordinado selecionado- "Visualizar Histórico do Funcionário"(Hint).  
 • Botão para excluir os horários aplicados na grid - "Imagem exclusão".

O gestor pode realizar alteração do horário por intervalo ou por jornada, passando as seguintes informações:

• Caso o tipo do horário seja Horário por intervalo: Código do Horário por intervalo.  
 • Caso o tipo do horário seja Horário por jornada: Código do Horário por jornada.  
 • Comportamento Horário Anterior  
 • Comportamento Horário Atual  
 • Índice Data Mudança

• Índice Data Base  
 • Manter horário por (x) dia(s) - irá aplicar a alteração de horário na grid para a quantidade de dias definido.

Ao marcar a opção "Visualizar apenas horários da escala", o lookup de horário carrega somente os horários que possuem o parâmetro "Horário da escala" marcado.

Ao clicar no botão "Aplicar", será feita validação se a data é igual ou posterior a data atual. Caso passe na validação, a grid será atualizada com as novas informações.

Será apresentado o código do horário e o índice alterado para identificação na grid. (0001-1).

Ao clicar no botão "Visualizar Horário Planejado", abrirá a visualização dos horários do período do subordinado selecionado considerando as alterações de horário já realizadas na sessão corrente.  Serão exibidas as seguintes informações:

• Cabeçalho: Chapa.  
 • Colunas: Data.  
                  Código do horário.  
                  Índice.  
                  Id da jornada.  
                  Dia da semana.  
                  Entrada X - será conforme número de entradas.  
                  Saída X - será conforme número de saídas.  
 • Rodapé: Período da grid.

Ao clicar no botão "Visualizar Histórico do Funcionário", abrirá a visão do histórico de horário do subordinado selecionado.

Ao clicar no botão de exclusão, todos os horários que foram adicionados pelo gestor na seção corrente e estiverem selecionados, serão removidos da grid.

Abono

Para o lançamento de Abono, segue os seguintes componentes:

• Lookup para informar o código do abono - "Abono". (**Obrigatório**)  
 • Textbox para informar o início do intervalo de abono - "Início". (**Obrigatório caso abono por intervalo**)  
 • Textbox para informar o fim do intervalo de abono - "Fim". (**Obrigatório caso abono por intervalo**)  
 • Textbox para informar o número de horas de abono - "Núm. horas". (**Obrigatório caso abono por número de horas**)  
 • Checkbox para definir se é abono futuro - "Considera atrasos e faltas calculadas".  
 • Checkbox para definir se abona até o fim da jornada - "Abona até o fim da jornada".  
 • Botão para alicar o abono na seleção da grid - "Aplicar".  
 • Botão para excluir os abonos aplicados na grid - "Imagem exclusão".

O gestor pode realizar lançamento de abono, passando as seguintes informações:

• Código do abono  
 • Caso a configuração do sistema seja para abono por intervalo:   
 Hora início do abono  
 Hora fim do abono  
 Número de horas ficará desabilitado e apresentará o número de horas do intervalo.  
 • Caso a configuração do sistema seja para abono por número de horas:  
 Número de horas do abono  
 Hora início não ficará visível  
 Hora fim não ficará visível  
 • Se irá considerar atrasos e faltas calculadas. Caso não considere ou caso a data seja posterior a data atual, será lançado como abono futuro.  
 • Se abona até o fim da jornada.

Ao clicar no botão "Aplicar", será feita validação se a data é igual ou posterior a data atual. Caso passe na validação a grid será atualizada com as novas informações. Será apresentado o ícone de indisponibilidade do abono para identificação na grid.

Ao clicar no botão de exclusão, todos os abonos que foram adicionados pelo gestor na seção corrente e estiverem selecionados, serão removidos da grid.

Modificação de Ocorrência 

Para o lançamento das modificações de ocorrências segue os seguintes componentes:

• Lookup para informar o tipo de ocorrência destino - "Tipo Ocorrência Destino".  
 • Combobox para definir a Atitude da ocorrência - "Atitude".  
 • RadioButton para identificar se a modificação é por intervalo ou por número de horas - "Intervalo/Número de horas". (**Obrigatório**)  
 • Textbox para informar o início do intervalo da modificação de ocorrência - "Início". (**Obrigatório**)  
 • Textbox para informar o fim do intervalo da modificação de ocorrência - "Fim". (**Obrigatório**)  
 • Textbox para informar o número de horas da modificação de ocorrência - "Núm. horas".  
 • Textbox para informar a justificativa - "Justificativa".  
 • Checkbox para definir o comportamento da modificação de ocorrência. - "Considera somente interseção com as ocorrências calculadas". (**Obrigatório**)  
 • Lookup multirecord para informar os tipos de ocorrência origem - "Tipo Ocorrência Origem".  
 • Botão para aplicar a modificação de ocorrência na seleção da grid - "Aplicar".  
 • Botão para excluir as modificações de ocorrência aplicadas na grid - "Imagem exclusão".

O gestor pode realizar lançamento das modificações de ocorrência, passando as seguintes informações:

• Código do tipo de ocorrência destino.  
 • Atitude da ocorrência (PagarDescontar/Compensar).  
 • Caso a modificação seja por intervalo: Hora início da modificação de ocorrência.  
                                                                   Hora fim da modificação de ocorrência.  
 • Caso a modificação seja por número de horas: Número de horas da modificação de ocorrência.  
 • Justificativa da modificação de ocorrência.  
 • Comportamento da modificação de ocorrência: Considera somente interseção com a ocorrência calculada. (Padrão); Considera toda a modificação de ocorrência.  
 • Código dos tipos de ocorrência origem. Neste caso irá modificar a ocorrência somente se o tipo de ocorrência que faz interseção for o mesmo de um dos tipos de ocorrência origem.

Ao clicar no botão "Aplicar", será feita validação se a data é igual ou posterior a data atual. Caso passe na validação, a grid será atualizada com as novas informações. Será apresentada a sigla "M.O" para identificação na grid.

Ao clicar no botão de exclusão, todas as modificações de ocorrência que foram adicionadas pelo gestor na seção corrente e estiverem selecionadas, serão removidas da grid.

Impressão da Escala

A opção para impressão da escala dos subordinados pode ser realizada através do botão "Imprimir".   
 Ao mandar imprimir a escala, será aberto o preview de impressão com a grid na página e a legenda da escala.

Exportação por Excel

A opção para exportar a grid para excel pode ser realizada através do botão "Exportar".  
 Ao mandar exportar, será feito download do arquivo excel contendo as informações da grid. As imagens serão representadas por texto:

ABONO.  
DESCANSO.  
 FERIADO.  
 FÉRIAS.  
AFASTAMENTO.   
 SEM PONTO

Filtros Avançados

O gestor tem um controle de filtros avançados a disposição, semelhante ao de gestão de férias. É possível executar os seguintes filtros:

• Filtro de seção.  
 • Filtro de subordinados diretos.  
 • Filtro de equipe.  
 • Filtro de chapa.  
 • Filtro de função.

O controle de filtros ficará disponível ao lado esquerdo da página de Gestão por Escala, conforme a imagem acima

Solicitação de Abono

É possível definir se o abono é futuro. Em algumas situações, é necessário tirar a permissão somente de solicitar abono comum ou somente de solicitar abono futuro.  
 Portanto foram disponibilizadas tags de permissão para desabilitar a solicitação de abono e abono futuro no portal:  
 • Solicitar abono.  
 • Solicitar abono futuro.

Segue seguinte componente para esta definição:  
 • Checkbox para definir se considera atrasos e faltas calculadas – ‘’Considera atrasos e faltas calculadas’’.

O perfil de segurança será validado na solicitação de abono do portal:  
 • Caso as tags ‘’Solicitar abono’’ e ‘’Solicitar abono futuro’’ estejam sem permissão, não será possível solicitar abono.  
 • Caso a tag ‘’Solicitar abono esteja sem permissão, o checkbox ‘’Considera atrasos e faltas calculadas’’ ficará desmarcado e desabilitado.  
 • Caso a tag ‘’ Solicitar abono futuro’’ estejam sem permissão, o checkbox ‘’Considera atrasos e faltas calculadas’’ ficará marcado e desabilitado; Só poderá solicitar abono até o dia atual.

Regras de Integridade

MDI: Modificação de ocorrências

Cadastro  
  
 O cadastro respeita corretamente todas as tags do perfil de segurança.  
 O cadastro valida se o fim da modificação de ocorrência é posterior ou igual ao início. Caso não passe pela validação o sistema não irá gravar e irá dar o feedback ao usuário.  
 Caso a modificação seja por intervalo, não poderá salvar a informação do número de horas.   
 Caso a modificação seja por número de horas, não poderá exibir e nem gravar a hora da data início e a hora da data fim.  
 O cadastro permite que nenhum tipo de ocorrência origem seja informado. Nesse caso a modificação será realizada considerando qualquer tipo de ocorrência.  
 Caso a modificação seja por número de horas, deve desabilitar e desmarcar o parâmetro ‘’considera somente interseção com as ocorrências calculadas’’.

Processo

O processo deve carregar somente as informações em comum das ocorrências calculadas selecionadas. Os outros campos ficarão desabilitados.  
 O processo irá sempre considerar o comportamento ‘’Considera somente interseção com as ocorrências calculadas’’.  
 Para cada ocorrência calculada selecionada, deverá gerar uma nova modificação de ocorrência.

Cálculo

O cálculo gera um registro na tabela **AMODIFICAOCORRENCIACALCULADA** para toda a modificação de ocorrência aplicada, tendo interseção ou não.

RM Portal

Página da Gestão por Escala:

O controle de definições do período da grid respeita as regras de integridade relacionadas ao período ativo, ou seja, não poderá permitir alterações em datas anteriores ao período ativo.  
   
 Filtro de subordinados

O filtro selecionado é aplicado aos subordinados da grid respeitando as mesmas regras do filtro existente na página de subordinados.  
  
Dias de indisponibilidade

O sistema garante que a indisponibilidade esteja vinculada corretamente a sua respectiva cor.  
 No caso de mais de uma indisponibilidade coincidir no mesmo dia (férias com sem ponto, por exemplo), ?.  
 Ao visualizar os dias de indisponibilidade, onde o fundo das células ficarão em cinza claro, o sistema deve garantir a boa visualização das legendas.  
   
 Horário

O controle respeita corretamente a tag do perfil de segurança e fica desabilitado caso o usuário não tenha permissão.  
 O sistema garante a alteração do horário conforme seu tipo. Caso seja horário por jornada, ao confirmar irá gravar a alteração no histórico do horário por jornada, caso contrário, irá gravar no histórico do horário por intervalo.

Abono

O controle respeita corretamente a tag do perfil de segurança e fica desabilitado caso o usuário não tenha permissão.  
 O lookup de abono considera somente abonos disponíveis no Portal.  
 O processo valida se o fim do abono é posterior ou igual ao início. Caso não passe pela validação o sistema não irá gravar e irá dar feedback ai usuário.

Modificação de ocorrências

O controle respeita corretamente a tag do perfil de segurança e fica desabilitado caso o usuário não tenha permissão.  
 O processo valida se o fim da modificação de ocorrência é posterior ou igual ao início. Caso não passe pela validação o sistema não irá gravar e irá dar feedback ai usuário.
