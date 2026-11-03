---
content_hash: 91b0023eb9a0fe5e993b4f919032aa284f5ca891957bda55bc89716116de173b
fetched_at: '2026-06-29T00:11:42.822969+00:00'
page_id: '799265656'
product: rm
source: tdn-rm
title: Peso e Altura dos Equipamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Peso+e+Altura+dos+Equipamentos
version: 3
---

Essa página dedica-se a explicar desde o início como funciona o cadastro e o uso dos equipamentos de sala dentro do sistema, com suas devidas regras.

O cadastro de equipamentos de sala fica localizado no menu Cadastros > Unidades de Diagnóstico > Cadastro de Equipamentos de Sala , conforme ilustração abaixo.

Neste cadastro apenas os campos Cód. Equipamento, Descrição do Equipamento e a marcação Ativo são campos obrigatórios. Os campos de peso mínimo e máximo, assim como altura mínimo e máximo são de preenchimento opcional por parte do usuário e serão utilizados para validações no agendamento e assistente de agendamento ao incluir exames para pacientes em salas com equipamentos vinculados.

A tabela de equipamentos de sala no banco de dados tem o nome SZEQUIPAMENTOSDESALA cuja chave primária é composta pelo código da coligada e o código do equipamento.

Ao informar os campos do cadastro de equipamentos algumas validações serão feitas antes de salvar o mesmo com sucesso. Caso sejam informados peso ou altura inválidos o cadastro será impedido de ser gravado, seguem alguns exemplos desta validação:

E caso seja identificado que o equipamento está vinculado a uma sala que possui agendamento futuro e o usuário tente inativar o equipamento o sistema irá disparar uma mensagem alertando este erro e impedirá o salvamento do cadastro.

Dentro do cadastro de salas, em Cadastros > Registro e Controle > Salas é possível vincular um equipamento de sala a ela, e somente com equipamentos vinculados que será possível fazer validações de peso e altura do paciente no agendamento. Segue exemplo abaixo:

Como regra geral apenas equipamentos Ativos poderão ser selecionados para ser vinculados às salas, e uma vez feito isso, os equipamentos de sala só poderão ser inativados caso não seja identificado agendamento futuro para salas com este equipamento vinculado.

Na Agenda de Atendimentos, ao selecionar uma agenda do tipo Sala, ao configurar a mesma em Opções > Períodos a coluna Sala automaticamente será preenchida com a Sala selecionada anteriormente para evitar que o usuário mude a mesma durante a configuração, para agendas do tipo Médico o comportamento será exatamente o anterior à inovação. segue exemplo abaixo:

Durante a criação de um agendamento, na aba de Exames ao selecionar um ou múltiplos exames e nas informações complementares forem informados peso e altura do paciente algumas validações ocorrerão.

Caso seja informada uma altura superior a 3m o sistema disparará uma mensagem de erro alertando ao usuário para que corrija o preenchimento:

E caso seja informados peso ou altura que o equipamento de sala vinculado à sala do exame não suporte, será dispara a msg de erro alertando ao usuário e abortando o processo de agendamento.

No assistente de agendamento, ao incluir exames tendo peso e altura informados, ao selecionar a unidade de atendimento e a agenda, apenas unidades e salas cujo equipamento teve seu peso e altura validados serão demonstrados na lista de seleção, segue exemplo:

1º caso não seja validado o peso e ou altura:

2º caso sejam validados o peso e a altura:
