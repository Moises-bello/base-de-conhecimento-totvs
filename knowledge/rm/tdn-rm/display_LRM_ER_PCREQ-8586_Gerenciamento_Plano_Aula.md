---
content_hash: e12df1ad26742970b5884e35bf8aeb1a037b764499821ab0ff49bb5fc5ff2002
fetched_at: '2026-06-29T00:06:19.977538+00:00'
page_id: '221546028'
product: rm
source: tdn-rm
title: ER_PCREQ-8586_Gerenciamento_Plano_Aula
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8586_Gerenciamento_Plano_Aula
version: 141
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | R\_EDU016 | **IRM1** | PCREQ-8490 |
| **Requisito1** | PCREQ-8586 | **Subtarefa1** | PDR\_EDU\_EDU016-38 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Possibilitar ao usuário realizar o gerenciamento do plano de aula através de uma única interface, permitindo realizar a manutenção no cadastro e entidades que estejam relacionadas diretamente com o plano de aula.

## Definição da Regra de Negócio

Atualmente os módulos de horários, professores e plano de aula que estão disponíveis através da entidade de Turmas/Disciplinas do TOTVS Educacional estão distribuídas entre cadastros, anexos e processos, o que impacta no dinamismo de elaboração destes mapeamentos (horário, alocação de professor, definição de valores, locais, salas, etc) para resultar no horário e plano de aula. A distribuição destas informações faz com que o usuário tenha que realizar acesso a vários lugares para conseguir concluir sua tarefa e/ou visualizar as informações.

Com essa nova interface (Gerenciamento de Plano de Aula), nosso cliente terá todas informações em uma única interface, onde poderá ter acesso direto e simplificado às informações para ajustes necessários, bem como as informações complementares relacionadas diretamente a entidade de plano de aula. Lembrando que os cadastros, anexos e processos existentes para criação do plano de aula continua com o mesmo comportamento e não será alterado, pois essa "nova" funcionalidade irá unificar as informações e permitir uma manutenção no plano de aula de forma mais ágil e fácil para nosso cliente.

Em resumo, a geração de plano de aula atualmente no sistema TOTVS Educacional consiste em: Cadastrar turnos/horários, associar professores a turma/disciplina (opcional), cadastrar ou gerar horários para as turma/disciplinas e por fim, realizar a geração do plano de aula, que é a "geração dia a dia" das aulas, de acordo com os horários para a turma/disciplina.

**Nova funcionalidade - Gerenciamento de aula**

Essa nova funcionalidade irá conter algumas divisões, para facilitar o entendimento e operação, tais como:

* **Filtro**: Nessa partição, o usuário deverá informar alguns filtros para possibilitar o carregamento dos dados a serem exibidos/alterados, são eles:
  + **Período letivo**: Este campo será um lookup para o cadastro de período letivo do sistema, por padrão, o sistema irá carregar o período letivo definido na parametrização do sistema (TOTVS Educacional | Configurações | Parâmetros | 15.01 Secretaria | Período letivo | Período letivo); Este campo será de preenchimento obrigatório e seguirá a mesma regra das outras funcionalidades, exibindo apenas períodos letivos que não estejam encerrados.
  + **Turma**: Este campo será um lookup para o cadastro de turmas, que irá exibir apenas turmas pertencentes ao período letivo selecionado anteriormente. Este campo será de preenchimento obrigatório, e deverá ser informado.
  + **Disciplina**: Este campo será um lookup para o cadastro de turma/disciplinas, que irá exibir apenas turmas/disciplinas pertencentes ao período letivo e turma selecionados anteriormente. Este campo será de preenchimento opcional.
  + **Selecionar**: Este componente será um botão, que ao ser acionado irá filtrar os dados a serem exibidos na partição "dados". Este botão deverá obrigar o preenchimento dos campos "Período letivo" e "Turma", permitindo a consulta dos dados baseado nestes campos.
