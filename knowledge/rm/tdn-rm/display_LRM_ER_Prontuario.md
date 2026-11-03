---
content_hash: 32b41947e3989539fc54adcaf86794cc9081e2320c1d157a7df211ee94ef9bbe
fetched_at: '2026-06-29T00:08:09.831949+00:00'
page_id: '240289080'
product: rm
source: tdn-rm
title: ER_Prontuario
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Prontuario
version: 19
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Segurança e Saúde Ocupacional | **Módulo** | PCMSO |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** | PDR\_RH\_RHU004-111 | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## 1.     Objetivo

O objetivo destas melhorias consiste em fornecer aos usuários do produto:  
• Maior clareza na interpretação de resultados de exames médicos;  
• Identificação de lotes de vacinas;  
•  Controle do fornecimento de medicamento aos colaboradores;  
•  Possibilidade dos próprios médicos organizarem sua agenda;  
•  Fornecimento de uma visualização centralizada de todo o prontuário médico dos colaboradores.

As implementações estão classificadas em dois tipos: Criação e Alteração.  
Os itens classificados como Criação referem-se a novas funções que serão adicionadas ao produto. Os itens classificados como Alteração referem-se a modificações em funções que já existem no produto.

## 2.      Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Faixas de Itens de Informação Clínica | Criação | PCMSO > Itens de Informação Clínica > Faixas | - |
| Opções de Itens de Informação Clínica | Criação | PCMSO > Itens de Informação Clínica > Opções | - |
| Itens de Informação Clínica | Alteração | PCMSO > Itens de Informação Clínica | - |
| Informações Clínicas | Alteração | Cadastros > Funcionário > Segurança e Medicina > Consultas Realizadas > Exames Realizados > Informações Clínicas | - |
| Lotes de Vacina | Criação | PCMSO > Vacinas > Lotes | - |
| Controle de Vacinas | Alteração | Cadastros > Funcionário > Segurança e Medicina > Controle de Vacinas | - |
| Lançamento de Vacinas | Criação | PCMSO > Assistente de Lançamento de Vacinas | - |
| Medicamentos | Criação | PCMSO > Medicamentos | - |
| Retirada de Medicamentos | Criação | PCMSO > Retirada de Medicamento | - |
| Medicamentos Retirados (Prontuário) | Criação | PCMSO > Prontuário > Medicamentos Retirados | - |
| Medicamentos Retirados (Anexo) | Criação | Cadastro > Funcionário > Segurança e Medicina > Medicamentos Retirados | - |
| Consultas Realizadas | Alteração | Cadastro > Funcionário > Segurança e Medicina > Consultas Realizadas | - |
| Tipo de Atendimento | Criação | PCMSO > Tipo de Atendimento | - |
| Disponibilidade do Profissional de Saúde | Criação | Cadastro > Profissional de Saúde > Disponibilidade | - |
| Agenda de Exames | Alteração | PCMSO > Assistente de Importação de Resultado de Exames | - |
| Assistente de Importação de Resultado de Exames | Alteração | PCMSO > Convênios | - |
| Convênios | Alteração | PCMSO > Assist. Agendamento Automático | - |
| Assistente de Agendamento Automático | Alteração | PCMSO > Agenda de Exames > Lançamento de Resultados de Exames | - |
| Lançamento de Resultados de Exames | Alteração | PCMSO > Agenda Médica | - |
| Prontuário | Criação | Agenda Médica > Prontuário Médico | - |

# 2.1.    Faixas de Itens de Informação Clínica

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Anexo.

**Acesso:** PCMSO > Itens de Informação Clínica > Faixas.

**Controle de Segurança:** O mesmo do cadastro de Item de Informação Clínica.

**Descrição:**Será implementado um anexo ao cadastro de **Item de Informação Clínica**, denominado **Faixas**.

