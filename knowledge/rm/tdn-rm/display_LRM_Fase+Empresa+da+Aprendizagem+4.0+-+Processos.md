---
content_hash: 52d658b529a49e2c7ce1ecced2836efb0e301de68676eb0c21645322df2c8dd1
fetched_at: '2026-06-29T00:11:29.334101+00:00'
page_id: '736175462'
product: rm
source: tdn-rm
title: Fase Empresa da Aprendizagem 4.0 - Processos
type: documentation
url: https://tdn.totvs.com/display/LRM/Fase+Empresa+da+Aprendizagem+4.0+-+Processos
version: 11
---

Conforme o novo formato de Gestão da Fase Empresa da Aprendizagem 4.0, não será mais necessário vincular o aluno ao período letivo exclusivo para registros da fase empresa (AAAA/FE) e, da mesma forma, a uma turma e disciplina exclusiva da fase empresa.  
Desta forma, a vivência profissional do aluno passa a ser realizada  por meio de uma Atividade ofertada, vinculada à empresa na qual o aluno possui um contrato.

Assim, através do componente curricular vinculado a esta atividade ofertada, é possível realizar a análise curricular do aluno mediante a conclusão do mesmo, além das informações associadas à Matriz Curricular e Curso/Habilitação.

# **1. FASE EMPRESA DA APRENDIZAGEM**

# **1.1. Cadastro de Componente Curricular e Modalidade**

O “Componente Curricular” e a “Modalidade” serão criados por scripts, de modo que sejam os mesmos "códigos" em todos os regionais para utilização na Solução Integradora.

* **O que são os Componentes Curriculares?**

O Componente Curricular é a nova nomenclatura para utilizarmos a Fase Empresa da Aprendizagem. 

* **O que é a modalidade?**

A modalidade é a Prática Profissional da Aprendizagem.

* **O cadastro dos Componentes Curriculares está disponível em:** Currículo e Oferta l Estrutura Curricular l Componentes Curriculares.  Abrirá a tela dos Componentes Curriculares:

Em “Anexos”, “Modalidades” está vinculado ao cadastro da “Prática Profissional”.  Podemos observar o “Código” e a “Descrição da Modalidade”.

# **1.2. Matriz Curricular**

No tipo de avaliação das Atividades Curriculares deverá ser selecionado a “Carga Horária”.

Aviso:

Necessário informar no campo complementar a Carga Horária - Presencial do plano do curso.

# **1.3. Matriz Aplicada**

No anexo Componente, vincular o componente “Fase Empresa da Aprendizagem” e as horas mínimas obrigatórias.

Caminho: Matriz Curricular l Anexos l Matriz aplicada l Anexos l Componentes.

Clique em “Incluir” ou “Editar” o “Componente da Matriz Curricular”.

Vincular o item do componente “Prática Profissional” e informar as horas mínimas e máximas. 

Caminho: Matriz Curricular l Anexos l Matriz aplicada l Anexos l Componentes l Anexos l Item Curricular.

Clique em “Incluir” ou “Editar” o “Item Curricular”.

Informe o “Valor Máximo” e “Valor Mínimo” correspondente às horas do “Item Curricular”.

Aviso:

Para o “Valor Mínimo” de Carga Horária da Prática Profissional, deverá ser verificado o **item 9**

# **2. CADASTRO DE COMPETÊNCIAS DA FASE EMPRESA (CUSTOMIZADO)**

O objetivo deste processo é detalhar a criação da interface customizada de **Cadastro de Competências da Fase Empresa** que estará disponível em TOTVS Educacional | Sistema Indústria | Cadastro de Competências.

A interface exibirá uma visão de dois campos, sendo eles: 

* **Código:** Será sequencial e de preenchimento automático.
* **Descrição:** Será do tipo texto.

Importante:

