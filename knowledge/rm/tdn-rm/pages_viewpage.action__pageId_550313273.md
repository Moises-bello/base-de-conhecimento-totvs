---
content_hash: a3dc43d3eb5eccc222bf2cabbdd07f4988aa5ee0221c18ae7b8a10776cd5f370
fetched_at: '2026-06-29T00:10:43.242215+00:00'
page_id: '550313273'
product: rm
source: tdn-rm
title: Censo Escolar Ensino Básico – Apoio para a realização do processo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550313273
version: 15
---

---

---

|  |  |
| --- | --- |
| Descrição | Censo Escolar Ensino Básico |
| Objetivo | Auxiliar na coleta de  informações sobre os alunos, os professores e a infraestrutura da escola e enviar para o INEP. |

O Censo Escolar é um levantamento de dados estatístico-educacionais de âmbito nacional realizado todos os anos e coordenado pelo Inep. Ele é feito com a colaboração das secretarias estaduais e municipais de Educação e com a participação de todas as escolas públicas e privadas do país.

Trata-se do principal instrumento de coleta de informações da Educação Básica, que abrange as suas diferentes etapas e modalidades: Ensino Superior, Ensino Regular (Educação Infantil e Ensinos Fundamental e Médio), Educação Especial e Educação de Jovens e Adultos (EJA).

Nele são coletadas informações sobre os alunos, os professores e a infraestrutura da escola. O preenchimento é de responsabilidade de cada escola, supervisionado pela respectiva secretaria de educação.

Para mais informações [clique aqui](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar) e acesse a página do INEP.

# Desenvolvimento/Procedimento

Requisitos mínimos:

**Para que os dados do Educacenso possam ser extraídos é necessária uma complementação dos cadastros do sistema e a utilização das versões mínimas na Primeira Etapa: 12.1.2205.276, 12.1.2209.232, 12.1.2302.155, 12.1.2306.100, base atualizada com todos os scripts rodados. Na Segunda Etapa precisa as versões mínimas : 12.1.2302.249, 12.1.2306.201, 12.1.2310.133, base atualizada com todos os scripts rodados.**

**O processo necessita que todos os scripts do censo já tenham sido executados. É de extrema importância que verifique se os scripts dos censos anteriores e do atual já foram executados, pois caso não tenham sido, o processo não permitirá realizar o censo. Scripts utilizados no censo atual serão disponibilizados no FTP:**

* **FTP:  <ftp://ftp.rm.com.br/Clientes/CensoEducacional>**

  **Usuário e senha para acessar o FTP:**

  **Usuário: clienteonline**
* **Senha: ftponline02**

O TOTVS Educacional disponibiliza funções que permitem a criação dos arquivos com dados da Escola, Turmas, Docentes, Alunos, Gestores e Pessoas.

Estas funções se dividem em:

* Assistente de preparação do arquivo;
* Preparação dos cadastrados nas visões: Escola, Turmas, Docentes, Alunos, Gestores e Pessoas;
* Relatórios de exportação de dados.

 O usuário deverá estar autenticado no Contexto Ensino Básico, e parametrizar os dados para a geração do arquivo Censo. Para que os dados do Censo possam ser extraídos é necessária uma complementação dos cadastros do sistema.

# Cadastros- Parâmetros do Censo

**Cadastro da Instituição**

**Acesse: Atividades acadêmicas | Acadêmico | Censo | Parâmetros do Censo**

O cadastro dos dados da instituição agora pode ser realizado de duas formas:

* Filial
* Nível de Ensino

# Cadastros- Instituição do MEC

**Cadastro da Instituição pela Filial**

**Acesse: Módulo Gestão Fiscal | Cadastros | Filiais | Anexo > Dados Educacionais | Anexo > Instituição do MEC**

Estes dados agora podem ser informados no anexo Instituição do MEC no cadastro da Filial em gestão de fiscal.

A tela exibe os dados solicitados no questionário “Dados da Escola”. Preencha as abas de acordo com as instruções solicitadas pelo MEC.

**Cadastro da Instituição pelo Nível de Ensino**

**Acesse:** Configurações | Níveis de ensino | Anexo > Instituição do MEC

