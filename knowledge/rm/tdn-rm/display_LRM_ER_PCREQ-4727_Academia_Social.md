---
content_hash: 2e234321644719a33675a002e34c94e56da8b0af529a4c356e333fb0d636977e
fetched_at: '2026-06-29T00:06:03.203790+00:00'
page_id: '198951325'
product: rm
source: tdn-rm
title: ER_PCREQ-4727_Academia_Social
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-4727_Academia_Social
version: 4
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | R\_EDU\_EDU011 | **IRM1** | PCREQ-4726 |
| **Requisito1** | PCREQ-4727 | **Subtarefa1** | PDR\_EDU\_EDU011-399 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Definir as regras de negócio para a integração entre TOTVS Educacional e Comunidades do Fluig para implementar o conceito de Academia Social.

 

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Turma e Turma/Disciplina | Alteração | Atividades acadêmicas -> Assistentes -> Cadastro de Turma e Turma/Disciplina | - |
| Inclusão de disciplinas em turmas | Alteração | Atividades acadêmicas -> Assistentes -> Inclusão de disciplinas em turmas | - |
| Cadastro de Curso | Alteração | Currículo e Oferta -> Cursos | - |
| Cadastro de Habilitação / Serie | Alteração | Currículo e Oferta -> Cursos -> Habilitação / Série |  |
| Cadastro de Turmas | Alteração | Currículo e Oferta -> Turmas |  |
| Cadastro de Turmas/Disciplinas | Alteração | Currículo e Oferta -> Turmas/Disciplinas |  |
| Cadastro de subturmas | Alteração | Currículo e Oferta -> Turmas/Disciplinas -> Subturmas |  |
| Cadastro de atividade Ofertada | Alteração | Atividades acadêmicas -> Atividades Ofertadas |  |
| Comissão coordenadora | Alteração | Currículo e Oferta -> Matrizes curriculares -> Matriz aplicada -> Comissão coordenadora |  |
| Cadastro de Professor da Turma/Disciplina | Alteração | Currículo e Oferta -> Turmas/Disciplinas -> Professores |  |
| Matrícula de aluno em Turma/Disciplina | Alteração | Matrícula e Avaliação -> Matrículas -> Matricular Alunos nas disciplinas |  |
| Matrícula no curso e habilitação | Alteração | Currículo e Oferta -> Aluno -> Cursos / Habilitações |  |
| Matrícula do aluno em período letivo | Alteração | Matrícula e Avaliação -> Matrículas |  |
| Criar estrutura de oferta para as turmas/disciplinas sugeridas | Alteração | Integrações -> Scientia -> Criar estrutura de oferta para as turmas/disciplinas sugeridas |  |
| Criar comunidades no Fluig | Criação | Integrações -> Comunidades -> Criar comunidades no Fluig |  |
| Atualizar status das comunidades | Criação | Integrações -> Comunidades -> Atualizar status das comunidades |  |
| Adicionar participantes e moderadores às comunidades | Criação | Integrações -> Participantes -> Adicionar participantes e moderadores às comunidades |  |
| Sincronizar participantes nas comunidades do Fluig | Criação | Integrações -> Participantes -> Sincronizar participantes nas comunidades do Fluig |  |
| Log da sincronização dos participantes nas comunidades do Fluig | Criação | Integrações -> Participantes -> Log da sincronização dos participantes nas comunidades do Fluig |  |

### **Parametrização da Academia Social**

A parametrização da integração com o Fluig (Academia Social) possui os seguintes itens:

**Aba: Geral**

* Definir o código da conta de comunicação com o Fluig.
* Filtrar apenas as informações de períodos letivos em aberto.  
  Este parâmetro determina se as informações vinculadas a períodos letivos encerrados devem ou não ser consideradas nos processos da academia social.

**Aba: Curso, habilitação (Serie), turma, turma/disciplina, subturma e atividade ofertada**

Os parâmetros abaixo estão disponíveis para todas as entidades que podem ser integradas as comunidades do Fluig:

**Geral:**

* Integrar com o Fluig <nome entidade>  
  Define se a entidade em questão estará ou não integrada com as comunidades do Fluig