O SENAI irá padronizar 10 competências iniciais que serão utilizadas neste processo. No entanto, o Regional poderá incluir, alterar ou excluir qualquer competência do padrão, inclusive poderá incluir novos itens. Essas 10 competências iniciais serão criadas através de script customizado. 

Aviso:

Para que os usuário chave (DBA ou Secretária)  consiga visualizar o Cadastro de Competência da Fase Empresa da Aprendizagem e o Anexo no cadastro da Atividade Ofertada, será necessário que seja dado a permissão de acesso no perfil de cada usuário, para que fique visível no Sistema.

**Caminho:** Serviços Globais l  Segurança l Perfis l Sistema l Educacional l Usuário l Acesso a Menus l Sistema Indústria l Fase Empresa l Competências da  Fase Empresa.

# **3. CADASTRO DA EMPRESA**

Cadastrar as empresas que serão responsáveis pelos contratos da fase empresa. Clicar em “Editar” ou “Incluir”.

Preencha as informações relacionadas ao “Cadastro da Empresa”.

Dica:

O tipo de documento CEI (Cadastro Específico do INSS) composto por 12 (doze) dígitos numéricos, permite   que o usuário cadastre uma empresa com este tipo de documento. Versão mínima do RM 12.1.27.263

# **3.1. Cadastro do Funcionário da Empresa**

**Caminho:** Empresa l Anexo l Funcionários da Empresa

Selecione “Editar” ou “Incluir”.

# **3.2. Cadastro do Professor**

Cadastrar os professores (instrutores) que são responsáveis pelo acompanhamento da fase empresa. Clicar em “Editar” ou “Incluir”.

Aviso:

Informar Filiais do Professor, e gerar o usuário do Portal para o mesmo, pois será utilizado no Plano de Acompanhamento da Fase Empresa (customizado) e Ocorrências. 

Preencha as informações relacionadas ao cadastro do “Professor” na aba: “Identificação”. Em “Anexos”, “”Filiais do Professor”, vincule a “Filial” de atuação.

# **4. CADASTRO DA ATIVIDADE OFERTADA**

Criar a atividade ofertada vinculando o componente e a modalidade.

**Caminho:** Atividades Acadêmicas l Clicar em Atividades Ofertadas l Incluir.

* Preencher a Descrição com o nome da Fase Empresa;
* Preencher o Período (data inicial e final) da Atividade Ofertada que poderá ser único para todos os alunos ou na inscrição dos alunos poderá realizar a alteração das datas.
* Preencher a Carga horária aproveitada (contratada) deverá ser Única quando for uma atividade para uma empresa específica para vários alunos.

Importante:

* **Exibir Acompanhamento no Portal:** Este campo foi incluído a partir da versão: **12.1.32.004**. à interface nativa de Atividade Ofertada no SGE, para que o usuário possa definir por Atividade Ofertada de “Fase Empresa da Aprendizagem” o bloqueio de acesso aos planos de acompanhamento através dos portais do Aluno, Professor e Empresa, para os casos onde os alunos estão fazendo a prática presencial no SENAI.

Caso esse campo esteja desmarcado não serão exibidos os Planos de Acompanhamento vinculados à Atividade Ofertada nos portais.  
Para os registros já existentes, será necessário marcar essa opção para que os planos de acompanhamento voltem a ser exibidos no Portal.   
Para os novos planos de acompanhamento, o valor inicial padrão será marcado. 

Cada atividade ofertada terá um único Professor (Instrutor) que acompanha a Fase Empresa de determinado curso ou mais de um curso/matriz. Porém, somente um professor acompanhará um número X de cursos na Fase empresa. 

Aviso:

No “Anexo”, “Professores da Atividade” é possível vincular mais de um Professor (Instrutor), neste caso deve-se vincular mais de um Professor (Instrutor) se ocorrer o caso de substituição do primeiro.

O cadastro do Professor (Instrutor) será realizado no caminho: Atividade Oferta l Anexo l Professores da Atividade.

