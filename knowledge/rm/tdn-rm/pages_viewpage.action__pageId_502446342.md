---
content_hash: 25673bebfde563ba804fc846722a35a511e51585ef3f2f368a381795bf1f9b2f
fetched_at: '2026-06-29T00:10:25.209198+00:00'
page_id: '502446342'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Opções > Parâmetros > Parâmetros Gerais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502446342
version: 3
---

### Esta página tem como objetivo explicar os parâmetros utilizados pelo TOTVS Gestão Hospitalar.

Importante

Após modificar um parâmetro é necessário fechar e reabrir o sistema.

Parâmetros GeraisParametrização da Agenda

É possível configurar a rotina de agendamento de acordo com as necessidades da instituição, os parâmetros estão nos menus:

* Opções / Parâmetros / Parâmetros Gerais guia Registro e Controle II.
* Opções / Parâmetros / Parâmetros Gerais guia Registro e Controle III.
* Opções / Parâmetros / Parâmetros Gerais guia Registro e Controle IV.
* Opções / Parâmetros / Parâmetros Gerais guia Faturamento.

#### Tela de Registro e Controle II, acessada no menu Opções/Parâmetros/Parâmetros Gerais guia Registro e Controle II.

| **Parâmetro** | Descrição |
| --- | --- |
| **Filtra unidade de atendimento?** | Se este parâmetro estiver marcado ativará o processo  que foi cadastrado no anexo do RM Saúde na rotina de perfil de segurança (Cadastros/segurança/perfil). Somente válido para registro de atendimento e agenda de atendimento. No sistema o padrão é por padrão desmarcado. |
| **Desconsidera unidade na pesquisa.** | Se este parâmetro estiver desmarcado o sistema irá desconsiderar os filtros nas pesquisas de agendamento de atendimento somente valido para registro de atendimento e Agenda de atendimento. No sistema o padrão é por padrão desmarcado. |

#### Tela de Registro e Controle III,acessada no menu Opções/Parâmetros/Parâmetros Gerais guia Registro e Controle III.

