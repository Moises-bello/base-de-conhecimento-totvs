---
content_hash: 7eeb9f282a3871448c1927faa3c34a7f7f9f700e0391c906e69ff373e52154e5
fetched_at: '2026-06-29T00:10:41.888223+00:00'
page_id: '546674442'
product: rm
source: tdn-rm
title: 13 - Gestão de TCC - SENAI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546674442
version: 31
---

Gestão do TCC - Trabalho de Conclusão de Curso através do Portal Educacional, possibilita agilidade à realização do cadastro do TCC pelo aluno, bem como interações entre alunos e professores (Orientadores), seja nas solicitações de orientações, acompanhamento e desenvolvimento de trabalhos, envio de arquivos e inclusão de agendamentos para reunião entre alunos e professores (Orientadores) de forma rápida e prática.

# **PARAMETRIZAÇÕES - SERVIÇOS GLOBAIS**

Para que as atividades relacionadas ao desenvolvimento de TCC possam ser realizadas através do Portal Educacional, é necessário que previamente sejam configuradas as permissões de acesso e envio de e-mails, através do no Módulo TOTVS Serviços Globais.

Deverão ser configurados os seguintes itens:

* **Perfis de acesso para as novas tabelas do processo do TCC:** Disponível em TOTVS Serviços Globais l Aba: Segurança l Perfil
* **Envio de e-mails:**Disponível em TOTVS Serviços Globais l Administração l Coligada e TOTVS Serviços Globais l Ambiente l Configuração l Parâmetros l Globais l Envio de e-mails

# **PARAMETRIZAÇÕES - EDUCACIONAL**

Para que Gestão de TCC siga sua logística corretamente, é necessário que previamente sejam realizados os cadastros e parametrizações essenciais ao processo, através do Módulo TOTVS Educacional l Educacional

Ambiente l Parâmetros l Educacional

Os Parâmetros Educacionais do TCC deverão ser configurados a  partir do Processo: 15.07 - TCC, de acordo com os processos definidos pela Unidade Operacional (Filial) para desenvolvimento do TCC

Em: TCC1/1, configure os processos de acordo com as suas funcionalidades:

* **Permitir aceite do aluno para conclusão de reuniões de acompanhamento:** Marcando este parâmetro, o professor irá conseguir finalizar uma reunião de acompanhamento somente depois do aceite do aluno.
* **Exibir os participantes da banca para o aluno no portal:** Marcando este parâmetro, o aluno poderá visualizar os participantes de sua banca examinadora, ao expandir <mais> os detalhes de seu TCC.
* **Enviar versão final dos trabalhos para os participantes da banca:** Marcando este parâmetro, quando o aluno postar a versão final do seu TCC, todos os participantes cadastrados em sua banca examinadora (que possuem e-mail cadastrado) irão receber a versão final do TCC por e-mail.
* **Permitir orientações acima do máximo cadastrado para o professor**: Marcando este parâmetro, mesmo que no cadastro "Professores/Orientadores por período letivo" esteja definido um número máximo de orientações, o professor poderá ultrapassar esse limite definido.
* **Relatório do aceite da publicação do trabalho final:** Informando o relatório de aceite de publicação (que deve ser o relatório "EDUREL0071 - Autorização para publicação do TCC" disponibilizado no book de relatórios do TOTVS Educacional), o aluno poderá imprimir essa autorização, depois de cadastrar o seu TCC no portal.
* **Situação do TCC (Padrão):** Essa situação do TCC deve ser informada, pois quando o aluno cadastrar o seu TCC pelo portal, o sistema irá assumir essa situação padrão. Ou seja, quando um aluno cadastrar o seu TCC pelo portal o sistema irá buscar essa situação e cadastrar em seu TCC.
* **Situação de matrícula em disciplina:** Essa situação de disciplina deve ser informada, pois quando a situação do TCC for alterada para uma que indique desistência, o sistema irá alterar a situação de matrícula da disciplina (matrícula em disciplina vinculada ao TCC) para essa informada.
* **Motivo de alteração da situação de matrícula em disciplina:** Esse motivo de alteração deve ser informado, pois quando a situação do TCC for alterada para uma que indique desistência, o sistema irá usar esse motivo quando alterar a situação de matrícula da disciplina.

Em: TCC 2/2, configure os processos de acordo com as suas funcionalidades:

* **Tipo de armazenamento:** Nesse parâmetro deve-se configurar o tipo de armazenamento que a Instituição de Ensino irá usar, podendo ser: Arquivo da base de dados, Arquivo de algum diretório ou Arquivo no ECM.
* **Diretório de armazenamento:** Nesse parâmetro deve-se informar o diretório que os arquivos serão armazenados, quando o tipo de armazenamento for de Arquivo de algum diretório.
* **Tamanho máximo de armazenamento:** Nesse parâmetro podemos informar o tamanho máximo dos arquivos que irão ser postados, pois é de extrema importância limitar os arquivos para economizar espaço, seja em disco ou no banco de dados.
* **Extensões de arquivos permitidas (Exemplo:** **"pdf;ppt"):** Neste parâmetro podemos informar as extensões permitidas para postar arquivos referentes ao TCC.

# **CONFIGURAÇÃO DE DISCIPLINAS DA MATRIZ CURRICULAR**

Para que as Disciplinas que estejam relacionadas ao TCC (conforme plano de curso) sejam apresentadas nos Portais dos Alunos e Professores (orientadores), é necessário que ao vínculo da disciplina ao Período da Matriz Curricular esteja selecionado o parâmetro: Indica se a Disciplina é de TCC.

Através da aba: Currículo e Oferta", selecione Matrizes Curriculares e após selecionar a Matriz Curricular desejada em: Anexos, clique em: Período

A partir do Período, em: Anexos, selecione: Disciplinas da Matriz Curricular

Selecione o Parâmetro: Indica se a Disciplina é de TCC

# **CADASTROS RELACIONADOS À GESTÃO E DESENVOLVIMENTO DO TCC**

Em Atividades Acadêmicas, estão relacionados os cadastros/dados referentes ao Trabalho de Conclusão de Curso (TCC)

**PROFESSORES/ORIENTADORES POR PERÍODO LETIVO**

O cadastro de Professores/Orientadores por Período Letivo deve estar relacionado ao Período Letivo de oferta de curso vinculado ao Número Máximo de Orientações Permitidas

**LINHAS DE PESQUISA**

O cadastro das Linhas de Pesquisa deverá conter o Tema e Descrição da mesma.

Para que esteja disponível aos alunos, é necessário que o parâmetro: Ativa esteja selecionado

Através dos Anexos da Linha de Pesquisa, deverão ser vinculadas as Matrizes Aplicadas e os Professores Orientadores da Linha Pesquisa

**STATUS DOS TCC**

O cadastro de Status do TCC deve estar relacionado à sua indicação, para a qual deverá estar selecionado o parâmetro correspondente, sendo:

* **Indica Status Final do TCC**
* **Indica Desistência**

O cadastro de Status do TCC devem ser previamente realizados e não deverão ser posteriormente alterados, uma vez que os mesmos foram parametrizados na base Template para todos os Departamento Regionais SENAI

**TIPOS DE PARTICIPANTES DA BANCA**

O cadastro dos Tipos de Participantes da Banca deve estar relacionado ao papel de atuação de cada participante que irá compor a Banca examinador/avaliadora

**TIPOS DE TCC**

O cadastro dos Tipos de TCC devem compreender as atividades determinadas para desenvolvimento e apresentação dos mesmos

**ENDEREÇO DE E-MAIL PARA ASSUNTOS DO TCC (MATRIZ APLICADA)**

À Matriz Aplicada l Aba: TCC, deverá estar associado o endereço de e-mail para o qual os e-mails relacionados à oferta e desenvolvimento de TCC deverão ser direcionados para atendimento

# **REGISTRO TCC - PORTAL DO ALUNO**

O registro do TCC pode ser realizado por um aluno que tenha vínculo de matrícula (ativa), em período letivo e disciplina exclusiva de TCC.

Para se inscrever, através do Portal do Aluno, no menu: TCC, ao clicar em: Cadastrar TCC, deverão ser adicionadas as demais informações:

* **Tema do TCC**
* **Matrícula vinculada ao TCC**
* **Linha de Pesquisa**
* **Tipo**
* **Autoriza Publicação de TCC**

***Este cadastro também poderá ser realizado pela Secretaria Escolar via TOTVS Educacional (SGE)***

Após, em: Identificador do TCC l Aba: Orientador(es), o aluno deverá associar o Professor orientador desejado e, e, seguida, clicar em: Convidar Orientador.

# **ACESSO E ACEITE AO CONVITE DE ORIENTAÇÃO - PORTAL DO PROFESSOR**