O professor da atividade deverá ser registrado com o tipo de participação como “Instrutor”.

Aviso:

Poderá ser criada uma Atividade Ofertada de “Fase Empresa da Aprendizagem” para um ou mais cursos desde que o Professor/Instrutor que acompanha a Fase Empresa seja o mesmo.

Atividade ofertada l Anexos l Cursos/Habilitações.

Informar Matriz Aplicada:

# **4.1. Empresa Vinculada à Atividade Ofertada (customizado)**

A Atividade será criada para uma única empresa. 

**Caminho:** TOTVS Educacional | Atividades Acadêmicas| Atividades ofertadas | Anexos | Empresa Aprendizagem.

Será disponibilizado um anexo estendido que o usuário poderá informar a qual Empresa aquela Atividade Ofertada está vinculada.

# **4.2. Anexo Competências da Fase Empresa (Customizado)**

O anexo Competências da Fase Empresa estará disponível na interface nativa de Atividades Ofertadas e poderá ser acessado em: TOTVS Educacional | Atividades Acadêmicas | Atividades Ofertadas | Anexos | Competências da Fase Empresa.

Ao acessar o anexo customizado serão exibidos 10 (dez) campos do tipo lookup, onde o usuário deverá informar quais competências serão avaliadas naquela Atividade Ofertada.

Só será permitido salvar o registro do anexo para as Atividades Ofertadas que possuem uma Empresa associada a ela. Caso contrário, será exibida mensagem informativa ao usuário e o registro não será salvo. 

Aviso:

Os registros informados no anexo serão gravados em tabela customizada. 

# **4.3. Efetivar a Fase Empresa da Aprendizagem -  Aluno na Atividade Ofertada**

Quando for fechado o contrato do(s) aluno(s) com a Empresa para realizar a prática profissional deverá ser cadastrado no SGE a “Atividade Ofertada => Fase Empresa da Aprendizagem” para o(s) aluno(s) com as seguintes informações:

* Período Letivo correspondente ao início da Fase Empresa;
* Curso em andamento (Matriz Aplicada);
* Professor que acompanha a Fase Empresa (Instrutor);
* Carga Horária Aproveitada (Carga Horária Contratada);
* Data inicial e final (datas do contrato com a Empresa);
* Empresa responsável pelo contrato;
* Competências que serão avaliadas pela empresa (no Plano de Acompanhamento);
* Inscrição confirmada.

# **4.4. Inscrição do Aluno na Atividade Ofertada (Em Lote)**

Este processo poderá ser utilizado para realizar as inscrições dos alunos em lote quando a atividade ofertada for para o mesmo período letivo, mesma data inicial/final (do contrato) , a mesma Carga Horária Aproveitada (Contratada) e a mesma Empresa para todos os alunos.

**Caminho:** Atividade Ofertada l Processos l Inscrições em Atividades Ofertadas.

Abrirá a tela de Assistente para inscrição em Atividade Ofertada, clique em “Avançar”. Em seguida, informe para qual grupo será feita a inscrição na atividade, neste caso será o grupo de “Alunos”.

Selecionar o filtro desejado, preencher as informações do filtro e clicar em adicionar alunos e clicar em “Avançar”.

Nesta tela aparecerá todos os alunos que foram filtrados para a inscrição na Atividade Ofertada; clique em “Avançar”.

Não esquecer de selecionar o parâmetro “Inscrição Confirmada”. Clique em “Avançar” e, em seguida, em "Executar".

# **4.5. Inscrição do Aluno na Atividade Ofertada (Por Aluno)**

Ao criar a inscrição por aluno na Atividade Ofertada deverá ser informado: Período Letivo, Data início e fim, Carga Horária Aproveitada e Empresa responsável pelo contrato.

* O Período Letivo correspondente ao ingresso no curso;
* A Data início e fim (Datas do contrato com a Empresa);
* A Carga Horária Aproveitada (Carga Horária Contratada);
* Marcar que o aluno está com a inscrição confirmada.

