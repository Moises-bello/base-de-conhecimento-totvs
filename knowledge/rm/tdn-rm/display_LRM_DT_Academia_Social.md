---
content_hash: 1d573fe22b27b99c4562ac4efdc284eeb65c07ffe7803f48f84ec0c8b81c7442
fetched_at: '2026-06-29T00:06:05.537265+00:00'
page_id: '201723619'
product: rm
source: tdn-rm
title: DT_Academia_Social
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Academia_Social
version: 15
---

# Academia Social

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS* |
| **Módulo:** | *Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Assist**ente de criação de tu**rma e turma/disciplina* | Cadastro de turma e turma/disciplina | | Assistente de criação de turma/disciplina | Inclusão de disciplinas em turmas | | Assistente de cópia de turma entre períodos letivos | Copiar turmas entre períodos letivos | | Assistente de criação de oferta do Scientia | Criar estrutura de oferta a partir das turmas/disciplinas sugeridas | | Parametrização do sistema | Parâmetros |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Turma* | *Cadastro de turma* | | Turma/disciplina | Cadastro de turma/disciplina | | Subturma | Cadastro de subturma | | Atividade Ofertada | Cadastro de atividades ofertadas | | Curso | Cadastro de curso | | Habilitação / serie | Cadastro de habilitação / Cadastro de serie | | Matrícula de alunos | Matricular | | Inscrição em atividade ofertada | Inscrições em atividades ofertadas, cadastro de inscrição de alunos, professores e pessoas | | Professores da turma/disciplina | Cadastro de professores da turma/disciplina | | Coordenadores das matrizes aplicadas | Cadastro de comissão coordenadora | | Alteração de status das disciplinas, período letivo e curso | Alterar situação de matrícula | | Situação de matrícula | Cadastro de situação de matrícula | |
| **Cadastros Iniciais:** | **Parâmetros do sistema e dependendo deste deve-se possuir turma, turma/disciplina, subturma, curso, habilitação (serie) e/ou atividade ofertada** |
| **Parâmetro(s):** | *Parâmetros do sistema relacionado a acadêmia social* |
| **Requisito (ISSUE):** | [PCREQ-4727](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-4727 "PCREQ-4727") |
| **País(es):** | *Brasil* |
| **Tabelas utilizadas:** | *STURMADISC, SSUBTURMA, SCOMUNIDADESOCIAL, SCOMUNIDADESOCIAL, SCOMUNIDADESOCIALLOGSINC, SCOMUNIDADESOCIALPUBLICOALVO, SSTATUS* |
| **Versões/Release:** | *12.1.7* |

## Descrição

A utilização de comunidades sociais no contexto acadêmico já é uma realidade nas instituições de ensino e a TOTVS já disponibiliza através do Fluig todos os recursos necessários para implantação deste conceito. A partir da versão 12.1.7 com a implementação da integração entre TOTVS Educacional e Fluig a criação de comunidades e manutenção de seus participantes ficou muito mais ágil e simples para nossos clientes.

Este documento será dividido em três grandes blocos: configuração do ambiente, parametrizações do TOTVS Educacional e o funcionamento das funcionalidades, cada um destes abordando o passo a passo para ativar a integração.

# Configuração do ambiente

## Fluig:

1. Utilizar o usuário administrador do Fluig e acessar o **Painel de controle -> WCM**
2. Configurar o **Oauth Provider**
3. Configurar o **Oauth App** (pode-se utilizar qualquer conjunto de caracteres para definição do *Consumer Key* e *Consumer Secret*)  
   Para mais detalhes sobre o passo 2 e 3 consulte o documento "Cadastrar aplicativo no Fluig" pelo link: <http://tdn.totvs.com/display/public/fluig/Fluig+API#FluigAPI-CadastraraplicativonoFluig>

## Parâmetros Globais e Contas de Comunicação

1. Acessar a guia **Ambiente -> Parâmetros -> Globais**
   1. Aba: **Integração Fluig** definir:
      1. Endereço do servidor do Fluig
      2. Id da empresa do Fluig
      3. Usuário administrador do Fluig
      4. Senha do usuário administrador do Fluig
   2. Aba: **Integração oAuth** definir:
      1. Chave de consumo: é a chave *consumer key* definida na etapa da configuração do fluig.
      2. Chave secreta: é a chave *consumer secret* definida na etapa da configuração do fluig.
   3. Salvar os parâmetros