**Comunidade:**

* Comunidade privada
* Comunidade oculta
* Participação na comunidade deve ser aprovada
* Após exclusão <nome entidade> a comunidade continua ativa  
  Exemplo: A turma “FISIO-0001” é cadastrada e a comunidade “C\_FISIO-0001” é gerada, se a turma “FISIO-0001” for eliminada da base de dados a comunidade vinculada “C\_FISIO-0001” deverá continuar ativa ou será desativada.

* Usuário administrador (este é o usuário que tem total permissão na comunidade que será gerada)
  + Definir administrador da comunidade no processo  
    Neste caso a definição do código do usuário que desempenhará o papel de administrador da comunidade deverá ser realizado nos processos que criarão as comunidades no Fluig.
  + Utilizar como administrador da comunidade o usuário definido nos parâmetros globais
  + Usuário administrador das comunidades relacionadas <nome entidade>  
    A definição do código do usuário que desempenhará o papel de administrador da comunidade deverá ser realizada no próprio parametrizador do TOTVS Educacional.
* Nome padrão para a comunidade (conterá as mesmas tag’s disponíveis na criação da comunidade)
  + Quando a opção “Permitir alterar nome da comunidade nos processos” estiver desmarcada, o usuário pode utilizar a tag [TEXTOLIVRE] na definição do nome da comunidade. Ao utilizar essa tag o sistema permitirá que no processo de criação de comunidade o usuário possa definir um texto que a substituíra. Essa tag só estará disponível na tela de parametrização e apenas para as entidades que podem gerar mais de uma comunidade (curso, habilitação/serie, turma e atividade ofertada).
* Permitir alterar nome da comunidade nos processos.
  + Mesmo com a definição de um padrão para o nome da comunidade o usuário poderá alterá-lo dependendo deste parâmetro.

**Pastas**

* Nome padrão pasta de documentos (Tag disponível: [NOMECOMUNIDADE])
* Nome padrão pasta de formulários (Tag disponível: [NOMECOMUNIDADE])
* Nome padrão pasta de artigos (Tag disponível: [NOMECOMUNIDADE])
* Nome padrão pasta de vídeos (Tag disponível: [NOMECOMUNIDADE])
* Nome padrão pasta de imagens (Tag disponível: [NOMECOMUNIDADE])
* Permitir alterar o nome das pastas nos processos.  
  Se todos os tipos de pastas contiverem o mesmo nome será criada apenas uma pasta no Fluig que centralizará todas os artefatos.
* Permissão para membros (Nenhuma, Leitura, Gravação, Modificação, Total – permissões disponibilizadas pelo Fluig)
* Permissão para moderadores (Nenhuma, Leitura, Gravação, Modificação, Total – permissões disponibilizadas pelo Fluig)
* Identificador da pasta raiz para criação das subpastas
* Permitir alterar a pasta raiz nos processos

**Participação na comunidade:**

* Data da última sincronização dos participantes realizada pelo processo
* Data da última sincronização dos participantes realizada com sucesso pelo processo

**Aba: Curso, habilitação (Serie)**

Os parâmetros abaixo estão disponíveis para as entidades de curso e habilitação:

* ***Coordenadores***  
  + Sincronizar coordenador vinculado <nome entidade>
    - Como moderador da comunidade
    - Como participante da comunidade
  + Nenhuma ação definida (neste caso os coordenadores não serão sincronizados com as comunidades vinculadas a entidade)
  + Coordenador excluído <nome entidade> continua ativo na comunidade  
    Se um coordenador é excluído da comissão coordenadora da matriz aplicada este parâmetro define se este também deve ser excluído das comunidades. O usuário relacionado ao coordenador de um curso pode estar vinculado a uma comunidade também por ser um professor do curso, neste cenário a exclusão do coordenador não acarretará a sua exclusão na comunidade.
  + Coordenador com data final de participação na comissão ultrapassada continua ativo na comunidade  
    A exclusão do usuário vinculado ao coordenador das comunidades segue a mesma regra do item acima.