Este anexo somente aceitará inclusão de registros para itens de informação clínica cujo o **Tipo de Valor** seja **Numérico**.

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Nome | Texto | Sim | Máximo de 255 caracteres. |
| Operador Inicial | Combobox | Sim | Itens: =, >, >=, <, <=. |
| Valor Inicial | Double | Sim |  |
| Operador Final | Combobox | Não | Itens: >, >=, <, <=. |
| Valor Final | Double | Não |  |
| Cor | Cor | Sim | Seleção de cor à partir de uma paleta de cores. |
| Descrição | Texto | Não |  |
| Consulta SQL | Lookup | Não | Seleção de registro do Cadastro de **Consulta SQL** (Item de menu: **Gestão / Visões de Dados**) cujo campo **Aplicação** seja igual a **V** (Vitae). |

**Validações:**

• Se Operador Final estiver preenchido. Então Valor Final deve estar preenchido.  
• Se Operador Inicial igual a =. Então Operador Final e Valor Final não podem ser preenchidos.  
• Operador Inicial e Operador Final devem ser diferentes.  
• Se Operador Inicial igual a < ou <=. Então Operador Final, se preenchido, deve ser igual a > ou >=.  
• Se Operador Inicial igual a > ou >=. Então Operador Final, se preenchido, deve ser igual a < ou <=.  
• Se Operador Inicial igual a > ou >=. Então o Valor Final deve ser maior ou igual ao Valor Inicial.  
• Se Operador Inicial igual a < ou <=. Então o Valor Final deve ser menor ou igual ao Valor Inicial.  
• O intervalo lógico contido em uma faixa cadastrada, não pode conter um valor comum (interseção) com o intervalo lógico contido em outra faixa cadastrada para o mesmo Item de Informação Clínica, salvo se o valor do campo Consulta SQL for diferente em ambas faixas.  
• A sentença da Consulta SQL selecionada deve conter apenas parâmetros com a identificação **CODPESSOA**.

# 2.1.1.    Cópia de Faixas entre Itens de Informação Clínica:

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Processo.

**Acesso:** PCMSO > Itens de Informação Clínica > Cópia de Faixas entre Itens de Informação Clínica.

**Controle de Segurança:** O mesmo do cadastro de Item de Informação Clínica.

**Descrição:**Será implementado um processo que permitirá, a partir da seleção de um Item de Informação Clínica, de tipo de valor Numérico, copiar todas as faixas cadastradas para outro Item de Informação Clínica que também seja de tipo de valor Numérico e que não possua faixas cadastradas.

Para execução do processo, o usuário deverá selecionar apenas um Item de Informação Clínica na visão, onde estão contidas as faixas a serem copiadas e, antes de executar o processo, selecionar a partir de uma caixa de diálogo o Item de Informação Clínica para onde as faixas deverão ser copiadas.

# 2.2.     Opções de Itens de Informação Clínica

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Anexo.

**Acesso:** PCMSO > Itens de Informação Clínica > Opções.

**Controle de Segurança:** O mesmo do cadastro de Item de Informação Clínica.

**Descrição:**Será implementado um anexo ao cadastro de Item de **Informação Clínica**, denominado **Opções**.

Este anexo somente aceitará inclusão de registros para itens de informação clínica cujo o **Tipo de Valor** seja **Opções**.

**Campos:**

|  |  |  |  |
| --- | --- | --- | --- |
| Item de opção | Lookup | Sim | Seleciona registro do cadastro de **Consistência de Campos** correspondentes à **Tabela Dinâmica** selecionada no **Item de Informação Clínica**. |
| Cor | Cor | Sim | Seleção de cor à partir de uma paleta de cores. |
| Descrição | Texto | Sim |  |

**Validações:**

• Não pode existir dois registros com o mesmo Item de Opção no mesmo Item de Informação Clínica.

# 2.3.    Itens de Informação Clínica

**Tipo de Operação:** Alteração.

**Acesso:** PCMSO > Itens de Informação Clínica.

**Descrição:**Em face dos novos anexos a serem adicionados ao cadastro de Item de Informação Clínica, uma validação será realizada antes da ação de exclusão de registro, impedindo que itens de informação clínica que possuam Faixas ou Opções cadastradas não possam ser excluídas.

# 2.4.    Informações Clínicas

**Tipo de Operação:** Alteração.

**Acesso:** Cadastros > Funcionário > Segurança e Medicina > Consultas Realizadas > Exames Realizados > Informações Clínicas.

