---
content_hash: 40f003543de27b413a86d857866756b2655649752fe7a2be6933f2db8d1448a9
fetched_at: '2026-06-29T00:11:04.144402+00:00'
page_id: '625471226'
product: rm
source: tdn-rm
title: Censo da Educação Básica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625471226
version: 267
---

# Introdução

A rotina que simplifica a migração dos dados das escolas para o sistema Educacenso está cheia de novidades!

Foram implementadas novas telas de visões que facilitam a manipulação e interpretação dos dados a serem encaminhados, processos que realizam atualizações cadastrais em lote, atalhos (menu centralizado) para acesso às informações, preview do arquivo a ser enviado...

Confira a documentação e veja mais!

Para mais informações [clique aqui](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar) e acesse a página do INEP.

| Etapa | Período de coleta de dados | Layout | Versão do layout | Liberação do layout pelo INEP |
| --- | --- | --- | --- | --- |
| 1ª Etapa (Matrícula Inicial) | 28/05/2025 a 06/08/2025 |  | 3 | 14/07/2025 |

**Data de referência do Censo:** 28/05/2025

# Requisitos mínimos

* 12.1.2502.315
* 12.1.2506.329
* 12.1.2510.259
* 12.1.2602.174
* Base atualizada com todos os scripts executados.

# Fluxo para o Censo do Ensino Básico

trueCenso do Ensino Básicofalseautotoptrue13419

# Instituição do MEC

Novidades do Censo 2026

* Campo 35 (Parcerias/Convênios) – Excluído: A opção *"Não possui parceria ou convênio"* foi fisicamente removida da tela de Instituição do MEC por ser considerada redundante.
* Campo 50 (Esfera Administrativa do Conselho) – Novo combobox**:** Substitui as três antigas caixas de seleção (*checkboxes*) por um campo único de seleção.  
  + Opções permitidas: `1 Federal`, `2 Estadual`, `3 Municipal`, `4 Estadual e Municipal`, `5 Federal e Estadual`.
* Infraestrutura e Dados da Escola
  + Campo 116 (Acesso à Internet pelos Alunos) – Novo comobox: Unifica os campos antigos de seleção. Permite escolher se o acesso ocorre por equipamentos da escola, dispositivos pessoais ou ambos.
  + Campo 118 (Rede Local de Computadores) – Novo comobox: Consolida o tipo de rede interna. 
    - Opções permitidas: `0 Não há rede local`, `1 A cabo`, `2 Wireless`, `3 A cabo e Wireless`.
  + Campo 158 (Escola Indígena) – excluído**:** O campo que marcava a escola como indígena foi removido, assim os campos deLíngua de Ensino (Campo 160) agora permanecem sempre habilitados para preenchimento direto na secretaria, independentemente de qualquer marcação prévia.
* Inclusão de novos campos: 
  + Laboratório de robótica, campo 56.
  + Assistente social, campo 120.
  + Equipamentos audiovisuais para produção estudantil, campo 144.
  + Kits de robótica, campo 148.
  + Materiais para a educação emocional e mediação de conflitos, campo 150.
* Alteração de Nomenclatura: O antigo Campo 133 foi renomeado para "Orientador(a) comunitário(a)".
Novidades do Censo 2025

* Inclusão da opção "Quantidade de salas de aula com Cantinho da Leitura para a Educação Infantil e o Ensino fundamental (Anos iniciais)" no campo "Salas", da aba Dependências.  
  O valor da quantidade de salas de aula com Cantinho da Leitura para a Educação Infantil e o Ensino fundamental (Anos iniciais), não pode ser maior que a soma Quantidade de salas de aula utilizadas pela escola dentro do prédio escolar e Quantidade de salas de aula utilizadas pela escola fora do prédio escolar.

Na tela de Instituição do MEC se encontram todas as informações da instituição que deverão ser enviadas ao Censo.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Instituição do MEC

