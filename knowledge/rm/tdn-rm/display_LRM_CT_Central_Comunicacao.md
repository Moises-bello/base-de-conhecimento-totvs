---
content_hash: a8b27609bbdbb737fea9c115ec6bb282ee20ae291febe526a188199a59a6fb8b
fetched_at: '2026-06-29T00:08:30.404299+00:00'
page_id: '272430859'
product: rm
source: tdn-rm
title: CT_Central_Comunicacao
type: documentation
url: https://tdn.totvs.com/display/LRM/CT_Central_Comunicacao
version: 116
---

# Central de Comunicação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | **TOTVS Gestão Educacional*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Central de Comunicação.* | *Central de Notificação.* | |
| **Cadastros Iniciais:** | *Cadastro de mensagens.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | EDUEDU003-10*.* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *SQL Server e Oracle.* |
| **Tabelas Utilizadas:** | *SMENSAGENSNOTIFICACAO.* |

## Descrição

Melhoria na seleção de usuários da Central de Comunicação e cadastro de mensagens, possibilitando que o usuário informe o público alvo da notificação.  
Como público alvo da mensagem, foram disponibilizadas as seguintes opções:

* Alunos
* Pais
* Responsável Acadêmico
* Responsável Financeiro
* Professor
* Coordenador.

Além disso, há a possibilidade de selecionar usuários para notificação a partir de consulta SQL.

**Importante:** Neste caso, a consulta selecionada será executada no momento da execução do processo 1.

1. **Mensagem**

No cadastro da mensagem foram disponibilizados campos para o público alvo. Esta informação tem como objetivo permitir que o usuário informe quais são os públicos alvo da mensagem, evitando assim que seja enviada para usuários desnecessários.  
 É importante alertar que o público alvo só tem impacto na execução do processo de envio de notificação temporal. No caso de eventos gerados automaticamente pelo sistema(ex. liberação de notas), os usuários que receberão a notificação serão os usuários selecionados no evento.

A seleção do público alvo da mensagem fica restrita as permissões do usuário, concedidas no item Central de Comunicação no cadastro de perfil, conforme explicado abaixo.

**Observação:** Ao selecionar um objetivo para a mensagem, alguns itens do público alvo podem ficar desabilitados. Este bloqueio ocorre para que a mensagem não sejam enviadas para usuários que não estejam relacionados ao objetivo da mensagem. Ex.: Caso seja selecionado o objetivo "Reserva de recurso", somente o item professor ficará disponível para seleção no público alvo. Isto ocorre porque entendemos que não há a necessidade de notificar pais, alunos, etc. sobre o evento de reserva de recurso.

Outro motivo para que os itens fiquem desabilitados é a falta de permissão do usuário no cadastro/edição da mensagem. Fique atento!

2. **Envio de mensagens temporais**

O processo de envio de notificações temporais consiste em selecionar/criar uma mensagem e enviá-la para os usuários selecionados. Este envio pode ser imediato ou agendado para envio posterior ou recorrente.

O processo possibilita o envio de mensagens de duas formas:

* + Pré-Configuradas: Mensagens cadastradas anteriormente no sistema.
  + Texto livre: Mensagens criadas no momento da execução do processo de envio da notificação.

Na execução do processo, caso opte por informar uma mensagem pré-cadastrada, toda a informação referente a esta mensagem será exibida no processo, inclusive seu público alvo.

Após seleção do público alvo será exibido o conteúdo da mensagem. Este passo tem o objetivo exibir o texto que será enviado aos usuários, porém caso o usuário tenha permissão, ele poderá editar o conteúdo da mensagem pré-configurada diretamente no processo. Esta opção é um facilitador, mas devemos ficar cientes que as alterações do conteúdo da mensagem não serão armazenados no sistema.

No terceiro passo do processo devemos selecionar os filtros para seleção dos usuários. Neste ponto disponibilizamos três agrupadores, sendo que estes ficarão habilitados conforme público alvo da mensagem.   
Os agrupadores permitem a seleção por período letivo, usuário específico, matriz aplicada, turma ou consulta SQL.

**Observação:** No agrupador de aluno, o mesmo filtro selecionado será usado para buscar pais e responsáveis. Estes itens serão carregados de acordo com o filtro de alunos, ou seja, se selecionarmos a opção "pais", o processo buscará os pais dos alunos selecionados no filtro 2.

Após seleção dos usuários no filtro, o processo poderá ser executado ou agendado.

3. **Permissões especiais**

Com a criação do público alvo, disponibilizamos algumas opções de permissão para controle da seleção do público alvo. Estas opções foram disponibilizadas em "Perfil / anexo: Parâmetros educacionais / Aba: Central de comunicação.

Os parâmetros disponibilizados são:

* **Permitir alteração do conteúdo da mensagem selecionada no processo de envio de Notificação:**Esta opção permite que o usuário selecione uma mensagem pré-cadastrada no processo de envio de notificação temporal e edite seu conteúdo diretamente no processo. Caso não tenha permissão, os campos ficarão desabilitados e o usuário só poderá enviar a mensagem com o conteúdo cadastrado na mensagem.
* **Público alvo:**Neste item podemos permitir para qual público o usuário poderá enviar notificação. Esta permissão vale mesmo que a mensagem cadastrada esteja parametrizada para envio para um público específico.  
  Ex.: A mensagem é cadastrada com envio para Pais e Alunos. Caso o perfil do usuário permita o envio apenas para Alunos, ao selecionar uma mensagem pré-cadastrada, a opção Pais ficará desmarcada e desabilitada.  
  Desta forma o usuário só enviará notificações para o público que ele tem acesso.

1 - Caso seja configurado o jobserver, o processo poderá ser agendado. Neste caso a consulta SQL será executada no momento do agendamento, podendo assim trazer registros que não estavam disponíveis no cadastro do processo.

2 - Quando utilizamos a opção de filtro por consulta SQL, os usuários que receberão a notificação serão os usuários retornados na consulta. Caso marque a opção "pais" e a consulta SQL só traga alunos, a notificação só será enviada para os alunos retornados na consulta. Neste caso, para enviar para pais e alunos a consulta SQL tem que ser criada retornando estes dados.

## Procedimento para Utilização

* **Cadastro de mensagens**

1. No TOTVS  Gestão Educacional, acesse Atividades acadêmicas / Central de Comunicações / Mensagens.
2. Selecione o objetivo da mensagem e seu público alvo.
   1. Fique atento, pois alguns objetivos só poderão ser executados automaticamente pelo sistema, conforme eventos.
3. Informe o texto do conteúdo da mensagem. Utilize as TAGs disponíveis para personalizar a mensagem.

* **Execução do processo de envio de notificação**

1. No TOTVS Gestão Educacional, acesse Atividades acadêmicas / Central de Comunicações / Agendamento/envio de mensagens de notificações temporais.
2. No processo selecione o tipo de mensagem "Pré-configurada" ou "Texto livre". Lembre-se que para listar mensagens no lookup, o usuário deve cadastrá-las previamente no sistema.
3. Informe o público alvo da notificação.
4. Ao visualizado o conteúdo da mensagem, se o usuário tiver permissão os campos ficarão habilitados para edição. Caso contrário, os campos ficarão desabilitados para edição.
5. Selecione os usuários que receberão as notificações, conforme os filtros selecionados. Caso os filtros disponíveis não sejam suficientes, o podemos utilizar consultas SQL previamente cadastradas.
6. Execute ou faça o agendamento da execução do processo.

divs