Estes dados agora podem ser informados no anexo Instituição do MEC no cadastro de Nível de Ensino.

A tela exibe os dados solicitados no questionário “Dados da Escola”. Preencha as abas de acordo com as instruções solicitadas pelo MEC.

**Cadastro da Instituição pelo Menu Censo**

Na tela de Instituição do MEC se encontram todas as informações da instituição que deverão ser enviadas ao Censo.

**Acesse: Módulo Educacional | Atividades Acadêmicas | Censo | Instituição do MEC**

**Observação:** Serão listados os períodos letivos ativos de acordo com:

* Coligada corrente;
* Filial corrente e níveis de ensino do Censo Básico (caso a instituição seja por filial) ou nível de ensino corrente (caso a instituição seja por nível de ensino);
* Data de referência informada, portanto, o período letivo deve possuir data de início e data de término ou previsão de término.
Censo 2023

* A aba convênio foi reformulada. O campo "Poder público responsável pela parceria ou convênio..." foi transferido para essa aba e agora existem opções separadas de formas de contratação da parceria ou convênio para quando é com a secretaria estadual ou com a secretaria municipal.
* Inclusão da opção "Estúdio de gravação e edição" no campo "Dependências físicas existentes e utilizadas na escola" da aba "Dependências".
* Inclusão da opção "Tradutor e Intérprete de Libras para atendimento em outros ambientes da escola que não seja sala de aula" no campo "Total de profissionais que atuam nas seguintes funções na escola" da aba "Profissionais".
* Inclusão da opção "Materiais pedagógicos para a educação bilíngue de surdos" no campo "Instrumentos e materiais socioculturais e/ou pedagógicos em uso na escola para o desenvolvimento de atividades de ensino-aprendizagem" da aba "Organização do Ensino".
Censo - 2024

* Inclusão da opção "Carro-pipa", no campo, "Abastecimento de água" da aba "Infraesturtura".
* Inclusão da opção "Área de horta, plantio e/ou produção agrícola", no campo "Dependências físicas existentes e utilizadas na escola" da aba "Dependências".
* Inclusão da opção "Sinalização/Alarme luminoso", no campo "Recursos de acessibilidade para pessoas com deficiência ou mobilidade reduzida nas vias de circulação internas na escola" da aba "Dependências".
* Inclusão da opção "Agrônomos(as), horticultores(as), técnicos ou monitores(as) responsáveis pela gestão da área de horta, plantio e/ou produção agrícola", no campo "Total de profissionais que atuam nas seguintes funções na escola" da aba "Profissionais".
* Inclusão da opção "Revisor de texto Braille, assistente vidente (assistente de revisão do texto em Braille)", no campo "Total de profissionais que atuam nas seguintes funções na escola" da aba "Profissionais".
* Inclusão da opção "Equipamentos e instrumentos para atividades em área de horta, plantio e/ou produção agrícola" no campo "Instrumentos e materiais socioculturais e/ou pedagógicos em uso na escola para o desenvolvimento de atividades de ensino-aprendizagem" da aba "Organização do Ensino".
* Inclusão da opção "Materiais pedagógicos para a educação escolar quilombola" no campo "Instrumentos e materiais socioculturais e/ou pedagógicos em uso na escola para o desenvolvimento de atividades de ensino-aprendizagem" da aba "Organização do Ensino".
* Inclusão da opção "Materiais pedagógicos para a educação especial" no campo "Instrumentos e materiais socioculturais e/ou pedagógicos em uso na escola para o desenvolvimento de atividades de ensino-aprendizagem" da aba "Organização do Ensino".
* Inclusão da opção "A escola desenvolve ações na área de educação ambiental?", na aba "Organização do Ensino". Ao marcar a opção, pelo menos um dos campos abaixo precisa ser informado:
  + Como conteúdo dos componentes/campos de experiências presentes no currículo;
  + Como um componente curricular especial, específico, flexível ou eletivo;
  + Como um eixo estruturante do currículo;
  + Em eventos;
  + Em projetos transversais ou interdisciplinares;
  + Nenhuma das opções listadas.

 

**Cadastro de gestores pela Instituição do MEC**