2. Acessar a guia **Gestão -> Fontes** e verificar se a fonte de comunicação com o Fluig está cadastrada. Caso não encontre entre em contato com o suporte da TOTVS.
3. Acessar a guia **Gestão -> Contas -> Contas individuais** e criar um novo registro
   1. Código da fonte de comunicação: vincular a fonte relacionada ao Fluig
   2. Utilizar "Usar esta conta como remetente"
   3. Identificação na rede social: informar o usuário mestre do Fluig
   4. Obter credenciais: ao clicar neste botão será exibida a tela de login do Fluig onde deve ser informado o usuário administrador e sua senha
   5. As credenciais serão obtidas e o campo Descrição será preenchido com o nome do usuário administrador.
   6. Salvar o registro

# Parametrizações do TOTVS Educacional

O TOTVS Educacional passa a disponibilizar a integração com o Fluig - Social, possibilitando a criação de comunidades para as seguintes entidades:

* Curso
* Habilitação ou Serie
* Turma
* Turma/disciplina
* Subturma
* Atividade ofertada

Por padrão a integração com as entidades acima estão desativadas e para ativá-las deve-se acessar os parâmetros do TOTVS Educacional (Integração -> Fluig) e realizar as configurações, abaixo uma descrição dos parâmetros disponibilizados:

**Aba: Geral**

* Definir o código da conta de comunicação com o Fluig.  
  Registro criado no cadastro de "Contas individuais" mencionado no item de configuração do ambiente.
* Filtrar apenas as informações de períodos letivos em aberto.  
  Este parâmetro determina se as informações vinculadas a períodos letivos encerrados devem ou não ser consideradas nos processos da academia social.

**Aba: Curso, habilitação (serie), turma, turma/disciplina, subturma e atividade ofertada**

Os parâmetros abaixo estão disponíveis para todas as entidades:

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
  Quando a opção “Permitir alterar nome da comunidade nos processos” estiver desmarcada, o usuário pode utilizar a tag [TEXTOLIVRE] na definição do nome da comunidade. Ao utilizar essa tag o sistema permitirá que no processo de criação de comunidade o usuário possa definir um texto que a substituíra. Essa tag só estará disponível na tela de parametrização e apenas para as entidades que podem gerar mais de uma comunidade (curso, habilitação/serie, turma e atividade ofertada).
* Permitir alterar nome da comunidade nos processos.  
  Mesmo com a definição de um padrão para o nome da comunidade o usuário poderá alterá-lo dependendo deste parâmetro.

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

* Data da última sincronização dos participantes realizada
* Data da última sincronização dos participantes realizada com sucesso

**Aba: Curso, habilitação (Serie)**

Os parâmetros abaixo estão disponíveis para as entidades de curso e habilitação (serie):

* ***Coordenadores***  
  + Sincronizar coordenador vinculado <nome entidade>
    - Como moderador da comunidade
    - Como participante da comunidade
    - Nenhuma ação definida (neste caso os coordenadores não serão sincronizados pelo processo de sincronização automática)
  + Coordenador excluído <nome entidade> continua ativo na comunidade  
    Se um coordenador é excluído da comissão coordenadora da matriz aplicada este parâmetro define se este também deve ser excluído das comunidades.   
    O usuário relacionado ao coordenador de um curso pode estar vinculado a uma comunidade também por ser um professor do curso, neste cenário a exclusão do coordenador não acarretará a sua exclusão na comunidade.
  + Coordenador com data final de participação na comissão ultrapassada continua ativo na comunidade  
    Segue a mesma regra do item acima.

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

* ***Alunos****:*
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

# Funcionamento das funcionalidades

## **Associação entre comunidade do Fluig e as entidades do TOTVS Educacional**

### Regras especificas para as entidades: Turma/disciplina e Subturma