**Descrição:**Atualmente, para cada **Item de** **Informação Clínica** associada ao **Tipo de Exame** selecionado, é criado, dinamicamente, um campo, conforme o **Tipo de Valor** definido no cadastro do Item de Informação Clínica: **Numérico**, **Opções**, **Texto (linha única)** e **Texto (múltiplas linhas)**, para que o usuário informe o resultado de cada um dos itens de informação clínica.

A partir desta implementação, nos casos de itens de informação clínica de tipos de valor **Numérico ou Opções**, poderá será exibida uma legenda, contendo uma caixa de cor e um nome, que deverão ser atualizadas de acordo com o valor informado pelo usuário no respectivo campo, conforme regras descritas adiante.

**a) T****ipo de Valor: Numérico**

Preliminarmente serão identificadas todas as faixas de valores cadastradas para o Item de Informação Clínica (vide item 2.1 desta especificação).

Se nenhuma faixa for encontrada, nenhuma legenda será ser exibida.

Se apenas uma faixa for encontrada, será exibida legenda com a cor e o nome da faixa.

Se mais de uma faixa for encontrada, a faixa que tiver uma Consulta SQL será identificada e a sentença da consulta SQL será executada, passando ao parâmetro CODPESSOA o valor do código da pessoa a que pertence o exame selecionado. Se a consulta retornar um ou mais registros, será exibida legenda com a cor e o nome da faixa em questão, senão será exibida legenda com a cor e nome da faixa que não contém a consulta SQL.

Nos casos em que existirem mais de uma faixa com Consulta SQL, será exibida legenda com a cor e nome da primeira faixa em que a consulta SQL retornar um ou mais registros.

Se forem identificadas apenas faixas com Consulta SQL e nenhuma das consultas retornar um ou mais registros, nenhuma legenda será exibida.

Exemplo:

**B)****Tipo de Valor: Opções**

Se existir para o item uma **Opção** cadastrada (vide item 2.2 desta especificação) será exibida a legenda com a cor e descrição cadastrados.

Protótipo:

# 2.5.    Lotes de Vacina

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Anexo.

**Acesso:** PCMSO > Vacinas > Lotes.

**Controle de Segurança:** O mesmo do cadastro de Vacina.

**Descrição:**Será implementado um anexo ao cadastro de Vacinas, denominado Lotes.

**Campo:**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Identificação do Lote | Texto | Sim | Máximo de 255 caracteres. |

**Validações:**

• Não pode ser excluído um registro de lote que esteja associado ao **Controle de Vacinas** de uma pessoa (vide item 2.6 desta especificação).

# 2.6.    Controle de Vacinas

**Tipo de Operação:** Alteração.

**Acesso:** Cadastros > Funcionário > Segurança e Medicina > Controle de Vacinas.

**Descrição:**Será adicionado um novo campo nesta tela, descrito abaixo, posicionado após o campo **Cod. da Vacina**.

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Lote | Lookup | Não | Seleciona registro do cadastro de **Lotes** (anexo do cadastro de **Vacinas**) dentre os registros vinculados à vacina selecionada no campo **Cod. da Vacina**. |

# 2.7.    Lançamento de Vacinas

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Processo.

**Acesso:** PCMSO > Assistente de Lançamento de Vacinas.

**Controle de Segurança:** Segurança e Medicina do Trabalho / PCMSO / Assistente de Lançamento de Vacinas.

**Descrição:**Será implementado um processo destinado ao lançamento de registros de vacina para vários funcionários em uma única ação. Atualmente, o registro é feito por meio de um anexo do cadastro de funcionários (Controle de Vacinas) obrigando o usuário a lançar cada registro separadamente.

**Campos:**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Cod. da Vacina | Lookup | Sim | Seleciona registro do cadastro de Vacinas. |
| Lote | Lookup | Não | Seleciona registro do cadastro de **Lotes** (anexo do cadastro de **Vacinas**) dentre os registros vinculados à vacina selecionada no campo **Cod. da Vacina**. |
| Data | Data | Sim |  |
| Funcionário | Lookup Multirecord | Sim | Seleciona registros do cadastro de funcionários. |

**Validação:**