Aviso:

Empresa responsável pelo contrato - A customização preencherá o nome da empresa automaticamente de acordo com a empresa cadastrada na atividade ofertada.

O vínculo da empresa na inscrição do aluno será armazenado em Tabela Customizada.

# **4.6. Finalizar Inscrição do Aluno (Customizado)**

Ao finalizar a inscrição do aluno na Atividade Ofertada de “Fase Empresa da Aprendizagem” será criado um “Plano de Acompanhamento da Fase Empresa da Aprendizagem” para o Aluno. 

**Caminho:** TOTVS Educacional | Atividades Acadêmicas | Atividades ofertadas | Anexos | Plano de Acompanhamento.

Neste Plano de Acompanhamento terão as informações básicas, sendo: atividade ofertada, data início/data fim do contrato, aluno, empresa (responsável) e professor (instrutor), comentários da empresa e comentários do professor (instrutor).

# **5. PLANO DE ACOMPANHAMENTO DA FASE EMPRESA DA APRENDIZAGEM (CUSTOMIZADO)**

Será disponibilizado um anexo estendido que será preenchido automaticamente ao finalizar a inscrição de um aluno em uma atividade ofertada que tenha o campo Empresa preenchido.

**Caminho:** TOTVS Educacional | Atividades Acadêmicas | Atividades ofertadas | Anexos | Plano de Acompanhamento.

Esse anexo será preenchido ao finalizar a inscrição do aluno. A tela do anexo terá os campos abaixo:

* Atividade Ofertada;
* Data Início;
* Data fim;
* Aluno;
* Empresa;
* Instrutor;
* Comentários Instrutor;
* Comentários Empresa.

No Plano de Acompanhamento o Responsável da Empresa, pelo Portal do SGE, fará periodicamente a inclusão do registro de avaliação do aprendiz durante um determinado período de tempo (Data de início e término) informando sua percepção em relação a cada uma das “competências” selecionadas para análise. E também poderá incluir comentários sobre o Plano. O professor (Instrutor) terá acesso apenas para incluir os “comentários” e poderá visualizar as competências adquiridas pelo aluno.

Aviso:

Para que os usuários de DBA, Secretária,  Aluno, Professor (Instrutor) e Empresa consiga visualizar o Plano de Acompanhamento da Fase Empresa da Aprendizagem, será necessário que seja dado a permissão de acesso no perfil de cada usuário, para que fique visível no Portal.

Serviços Globais l Segurança l Perfis l Sistema l Educacional l Usuário l Acesso a Menus l Sistema Indústria l Fase Empresa l Acompanhamento Fase Empresa

**Perfil DBA ou Secretaria:** Plano de Acompanhamento

**Perfil Professor:** Acompanhamento Professor - Web

**Perfil Aluno:** Acompanhamento Fase Empresa - Portal Aluno

**Perfil Empresa:** Acompanhamento Empresa - Web

# **5.1. Página de “Acompanhamento Fase Empresa” (Customizado)**

O menu Acompanhamento Fase Empresa será disponibilizado no Portal do Aluno, Portal do Professor e Portal da Empresa, possibilitando o acesso aos registros de Plano de Acompanhamentos gerados na finalização da inscrição. 

No Portal do Aluno estará disponível em: Portal do Aluno | Oportunidades | Acompanhamento Fase Empresa

O aluno terá acesso ao registro do Plano de Acompanhamento cadastrado automaticamente na finalização da inscrição do aluno  na atividade ofertada.

Nesta tela o aluno terá permissão apenas de visualização dos registros inseridos pelo Instrutor e Empresa. Sendo assim, o sistema não permitirá que o aluno realize inclusão, edição e exclusão nos campos da tela de Plano de Acompanhamento.

No Portal do Professor estará disponível em **Portal do Professor | Acompanhamento Fase Empresa.**