Cada registro relacionado as entidades de turma/disciplina e subturma poderá possuir apenas uma comunidade associada e estas poderão ter como participantes professores, alunos e coordenadores. Como forma de registrar esse vínculo os cadastros dessas entidades conterão um novo campo responsável por armazenar o alias da comunidade (este valor será gerado no momento da criação da comunidade no Fluig).

Para acessar as informações da comunidade associada a estes cadastros basta acessar:

* **Currículo e Oferta -> Turmas/Disciplinas -> Comunidades do Fluig**
* **Currículo e Oferta -> Turmas/Disciplinas -> Subturmas -> Comunidades do Fluig**

Será exibida as informações relacionadas a comunidade:

* Nome da comunidade
* Descrição da comunidade
* Número de moderadores
* Número de participantes.
* Status
* Conteúdo privado
* Comunidade oculta
* Data de atualização
* Data de criação
* Requer aprovação
* Lista dos participantes

### Regras especificas para as entidades: Curso, Habilitação (Serie), Turma e Atividade Ofertada

Cada registro relacionado as entidades de curso, habilitação (serie), turma e atividade ofertada poderá possuir “n” comunidades associadas e para cada uma delas será possível estabelecer o público alvo ao qual devem pertencer os participantes. As associações entre comunidades e entidades poderão ser consultadas através de um anexo disponibilizado nessas entidades. Para acessar as informações basta acessar:

* **Currículo e Oferta -> Cursos -> Comunidades do Fluig**
* **Currículo e Oferta -> Cursos -> Habilitações (Series) -> Comunidades do Fluig**
* **Currículo e Oferta -> Turmas -> Comunidades do Fluig**
* **Atividades Acadêmicas -> Atividades Ofertadas -> Comunidades do Fluig**

Será exibida as informações relacionadas a comunidade:

* Nome da comunidade
* Descrição da comunidade
* Número de moderadores
* Número de participantes.
* Status
* Conteúdo privado
* Comunidade oculta
* Data de atualização
* Data de criação
* Requer aprovação
* Lista dos participantes
* Lista do público alvo da comunidade

### Regras gerais para todas as entidades

A criação de atividades ofertadas, turma, turma/disciplina, subturma, curso ou habilitação (serie) não acarreta a criação automática de uma comunidade, caso seja necessário o usuário deverá executar o processo de criação de comunidades (**Integrações -> Comunidades -> Criar Comunidades no Fluig**).

Quando houver a exclusão de um registro relacionado as entidades de turma, turma/disciplina, subturma, atividade ofertada, curso ou habilitação o sistema verifica o parâmetro do educacional que determina se a(s) comunidade(s) deve(m) ser desativada(s) ou deve(m) continuar ativa(s). Nos casos em que as comunidades continuam ativas o sistema apenas elimina o vinculo entre a entidade e a comunidade, ou seja, a comunidade continua ativa e sem nenhum tipo de vinculo com o TOTVS Educacional.

Para os registros de turma/disciplina e subturma, a comunidade também poderá ser desativada quando o status da turma/disciplina for alterado para inativa, dependendo do parâmetro que determina este comportamento no sistema. As turmas/disciplinas que tiverem o status alterado para ativo não terão suas comunidades ativadas automaticamente, para isso o usuário deverá executar o processo de "Atualizar Status das Comunidades do Fluig" (**Integrações -> Comunidades -> Atualizar Status das Comunidades do Fluig**).

## **Processos de criação de oferta**

Quando as entidades de turma e/ou turma/disciplina estiverem parametrizadas para integrar com o Fluig os processos que criam a oferta passam a disponibilizar uma nova aba que permite a criação da comunidade. Nesta nova aba será possível definir o nome, descrição da comunidade e se o parâmetro “Definir o usuário administrador da comunidade no processo de criação” estiver marcado é possível definir o usuário administrador da comunidade. Os processos que passam a possibilitar a criação de comunidades são:

* Processo cadastro de turma e turma /disciplina (**Atividades acadêmicas -> Assistentes -> Cadastro de turma e turma/disciplina**)
* Processo inclusão de disciplinas em turmas (**Atividades acadêmicas -> Assistentes -> Inclusão de disciplinas em turmas**)
* Copiar turmas entre períodos letivos (**Currículo e Oferta -> Turmas -> Copiar turmas entre períodos letivos**)
* Processo de criação de oferta através do modelo 2 de integração do Scientia (**Integrações -> Scientia ->****Criar estrutura de oferta a partir das turmas/disciplinas sugeridas**)

Cada entidade deve possibilitar o uso de algumas tags para definição do nome e da descrição das comunidades:

* Turma (STURMA) - Tags disponíveis: [CODTURMA], [CODPERLET], [NOME], [NOMERED], [DTINICIAL], [DTFINAL].
* Turma/disciplina (STURMADISC) - Tags disponíveis: [CODTURMA], [CODPERLET], [CODDISC], [NOMEDISC], [NOMETURMADISC], [DTINICIAL], [DTFINAL].
* Subturma (SSUBTURMA) - Tags disponíveis: [CODTURMA], [CODPERLET], [CODDISC], [NOMEDISC], [NOMETURMADISC], [DTINICIAL], [DTFINAL], [CODSUBTURMA].

No caso da entidade turma os processos devem possibilitar a criação de “n” comunidades bem como a definição para cada uma de seu público alvo.

Dependo dos parâmetros do educacional o usuário poderá definir as pastas onde serão armazenados os artefatos e também em qual pasta raiz deverão ser criadas.

 Algumas informações relacionadas a nome da comunidade, nome das pastas e identificador da pasta raiz podem ser alteradas no processo desde que parametrizado com esta permissão.

## Processo: "Criar comunidades no Fluig" (Integrações -> Comunidades -> Criar comunidades no Fluig):

O usuário deve definir o nome e a descrição das comunidades a serem criadas e poderá para estes campos utilizar algumas tags que no momento da criação da comunidade serão substituídas pelos valores do registro. As tags disponíveis são:

* Turma (STURMA)
  + Tags disponíveis: [CODTURMA], [CODPERLET], [NOMETURMA], [NOMERED], [DTINICIAL], [DTFINAL].
* Turma/disciplina (STURMADISC)
  + Tags disponíveis: [CODTURMA], [CODPERLET], [CODDISC], [NOMEDISC], [NOMETURMADISC], [DTINICIAL], [DTFINAL].
* Subturma (SSUBTURMA)
  + Tags disponíveis: [CODTURMA], [CODPERLET], [CODDISC], [NOMEDISC], [NOMETURMA], [CODSUBTURMA]
* Atividade Ofertada pela instituição (SATIVIDADE)
  + Tags disponíveis: [IDOFERTA], [CODCOMPONENTE],[DESCCOMPONENTE], [CODMODALIDADE], [DESCMODALIDADE], [LOCAL], [DESCRICAO], [DTINICIAL], [DTFINAL].
* Curso (SCURSO)
  + Tags disponíveis: [CODCURSO], [NOMECURSO].
* Habilitação ou Serie (SHABILITACAO)
  + Tags disponíveis: [CODCURSO], [NOMECURSO], [CODHABILITACAO] ou [CODSERIE], [NOMEHABILITACAO] ou [NOMESERIE].

Na seleção dos registros para criação das comunidades existem alguns pré requisitos que podem impedir que um determinado registro seja listado.

* Turma:
  + Dependendo da parametrização da integração turmas de períodos letivos encerrados não são listadas.
* Turma/Disciplina
  + Dependendo da parametrização da integração turmas de períodos letivos encerrados não são listadas.
  + Turmas/disciplinas devem estar ativas e não devem conter uma comunidade já gerada.
* Subturma  
  + Dependendo da parametrização da integração turmas de períodos letivos encerrados não são listadas.
  + Turmas/disciplinas vinculadas a subturma devem estar ativas.
  + Subturmas não devem conter uma comunidade já gerada.
* Atividade Ofertada
  + Apenas atividades ofertadas cujo período entre a data inicial e final ainda esteja válido.

Dependo dos parâmetros do educacional o usuário poderá definir as pastas onde serão armazenados os artefatos e também em qual pasta raiz deverão ser criadas.

 Algumas informações relacionadas a nome da comunidade, nome das pastas e identificador da pasta raiz podem ser alteradas no processo desde que parametrizado com esta permissão.