* ***Professores:***
  + Sincronizar professor vinculado à <nome entidade>:
    - Como participantes da comunidade
    - Nenhuma ação definida (neste caso os professores não serão sincronizados com as comunidades vinculadas a entidade)
  + Professor excluído continua ativo na comunidade.  
    Para que o professor seja retirado da comunidade este deve ser excluído de todas as turmas/disciplinas relacionadas ao curso.
  + Professor com data final de participação nas turmas ultrapassada continua ativo na comunidade  
    Da mesma forma que o item anterior não pode estar com data válida em nenhuma turma/disciplina relacionada ao curso.

**Aba: Turma, Turma/Disciplina e Subturma**

Os parâmetros abaixo estão disponíveis para as entidades turma, turma/disciplina e subturma:

**Geral:**

* Período letivo encerrado comunidades continuarão ativas  
  Este parâmetro define se as comunidades vinculadas a turma, turma/disciplina e/ou subturmas continuam ativas mesmo após o encerramento de um período letivo.  Se este parâmetro estiver definido para desativar as comunidades o encerramento de período letivo ocasionará a desativação de todas as comunidades vinculadas ao período letivo. Caso o período letivo seja reaberto as comunidades vinculadas não serão ativadas, o usuário deverá executar o processo de ativação de comunidade.

**Comunidade:**

* A entidade turma/disciplina possui o seguinte parâmetro adicional.
  + Turma/disciplina gerenciais e gerenciadas:
    - Criar comunidade para turma/disciplina gerencial
    - Criar comunidade para turma/disciplina gerenciada  
      As opções não são excludentes, ou seja, pode-se criar comunidades para turma/disciplinas gerencial e gerenciada desde que os dois parâmetros acima estejam marcados.

* A entidade turma/disciplina e subturma possuem o seguinte parâmetro adicional.
  + Após turma/disciplina inativada comunidade continuará ativa  
    Se este parâmetro estiver desmarcado ao colocar uma turma/disciplina como inativa as comunidades relacionadas a turma/disciplina e subturmas serão desativadas, no entanto, a ativação da turma/disciplina não ativará as comunidades.

**Participação na comunidade:**

* ***Coordenadores:***
  + Sincronizar coordenador vinculado <nome entidade>
    - Como moderador da comunidade
    - Como participante da comunidade
    - Nenhuma ação definida (neste caso os coordenadores não serão sincronizados com as comunidades vinculadas a entidade)
  + Coordenador excluído da matriz aplicada da <nome entidade> continua ativo na comunidade
  + Coordenador com data final de participação na comissão ultrapassada continua ativo na comunidade

* ***Alunos:***
  + Aluno excluído da <nome entidade> continua ativo na comunidade

* ***Professores:***
  + Sincronizar professor vinculado à <nome entidade>:
    - Como moderadores da comunidade
    - Como participantes da comunidade
    - Nenhuma ação definida (neste caso os professores não serão sincronizados com as comunidades vinculadas a entidade)
  + Professor excluído da <nome entidade> continua ativo na comunidade
  + Professor com data final de participação na <nome entidade> ultrapassada continua ativo na comunidade

**Atividade Ofertada**

Os parâmetros abaixo devem ser criados para atividade ofertada:

**Participação na comunidade:**

* ***Inscrito:***
  + Sincronizar pessoas na atividade ofertada:
    - Como participante da comunidade
    - Nenhuma ação definida (neste caso as pessoas inscritas não serão sincronizadas com as comunidades vinculadas a atividade ofertada)
  + Sincronizar alunos na atividade ofertada:
    - Como participante da comunidade
    - Nenhuma ação definida (neste caso os alunos inscritos não serão sincronizados com as comunidades vinculadas a atividade ofertada)
  + Sincronizar professores na atividade ofertada:
    - Como participante da comunidade
    - Como moderador da comunidade
    - Nenhuma ação definida (neste caso os professores inscritos não serão sincronizados com as comunidades vinculadas a atividade ofertada)
  + Inscrito excluído da atividade ofertada continua ativo na comunidade
  + Inscrito com data final de participação ultrapassada na atividade ofertada continua ativo na comunidade

**Associação entre comunidade do Fluig e as entidades do TOTVS Educacional**