**Acesse:** **Módulo Educacional | Atividades Acadêmicas | Censo | Instituição do MEC****| Anexo > Gestor da instituição**

ou

**Acesse:** **Módulo Gestão Fiscal | Cadastros | Filial | Anexo > Dados Educacionais | Anexo > Instituição do MEC| Anexo > Gestor da instituição**

Estes dados agora podem ser informados no anexo Instituição do MEC no cadastro de Nível de Ensino ou Filial.

A tela exibe os dados solicitados no questionário “Gestores”. Preencha as abas de acordo com as instruções solicitadas pelo MEC.

Censo 2023

Foram incluídas as opções "Educação bilíngue de surdos" e "Tecnologia de Informação e Comunicação" no campo "Cursos específicos" da aba "Outros".

# Relação de Cadastros do Censo

Na tela de relação de cadastros do Censo devem ser cadastradas as relações dos cadastros do sistema com as tabelas auxiliares do Censo.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Relação de Cadastros do Censo

* ### **Deficiências**

Relação de cadastro entre as sub deficiências do sistema e as deficiências do Censo.

* ### **Professores**

Visualização de professores com problema no cadastro a serem corrigidos.

* ### **País de Origem**

Relação de cadastro entre as nacionalidades do sistema e os países de origem do Censo.

* ### **Disciplinas**

Relação de cadastro entre as disciplinas do sistema e as disciplinas do Censo.

São exibidas todas as disciplinas da coligada e nível de ensino básico do contexto atual.

# Itinerário Formativo