Aviso

**A partir da versão 12.1.2506**, o cadastro da Instituição do MEC deixa de ser por filial ou por nível de ensino e passa a ser um cadastro global, permitindo que sejam associados os contextos educacionais à respectiva Instituição do MEC.

Alguns ajustes serão necessários no(s) cadastro(s) de Instituição do MEC já existente(s).

Para mais detalhes, verifique a documentação em <https://tdn.totvs.com/x/IBKHNw>.

**Para versões anteriores a 12.1.2506**, deve-se definir se a instituição do MEC é por filial ou nível de ensino acessando os parâmetros do sistema. **Acesse**:  Configurações | Parâmetros | Secretaria| Geral 7/7

Na Instituição do MEC deverá ser configurada a data de referência e períodos letivos participantes do Censo. Caso seja necessário, as consultas SQL do Censo poderão ser customizadas aqui.

**Observações:**

Serão listados os períodos letivos ativos de acordo com:

* Coligada corrente;
* Filial corrente e níveis de ensino do Censo Básico (caso a instituição seja por filial) ou nível de ensino corrente (caso a instituição seja por nível de ensino);
* Data de referência informada, portanto, o período letivo deve possuir data de início e data de término ou previsão de término.

Só serão enviados para o Censo os períodos letivos e disciplinas que estejam sendo cursadas na data de referência do Censo. Isso será verificado através da situação de matrícula:

|  | Nível de ensino básico | Nível de ensino superior |
| --- | --- | --- |
| **No período letivo** | Aluno ativo | Aluno ativo  Indica trancamento |
| **Na disciplina** | Conta como aluno matriculado na turma e turma/disciplina | É uma disciplina em curso |

Sempre que a data de referência ou os períodos letivos forem alterados, o sistema precisará reprocessar os registros que serão enviados para o Censo. Isso poderá levar alguns minutos.

# Gestores da instituição

Na tela de Instituição do MEC se encontram todas as informações do gestor que deverão ser enviadas ao Censo.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Instituição do MEC | Anexos | Gestores da instituição

# Relação de Cadastros do Censo

Na tela de relação de cadastros do Censo devem ser cadastradas as relações dos cadastros do sistema com as tabelas auxiliares do Censo.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Relação de Cadastros do Censo

* ### **Deficiências**

Relação de cadastro entre as sub deficiências do sistema e as deficiências do Censo.

**Observação:** Em nível de ensino onde esteja habilitado "**Usa Educacenso**" as deficiências do Censo disponíveis serão as do Censo do Ensino Básico.

* ### **Professores**

Visualização de professores com problema no cadastro a serem corrigidos.

**Observação:** Na aba de professores não há uma relação de cadastro a ser feita. Aqui aparecerão os professores que possuem uma não conformidade entre o grau de instrução e a formação superior. Através dessa tela será possível acessar o cadastro de professores e fazer a correção.

* ### **País de Origem**

Relação de cadastro entre as nacionalidades do sistema e os países de origem do Censo.

**Observação:** Será possível localizar as nacionalidades do sistema que estão sendo utilizados no Censo (de acordo com os parâmetros do Censo) através do campo "Usado no Censo".

Este é um campo informativo e para que o parâmetro "Usado no Censo" apareça marcado é necessário que a nacionalidade esteja vinculada a algum aluno, professor ou gestor que irá participar do Censo.

* ### **Disciplinas**

Relação de cadastro entre as disciplinas do sistema e as disciplinas do Censo.

São exibidas todas as disciplinas da coligada e nível de ensino básico do contexto atual.

**Observação:** Será possível localizar as disciplinas do sistema que estão sendo utilizadas no Censo (de acordo com os parâmetros do Censo) através do campo "Usado no Censo".

Este é um campo informativo e para que o parâmetro "Usado no Censo" apareça marcado é necessário que a disciplina esteja sendo utilizada por alguma turma que irá participar do Censo.