Regras especificas para as entidades: Turma/disciplina e Subturma

Cada registro relacionado as entidades de turma/disciplina e subturma poderá possuir apenas uma comunidade associada e estas poderão ter como participantes professores, alunos e coordenadores. Como forma de registrar esse vínculo os cadastros dessas entidades conterão um novo campo responsável por armazenar o alias da comunidade (este valor será gerado no momento da criação da comunidade no Fluig).

Estas entidades também disponibilizarão exctenderactions, responsáveis por exibir as informações gerais da comunidade vinculada ao registro selecionado. Informações do tipo: Nome da comunidade, descrição da comunidade, número de moderadores, número de participantes.

Regras especificas para as entidades: Curso, Habilitação (Serie), Turma e Atividade Ofertada

Cada registro relacionado as entidades de curso, habilitação, turma e atividade ofertada poderá possuir “n” comunidades associadas e para cada uma delas será possível estabelecer o público alvo ao qual devem pertencer os participantes. As associações entre comunidades e entidades serão armazenadas na tabela SCOMUNIDADESOCIAL e poderão ser consultadas através de um anexo a ser disponibilizado nessas entidades. Estes anexos exibirão as informações gerais das comunidades, como por exemplo, nome comunidade, descrição comunidade, número de moderadores, número de participantes e público alvo.

Regras gerais para todas as entidades

A criação de atividades ofertadas, turma, turma/disciplina, subturma, curso ou habilitação (serie) não acarreta a criação automática de uma comunidade, para tanto, o usuário deverá executar o processo de criação de comunidades.

Quando um registro relacionado a uma das entidades de turma, turma/disciplina, subturma, atividade ofertada, curso ou habilitação for excluído e o mesmo estiver vinculado a uma comunidade esta será desativada ou continuará ativa dependendo da parametrização definida pelo usuário. A mesma regra será aplicada para turmas/disciplinas e suas subturmas que tiverem o status alterado para inativa.

### **Período letivo encerrado**

No encerramento do período letivo as comunidades vinculadas às turmas, turma/disciplinas e subturmas serão desativadas ou continuarão ativas dependendo da parametrização.

### **Situação de Matrícula**

Incluir no cadastro de situação de matrícula novos campos para definição do status do aluno nas comunidades (ativo ou inativo), esta opção deverá estar disponível nas abas “Status no curso”, “Status no período letivo”, “Status na disciplina”.

### **Apuração de resultado**

Quando a opção de encerrar o período letivo estiver marcada na apuração de resultado dependendo da parametrização as comunidades podem continuar ativas ou serem desativadas.

### **Processos de criação de oferta**

Processos que criam oferta quando a integração com o Fluig estiver ativada devem possibilitar a criação de comunidades. Tais processos devem possuir campos para permitir a definição do nome, descrição da comunidade e se o parâmetro “Definir o usuário administrador da comunidade no processo de criação” estiver marcado deve-se permitir a definição do usuário administrador. Os processos impactados são:

* Processo cadastro de turma e turma /disciplina
* Processo inclusão de disciplinas em turmas
* Copiar turmas entre períodos letivos
* Processo de criação de oferta através do modelo 2 de integração do Scientia

Cada entidade deve possibilitar o uso de algumas tags:

* Turma (STURMA) - Tags disponíveis: [CODTURMA], [CODPERLET], [NOMETURMA], [NOMERED], [DTINICIAL], [DTFINAL].
* Turma/disciplina (STURMADISC) - Tags disponíveis: [CODTURMA], [CODPERLET], [CODDISC], [NOMEDISC], [NOMETURMA], [DTINICIAL], [DTFINAL].
* Subturma (SSUBTURMA) - Tags disponíveis: [CODTURMA], [CODPERLET], [CODDISC], [NOMEDISC], [NOMETURMA], [DTINICIAL], [DTFINAL], [CODSUBTURMA].

Para entidades que podem conter “n” comunidades os processos devem possibilitar a criação de “n” comunidades bem como a definição para cada uma de seu público alvo.

Dependo dos parâmetros do educacional o usuário poderá definir as pastas onde serão armazenados os artefatos e também em qual pasta raiz deverão ser criadas.

 Algumas informações relacionadas a nome da comunidade, nome das pastas e identificador da pasta raiz podem ser alteradas no processo desde que parametrizado com esta permissão.

### **Processo que permite realizar a criação, desativação de comunidade em lote**

Quando o tipo de operação selecionado no processo for “criação de novas comunidades” as seguintes funcionalidades devem ser disponibilizadas:

Disponibilizar dois campos para que o usuário possa definir o nome e a descrição das comunidades a serem criadas. Para tornar o processo mais fácil deve-se disponibilizar algumas tags que no momento da criação da comunidade serão substituídas pelos valores do registro.

* Turma (STURMA)
  + Tags disponíveis: [CODTURMA], [CODPERLET], [NOMETURMA], [NOMERED], [DTINICIAL], [DTFINAL].
* Turma/disciplina (STURMADISC)
  + Tags disponíveis: [CODTURMA], [CODPERLET], [CODDISC], [NOMEDISC], [NOMETURMA], [DTINICIAL], [DTFINAL].
  + Listar as turmas/disciplinas que estejam ativas.
* Subturma (SSUBTURMA)
  + Tags disponíveis: [CODTURMA], [CODPERLET], [CODDISC], [NOMEDISC], [NOMETURMA], [CODSUBTURMA]
  + Listar as subturmas de turmas/disciplinas que estejam ativas
* Atividade Ofertada pela instituição (SATIVIDADE)
  + Tags disponíveis: [IDOFERTA], [CODCOMPONENTE],[DESCCOMPONENTE], [CODMODALIDADE], [DESCMODALIDADE], [LOCAL], [DESCRICAO], [DTINICIAL], [DTFINAL].
  + Listar as atividades ofertadas cujo período de datas ainda seja válido (campos: DTINICIAL e DTFINAL)
* Curso (SCURSO)
  + Tags disponíveis: [CODCURSO], [NOMECURSO].
* Habilitação ou Serie (SHABILITACAO)
  + Tags disponíveis: [CODCURSO], [NOMECURSO], [CODHABILITACAO], [NOMEHABILITACAO].

Dependo dos parâmetros do educacional o usuário poderá definir as pastas onde serão armazenados os artefatos e também em qual pasta raiz deverão ser criadas.

 Algumas informações relacionadas a nome da comunidade, nome das pastas e identificador da pasta raiz podem ser alteradas no processo desde que parametrizado com esta permissão.

Se a opção “Definir o usuário administrador da comunidade no processo de criação” estiver marcada deve-se disponibilizar ao usuário a possibilidade de escolher o usuário administrador para as comunidades que serão criadas.

Para as entidades de curso, habilitação, turma e atividade ofertada será possível solicitar a criação de “n” comunidades para cada registro e definir para cada uma delas o público alvo.

Este processo deverá permitir ao usuário determinar que após a criação da comunidade já seja realizada a adição de participantes e moderadores. Neste processo não será possível definir pontualmente os participantes ou moderadores, ou seja, se solicitar a inclusão dos professores todos vinculados a entidade serão incluídos à comunidade.

Quando o tipo de operação selecionado no processo for “desativar comunidades” ou “ativar comunidades” as seguintes funcionalidades devem ser disponibilizadas:

O usuário poderá consultar dentre as comunidades ativas ou inativas quais deseja desativar ou ativar respectivamente. Será disponibilizada uma consulta para cada entidade que estiver integrada com as comunidades do Fluig, permitindo a seleção dos registros e execução do tipo de operação escolhido.

### **Processo adicionar moderadores e participantes para as comunidades**

O processo deverá possibilitar a adição de participantes e moderadores as comunidades de todas a entidades que estiverem com a integração ativada.

* Funcionalidades do processo
  + Definir para qual entidade o processo será executado.
  + Selecionar os registros vinculados a entidade definida.

**Turma, Turma/disciplina, subturma, curso, habilitação (serie):**