Ao acessar o Portal do Professor, através do menu: TCC l Convites para Orientação de TCC, o Professor orientador terá acesso ao convite de orientação do TCC.

Tratando-se de um novo convite, este será apresentado com status: Não Aceito.

Para realizar o Aceite ou recusa de um convite de orientação, o Professor orientador deverá clicar em: Editar

Para registrar o Aceite, o  Professor orientador deverá clicar em: Convite Aceito.

Para registrar a Recusa, será obrigatório o preenchimento do campo: Justificativa.

# **AGENDAMENTO E ACOMPANHAMENTO DE REUNIÕES - PORTAL DO PROFESSOR**

O desenvolvimento do acompanhamento de TCC é realizado/registrado através do menu: TCC l Acompanhamento.

Neste menu, o professor orientador poderá incluir, editar ou excluir agendamentos (reuniões) para desenvolvimento das atividades, que possibilitam a interação entre aluno e professor orientador, incluindo permissão para envio e recebimento de arquivos.

Quando do registro de interação do aluno ao agendamento realizado pelo professor orientador, o mesmo terá acesso às observações registradas e aos anexo(s) inserido(s) pelo aluno.  
Ao clicar em: Baixar Arquivo, o professor orientador terá acesso ao(s) arquivo(s) anexado(s).

Finalizada a interação relacionada ao agendamento, o parâmetro: Reunião Encerrada deverá ser selecionado para sua conclusão.

# **ACOMPANHAMENTO DE REUNIÕES - PORTAL DO ALUNO**

O desenvolvimento do acompanhamento de TCC é realizado/registrado através do menu: TCC l Acompanhamento.

Neste menu, o aluno poderá visualizar agendamentos (reuniões) registradas pelo Professor orientador para desenvolvimento das atividades, que possibilitam a interação entre aluno e professor orientador, incluindo registro do aceite, registro de observações e permissão para envio e recebimento de arquivos.

# **BANCA AVALIADORA - PORTAL DO PROFESSOR**

Concluídas as interações relacionadas ao desenvolvimento de TCC, ao acessar o Portal do Professor, através do menu: TCC l Banca, o Professor orientador deverá selecionar/cadastrar a Banca que irá compor a análise do TCC a ser apresentado pelo aluno.

Ao clicar em: Incluir Banca. vincule as informações:

* **TCC**
* **Data e Horário**
* **Local da Banca**

Após, ao clicar em "Incluir participante", informe os dados relacionados à pessoa e sua participação. Clique em "Salvar".

***Este cadastro também poderá ser realizado pela Secretaria Escolar via TOTVS Educacional (SGE).***

É importante registrar se a pessoa convidada a compor a Banca é uma Pessoa Externa ou Professor da Instituição.

Neste primeiro momento, deve ser realizado o vínculo de um Professor da Instituição.

# **RELATÓRIO FINAL E AVALIAÇÃO - PORTAL DO ALUNO**

Finalizado o cadastro e a composição da Banca, o aluno deverá realizar o envio do Arquivo Final do TCC.

Através do Portal do Aluno, através do menu: TCC l Aba: Arquivo Final, ao clicar em: Enviar Arquivo Final, o relatório deverá ser anexado. Após, ao clicar em: Enviar Arquivo, o mesmo será disponibilizado ao Professor orientador..

# **RELATÓRIO FINAL E AVALIAÇÃO - PORTAL DO PROFESSOR**

Realizado o envio do "Arquivo final", o orientador receberá via e-mail a notificação de envio, juntamente com o arquivo anexado.

Considerando a conclusão de todas as etapas de avaliação do TCC e a sua apresentação, o Professor orientador deverá registrar a nota final obtida pelo aluno.

Ao acessar o Portal do Professor, através do menu: Diário de Classe l Seleção de Disciplina l Notas/Faltas de Etapas, será apresentada a tela de registro de nota

Após selecionar, na coluna: Nota deverá ser registrada a pontuação obtida pelo aluno.

Aplicado o registro, clique em: Salvar

Após registro de nota, a equipe de Secretaria Escolar poderá executar a Apuração de Resultado Final para a Disciplina (TCC), conforme orientações do Manual de Capacitação de Processos Educacionais (Módulo II), no item: Rendimento Escolar

# **CONCLUSÃO - PORTAL DO ALUNO**

Realizado o processo de apuração de resultados, o aluno poderá consultar no Portal Educacional o status de aprovação final da disciplina TCC