A definição do usuário administrador para as comunidades é obrigatória no processo se a opção “Definir o usuário administrador da comunidade no processo de criação” estiver marcada nos parâmetros de integração do TOTVS Educacional.

As entidades de curso, habilitação, turma e atividade ofertada podem conter  “n” comunidades para cada registro e cada uma dessas comunidades possui a definição do público alvo.

Além da criação da comunidade este processo permite que os participantes e moderadores das comunidades sejam incluídos, no entanto, não permite a escolha pontual dos registros como pode ser feito no processo "Adicionar participantes e moderadores às comunidades". Desta forma quando selecionada a opção de adicionar os participantes e moderadores o sistema executa a inclusão de todas as pessoas aptas a ingressarem nas comunidades.

## Processo: "Atualizar status das comunidades do Fluig" (Integrações -> Comunidades -> Atualizar status das comunidades do Fluig):

Através deste processo o usuário pode consultar dentre as comunidades ativas ou inativas quais deseja desativar ou ativar respectivamente. Para tanto basta seguir os seguintes passos:

* Primeiro passo: Definir a operação: ativar ou desativar
* Segundo passo: Definir a entidade: Curso, Habilitação (Serie), Turma, Turma/Disciplina, Subturma ou Atividade Ofertada
* Terceiro passo: Selecionar as comunidades vinculadas aos registros da entidade selecionada no passo anterior
* Quarto passo: Executar o processo

## **Processo: "Adicionar participantes e moderadores às comunidades" (Integrações -> Participantes -> Adicionar participantes e moderadores às comunidades)**

O processo deverá possibilitar a adição de participantes e moderadores as comunidades de todas a entidades que estiverem com a integração ativada.

* Primeiro passo: definir a entidade e realizar o filtro dos registros que desta entidade.
* Segundo passo:
  + **Entidades: Turma, Turma/disciplina, subturma, curso, habilitação (serie):**

    - Estas entidades podem conter mais de uma comunidade, por esta razão deve-se possibilitar a definição de quais comunidades serão alvo do processo.
    - Selecionar os alunos que devem ser incluídos como participantes da comunidade

      * O usuário poderá optar por não chamar nenhum aluno
    - Selecionar os professores:

      * O usuário poderá optar por não chamar nenhum professor
      * Para as entidades de turma, turma/disciplina e subturma deve ser possível definir para cada professor o seu papel na comunidade (participante ou moderador)
    - Selecionar os coordenadores:
      * O usuário poderá optar por não chamar nenhum coordenador
      * Para todas as entidades deve ser possível definir para cada coordenador seu papel na comunidade (participante ou moderador)
  + **Entidades: Atividade ofertada**
    - Selecionar os inscritos:
      * Os inscritos devem ser selecionados em três passos:
        + Seleção de pessoa
        + Seleção de professor
        + Seleção de alunos  
          Para todos os passos o usuário terá a opção de não chamar nenhum participante
* Terceiro passo: execução do processo e exibição do log que  deverá detalhar para cada entidade os alunos, professores, coordenadores e/ou inscritos que foram inseridos como participantes ou moderadores das comunidades.

Regras para que um usuário possa ser definido como participante ou moderador de uma comunidade

**Foco: Aluno**

* Os alunos com situação de matrícula que estabeleça o status de ativo na comunidade do fluig.
  + Situação de matrícula no curso apenas para o ensino superior: impacto nas comunidades do curso e habilitação.
  + Situação de matrícula no período letivo: impacto nas comunidades de turma quando ensino superior e para curso, serie e turma quando ensino básico.
  + Situação de matrícula na disciplina: impacto nas comunidades das turmas/disciplinas e subturmas.
  + Deve possuir usuário gerado

**Foco: Professores**

* Os professores devem estar associados à turma/disciplina ativas.
* A data atual deve estar compreendida entre a data inicial e final de participação dos professores nas turmas/disciplinas.
* Os professores não podem estar demitidos.
* Deve possuir usuário gerado

**Foco: Coordenadores**