* Estas entidades podem conter mais de uma comunidade, por esta razão deve-se possibilitar a definição de quais comunidades serão alvo do processo.
* Selecionar os alunos que devem ser incluídos como participantes da comunidade
  + O usuário poderá optar por não chamar nenhum aluno
  + Selecionar os professores:
    - O usuário poderá optar por não chamar nenhum professor
    - Para as entidades de turma, turma/disciplina e subturma deve ser possível definir para cada professor o seu papel na comunidade (participante ou moderador)
  + Selecionar os coordenadores:
    - O usuário poderá optar por não chamar nenhum coordenador
    - Para todas as entidades deve ser possível definir para cada coordenador seu papel na comunidade (participante ou moderador)

**Atividade ofertada**

* Selecionar os inscritos:
  + Os inscritos devem ser selecionados em três passos:
    - Seleção de pessoa
    - Seleção de professor
    - Seleção de alunos  
      Para todos os passos o usuário terá a opção de não chamar nenhum participante

O log deverá detalhar para cada turma, turma/disciplina, subturma, curso, habitação (serie) e atividade ofertada pela instituição quais os alunos, professores, coordenadores e/ou inscritos que foram inseridos como participantes ou moderadores das comunidades.

Regras para que um usuário possa ser definido como participante ou moderador de uma comunidade

**Foco: Aluno**

* Os alunos com situação de matrícula que estabeleça o status de ativo na comunidade do fluig.
  + Situação de matrícula no curso apenas para o ensino superior: impacto nas comunidades do curso e habilitação.
  + Situação de matrícula no período: impacto nas comunidades de turma quando ensino superior e para curso, serie e turma quando ensino básico.
  + Situação de matrícula na disciplina: impacto nas comunidades das turmas/disciplinas e subturmas.

**Foco: Professores**

* Os professores devem estar associados à turma/disciplina ativas.
* A data atual deve estar compreendida entre a data inicial e final de participação dos professores nas turmas/disciplinas.
* Os professores devem estar ativos.

**Foco: Coordenadores**

* A data atual deve estar compreendida entre a data inicial e final de participação do coordenador na comissão coordenadora da matriz aplicada.

### **Processo de sincronização de participantes das comunidades**

Vários processos do TOTVS Educacional podem acarretar a necessidade de inclusão ou exclusão de participantes das comunidades no Fluig. Entre eles podemos citar:

* Cadastro de professor da turma/disciplina
* Cadastro de professor do horário da turma/disciplina (apenas para subturma)
* Cadastro de inscrições em atividades ofertadas disciplina
  + Alunos inscritos na atividade ofertada
  + Professores da atividade ofertada
  + Pessoas inscritas na atividade ofertada
* Processos de inscrição em atividade ofertada disciplina
* Cadastro de comissão coordenadora da matriz aplicada
* Cursos / Habilitações
* Matricula de aluno em disciplinas
* Matricula de aluno em um período letivo
* Matrícula isolada
* Alteração de situação de matricula nas disciplinas
* Alteração de situação de matricula no período letivo
* Transferência interna
* Mudança de turma
* Enturmação
* Enturmação em turma mista
* Rematrícula
* Processo seletivo RM
* Processo seletivo terceirizado
* Demissão de um professor

O processo de sincronização deverá verificar nas tabelas do TOTVS Educacional os registros alterados pelos itens definidos acima para determinar os cenários em que haverá a necessidade de inclusão ou exclusão de participantes e ou moderadores nas comunidades. O processo de sincronização deve verificar estes cenários e realizar a atualização das comunidades vinculadas obedecendo os parâmetros do educacional que definem regras para este processo. (verificar para mais detalhes “Parametrização da Academia Social”)

As exclusões de registros das tabelas (exemplo: professor da turma/disciplina, coordenador da matriz aplicada, inscritos em atividades ofertadas) também não serão sincronizadas automaticamente, estas serão registras na tabela de log de sincronização como uma exclusão agendada. Desta forma ao eliminar um professor da turma/disciplina este não será automaticamente eliminado da comunidade vinculada a turma/disciplina.

Para cada entidade com integração com o Fluig ativada temos parâmetros que interferem na execução do processo: 