# Itinerário Formativo

No cadastro da [Área do Conhecimento](https://tdn.totvs.com/pages/viewpage.action?pageId=547239582) deverá ser feita a associação com o tipo do itinerário formativo do Censo.

No cadastro do [Itinerário Formativo](https://tdn.totvs.com/pages/releaseview.action?pageId=547240322) existe a opção de colocar se ele é integrado ou não. Isso irá dizer se os tipos de itinerários correspondentes às áreas do conhecimento das disciplinas desse itinerário são trabalhados de forma integrada.

**Observação:** Para buscar os tipos de itinerários do Censo das turmas do aluno serão verificadas todas as áreas de conhecimento de todas as disciplinas de itinerário formativo que o aluno está cursando

# Turmas - Dados do Censo Escolar

Novidades do Censo 2026

* Tipo de Turma: todas as opções de tipo de turma foram agrupadas nesse único campo.
* Código do eixo do curso de qualificação profissional**:** campo novo incluído.
* Formas de organização da turma: todas as opções de forma de organização da turma foram agrupadas nesse único campo.

As informações de dados do Censo da turma podem ser acessadas de forma direta através do menu do Censo.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Turmas - Dados do Censo Escolar

**Observação:** Somente serão exibidas as turmas cujo o curso esteja com o parâmetro "Enviar ao Censo" marcado.

**Observação:**Só serão listadas as turmas dos períodos letivos selecionados na tela de parâmetro do censo.

Ao marcar a opção “Itinerário de formação técnica e profissional”, será disponibilizado na aba Registro 20 o campo 27 - Carga Horária Total do Curso, responsável por apresentar a carga horária total do itinerário formativo.

Para instituições que utilizam o EducaCenso com essa opção marcada, o campo 27 - Carga Horária Total do Curso exibirá a carga horária total da matriz curricular.

Disponível através das versões: 12.1.2502.310; 12.1.2506.317; 12.1.2510.242; 12.1.2602.156.

* ### **Alteração em lote de Turmas - Dados do Censo Escolar**

A alteração dos dados do Censo também poderá ser feita em lote. Para isso basta selecionar as turmas desejadas e acessar o processo de alteração em lote.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Turmas - Dados do Censo Escolar | Processos | Alteração em lote de Turmas - Dados do Censo Escolar

# Professores - Dados do Censo Escolar

Novidades do Censo 2025

* Inclusão dos campos Cor/Raça e Povos Indígenas no cadastro de Professor.

As informações de dados do Censo dos professores podem ser acessadas de forma direta através do menu do Censo.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Professores - Dados do Censo Escolar

Apenas os campos de dados do Censo do professor poderão ser alterados na tela de edição.

**Observação:**Só serão listadas os professores vinculados à alguma turma e que tenham data de início menor ou igual a data de referência parametrizada na tela de parâmetro do censo e que a data de término do professor, caso preenchida, seja maior que a data de referência parametrizada.

* ### **Alteração em lote de Professores - Dados do Censo Escolar**

A alteração dos dados do Censo também poderá ser feita em lote . Para isso basta selecionar os professores desejados e acessar o processo de alteração em lote. 

# Turmas do Professor - Dados do Censo Escolar

Novidades do Censo 2025 para o cadastro de Turmas do Professor - Dados do Censo Escolar

* Foi removido o campo "Unidade curricular para a disciplina de Itinerário Formativo".
* Foi incluído o campo "Área(s) do itinerário formativo" composto com as seguintes opções de múltipla seleção: "Linguagens e suas tecnologias". "Matemática e suas tecnologias", "Ciências da natureza e suas tecnologias", "Ciências humanas e sociais aplicadas". Esse campo fica habilitado e deve ser preenchido quando o campo "Função do professor" for preenchido como Docente ou Docente titular, e o registro da turma tiver o campo "Organização curricular da turma" marcado como "Itinerário formativo de aprofundamento".
* Foi incluído o campo Profissional escolar leciona no Itinerário de formação técnica e profissional (IFTP) que fica habilitado quando o campo quando o campo "Função do professor" for preenchido com uma das opções: Docente, Docente titular ou Instrutor da Educação Profissional,

As informações de dados do Censo dos professores podem ser acessadas de forma direta através do menu do Censo.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Turmas do Professor - Dados do Censo Escolar

**Observação:** O professor terá um registro para cada turma vinculada, considerando a turma da matrícula no período letivo dos alunos e as turmas dos itinerários.

* ### **Alteração em lote de Turmas do Professor - Dados do Censo Escolar**

A alteração dos dados do Censo também poderá ser feita em lote. Para isso basta selecionar as turmas desejadas e acessar o processo de alteração em lote.

# Alunos - Dados do Censo Escolar

As informações de dados do Censo dos alunos podem ser acessadas de forma direta através do menu do Censo.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Alunos - Dados do Censo Escolar.

Novidades do Censo 2025

* Inclusão dos campos Cor/Raça e Povos Indígenas no cadastro de Aluno.
* Inclusão do campo Tempo adicional na Aba Recursos Necessários.
* Inclusão do campo Pessoa Física com Transtorno de aprendizagem, com as opções: Discalculia ou outro transtorno da matemática e raciocínio lógico; Disgrafia, Disortografia ou outro transtorno da escrita e ortografia; Dislalia ou outro transtorno da linguagem e comunicação; Dislexia; Transtorno do Déficit de Atenção com Hiperatividade (TDAH);Transtorno do Processamento Auditivo Central (TPAC).
Novidades do Censo 2026 - Registro 60

* Foi adicionado ao **Registro 60** o **Campo 9**, denominado *"Carga horária integralizada pelo(a) aluno(a) no curso técnico ou de qualificação profissional"*.

  Este campo não é exibido nas telas de cadastro para preenchimento manual; seu valor é **calculado automaticamente** pelo sistema durante a geração do arquivo de exportação de matrícula inicial.

  ### Pré-requisitos para o Cálculo

  Para que a carga horária seja contabilizada no Campo 9, é necessário que as seguintes condições sejam atendidas simultaneamente:

  + O aluno deve estar **matriculado** na turma.
  + O aluno deve possuir o status de **aprovado**.
  + A turma deve possuir o anexo **"Dados do Censo Escolar e SISTEC"** cadastrado.
  + Dentro deste anexo, o campo **"Itinerário de formação técnica e profissional"** deve estar marcado.
  + A Instituição do MEC deve estar parametrizada para enviar a Carga Horária

  ### Regras de Cálculo

  A forma como o sistema totaliza a carga horária depende do contexto educacional do aluno. O cálculo é realizado de duas maneiras:

  + **No Ensino Básico:** O sistema realiza o somatório da carga horária de todas as disciplinas do itinerário formativo que estão presentes na turma.
  + **No Ensino Superior (em integrações com o EducaCenso):** O sistema contabiliza a carga horária integralizada apenas pelas disciplinas da turma nas quais o aluno obteve aprovação.

Apenas os campos de dados do Censo do aluno poderão ser alterados na tela de edição.

**Observação:**Só serão listadas os alunos que tenham matrícula em período letivo com data de matrícula menor ou igual a data de referência parametrizada na tela de parâmetro do censo e que a data de matrícula de encerramento da matrícula do período letivo deste aluno, caso preenchida, seja maior que a data de referência parametrizada.

* ### **Alteração em lote de Alunos - Dados do Censo Escolar**

A alteração dos dados do Censo também poderá ser feita em lote. Para isso basta selecionar os alunos desejados e acessar o processo de alteração em lote.

# Matricula - Dados do Censo Escolar

As informações de dados do Censo das matriculas dos alunos podem ser acessadas de forma direta através do menu do Censo.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Matricula - Dados do Censo Escolar.

**Observação:** O aluno terá um registro para cada turma que possuir, considerando a turma da matrícula no período letivo e as turmas dos itinerários.

* ### **Alteração em lote de matricula - Dados do Censo Escolar**

A alteração dos dados do Censo também poderá ser feita em lote. Para isso basta selecionar os alunos desejados e acessar o processo de alteração em lote.

# Primeira etapa do Censo Escolar

* ## Exportação da Matrícula Inicial - Censo Básico

Na tela de exportação da matrícula inicial aparecerá o parâmetro de data de referência já configurado e o ano base (baseado na data de referência). Ao clicar em "Gerar arquivo" será feito o processamento das informações cadastradas para o Censo e depois serão rodadas as consultas para a geração do arquivo. O arquivo gerado poderá ser consultado e alterado para posteriormente ser gerado o arquivo txt para enviar ao INEP.

A geração do arquivo txt deve ser feita através do botão "Gerar TXT". É necessário antes marcar qual é o arquivo xml oficial através do botão "XML Oficial", pois esse será o arquivo xml utilizado para a geração do txt.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Exportação da Matrícula Inicial - Censo Básico

**Observação:** As turmas de Itinerário não serão exportadas caso suas disciplinas não tenham Área do Conhecimento vinculada.

Informações

O que fazer quando algumas sentenças não retornam resultado e o arquivo base não é gerado:

* **Instituição**

- Verificar se existe uma instituição cadastrada em: Atividades acadêmicas > Acadêmico > Censo > Instituição do MEC

* **Turmas**

- Verificar se a data de referência do Censo está correta e se os períodos letivos estão selecionados em: Atividades acadêmicas > Acadêmico > Censo > Instituição do MEC

- Verificar se os cursos estão com a opção “Enviar ao Censo” marcada em: Currículo e Oferta > Estrutura curricular > Cursos

- Verificar se os dados do Censo da turma estão informados em: Atividades acadêmicas > Acadêmico > Censo > Turmas – Dados do Censo Escolar

* **Gestores**

- Verificar se existe gestor cadastrado em: Atividades acadêmicas > Acadêmico > Censo > Instituição do MEC > Anexos > Gestores da instituição

* **Professores**

- Verificar se os professores estão com a data de início menor ou igual a data de referência e não possuem data de término menor ou igual a data de referência.

- Verificar se os dados do Censo dos professores estão informados em: Atividades acadêmicas > Acadêmico > Censo > Professores – Dados do Censo Escolar

* **Alunos**

- Verificar se os alunos estão com a data de matrícula menor ou igual a data de referência e não possuem data de encerramento da matrícula menor ou igual a data de referência.

- Verificar se os dados do Censo dos alunos estão informados em: Atividades acadêmicas > Acadêmico > Censo > Alunos – Dados do Censo Escolar

- Verificar se a opção "Desconsiderar no Censo" está selecionada para a matrícula no período letivo dos alunos em: Atividades acadêmicas > Acadêmico > Censo > Matrículas – Dados do Censo Escolar

# Segunda etapa do Censo Escolar

* ## Importação de Dados - Censo Básico

Na tela de importação de dados aparecerá o ano base (baseado na data de referência). Deverá ser selecionado o arquivo txt que foi exportado do INEP e ao clicar em "Gerar arquivo" ele será gerado um arquivo xml. O arquivo gerado poderá ser consultado e posteriormente ser gerado o arquivo txt da situação do aluno para enviar ao INEP.

É necessário marcar qual é o arquivo xml oficial através do botão "XML Oficial", pois esse será o arquivo xml utilizado para a geração do txt da situação do aluno.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Importação de Dados - Censo Básico

* ## Exportação da Situação do Aluno - Censo Básico

Na tela de exportação da situação do aluno aparecerá o parâmetro de data de referência já configurado e o ano base (baseado na data de referência). Ao clicar em "Gerar arquivo" será feita a leitura do arquivo xml oficial importado e a geração do arquivo xml da situação do aluno. O arquivo gerado poderá ser consultado e alterado para posteriormente ser gerado o arquivo txt para enviar ao INEP.

A geração do arquivo txt deve ser feita através do botão "Gerar TXT". É necessário antes marcar qual é o arquivo xml oficial através do botão "XML Oficial", pois esse será o arquivo xml utilizado para a geração do txt.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Exportação da Situação do Aluno - Censo Básico

Foi realizada uma alteração nas rotinas de importação de dados, exportação da matricula inicial e exportação da  situação do aluno, com relação ao código da turmas que são enviadas para o Censo. Agora esse código é  gerado como uma chave aleatória, este campo fica armazenado no codturmamec da tabela sturmamec.

**Observação:**Não serão exportadas turmas exclusivas de itinerário formativo (itinerário formativo sem formação geral básica).

O parâmetro "**Aprovado (exclusivo para o Censo)**" no cadastro de situações de matricula em níveis de ensino onde esteja habilitado "**Usa Educacenso**" necessita estar marcado para situações de disciplina que representem aprovação do aluno. Esse passo é necessário para que alunos aprovados tenham sua situação de matrícula corretamente exportada.

**Atenção!** Ao realizar a mudança de turma de um aluno, o sistema vai considerar para a exibição da turma atual, a data de referência informada na instituição do Mec. Caso a data informada seja anterior à data da mudança, o sistema exibe a turma antiga. Se a data de referência for a data atual da mudança ou posterior o sistema exibe a turma atual.

 O Sistema verifica se o status da situação de matricula no período letivo está ativo.

E se o status da matricula em disciplina "Conta como aluno matriculado na turma e turma/disciplina", está marcado.

Apartir das versões: 12.1.2502.266; 12.1.2506.228; 12.1.2510.157. Os campos cargo do gestor escolar e e-mail do gestor foram removidos do registro 89.

O código da modalidade foi retirado do campo 9, e a situação do aluno passou a ser informada no campo 10 do registro 91.

**Observação**: As turmas que possuem o tipo “Curricular (etapa de ensino)” e não possuem organização curricular exclusiva de itinerário serão exibidas no arquivo de exportação da situação do aluno.

* ## Exportação da Identificação do Aluno - Censo Básico

Na tela de exportação da identificação do aluno aparecerá o parâmetro de data de referência já configurado e o ano base (baseado na data de referência). Ao clicar em "Gerar arquivo" será feita a leitura do arquivo xml oficial importado e a geração do arquivo xml da situação do aluno. O arquivo gerado poderá ser consultado e alterado para posteriormente ser gerado o arquivo txt para enviar ao INEP.

A geração do arquivo txt deve ser feita através do botão "Gerar TXT". É necessário antes marcar qual é o arquivo xml oficial através do botão "XML Oficial", pois esse será o arquivo xml utilizado para a geração do txt.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Exportação da Identificação do Aluno - Censo Básico

* ## Importação da Identificação do Aluno - Censo Básico

Na tela de importação de dados aparecerá o ano base (baseado na data de referência). Deverá ser selecionado o arquivo txt que foi exportado do INEP e ao clicar em "Gerar arquivo" ele será gerado um arquivo xml. O arquivo gerado poderá ser consultado atraves do botão Ler arquivo.

É necessário marcar qual é o arquivo xml oficial através do botão "XML Oficial", pois esse será o arquivo xml utilizado para a geração do txt da identificação  do aluno.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Importação da Identificação do  aluno - Censo Básico

# Documentação

Esta documentação do Censo poderá ser acessada rapidamente a qualquer momento através do próprio menu do Censo no sistema.

**Acesse**: Atividades acadêmicas | Acadêmico | Censo | Documentação - Censo da Educação Básica