O Instrutor (Professor) terá acesso ao registro do Plano de Acompanhamento.

Nesta tela o Instrutor terá permissão para inserir, editar e excluir informações apenas no campo **“Comentários Instrutor”,** nos demais campos o Instrutor terá a permissão apenas de visualização.

No Portal da Empresa estará disponível em **Portal da Empresa | Empresa | Acompanhamento Fase Empresa.**

O funcionário responsável pela empresa terá acesso ao registro do Plano de Acompanhamento. 

Nesta tela o responsável pela empresa terá permissão para inserir, editar e excluir informações apenas no campo **“Comentários Empresa”,** nos demais campos o responsável pela empresa terá a permissão apenas de visualização.

# **6. AVALIAÇÃO DO APRENDIZ - WEB (CUSTOMIZADO)**

O Professor e/ou a Empresa realizará o cadastro das Avaliações do Aprendizpelo Portal. A interface customizada será disponibilizada: 

* **Portal da Empresa:** O responsável pela empresa terá acesso a realizar cadastro de novas avaliações, sendo habilitados todos os campos para preenchimento da Empresa. Somente a empresa terá acesso ao preenchimento das competências e o Parecer de cada Avaliação do Aprendiz.
* **Portal do Professor**: O instrutor terá acesso para realizar cadastro de novas avaliações, porém apenas os campos Data de Início de Data Fim deverão ficar habilitados para preenchimento. Os demais campos deverão ficar desabilitados para preenchimento e o professor terá acesso apenas de visualização.
* **Portal do Aluno:** O aluno terá acesso apenas para visualização das avaliações.

Aviso:

Para cadastro da Avaliação do Aprendiz é obrigatório que já tenha criado o Plano de Acompanhamento ao finalizar uma inscrição em uma Atividade Ofertada. Cada aluno terá apenas um Plano de Acompanhamento e cada Plano poderá ter várias Avaliações. 

**Portal da Empresa:** O menu  “Avaliação do Aprendiz” no Portal da Empresa estará disponível em: Portal da Empresa | Acompanhamento Fase Empresa | Avaliação do Aprendiz.

Ao clicar em Nova Avaliação, será exibida página de inclusão etapas para avaliação do aprendiz.

Para cada avaliação o responsável da **Empresa** deverá informar: 

* **Data de Início:** Neste campo a empresa informará qual a Data de Início para execução das Atividades a serem desenvolvidos.
* **Data Fim:** Neste campo a empresa informará qual a Data de Fim para execução das Atividades a serem desenvolvidas.
* **Formulário de Competências:** Neste campo a customização deverá listar as Competências associadas à Atividade Ofertada, para avaliação da Empresa.

No cabeçalho do formulário deverá ter a seguinte instrução:“Solicitamos avaliar os itens abaixo considerando o desempenho do (a) aprendiz na prática profissional. Para tanto, pedimos analisar cada sentença e expressar sua opinião: ” 

Após o cabeçalho será liberado o formulário com todas as competências para avaliação da Empresa. Sendo que para cada competência o responsável pela empresa poderá selecionar em escalas apenas uma das opções abaixo:

* Não se aplica – Não informar escala
* Péssimo
* Ruim
* Regular
* Bom
* Ótimo
* **Parecer:** Será um campo texto obrigatório onde o responsável pela Empresa poderá preencher com maiores detalhes sobre a atuação do aluno na Fase Empresa

Aviso:

O sistema não enviará nenhum tipo de alerta informativo para o Aluno, Professor e/ou Empresa que foi inserido uma nova Avaliação do Aprendiz no Portal. Será responsabilidade do Aluno, Professor e Empresa acessar o portal frequentemente para visualizar as atualizações. 

**Portal da Professor:** O menu de “Avaliação do Aprendiz” estará disponível em: Portal do Professor | Acompanhamento Fase Empresa | Avaliação do Aprendiz. 