* Sincronizar alunos, professores, coordenadores ou inscritos como participantes ou moderadores ou não sincronizar?
* A exclusão de alunos, professores, coordenadores ou inscritos determinam a sua exclusão das comunidades?
* A data de participação de professores na turma ou de coordenadores na comissão coordenadora foi ultrapassada estes continuam ativos na comunidade?

Um professor ou coordenador só será efetivamente eliminado das comunidades se estes não estiverem ligados as comunidades através de outra função. Exemplo: um coordenador que deve ser excluído da comunidade de turma só o será se este não desempenhar a função de professor para essa mesma turma.

Qualquer erro durante a sincronização de um participante determina a inserção do mesmo na tabela de log da sincronização com o status de erro, acarretando a não atualização da data da última sincronização com sucesso. Desta forma quando o processo de sincronização for novamente executado o sistema deverá reenviar os registros com erro de sincronização ocorridos desde a última sincronização com sucesso.

* **Foco professor**
  + **Exclusão:**
    - Professores demitidos (verificar qual a integração Labore ou Protheus, caso não existe integração basta verificar o status do professor na filial)
    - Professores com a data de participação na turma/disciplina já expirada.  (Data de início e fim no cadastro do professor na turma).
  + **Inclusão:**
    - Professores incluídos em turmas/disciplinas devem ser adicionados as comunidades conforme parametrizações.

Para **limitar** os registros a serem verificados o sistema realiza os seguintes filtros:

+ - **Demitidos:**
    * Os professores que tiverem sido demitidos desde a última execução do processo. No caso de integração com o Protheus ou na ausência de integração verificar a data da alteração do cadastro de professor por filial, já no caso de integração com o Labore verificar esta mesma data no cadastro do funcionário.
  - **Participante/Moderador:**
    * Deve estar parametrizado para adicionar como participante ou moderador das comunidades
    * As datas de alteração dos registros relacionados ao professor devem ser posteriores a data em que ocorreu a última sincronização.

* **Foco aluno**
  + Alunos devem ser excluídos ou incluídos como participantes quando a situação de matricula assim determinar. Tais ações serão realizadas de acordo com a parametrização do sistema.

**Ensino Superior**

* + Comunidades de curso e habilitação deve-se verificar se a situação de matricula no curso determina que o aluno é um participante ativo da comunidade.

**Ensino Básico**

* + Comunidades de curso e serie deve-se verificar se a situação de matricula no período letivo determina que o aluno é um participante ativo da comunidade.

**Qualquer contexto**

* + Comunidade de turma/disciplina e subturma deve-se verificar se a situação de matrícula na disciplina determina que o aluno é um participante ativo da comunidade.
    - Comunidade de turma deve-se verificar se a situação de matrícula no período letivo determina que o aluno é um participante ativo na comunidade.
    - Para limitar os registros que devem ser verificados:
      * Apenas os alunos que tiveram alteração de situação de matricula posterior à data da última sincronização.
      * Verificar os parâmetros do sistema para determinar se apenas as informações dos períodos letivos em aberto deverão ser consideradas.
      * O que evidência que um aluno está matriculado na subturma é o preenchimento do campo CODSUBTURMA da matricula do aluno (SMATRICULA).

* **Foco inscritos**
  + Inscritos em uma atividade ofertada devem ser excluídos ou incluídos como participantes de acordo com a parametrização do sistema.

Para limitar os registros que devem ser verificados:

* + Apenas os inscritos que tiveram data de alteração posterior à data da última sincronização.

Este processo deve ser construído de forma que possa ser agendado.

Ao final da execução deste processo, o parâmetro “Data da última sincronização” deve ser atualizado e o parâmetro “Data da última execução com sucesso” só deverá ser atualizado quando não ocorrer erro na sincronização.

Para limitar ainda mais os registros a serem verificados neste processo temos como regra geral a verificação do parâmetro do educacional que estabelece se apenas as informações dos períodos letivos em aberto devem ser consideradas.

### **Visibilidade das funcionalidades**

A visibilidade das funcionalidades de integração com o Fluig está diretamente ligada à configuração dos parâmetros do sistema. Por exemplo, o anexo relacionado as comunidades no cadastro de turma só estará visível se a integração com esta entidade estiver ativada.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