* A data atual deve estar compreendida entre a data inicial e final de participação do coordenador na comissão coordenadora da matriz aplicada.
* Deve possuir usuário gerado

**Foco: Inscritos**

* A data atual deve estar compreendida entre a data inicial e final de participação do inscrito na atividade ofertada.
* Deve possuir usuário gerado

## **Processo: Sincronizar participantes nas comunidades do Fluig (Integrações -> Participantes -> Sincronizar participantes nas comunidades do Fluig)**

Inúmeros processos do TOTVS Educacional podem gerar a necessidade de inclusão ou exclusão de participantes das comunidades no Fluig. Segue abaixo a lista desses processos:

* Cadastro de professor da turma/disciplina
* Cadastro de inscrições em atividades ofertadas disciplina
  + Alunos inscritos na atividade ofertada
  + Professores da atividade ofertada
  + Pessoas inscritas na atividade ofertada
* Processos de inscrição em atividade ofertada disciplina
* Cadastro de comissão coordenadora da matriz aplicada
* Cadastro de Cursos
* Cadastro de Habilitações (Series)
* Matrícula do aluno no curso
* Matrícula de aluno em disciplinas
* Matrícula de aluno em um período letivo
* Matrícula isolada
* Alteração de situação de matrícula no curso
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

O processo de sincronização tem por objetivo verificar nas tabelas do TOTVS Educacional os registros alterados pelos itens definidos acima e determinar de acordo com as parametrizações da integração quais os cenários em que haverá a necessidade de inclusão ou exclusão de participantes e ou moderadores nas comunidades. (Verificar para mais detalhes “Parametrização da Academia Social”)

Para cada entidade com integração com o Fluig ativada temos parâmetros que interferem na execução do processo: 

* Sincronizar alunos, professores, coordenadores ou inscritos como participantes ou moderadores ou não sincronizar?
* A exclusão de alunos, professores, coordenadores ou inscritos determinam a sua exclusão das comunidades?
* A data de participação de professores na turma ou de coordenadores na comissão coordenadora foi ultrapassada, estes continuam ativos na comunidade?

As exclusões de registros das tabelas (exemplo: professor da turma/disciplina, coordenador da matriz aplicada, inscritos em atividades ofertadas) não serão sincronizadas automaticamente, estas serão registras na tabela de log de sincronização como uma exclusão agendada, desta forma ao eliminar um professor da turma/disciplina este não será automaticamente eliminado da comunidade vinculada a turma/disciplina.

Um professor ou coordenador só será efetivamente eliminado das comunidades se estes não estiverem ligados as comunidades através de outra função. Exemplo: um coordenador da matriz aplicada da "TURMA X" foi excluído, desta forma sua exclusão da comunidade da "TURMA X" só será agendada se este não desempenhar a função de professor desta mesma turma.

Qualquer erro durante a sincronização de um participante determina a inserção do mesmo na tabela de log da sincronização com o status de erro, este fato acarreta a não atualização do campo "data da última sincronização com sucesso". Na próxima execução do processo de sincronização o sistema tentará reenviar os registros com status de erro registrados entre as datas de última sincronização com sucesso e última sincronização.

**Foco professor: a execução ou não das ações definidas abaixo dependem das parametrizações realizadas no TOTVS Educacional**

* **Exclusão:**
  + Professores demitidos (verificar qual a integração Labore ou Protheus, caso não exista integração basta verificar o status do professor na filial)
  + Professores com a data de participação na turma/disciplina já expirada.  (Data de início e fim no cadastro do professor na turma).
* **Inclusão:**
  + Professores incluídos em turmas/disciplinas.

Para **limitar** os registros a serem verificados o sistema realiza os seguintes filtros:

* **Demitidos:**
  + Os professores que tiverem sido demitidos desde a última execução do processo de sincronização. No caso de integração com o Protheus ou na ausência de integração verificar a data da alteração do cadastro de professor por filial (**Currículo e Oferta -> Professores -> Filiais do Professor**), já no caso de integração com o Labore verificar esta mesma data no cadastro do funcionário.