No cadastro da [Área do Conhecimento](https://tdn.totvs.com/pages/viewpage.action?pageId=547239582)deverá ser feita a associação com o tipo do itinerário formativo do Censo.

**No cadastro do [Itinerário Formativo](https://tdn.totvs.com/pages/releaseview.action?pageId=547240322) existe a opção de colocar se ele é integrado ou não. Isso irá dizer se os tipos de itinerários correspondentes às áreas do conhecimento das disciplinas desse itinerário são trabalhados de forma integrada.**

**Observação:** Para buscar os tipos de itinerários do Censo das turmas do aluno serão verificadas todas as áreas de conhecimento de todas as disciplinas de itinerário formativo que o aluno está cursando

# Turmas - Dados do Censo Escolar

As informações de dados do Censo da turma podem ser acessadas de forma direta através do menu do Censo.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Turmas - Dados do Censo Escolar

**Observação:** Somente serão exibidas as turmas cujo o curso esteja com o parâmetro "Enviar ao Censo" marcado.

**Observação:** Só serão listadas as turmas dos períodos letivos selecionados na tela de parâmetro do censo.

* ### **Alteração em lote de Turmas - Dados do Censo Escolar**

A alteração dos dados do Censo também poderá ser feita em lote. Para isso basta selecionar as turmas desejadas e acessar o processo de alteração em lote.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Turmas - Dados do Censo Escolar | Processos | Alteração em lote de Turmas - Dados do Censo Escolar

# Professores - Dados do Censo Escolar

As informações de dados do Censo dos professores podem ser acessadas de forma direta através do menu do Censo.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Professores - Dados do Censo Escolar

Apenas os campos de dados do Censo do professor poderão ser alterados na tela de edição.

**Observação:** Só serão listadas os professores vinculados à alguma turma e que tenham data de início menor ou igual a data de referência parametrizada na tela de parâmetro do censo e que a data de término do professor, caso preenchida, seja maior que a data de referência parametrizada.

* ### **Alteração em lote de Professores - Dados do Censo Escolar**

**A alteração dos dados do Censo também poderá ser feita em lote . Para isso basta selecionar os professores desejados e acessar o processo de alteração em lote.**

# Turmas do Professor - Dados do Censo Escolar

As informações de dados do Censo dos professores podem ser acessadas de forma direta através do menu do Censo.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Turmas do Professor - Dados do Censo Escolar

**Observação:** O professor terá um registro para cada turma vinculada, considerando a turma da matrícula no período letivo dos alunos e as turmas dos itinerários.

* ### **Alteração em lote de Turmas do Professor - Dados do Censo Escolar**

**A alteração dos dados do Censo também poderá ser feita em lote. Para isso basta selecionar as turmas desejadas e acessar o processo de alteração em lote.**

**Alunos-Dados do Censo Escolar**

**As informações de dados do Censo dos alunos podem ser acessadas de forma direta através do menu do Censo.**

**Acesse:** Currículo e Oferta | Aluno | Anexo | Dados do Censo Escolar e SISTEC

Apenas os campos de dados do Censo do aluno poderão ser alterados na tela de edição.

**Observação:** Só serão listadas os alunos que tenham matrícula em período letivo com data de matrícula menor ou igual a data de referência parametrizada na tela de parâmetro do censo e que a data de matrícula de encerramento da matrícula do período letivo deste aluno, caso preenchida, seja maior que a data de referência parametrizada.

* ### **Alteração em lote de Alunos - Dados do Censo Escolar**

A alteração dos dados do Censo também poderá ser feita em lote. Para isso basta selecionar os alunos desejados e acessar o processo de alteração em lote.

# Matricula - Dados do Censo Escolar

As informações de dados do Censo das matriculas dos alunos podem ser acessadas de forma direta através do menu do Censo.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Matricula - Dados do Censo Escolar.

**Observação:** O aluno terá um registro para cada turma que possuir, considerando a turma da matrícula no período letivo e as turmas dos itinerários.

* ### **Alteração em lote de matricula - Dados do Censo Escolar**

A alteração dos dados do Censo também poderá ser feita em lote. Para isso basta selecionar os alunos desejados e acessar o processo de alteração em lote.

# Exportação da Matrícula Inicial - Censo Básico

Na tela de exportação da matrícula inicial aparecerá o parâmetro de data de referência já configurado e o ano base (baseado na data de referência). Ao clicar em "Gerar arquivo" será feito o processamento das informações cadastradas para o Censo e depois serão rodadas as consultas para a geração do arquivo. O arquivo gerado poderá ser consultado e alterado para posteriormente ser gerado o arquivo txt para enviar ao INEP.

A geração do arquivo txt deve ser feita através do botão "Gerar TXT". É necessário antes marcar qual é o arquivo xml oficial através do botão "XML Oficial", pois esse será o arquivo xml utilizado para a geração do txt.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Exportação da Matrícula Inicial - Censo Básico

**Observação:** As turmas de Itinerário não serão exportadas caso suas disciplinas não tenham Área do Conhecimento vinculada.

# Importação de Dados - Censo Básico

Na tela de importação de dados aparecerá o ano base (baseado na data de referência). Deverá ser selecionado o arquivo txt que foi exportado do INEP e ao clicar em "Gerar arquivo" ele será gerado um arquivo xml. O arquivo gerado poderá ser consultado e posteriormente ser gerado o arquivo txt da situação do aluno para enviar ao INEP.

É necessário marcar qual é o arquivo xml oficial através do botão "XML Oficial", pois esse será o arquivo xml utilizado para a geração do txt da situação do aluno.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Importação de Dados - Censo Básico

# Exportação da Situação do Aluno - Censo Básico

Na tela de exportação da situação do aluno aparecerá o parâmetro de data de referência já configurado e o ano base (baseado na data de referência). Ao clicar em "Gerar arquivo" será feita a leitura do arquivo xml oficial importado e a geração do arquivo xml da situação do aluno. O arquivo gerado poderá ser consultado e alterado para posteriormente ser gerado o arquivo txt para enviar ao INEP.

A geração do arquivo txt deve ser feita através do botão "Gerar TXT". É necessário antes marcar qual é o arquivo xml oficial através do botão "XML Oficial", pois esse será o arquivo xml utilizado para a geração do txt.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Exportação da Situação do Aluno - Censo Básico

Foi realizada uma alteração nas rotinas de importação de dados, exportação da matricula inicial e exportação da  situação do aluno, com relação ao código da turmas que são enviadas para o Censo. Agora esse código é  gerado como uma chave aleatória, este campo fica armazenado no codturmamec da tabela sturmamec.

**Observação:** Não serão exportadas turmas exclusivas de itinerário formativo (itinerário formativo sem formação geral básica).

Atenção! Ao realizar a mudança de turma de um aluno, o sistema vai considerar para a exibição da turma atual, a data de referência informada na instituição do Mec. Caso a data informada seja anterior à data da mudança, o sistema exibe a turma antiga. Se a data de referência for a data atual da mudança ou posterior o sistema exibe a turma atual.

# Documentação

Esta documentação do Censo poderá ser acessada rapidamente a qualquer momento através do próprio menu do Censo no sistema.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Documentação - Censo da Educação Básica

# **Arquivamento e Recuperação de dados do Educacenso**

**Acesse:** Atividades acadêmicas | Acadêmico | Censo | Arquivamento e Recuperação de dados do Educacenso

**Caso este processo não seja executado, não será possível obter resultado no gerador de saídas.**

A etapa de Arquivamento e Recuperação de dados do Educacenso salva todos os registros de acordo com o que foi executado pelo censo anteriormente.

Ano Base e Data de Corte

 Na tela acima, devemos indicar o ano base e a data de corte do censo para que a busca de arquivos seja realizada.

Ano Base: Ano o qual o censo está sendo rodado.

Data de Corte: Data de início do censo.

Para que o aluno seja buscado, a data de matrícula deve ser inferior à Data de Corte.

Após executarmos o processo de Arquivamento e Recuperação de dados, é de suma importância que realize a seleção do arquivo gerado e logo após, clique no botão de "Ler Arquivo", pois desta forma poderemos informar dados obrigatórios que não são informados no sistema e também visualizar os dados cadastrados que estão sendo buscados.

 

 

Os campos obrigatórios de preenchimentos na tela de arquivamento, são:

* Campos 8 e 9 do registro 00;

Neste momento deve-se atentar para oficializar o dado que será utilizado.

Conforme imagem abaixo, basta selecionar os dados que serão oficializados e clicar no botão "XML Oficial".

Os registros salvos neste processo serão utilizados apenas no momento de executar o Gerador de Saídas.

# **Geração do Arquivo Censo**

**Acesse:** Gestão | Ferramentas de Análise | Gerador de Saída

O layout do Gerador de Saída utilizado pelo censo se encontra disponibilizado no FTP <ftp://ftp.rm.com.br/Clientes/CensoEducacional>

**Deve-se atentar para as consultas utilizadas no gerador. Todas estão disponibilizadas no FTP informado e devem ser devidamente importadas e incluídas no seguinte caminho:** 

**Atividades acadêmicas | Acadêmico | Censo | Parâmetros do Censo | Consultas para geração do Censo Básico**

**Caso as consultas estejam em branco, serão utilizadas consultas internas do sistema.****Importando o Arquivo**

Para realizar a importação do arquivo do censo, deve-se acessar o processo "Importar Layout".

Em seguida, será necessário adicionar os layouts do censo e executar o processo.

Atente-se que ao adicionar o layout através do botão de Adicionar Objetos, o mesmo deve possuir uma categoria na aba de parâmetros da tela de importação de layout.

**Seleção de Arquivo**

Selecione o arquivo que será gerado e utilize o processo "Geração de saída".

**Seleção de Layout**

Nesta tela, será necessária a seleção de um layout para o gerador.

**Parâmetros da Geração**

Em seguida, devemos informar a coligada, instituição, data início e data fim que visamos gerar.

Motivos que fazem com que um aluno não saia no arquivo do Censo:

1. O aluno não está matriculado;
2. O curso não possui o código do INEP;
3. A data de corte do Censo é menor que a data de início ou maior que a data de fim do período letivo;
4. A data de matrícula é maior que a data de corte do Censo;
5. A data de encerramento da matrícula é menor ou igual a data de corte do Censo;
6. A opção "Desconsiderar no Censo" está selecionada.

**Informações Técnicas**

Todos os materiais se encontram no FTP <ftp://ftp.rm.com.br/Clientes/CensoEducacional>

Usuário e senha para acessar o FTP:

Usuário: clienteonline

Senha: ftponline02

Tabelas Utilizadas

* SALUNOMEC
* SMATRCPLMEC
* PROFESSORMEC
* TURMAMEC
* SFILIALMEC