* **Dados**: Nessa partição, o usuário irá visualizar os dados em formato de "visão" (grid), referentes ao plano de aula, prédio, bloco, sala, disciplina, etc. Essa visão irá permitir o acesso e atalhos para recursos necessários a montagem do plano de aula, incluindo diretamente na visão os dados de disciplina, plano de aula, horário (caso não exista na turma/disciplina, será automaticamente inserido) e professor (caso não exista no professor da turma, será automaticamente inserido).
  + **Disciplina**: Essa coluna será um lookup para o cadastro de turma/disciplinas no sistema, que deverá filtrar pelas turmas/disciplinas do período letivo e turma selecionados no filtro. Mas caso o filtro "Disciplina" esteja preenchido, deve-se permitir selecionar apenas essa disciplina do filtro.
  + **Nome**: Essa coluna será para visualização (não permite alteração) para descrição da disciplina selecionada na coluna disciplina.
  + **Aula**: Essa coluna deverá permitir informar o dia da aula do plano de aula (sequencial).
  + **Data**: Essa coluna deverá permitir informar a data do plano de aula.
  + **Início**: Essa coluna deverá permitir informar o horário da aula, mas deverá ser filtrada pelo turno da disciplina (permitir informar apenas horários que pertencem ao turno da turma/disciplina) e que são do mesmo dia da semana para a data informada. Caso o horário não esteja cadastrado na turma/disciplina deve-se cadastrar este horário nos horários da turma/disciplina (Cadastro de turma/disciplina | anexo Horários).
  + **Término**: Essa coluna será para visualização (não permite alteração) para exibir o término do horário informado na coluna "início".
  + **Prédio**: Essa coluna será um lookup para o cadastro de prédio do sistema.
  + **Bloco**: Essa coluna será um lookup para o cadastro de blocos do prédio selecionado na coluna "prédio".
  + **Sala**: Essa coluna será um lookup para o cadastro de salas do bloco selecionado na coluna "bloco".
  + **Conteúdo**: Essa coluna será o conteúdo previsto do plano de aula, porém ela deverá exibir alguns poucos caracteres e para ser possível editar de uma forma mais amigável será exibida uma janela para alteração/inserção desse campo.
  + **Observação**: Essa coluna será uma observação do plano de aula, porém ela deverá exibir alguns poucos caracteres e para ser possível editar de uma forma mais amigável será exibida uma janela para alteração/inserção desse campo. (Novo campo "OBSERVACAO" na tabela SPLANOAULA). Essa coluna será apenas informativo no cadastro e não existirá regra envolvida.
  + **Confirmado/Aula planejada**: Essa coluna será um checkbox para que o usuário possa confirmar o planejamento da aula (Novo campo "CONFIRMACAO" na tabela SPLANOAULA), essa coluna será apenas informativa no cadastro e não existirá regra envolvida. A coluna auxilia na orientação e organização interna da instituição, com o intuito de mostrar quais aulas já estão com o planejamento confirmado (dia, horário e professor confirmado). A utilização deste campo NÃO indica que a aula irá ocorrer ou não no dia e horário definidos, conforme citado anteriormente, pelo fato de não existir nenhuma regra no sistema associada à esse campo, seu valor não será considerado em nenhuma das visualizações/cadastros que envolvem as aulas e seus respectivos horários, seja para alunos ou para professores.  
      
      
    Para cada registro de plano de aula, será exibido uma outra "grid" (estilo registro mestre-detalhe) para associação do(s) professor(es) da turma/disciplina (Cadastro de turma/disciplina | anexo Professores):  
      
    - **Professor**: Essa coluna será um lookup para o cadastro de professor no sistema, mas deverá ser filtrado pelas seguintes condições:
      * Caso o parâmetro "Considerar somente disciplinas autorizadas dos professores (Parâmetros Educacional | Secretaria | Geral 1/5)" esteja marcado, deve-se filtrar os professores que estejam com a mesma disciplina autorizada cadastrada (Cadastro de Professor | anexo Disciplinas autorizadas);
      * Caso o parâmetro "Permitir cadastrar professor que não seja funcionário" (Parâmetros | 15.05 - Integração | 15.05.01 - Folha) esteja desmarcado, deve-se filtrar os professores que possuem função de professor no RM Labore (TOTVS Educacional | Currículo e Oferta | Professores | Função de professor);
      * Filtrar pelas filiais do professor (TOTVS Educacional | Currículo e Oferta | Professores | anexo Filiais do professor), ou seja, deve-se exibir os professores de acordo com a filial da turma/disciplina;
    - **Nome**: Essa coluna será para visualização (não permite alteração) para exibir o nome do professor na coluna professor.
    - **Valor hora**: Essa coluna será para informar o valor hora do professor na turma/disciplina;
    - **Valor Fixo**: Essa coluna será para informar o valor fixo do professor na turma/disciplina;
    - **Dt. início**: Essa coluna será para informar a data inicial do professor na turma/disciplina;
    - **Dt. término**: Essa coluna será para informar a data de término do professor na turma/disciplina;
    - **Compõe salári**o: Essa coluna será para informar se esse registro do professor irá compor salário;Caso o usuário esteja inserindo um professor que não esteja associado ao horário do plano de aula, este deverá ser inserido automaticamente como professor do horário (Cadastro de turma/disciplina | anexo Horários | anexo Professor do horário).  
      
    **Exclusão de plano de aula**: A exclusão de plano de aula será realizada conforme cadastro original da funcionalidade e obedecendo as mesmas validações que por ventura existam.  
    **Inclusão de plano de aula**: No momento da inclusão de um plano de aula, será verificado se existe horário selecionado para a turma/disciplina previamente selecionada. Caso negativo, será necessário a inclusão  de um horário (o horário selecionado para o registro de plano de aula que se está incluindo) na entidade de horários da turma/disciplina. Caso seja informado professor e este não esteja cadastrado na turma/disciplina ou no horário, este deverá ser cadastrado na turma/disciplina e adicionado ao horário da turma/disciplina.  
    **Alteração de plano de aula**: A alteração na data, horário ou disciplina do registro de plano de aula compete a exclusão do registro citado e a criação de um novo, visto que pela estrutura física da tabela essa alteração não será permitida, tendo que realizar a exclusão de um registro para inserção de outro. A alteração de qualquer outro campo poderá ser tratado como uma alteração simples a ser refletida nos campos das tabelas de plano de aula.  
      
    Todas as regras de inclusão/alteração/exclusão dos cadastros para possibilitar a geração de plano de aula por essa funcionalidade serão mantidas conforme as regras originais de cada cadastro, visto que essa funcionalidade tem como objetivo unificar os cadastros e permitir uma maior agilidade ao usuário em relação a manutenção (gerenciamento) do plano de aula. Lembrando que qualquer alteração no plano de aula, a ordenação da aula poderá ficar incoerente com o data da aula e deve-se rodar o "novo" processo para ordenar a aula com a data do plano de aula.