| **Parâmetro** | Descrição |
| --- | --- |
| **Alteração automática de Status ao acessar/fechar o Prontuário Eletrônico** | Este parâmetro altera o status automaticamente quando o médico termina o atendimento do paciente. No sistema o parâmetro é por padrão desmarcado. |
| **Exibir aviso de Existência de pendência (financeira, documentações) - aviso de débito** | No momento do atendimento do paciente o sistema alerta sobre a existência de pendências financeiras do paciente em questão. No sistema o parâmetro é por padrão desmarcado. |
| **Exibir Aviso de Cliente em Sala de Espera** | Este parâmetro sinaliza para o médico o tempo de espera do paciente para atendimento - Agenda de Atendimento. No sistema o parâmetro é por padrão desmarcado. |
| **Existência de lista de Espera para Realocar no Agendamento** | Sinaliza para a recepcionista que existem pacientes em lista de espera para especialidade no dia. Caso ocorra uma desistência de agendamento. No sistema o parâmetro é por padrão desmarcado. |
| **Tempo para atualização dos dados de agendamento** | Tempo em minutos em que o sistema irá atualizar a tela automaticamente com os agendamentos efetuados. No sistema o parâmetro é por padrão em branco. |
| **Tempo de verificação do aviso em Sala de Espera** | Tempo em minuto do aviso para o médico sobre a existência de paciente em sala de espera. No sistema o parâmetro é por padrão em branco. |
| **Exibir SALAS na agenda do usuário com perfil de MÉDICO** | Caso o parâmetro esteja marcado permite que o médico visualize as agendas de sala. No sistema o parâmetro é por padrão desmarcado. |
| **Plano obrigatório no agendamento** | Obriga a informação de plano de convênio no momento do agendamento. No sistema o parâmetro é por padrão desmarcado. |
| **Médico faz agendamento de Consulta** | Permite que o médico possa efetuar agendamento de consultas. No sistema o parâmetro é por padrão desmarcado. |
| **Data de nascimento do paciente obrigatório** | Obriga a informação da data de nascimento no momento do agendamento. No sistema o parâmetro é por padrão desmarcado. |
| **Alteração automática de Status ao Gravar Anamnese Especial** | No momento do preenchimento da anamnese Especial no Prontuário Eletrônico o sistema altera o status do agendamento para atendido. |
| **Valida Automaticamente a elegibilidade ao informar o código do beneficiário** | Valida Automaticamente a elegibilidade ao informar o código do beneficiário. No sistema o parâmetro é por padrão desmarcado. |
| **Valida automaticamente a elegibilidade ao pesquisar o paciente** | Valida automaticamente a elegibilidade ao pesquisar o paciente. No sistema o parâmetro é por padrão desmarcado. |
| **Permite conflito de horários no agendamento** | Permite conflito de horários no agendamento. No sistema o parâmetro é por padrão desmarcado. |
| **Utiliza Protocolo no Agendamento** | Gera ao usuário ao concluir um agendamento, um número de protocolo para registro. Este número pode ser pesquisado posteriormente. No sistema ele é por padrão desmarcado. |
| **Integra Agendas do Prestador e Sala** | Caso o parâmetro esteja marcado o sistema associará a agenda do prestador junto a sala cadastrada no sistema. No sistema o parâmetro é por padrão desmarcado. |
| **Lançar honorário associado à atividade da agenda ao registrar o atendimento** | Caso o parâmetro esteja marcado o sistema lançará automaticamente na conta do paciente  o honorário associado a atividade profissional. No sistema o parâmetro é por padrão desmarcado. |
| **Lança exames da agenda ao gerar informações de atend. Externo** | Se no registro do agendamento existir exames agendados o sistema automaticamente gerará os pedidos de exames ao registrar o atendimento do paciente. No sistema o parâmetro é por padrão desmarcado. |
| **Obriga preenchimento do telefone no agendamento.** | Obriga preenchimento do telefone no agendamento. No sistema o parâmetro é por padrão desmarcado. |
| **Relatório da agenda de atendimentos** | Indica qual Relatório do TOTVS REPORTS será utilizado para impressão da agenda de atendimentos. No sistema o parâmetro é por padrão em branco. Utiliza o do sistema. |
| **Não permite salvar um agendamento sem elegibilidade ou autorização** | Não permite que um agendamento seja salvo ao não realizar a solicitação de elegibilidade ou solicitação de procedimento na Agenda de Atendimentos para os convênios que possuem utilização de Web Service parametrizados no sistema. |
| **Não permite encaixe fora do período de atendimento** | Não permite que um encaixe seja realizado na Agenda de Atendimentos em períodos posteriores ou anteriores aos períodos diários parametrizados na agenda. |
| **Utiliza máscara no N° de celular ao Agendar** | Ao digitar o número de celular ao realizar um agendamento, é utilizada a máscara de DDD + 9 dígitos para telefones celulares. |

#### Tela de Registro e Controle IV,acessada no menu Opções/Parâmetros/Parâmetros Gerais guia Registro e Controle IV.

| **Parâmetro** | Descrição |
| --- | --- |
| **Não permitir bloquear período da agenda com agendamentos neste período** | Caso o parâmetro esteja marcado o sistema não permitira o bloqueio de período da Agenda, caso existam agendamentos no período. No sistema o parâmetro é por padrão desmarcado. |
| **Bloqueia alteração do nome do paciente na agenda de atendimento** | Caso o parâmetro esteja marcado o sistema não permitira a alteração do nome do paciente a partir da agenda de atendimentos. No sistema o parâmetro é por padrão desmarcado. |
| **Nro máximo de dias para agendamento de cirurgias a partir da data de hoje** | Caso o parâmetro esteja preenchido com uma quantidade de dias o sistema, a partir desta quantidade fará um controle de tempo em dias para agendamento de cirurgias. Após atingir esta quantidade  o sistema emitirá uma mensagem informando que o número máximo de dias foi excedido. No sistema o parâmetro é por padrão em branco. |

#### Tela de Registro e Controle VI,acessada no menu AmbienteConfiguração/Parâmetros/Gestão Hospitalar/Registro e Controle/Registro e Controle VI.

| **Parâmetro** | Descrição |
| --- | --- |
| **Preencher médico responsável e indicador por ao selecionar médico solicitante** | Caso o parâmetro esteja marcado, ao informar o médico solicitante no registro do atendimento irá preencher automaticamente as informações do médico indicado por e médico responsável, caso não estejam prenchidos. |

#### Tela de Faturamento, acessada no menu Opções/Parâmetros/Parâmetros Gerais guia Faturamento.