O Professor terá acesso a cadastrar novos períodos de avaliação e a visualizar as informações inseridas pela empresa.

Para cada Avaliação do Aprendiz o responsável da **Professor** poderá cadastrar as seguintes informações: 

▪ **Data de Início:** Neste campo o professor informará qual a Data de Início para execução das Atividades a serem desenvolvidos. 

▪ **Data Fim:** Neste campo o professor informará qual a Data de Fim para execução das Atividades a serem desenvolvidos. 

As demais informações estarão disponíveis apenas para a visualização do Professor, sendo elas **Formulário de Competências** e **Parecer.**

**Portal do Aluno:** O menu de “Avaliação do Aprendiz” estará disponível em: Portal do Aluno | Oportunidades | Acompanhamento Fase Empresa. 

O aluno terá acesso às avaliações cadastradas pelo Instrutor e Empresa e as avaliações das competências realizadas pela Empresa. O mesmo poderá apenas visualizar as informações inseridas nas Avaliação do Aprendiz.

# **6.1. Anexo de Avaliação do Aprendiz - Win (Customizado)**

Estará disponível na interface nativa de Atividades Ofertadas e poderá ser acessado em: TOTVS Educacional | Atividades Acadêmicas | Atividades Ofertadas | Anexos | Plano de Acompanhamento | Anexos | Avaliação do Aprendiz.

Será possível que o usuário visualize todas as informações inseridas na Avaliação do Aprendiz cadastrada pelo aluno via portal.

Ao acessar o **Avaliação do Aprendiz** o sistema retornará todas as informações inseridas pelo Professor e Empresa através do Portal. O processo permitirá que o usuário realize edição e inclusão de informações em todos os campos, porém não permitirá a exclusão do registro. 

Aviso:

Todas as alterações feitas diretamente neste anexo serão refletidas nas páginas do Portal do Aluno, Professor e Empresa. As informações serão armazenadas na mesma tabela customizada.

# **7. RELATÓRIO DO ACOMPANHAMENTO DA FASE EMPRESA DA APRENDIZAGEM (CUSTOMIZADO)**

Finalizando o Acompanhamento da Fase Empresa da Aprendizagem o Professor e/ou Empresa poderão imprimir o Relatório de Acompanhamento pelo Portal.

Esse relatório será gerado por “Plano de Acompanhamento” trazendo todas as informações do Plano de Acompanhamento (atividade ofertada, data início/data fim, Aluno, Empresa, Professor e Comentários) e avaliações do Aprendiz registradas pelo responsável da Empresa.

# **8. OCORRÊNCIAS PARA EMPRESA (CUSTOMIZADO)**

O objetivo deste processo é detalhar os parâmetros necessários para criação de uma ocorrência para um aluno que esteja vinculado a uma atividade ofertada que pertence a Fase Empresa. A interface de parâmetros estará disponível em: TOTVS Educacional | Sistema Indústria | Parâmetros | Fase Empresa.

A interface exibirá uma visão de dois parâmetros para serem configurados. Sendo eles:

* **Grupo de Ocorrência - Permite visualização pelo aluno (SOCORRENCIAGRUPO):** A customização retornará neste parâmetro todos os grupos de ocorrências cadastrados no TOTVS, porém permitirá associar no parâmetro apenas um Grupo de Ocorrência. O preenchimento será do tipo obrigatório. Neste parâmetro deverá ser associado o Grupo de Ocorrências que os alunos poderão visualizar.

Dica:

Para que o aluno consiga visualizar as ocorrências deste grupo, será necessário que seja marcado a flag visível no Portal, na aba Portal [Corpore.net](http://Corpore.net) no cadastro dos Tipos de Ocorrências.

* **Grupo de Ocorrência - Não permite visualização pelo aluno (SOCORRENCIAGRUPO):** A customização retornará neste parâmetro todos os grupos de ocorrências cadastrados no TOTVS, porém permitirá associar no parâmetro apenas um Grupo de Ocorrência. O preenchimento será do tipo obrigatório. Neste parâmetro deverá ser associado o Grupo de Ocorrências que os alunos não poderão visualizar.

Dica:

Para que o aluno não visualize as ocorrências deste grupo, será necessário que não seja marcado a flag visível no Portal, no cadastro dos Tipos de Ocorrências.

Aviso:

Para que o aluno consiga visualizar as ocorrências cadastradas será necessário que seja concedida a permissão de perfil, para que fique visível no Portal do Aluno (nativo), no caminho:Serviços Globais- Segurança l Perfis l Sistema l Educacional l Usuário l Anexos l Parâmetros Educacionais l Ocorrências.

Para que o Professor consiga realizar o cadastro das ocorrências será necessário que seja concedida a permissão de perfil, para que fique disponível a funcionalidade de cadastro de Ocorrências visível no Portal do Professor.

# **8.1. Página de Ocorrências (Customizado)**

O objetivo deste processo é a criação da funcionalidade de Cadastro de Ocorrências no Portal da Empresa, e no Portal do Professor. Com essa funcionalidade a Empresa e o Professor (Instrutor) poderá realizar o cadastro de ocorrências para os alunos que estiverem vinculados a ela através da Atividade Ofertada - Fase Empresa.

Para acesso a funcionalidade customizada no Portal da Empresa, o funcionário deverá acessar: Portal da Empresa | Acompanhamento Fase Empresa | Ocorrências Fase Empresa.

Aviso:

O sistema deverá retornar para cadastro de ocorrências no Portal da Empresa, apenas o Grupo de Ocorrências e Tipos de Ocorrências parametrizados. Caso não seja parametrizado nenhum grupo e/ou tipos de ocorrências a empresa não conseguirá realizar o cadastro.

Nesta tela poderá ser visualizado os seguintes campos:

* **Atividade Ofertada:** Será preenchido automaticamente pela inscrição do aluno na atividade
* **Aluno:** Será possível selecionar os alunos inscritos na atividade ofertada
* **Grupo:** Será preenchido automaticamente pela customização com o Grupo parametrizado. O campo será de preenchimento obrigatório
* **Tipo:** A customização retornará neste campo os Tipos de Ocorrências . O campo será de preenchimento obrigatório
* **Data:** Data de cadastro da ocorrência. O campo será de preenchimento opcional
* **Observação:** O campo será de preenchimento opcional
* **Incluir Arquivo:** O campo será de preenchimento opcional

A Empresa poderá realizar o cadastro de Ocorrências e anexar documentos o sistema  permitirá a realização de uploads de arquivos nos formatos .PDF, .JPEG; .DOC, .XLS, .PPT e serão armazenados na tabela (SOCORRENCIAALUNOARQ).

Para que o Professor consiga realizar o cadastro das ocorrências será necessário que seja concedida a permissão de perfil, para que fique disponível a funcionalidade de cadastro de Ocorrências visível no Portal do Professor, através do caminho: Serviços Globais l Segurança l Perfis l Sistema l Educacional l Usuário l Sistema Indústria l Cadastro de Ocorrências.

* **Perfil Professor:** Cadastro de Ocorrências Professor - Web

* **Perfil Empresa:** Cadastro de Ocorrências Empresa  - Web

Para acesso a funcionalidade customizada no Portal do Professor, o Professor (Instrutor) deverá acessar: Portal do Professor | Acompanhamento Fase Empresa | Ocorrências Fase Empresa

Aviso:

Todas ocorrências e seus documentos anexados cadastradas pelo Portal do Professor e pelo Portal da Empresa poderão ser visualizadas pelo aluno através da funcionalidade nativa que está disponível em: **Portal do Aluno | Menu | Central do Aluno | Ocorrências** e serão gravadas no TOTVS na funcionalidade nativa disponível em: TOTVS Educacional | Currículo e Oferta | Alunos | Anexos | Ocorrências do aluno (SOCORRENCIAALUNO).

# **9. REGISTRO DA FASE EMPRESA DA APRENDIZAGEM DO ALUNO**

**9.1. Análise Curricular**

Na Análise Curricular do aluno podemos observar que o componente curricular:  Fase Empresa, encontra-se **Não Concluída**

**9.2. Portal do Aluno**

No menu Grade Curricular o aluno poderá acompanhar o registro do Componente Curricular: Fase Empresa.

**9.3. Fase Empresa Concluída**

Quando o aluno concluir a Fase Empresa: Preencher a Data de conclusão da atividade curricular do aluno e selecionar o item: “Cumpriu a atividade''.

**9.4. Curso/Habilitação do Aluno**

No anexo Atividades curriculares será visualizado o registro da Fase Empresa do aluno.

**Caminho:** Currículo e Oferta l Alunos l Anexo l Cursos/Habilitações l Anexos l  Atividades Curriculares

Selecione a “Atividade Curricular”, e clique em editar

Preencher a data de conclusão e marcar que a conclusão da  atividade

E também na Análise Curricular poderá acompanhar se a CH do componente curricular (fase empresa) do curso já foi finalizado.

**Caminho:** Currículo e Oferta l Alunos l Anexo l Cursos/Habilitações l Selecionar o curso que aparecer na tela, clicar em editar e clicar em Análise Curricular

# **10 . INFORMAÇÕES IMPORTANTES**

Para o Extrator da Solução Integradora as informações sobre a Fase Empresa serão extraídas da Inscrição dos alunos das Atividades Ofertadas:

* A empresa que está vinculada na atividade ofertada do aluno (Empresa do contrato);
* A data de início e fim da atividade do aluno (datas do contrato);
* A carga horária aproveitada da atividade do aluno (Horas contratadas);
* Não serão mais enviadas as horas de prática profissional executadas.

Aluno poderá estar vinculado em mais de uma atividade ofertada desde que em Empresas e Datas Distintas. Esta situação somente poderá ocorrer quando o 1º contrato for rescindido e o aluno fizer contrato com outra empresa para as horas restantes da Fase Empresa:

* Neste caso, será preciso ajustar os dados da 1ª atividade do aluno, sendo a Carga Horária Aproveitada e Data final (contrato) até o momento que foi rescindido. E também preencher a data de conclusão e que “cumpriu” a atividade;
* Mas devido ao controle que o sistema faz da CH mínima do Item Curricular na Matriz Aplicada, o Item curricular deverá ter 0(zero) como horas mínimas para não travar este processo;
* Somente após estes procedimentos poderá inscrever o aluno em outra atividade ofertada de outra empresa e data de início posterior a data fim da 1ª atividade.

Aviso:

Ao realizar esse procedimento quando o 1º contrato do aluno for rescindido, deverá se atentar em realizar as alterações nos dados citados acima,  no mesmo dia da rescisão do contrato, para ser enviado informação atualizada no arquivo da Solução Integradora do mês vigente.

**Exemplo:**

Contrato: 400 hrs

Rescindido: 28/09/2024

Atualize os campos:

* CH contratada, com a quantidade de horas efetivadas = 100 hrs
* Data Fim do contrato: 28/09/2024
* Data Conclusão: 28/09/2024

 

O arquivo será enviado para a Solução Integradora referente ao mês 09 no início do mês 10. 

Caso o usuário atualize os dados deste contrato no mês seguinte ao da carga enviada, a alteração referente a CH aproveitada de 100 horas não terá reflexo na SI, pois no mês 09 as horas enviadas foram 400 hrs.    
Ao gerar o arquivo do mês 10, o contrato alterado para 100 horas não será gerado no arquivo pois o período não está mais vigente no mês de competência.

relacionadas à Matriz Curricular e Curso/Habilitação não sofreram alterações e, portanto, devem ser registradas.