• Se for identificado que já existe a mesma vacina, na mesma data, para um dos funcionários selecionados, o processo não deverá incluir um novo registro e informar tais ocorrências no log a ser exibido ao final da execução do processo.

# 2.8.    Medicamentos

**Tipo de Operação:** Criação.

**Tipo de Rotina:** CRUD.

**Acesso:** PCMSO > Medicamentos.

**Controle de Segurança:** Segurança e Medicina do Trabalho / PCMSO / Medicamentos.

**Descrição:**Será implementado um cadastro básico de Medicamento.

**Campos:**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Código | Texto | Sim | Máximo de 30 caracteres. |
| Nome | Texto | Sim | Máximo de 255 caracteres. |
| Descrição | Texto | Não |  |

**Validações:**

• Não pode existir dois registros com o mesmo **Código**.

# 2.9.    Retirada de Medicamentos

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Processo.

**Acesso:** PCMSO > Retirada de Medicamento.

**Controle de Segurança:** Segurança e Medicina do Trabalho / PCMSO / Retirada de Medicamentos.

**Descrição:**Será implementado um processo para lançamento de medicamentos fornecidos pela empresa a um determinado funcionário.

**Campos:**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Data | Data | Sim | Valor padrão: Data atual. |
| Pessoa | Lookup | Sim | Seleciona registro do cadastro de pessoas. |
| Medicamentos | Lookup Multirecord | Sim | Seleciona registros do cadastro de medicamentos. |

**Obs.: Este controle não é destinado a gerenciar estoque de medicamentos, apenas registrar a entrega do medicamento ao funcionário.**

# 2.10.    Medicamentos Retirados (Prontuário)

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Anexo.

**Acesso:** PCMSO > Prontuário > Medicamentos Retirados.

**Controle de Segurança:** Segurança e Medicina do Trabalho / PCMSO / Medicamentos Retirados.

**Descrição:**Será implementado um item no Prontuário destinado a registrar os medicamentos fornecidos ao funcionário durante o atendimento.

**Campos:**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Data | Data | Sim | Valor fixo: A mesma data da consulta. |
| Medicamento | Lookup | Sim | Seleciona registro do cadastro de medicamentos. |

# 2.11.    Medicamentos Retirados (Anexo)

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Anexo.

**Acesso:** Cadastro > Funcionário > Segurança e Medicina > Medicamentos Retirados.

**Controle de Segurança:** Mesmo do item 2.10.

**Descrição:**

Será implementado um anexo no cadastro de Funcionário destinado a manutenção dos registros de medicamentos fornecidos pela empresa ao colaborador.

**Campos:**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Data | Data | Sim | Valor padrão: Data atual. |
| Medicamento | Lookup | Sim | Seleciona registro do cadastro de medicamentos. |
| Consulta | Texto | Não | Indica o código da consulta que originou o fornecimento do medicamento. Campo apenas para leitura e visível apenas se o medicamento foi retirando numa consulta. |

**Validação:**

• Se o campo **Consulta** estiver preenchido, a data não pode ser diferente da data da consulta selecionada.

# 2.12.   Consultas Realizadas

**Tipo de Operação:** Alteração.

**Tipo de Rotina:** Anexo.

**Acesso:** Cadastro > Funcionário > Segurança e Medicina > Consultas Realizadas.

**Descrição:**Serão realizados vários ajustes, descritos a seguir, na rotina hoje denominada **Consultas Realizadas**, de modo que este cadastro passe a suportar também o registro de **Consultas Agendadas** e **Atendimentos Laboratoriais**.

Modificações a serem realizadas neste cadastro:

**a) Mudança de Nome**

O nome da tela passará a ser: **Consultas Médicas e Atendimentos Ambulatoriais**.

**b) Novo campo**

Será adicionado um campo denominado **Tipo de Atendimento**. Este campo será um Combobox e o usuário deverá selecionar um dos seguintes itens:

- Consulta Médica Ocupacional  
- Atendimento Ambulatorial

Na atualização para a versão 12.1.4, para todos os registros de consultas realizadas existentes na base de dados este campo receberá o valor: Consulta Médica Ocupacional.