* **Participante/Moderador:**
  + Deve estar parametrizado para adicionar como participante ou moderador das comunidades
  + As datas de alteração dos registros relacionados ao professor da turma/disciplina devem ser posteriores a data em que ocorreu a última sincronização. (**Currículo e Oferta -> Turmas/Disciplinas -> Professores**)
  + Verificar os parâmetros do sistema para determinar se apenas as informações dos períodos letivos em aberto deverão ser consideradas.

**Foco aluno: **a execução ou não das ações definidas abaixo dependem das parametrizações realizadas no TOTVS Educacional****

* Alunos devem ser excluídos ou incluídos como participantes quando a situação de matrícula assim determinar.  
  **Ensino Superior :** a inclusão de participantes nas comunidades de curso e habilitação é determinada pela  situação de matricula do aluno no curso, mais precisamente pelo campo "Aluno ativo na comunidade do Fluig" da aba "Status no curso".  
  **Ensino Básico:** a inclusão de participantes nas comunidades de curso e serie é determinada pela situação de matricula do aluno no período letivo, mais precisamente pelo campo "Aluno ativo na comunidade do Fluig" da aba "Status no período letivo".  
  **Qualquer contexto:**  
  A inclusão de participantes nas comunidade de turma/disciplina e subturma é determinada pela situação de matrícula do aluno nas disciplinas, mais precisamento pelo campo "Aluno ativo na comunidade do Fluig' da aba "Status na disciplina".  
  A inclusão de participantes nas comunidade de turma é determinada pela situação de matrícula do aluno no período letivo, mais precisamento pelo campo "Aluno ativo na comunidade do Fluig" da aba "Status no período letivo".
* Para limitar os registros que devem ser verificados:
  + Os alunos matriculados em um curso, período letivo ou disciplinas após a data da última sincronização.
  + Os alunos que tiveram alteração de situação de matricula (no período letivo e/ou disciplinas) após a data da última sincronização.
  + Verificar os parâmetros do sistema para determinar se apenas as informações dos períodos letivos em aberto deverão ser consideradas.

**Foco inscritos: ****a execução ou não das ações definidas abaixo dependem das parametrizações realizadas no TOTVS Educacional******

* Inscritos em uma atividade ofertada devem ser excluídos ou incluídos como participantes.

Para limitar os registros que devem ser verificados:

* Apenas os inscritos que tiveram data de alteração posterior à data da última sincronização.

A execução do processo de sincronização pode ter sua execução agendada.

Ao final da execução deste processo, o parâmetro “Data da última sincronização” é sempre atualizado, já o parâmetro “Data da última execução com sucesso” só será atualizado quando não ocorrer erros na sincronização. Como a sincronização pode ser realizada apenas para uma entidade essas datas podem ser diferentes para cada uma das entidades.

### **Período letivo encerrado e Apuração de resultado**

Quando o parâmetro "Período letivo encerrado comunidades continuarão ativas" estiver marcado a ação de alterar um período letivo para encerrado ou a execução da apuração de resultado com a opção de encerrar o período letivo marcada, acarretam a desativação de todas as comunidades vinculadas ao período letivo encerrado. Este parâmetro tem impacto das comunidades vinculadas as entidades de turma, turma/disciplina e subturma.

Após encerramento do período letivo e desativação das comunidades a alteração do período letivo para em aberto não provoca a ativação automática das comunidades, sendo necessário que o usuário execute o processo "Atualizar status das comunidades do Fluig".

**Situação de Matrícula**

O cadastro de situação de matrícula passa a disponibilizar novos campos para definição do status do aluno nas comunidades (ativo ou inativo), um campo para cada uma das abas “Status no curso”, “Status no período letivo”, “Status na disciplina”. Por padrão todas as situações de matrícula estão com o novo parâmetro desmarcado. A correta definição destes é muito importante para que o processo de sincronização seja realizado com sucesso.

### **Visibilidade das funcionalidades**

A visibilidade das funcionalidades de integração com o Fluig está diretamente ligada à configuração dos parâmetros do sistema. Por exemplo, o anexo relacionado as comunidades no cadastro de turma só estará visível se a integração com esta entidade estiver ativada.