* **Operação**: Nessa partição, o usuário deverá decidir em relação a atualização (salvar) ou cancelar as possíveis alterações realizadas nos dados:
  + **Salvar**: Este componente será um botão, que ao ser acionado irá realizar a atualização dos dados informados pelo usuário.
  + **Fechar**: Este componente será um botão, que ao ser acionado irá "descartar" todas alterações realizadas e fechar a funcionalidade.

**Alterações em funcionalidades existentes:**

* O cadastro de plano de aula (Cadastro de Turma/disciplina | Anexo Plano de aula) será alterado para adicionar os dois novos campos (Observação e Confirmado).
* Será disponibilizado o campo "Observação" do plano de aula para o Portal Educacional e EducaMobile somente para o professor, pois será um campo de tratamento entre o professor e/ou secretaria e que não justifica estar visível para os alunos.
* O campo "Confirmado" do plano de aula será disponibilizado somente no TOTVS Educacional (RM.exe), pois se trata de um campo apenas informativo e que não existirá nenhuma regra sobre o mesmo.
* Será alterado o cadastro de plano de aula (tabela SPLANOAULA) para incluir um novo campo para compor a chave primária (IDPLANOAULA). Com isso, o campo AULA deixará de ser chave primária da tabela, mas continua sendo de preenchimento obrigatório. Com isso, algumas tabelas serão alteradas para passarem a tratar a nova chave primária, são elas: SPLANOAULA, SPLANOAULAARQUIVO e SLOGPLANOAULA.
* Será alterado o processo de geração de plano de aula e o cadastro para compor o novo campo da tabela (SPLANOAULA.IDPLANOAULA).
* Será disponibilizado um novo processo dentro do cadastro de turma/disciplina para ordenação da "aula" do plano de aula pela data, visto que este poderá ficar desordenado, quando o usuário realizar alterações pela nova funcionalidade "Gerenciamento de aula" (incluindo uma nova aula por exemplo).
* Será disponibilizado um botão no cadastro de "Turma" e "Turma/Disciplina" para abrir a tela de gerenciamento de aula pelo registro selecionado, assim o usuário poderá ter acesso direto a funcionalidade pelo cadastro corrente

## Protótipo de Tela

## Dicionário de Dados

**Tabela: SPLANOAULA**

 

|  |  |
| --- | --- |
| **Campo** | OBSERVACAO |
| **Tipo** | TEXT |
| **Tamanho** |  |
| **Valor Inicial** |  |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Observação |
| **Título** |  |
| **Picture** |  |
| **Help de Campo** |  |

|  |  |
| --- | --- |
| **Campo** | CONFIRMADO |
| **Tipo** | VARCHAR(1) |
| **Tamanho** | 1 |
| **Valor Inicial** | N |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Confirmado |
| **Título** | Confirmado |
| **Picture** |  |
| **Help de Campo** |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