**c) Validação para geração do Atestado de Saúde Ocupacional**

Somente registros cujo o valor do novo campo Tipo de Atendimento seja igual a Consulta Médica Ocupacional, e que não estejam nos status "agendado" ou "pendente", é que serão passíveis de geração do Atestado de Saúde Ocupacional. Caso o usuário selecione um registro que não atenda a esta condição ele será impedido de prosseguir o processo.

**d) Campo Situação**

O campo **Situação Final**, terá o nome modificado para **Situação**.

Neste campo, será adicionada a opção: **Agendado**.

**e) Campo Tipo da Consulta E-Social**

Este campo deixa de ser editável. O **Tipo de Consulta E-Social** será buscado automaticamente do **Tipo da Consulta**, cujo cadastro deixará de ser uma tabela dinâmica conforme descrito no item 2.13 desta especificação.

**f) Filtro do Tipo da Consulta**

Em face da implementação descrita no item 2.13 desta especificação, no campo **Tipo da Consulta** (**Tipo de Atendimento Médico**) somente serão listados os tipos que estejam vinculados ao **Tipo de Atendimento** selecionado.

**g) Outros campos que mudarão de nome:**

- Data da Consulta = Data

- Tipo da Consulta = Tipo de Atendimento Médico

**h) Entidade Padrão e Filtro por Perfil:**

Os parâmetros "Entidade padrão para inclusão de exames no Prontuário" e "Obrigatório filtro de perfil de exames para Prontuário",  disponíveis no parametrizador. Continuam sendo considerados na consulta normalmente, em conformidade com as funcionalidades que se propunham a atender.

# 2.13.   Tipo de Atendimento Médico

**Tipo de Operação:** Criação.

**Tipo de Rotina:** CRUD.

**Acesso:** PCMSO > Tipo de Atendimento Médico.

**Controle de Segurança:** Segurança e Medicina do Trabalho / PCMSO / Tipo de Atendimento Médico.

**Descrição:**Será implementado um cadastro para manutenção da tabela **VTIPOCONSULTA** que define atualmente o **Tipo da Consulta**, mantida pela rotina de **Tabelas Dinâmicas**.

Assim, será retirado o acesso a esta tabela por meio da rotina Tabelas Dinâmicas, bem como outros campos serão acrescentados.

**Campos:**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Código | Texto | Sim | Máximo de 10 caracteres. |
| Descrição | Texto | Sim | Máximo de 50 caracteres. |
| E-Social | Lookup | Não | Seleciona registro da tabela dinâmica **Tipo de Exames conforme NR**. |
| Procedimento(s) | RadioGroup | Sim | Opções:  - Consulta Médica Ocupacional  - Atendimento Ambulatorial  - Ambos |

**Validação:**

• Não pode existir dois registros com o mesmo ****Código.****

# 2.14.   Disponibilidade do Profissional de Saúde

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Anexo.

**Acesso:** Cadastro > Profissional de Saúde > Disponibilidade.

**Controle de Segurança:** O mesmo do cadastro do cadastro de Profissional de Saúde.

**Descrição:**Será implementado um anexo ao cadastro de Profissional de Saúde, denominado Disponibilidade, destinado a registrar os períodos em que o profissional estará disponível para atendimentos para a empresa.

**Campos:**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Data de início | Data | Sim |  |
| Hora de início | Hora | Sim |  |
| Data de término | Data | Sim |  |
| Hora de término | Hora | Sim |  |
| Segunda | Checkbox | Sim |  |
| Terça | Checkbox | Sim |  |
| Quarta | Checkbox | Sim |  |
| Quinta | Checkbox | Sim |  |
| Sexta | Checkbox | Sim |  |
| Sábado | Checkbox | Sim |  |
| Domingo | Checkbox | Sim |  |

# 2.15.   Agenda de Exames

**Tipo de Operação:** Alteração.

**Tipo de Rotina:** CRUD.

**Acesso:** PCMSO > Agenda de Exames.

**Descrição:**Serão acrescentados dois campos, descritos a seguir:

• Médico, Lookup do cadastro de Profissional de Saúde, que permitirá indicar, opcionalmente, qual será o médico responsável pelo exame.