| **Parâmetro** | Descrição |
| --- | --- |
| **Integrar apenas o cirurgião do procedimento principal** | Ao realizar um registro de informações cirúrgicas a partir de uma agenda de cirurgias, ao realizar a criação do registro o sistema irá buscar do agendamento apenas o cirurgião do procedimento principal. |
| **Integrar todos os profissionais** | Ao realizar um registro de informações cirúrgicas a partir de uma agenda de cirurgias, ao realizar a criação do registro o sistema irá buscar do agendamento todos os profissionais pré selecionados. |
| **Não integrar** | Ao realizar um registro de informações cirúrgicas a partir de uma agenda de cirurgias, ao realizar a criação do registro o sistema não irá buscar os profissionais executantes da cirurgia. |

#### Tela de Prontuário Eletrônico, acessada no menu Opções/Parâmetros/Parâmetros Gerais guia Prontuário Eletrônico.

É possível configurar a rotina de agendamento de acordo com as necessidades da instituição, os parâmetros estão nos menus:

* Opções / Parâmetros / Parâmetros Gerais guia Registro e Controle II.
* Opções / Parâmetros / Parâmetros Gerais guia Registro e Controle III.
* Opções / Parâmetros / Parâmetros Gerais guia Registro e Controle IV.
* Opções / Parâmetros / Parâmetros Gerais guia Faturamento.

#### Tela de Registro e Controle II, acessada no menu Opções/Parâmetros/Parâmetros Gerais guia Registro e Controle II.

| **Parâmetro** | Descrição |
| --- | --- |
| **Filtra unidade de atendimento?** | Se este parâmetro estiver marcado ativará o processo  que foi cadastrado no anexo do RM Saúde na rotina de perfil de segurança (Cadastros/segurança/perfil). Somente válido para registro de atendimento e agenda de atendimento. No sistema o padrão é por padrão desmarcado. |
| **Desconsidera unidade na pesquisa.** | Se este parâmetro estiver desmarcado o sistema irá desconsiderar os filtros nas pesquisas de agendamento de atendimento somente valido para registro de atendimento e Agenda de atendimento. No sistema o padrão é por padrão desmarcado. |

#### Tela de Registro e Controle III,acessada no menu Opções/Parâmetros/Parâmetros Gerais guia Registro e Controle III.