• Consulta associada. Lookup de consulta que pertmite vincular o agendamento à consulta.

# 2.16.   Assistente de Importação de Resultado de Exames

**Tipo de Operação:** Alteração.

**Tipo de Rotina:** Processo.

**Acesso:** PCMSO > Assistente de Importação de Resultado de Exames.

**Descrição:**O processo passará a contemplar os novos campos: Médico e IDConsulta, acrescentado no cadastro de exames agendados, descrito no item 2.16 desta especificação.

As consultas serão incluídas no cadastro de Consultas Médicas com o campo TIPO (VCONSULTASPRONT.TIPO) preenchido como "Consulta Médica Ocupacional".

# 2.17.   Convênios

**Tipo de Operação:** Alteração.

**Tipo de Rotina:** CRUD.

**Acesso:** PCMSO > Convênios.

**Descrição:**Será acrescentado um novo campo, denominado **Prazo para resultado (dias)**, que aceitará valores numéricos inteiros, que determinará a quantidade de dias estimados que o convênio precisa para entregar o resultado do exame selecionado.

# 2.18.    Assistente de Agendamento Automático

**Tipo de Operação:** Alteração.

**Tipo de Rotina:** Processo.

**Acesso:** PCMSO > Assist. Agendamento Automático.

**Descrição:**

Atualmente o processo contempla quatro etapas:

***Opções de agendamento (de exames) > Seleção de Pessoas > Seleção de Exames > Pessoas x Exames***

Serão acrescentadas duas etapas, destacadas a seguir

*Opções de agendamento (de exames) > Seleção de Pessoas > Seleção de Exames > Pessoas x Exames > **Seleção de Médicos > Consultas Agendadas***

As novas etapas irão conter os seguintes campos.

**Campos (Nova etapa: Seleção de Médicos):**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Deseja agendar consultas para análise clínica dos exames selecionados? | Checkbox | Sim |  |
| Médicos | Lookup Multirecord | Sim | Lookup do cadastro de Profissionais de saúde.  Este campo só será habilitado se o usuário marcar o Checkbox “Deseja agendar consultas para análise clínica dos exames selecionados?”. |

**Campos (Nova etapa: Consultas Agendadas):**

| **Campo** | **Tipo** | **Obrigatório?** | **Observações** |
| --- | --- | --- | --- |
| Data da Consulta | Data | Sim |  |
| Hora da Consulta | Hora | Sim |  |
| Tipo da Consulta | Texto | Sim | Somente leitura. |
| Médico Responsável | Lookup | Sim | Lookup do cadastro de Profissionais de saúde.  Listará somente médicos selecionados na etapa **Seleção de Médicos**. |
| Nome do Paciente | Texto | Sim | Somente leitura. |
| Exames | Texto | Sim | Somente leitura. |

**Regra de Negócio:**

Com a implementação contida no item 2.12 desta especificação, passará a existir o registro de consultas “**agendadas**”. Na versão atual só existe o registro de consultas “**realizadas**”.

Isso possibilitará que as consultas clínicas ocupacionais destinadas a avaliar os resultados dos exames realizados, e responsável pela emissão do Atestado de Saúde Ocupacional, sejam planejadas juntamente com o planejamento da realização dos exames.

O planejamento de realização dos exames já existe atualmente e não sofrerá modificação. Entretanto, duas novas etapas serão adicionadas ao final do processo permitindo que também sejam planejadas as consultas clínicas destinadas a avaliar os resultados dos exames, se o usuário assim desejar.

Após a etapa **Pessoas x Exames**, será exibida uma nova etapa denominada **Seleção de Médicos**. Nesta etapa o usuário informará no campo “**Deseja agendar consultas para análise clínica dos exames selecionados?**” se deseja agenda as consultas clínicas. Se recusar, os exames serão agendados, como feito atualmente, sem vínculo direto com uma consulta clínica.

  

Por fim, executado o processo, os exames serão gerados estando vinculados à uma consulta clínica para análise dos mesmos. Essa consulta irá ser criada com o status “**Agendada**”.

**Validação:**

•  Um mesmo médico não poderá ser agendado para atender mais de um paciente na mesma data e horário.