| **Parâmetro** | Descrição |
| --- | --- |
| **Alteração automática de Status ao acessar/fechar o Prontuário Eletrônico** | Este parâmetro altera o status automaticamente quando o médico termina o atendimento do paciente. No sistema o parâmetro é por padrão desmarcado. |
| **Exibir aviso de Existência de pendência (financeira, documentações) - aviso de débito** | No momento do atendimento do paciente o sistema alerta sobre a existência de pendências financeiras do paciente em questão. No sistema o parâmetro é por padrão desmarcado. |
| **Exibir Aviso de Cliente em Sala de Espera** | Este parâmetro sinaliza para o médico o tempo de espera do paciente para atendimento - Agenda de Atendimento. No sistema o parâmetro é por padrão desmarcado. |
| **Existência de lista de Espera para Realocar no Agendamento** | Sinaliza para a recepcionista que existem pacientes em lista de espera para especialidade no dia. Caso ocorra uma desistência de agendamento. No sistema o parâmetro é por padrão desmarcado. |
| **Tempo para atualização dos dados de agendamento** | Tempo em minutos em que o sistema irá atualizar a tela automaticamente com os agendamentos efetuados. No sistema o parâmetro é por padrão em branco. |
| **Tempo de verificação do aviso em Sala de Espera** | Tempo em minuto do aviso para o médico sobre a existência de paciente em sala de espera. No sistema o parâmetro é por padrão em branco. |
| **Exibir SALAS na agenda do usuário com perfil de MÉDICO** | Caso o parâmetro esteja marcado permite que o médico visualize as agendas de sala. No sistema o parâmetro é por padrão desmarcado. |
| **Plano obrigatório no agendamento** | Obriga a informação de plano de convênio no momento do agendamento. No sistema o parâmetro é por padrão desmarcado. |
| **Médico faz agendamento de Consulta** | Permite que o médico possa efetuar agendamento de consultas. No sistema o parâmetro é por padrão desmarcado. |
| **Data de nascimento do paciente obrigatório** | Obriga a informação da data de nascimento no momento do agendamento. No sistema o parâmetro é por padrão desmarcado. |
| **Alteração automática de Status ao Gravar Anamnese Especial** | No momento do preenchimento da anamnese Especial no Prontuário Eletrônico o sistema altera o status do agendamento para atendido. |
| **Valida Automaticamente a elegibilidade ao informar o código do beneficiário** | Valida Automaticamente a elegibilidade ao informar o código do beneficiário. No sistema o parâmetro é por padrão desmarcado. |
| **Valida automaticamente a elegibilidade ao pesquisar o paciente** | Valida automaticamente a elegibilidade ao pesquisar o paciente. No sistema o parâmetro é por padrão desmarcado. |
| **Permite conflito de horários no agendamento** | Permite conflito de horários no agendamento. No sistema o parâmetro é por padrão desmarcado. |
| **Utiliza Protocolo no Agendamento** | Gera ao usuário ao concluir um agendamento, um número de protocolo para registro. Este número pode ser pesquisado posteriormente. No sistema ele é por padrão desmarcado. |
| **Integra Agendas do Prestador e Sala** | Caso o parâmetro esteja marcado o sistema associará a agenda do prestador junto a sala cadastrada no sistema. No sistema o parâmetro é por padrão desmarcado. |
| **Lançar honorário associado à atividade da agenda ao registrar o atendimento** | Caso o parâmetro esteja marcado o sistema lançará automaticamente na conta do paciente  o honorário associado a atividade profissional. No sistema o parâmetro é por padrão desmarcado. |
| **Lança exames da agenda ao gerar informações de atend. Externo** | Se no registro do agendamento existir exames agendados o sistema automaticamente gerará os pedidos de exames ao registrar o atendimento do paciente. No sistema o parâmetro é por padrão desmarcado. |
| **Obriga preenchimento do telefone no agendamento.** | Obriga preenchimento do telefone no agendamento. No sistema o parâmetro é por padrão desmarcado. |
| **Relatório da agenda de atendimentos** | Indica qual Relatório do TOTVS REPORTS será utilizado para impressão da agenda de atendimentos. No sistema o parâmetro é por padrão em branco. Utiliza o do sistema. |
| **Não permite salvar um agendamento sem elegibilidade ou autorização** | Não permite que um agendamento seja salvo ao não realizar a solicitação de elegibilidade ou solicitação de procedimento na Agenda de Atendimentos para os convênios que possuem utilização de Web Service parametrizados no sistema. |
| **Não permite encaixe fora do período de atendimento** | Não permite que um encaixe seja realizado na Agenda de Atendimentos em períodos posteriores ou anteriores aos períodos diários parametrizados na agenda. |
| **Utiliza máscara no N° de celular ao Agendar** | Ao digitar o número de celular ao realizar um agendamento, é utilizada a máscara de DDD + 9 dígitos para telefones celulares. |

#### Tela de Registro e Controle IV,acessada no menu Opções/Parâmetros/Parâmetros Gerais guia Registro e Controle IV.

| **Parâmetro** | Descrição |
| --- | --- |
| **Não permitir bloquear período da agenda com agendamentos neste período** | Caso o parâmetro esteja marcado o sistema não permitira o bloqueio de período da Agenda, caso existam agendamentos no período. No sistema o parâmetro é por padrão desmarcado. |
| **Bloqueia alteração do nome do paciente na agenda de atendimento** | Caso o parâmetro esteja marcado o sistema não permitira a alteração do nome do paciente a partir da agenda de atendimentos. No sistema o parâmetro é por padrão desmarcado. |
| **Nro máximo de dias para agendamento de cirurgias a partir da data de hoje** | Caso o parâmetro esteja preenchido com uma quantidade de dias o sistema, a partir desta quantidade fará um controle de tempo em dias para agendamento de cirurgias. Após atingir esta quantidade  o sistema emitirá uma mensagem informando que o número máximo de dias foi excedido. No sistema o parâmetro é por padrão em branco. |

#### Tela de Faturamento, acessada no menu Opções/Parâmetros/Parâmetros Gerais guia Faturamento.

| **Parâmetro** | Descrição |
| --- | --- |
| **Perfil Médico** | Selecione os perfis para definição, os perfils parametrizados possuem o acesso ao botão “Prontuário da Agenda”. |