# 2.19.    Lançamento de Resultados de Exames

**Tipo de Operação:** Alteração.

**Tipo de Rotina:** Processo.

**Acesso:** PCMSO > Agenda de Exames > Lançamento de Resultados de Exames.

**Descrição:**Atualmente o processo inicia com a etapa **Dados da Consulta** onde o usuário cadastra as informações que irão gerar um registro da consulta clínica (**Consulta Realizada**) em que ocorreu a análise dos exames selecionados para inclusão do resultado e a emissão do **Atestado de Saúde Ocupacional**. Será acrescentado o campo para o tipo de atendimento com as opções "Consulta Médica Ocupacional" e "Atendimento Ambulatorial", será obrigatório selecionar uma das opções. Também será acrescentada a opção "Agendada" no campo Situação Final.

Será realizado uma alteração nesta mesma etapa, onde a mesma será omitida quando todos os registros de agendas de exames selecionados estejam vinculados a uma **Consulta Agendada**. Neste caso, ao final da execução do processo será exibido uma etapa para se escolher qual a situação final de cada consulta vinculada aos registros de exames agendados. Caso dentro os registros selecionados exista alguma agendamento sem víncula com uma **Consulta Agendada**, a etapa Dados da Consulta será exibida normalmente e a última etapa para seleção de situação consulta não será exibida, uma vez que as informações da consulta serão preenchidas nesta etapa.

# 2.20.    Prontuário

**Tipo de Operação:** Criação.

**Tipo de Rotina:** Visão.

**Acesso:** Cadastros > Pessoa > Prontuário Médico | Agenda Médica > Prontuário Médico.

**Controle de Segurança:** Segurança e Medicina do Trabalho / PCMSO / Prontuário.

**Descrição:**

Será implementada uma visão que permitirá a visualização de todos os dados médicos de um determinado paciente.

Esta visão será carregada a partir da seleção de um registro de pessoa ou funcionário.

As seguintes informações serão exibidas de forma hierárquica (Tree View):

•  Consultas Médicas (Agendadas e Realizadas)

* Exames (Agendados e Realizados)
* Medicamentos

•  Atendimentos Ambulatoriais

* Exames Realizados
* Medicamentos

•  Vacinas

•  Exames Pendentes

•  Atestados

•  CAT’s

As informações serão exibidas para leitura.

As seguintes ações poderão ser executadas a partir das seguintes seleções nesta nova visão:

•  Visualizar dados da pessoa

•  Imprimir Atestado de Saúde Ocupacional (a partir da seleção de uma consulta médica)

**Protótipo:**

Informações a serem apresentadas não estão detalhadas nesta especificação, pois são as mesmas hoje já exibidas em telas existentes, conforme:

| **Item** | **Tela de origem** |
| --- | --- |
| 1. Consultas Médicas | Funcionário > Segurança e Medicina > Consultas Médicas e Atendimentos Ambulatoriais |
| 1.1.        Exames | Funcionário > Segurança e Medicina > Consultas Médicas e Atendimentos Ambulatoriais > Exames Realizados |
| 1.2.        Medicamentos | Funcionário > Segurança e Medicina > Consultas Médicas e Atendimentos Ambulatoriais > Medicamentos |
| 1. Atendimentos Ambulatoriais | Funcionário > Segurança e Medicina > Consultas Médicas e Atendimentos Ambulatoriais |
| 2.1.        Exames Realizados | Funcionário > Segurança e Medicina > Consultas Médicas e Atendimentos Ambulatoriais > Exames Realizados |
| 2.2.        Medicamentos | Funcionário > Segurança e Medicina > Consultas Médicas e Atendimentos Ambulatoriais > Medicamentos |
| 1. Vacinas | Funcionário > Segurança e Medicina > Controle de Vacinas |
| 1. Exames Pendentes | PCMSO > Agenda de Exames |
| 1. Atestados | Funcionário > Segurança e Medicina > Atestados |
| 1. CAT’s | Funcionário > Segurança e Medicina > Ocorrências de Acidente de Trabalho (CAT) |
| 1. Medicamentos | Pessoa > Medicamentos |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
