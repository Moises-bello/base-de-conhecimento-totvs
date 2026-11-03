---
content_hash: 634a7dd73d7025cacdd55f1048d130c5502117b60a4578651c350bad1df40898
fetched_at: '2026-06-28T21:35:19.576524+00:00'
page_id: '212902689'
product: fluig
source: tdn-fluig
title: Modelos de relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212902689
version: 48
---

# Índice

3true.\*ndicenone

# Objetivo

---

O objetivo deste guia é relacionar os exemplos de relatórios disponíveis para o TOTVS Fluig Plataforma.

Importante

* Os relatórios 'exemplo de uso' estão disponíveis em nosso repositório público:<https://git.fluig.com/projects/SAMPLES/repos/relatorios/browse>  Faça já o download!
* Em alguns navegadores, ao efetuar o *download* é adicionada a extensão .xml ao arquivo. É necessário alterar essa extensão para .rptdesign.
Compatibilidade no modo escuro

Este recurso ainda não é compatível com o modo escuro lançado na atualização [Voyager 2.0](https://tdn.totvs.com/x/6HxjN). Para mais detalhes, consulte a documentação [aqui](https://tdn.totvs.com/x/WEdgOQ).

# Pré-requisitos

---

Para fazer uso dos relatórios disponíveis nesta página, é imprescindível conhecer o processo de .

# Relatórios de Aprendizado - LMS

---

Os modelos de relatórios de aprendizado LMS disponíveis para o TOTVS Fluig foram descontinuados na atualização [Voyager (2.0)](https://tdn.totvs.com/x/6HxjN).

### *EnrollmentDetail.rptdesign*- Relatório de matrículas em trilhas e treinamentos

O objetivo deste relatório é exibir as matrículas realizadas no LMS, bem como seu status e o status final da matrícula. Este relatório fará consulta ao dataset  já disponível no produto, solicitando ao usuário filtrar por um treinamento/trilha quais matriculados deseja exibir, além de definir a ordem dos matriculados pelos campos: nome do usuário, sobrenome do usuário, pontuação, data da matrícula, data de conclusão.

Veja o exemplo em nosso repositório **[aqui](https://git.fluig.com/projects/SAMPLES/repos/relatorios/browse/lms-reports/EnrollmentDetail)**.

### *ProgressByTraining.rptdesign*- Relatório de andamento em treinamentos

O objetivo deste relatório é exibir o andamento de cada matrícula de um treinamento específico que deve ser informado na tela de parâmetros do relatório. É possível também definir a ordem das matrículas que aparecem no relatório conforme as seguintes opções: nome do usuário, sobrenome do usuário, pontuação, status da matrícula e data da matrícula. Este relatório é dividido em duas seções, no estilo Cabeçalho -> Detalhe, onde a parte 'Mestre' diz respeito aos dados da matrícula do usuário e a parte 'Detalhe' diz respeito aos dados do andamento dessa matrícula em si para determinado treinamento.

### *ProgressByTrack.rptdesign*- Relatório de andamento em trilhas

O objetivo deste relatório é exibir o andamento de cada matrícula de uma trilha que deve ser informada na tela de parâmetros do relatório. É possível também definir a ordem das matrículas que aparecem no relatório conforme as seguintes opções: nome do usuário, sobrenome do usuário, pontuação, status da matrícula e data da matrícula. Este relatório é dividido em duas seções, no estilo Cabeçalho -> Detalhe, onde a parte 'Mestre' diz respeito aos dados da matrícula do usuário e a parte 'Detalhe' diz respeito aos dados do andamento dessa matrícula em si para determinada trilha.

### *NormalClassEnrollment.rptdesign*- Relatório de matrículas de turmas

O objetivo deste relatório é exibir as matrículas realizadas em turmas do fluig LMS, bem como seu status e o status final da matrícula. Este relatório fará consulta ao dataset já disponível no produto, solicitando ao usuário filtrar por uma turma quais os matriculados que deseja exibir, além de definir a ordem dos matriculados pelos campos: nome do usuário, sobrenome do usuário, pontuação, data da matrícula e data de conclusão.

### *NormalClassProgress.rptdesign*- Relatório de andamento de turmas

O objetivo deste relatório é listar os detalhes do andamento dos usuários matriculados em turmas do fluig LMS, o relatório possui 3 níveis, no primeiro nível são listadas as matrículas da turma e o detalhamento do andamento do usuário para cada matrícula, no segundo nível são listados os tópicos dessa turma bem como o detalhe de andamento do usuário para determinado tópico e no terceiro nível são listados os itens de tópico com os detalhes do andamento do usuário em cada item de tópico. Este relatório fará consulta a 4 datasets, sendo estes: *disciplineClassDataset*, *enrollmentDataset*, *enrollmentTopicDataset* e *enrollmentTopicItemDataset*.

### *AssessmentApplicationGenericReport.rptdesign*- Relatório de execuções de avaliações

O objetivo deste relatório é exibir as execuções de avaliações para usuários e também para agendamentos por email.  
Na execução do relatório será necessário selecionar o nome da avaliação desejada. A apresentação do relatório será definida em três níveis/tabelas:

1. **Execução** (cabeçalho em fundo amarelo, com separador em linha vermelha): Execução do Relatório com informações do executor e da avaliação:
   1. Executor (Nome do usuário ou email caso seja agendamento)
   2. Data/Hora início
   3. Data/Hora fim
   4. Pontuação mínima
   5. Pontuação obtida
   6. Indicador de aprovação
2. **Bloco** (cabeçalho em fundo azul claro):  Informações do bloco da respectiva avaliação:
   1. Nome do bloco
   2. Peso
   3. Mínimo de acertos
   4. Pontuação obtida
3. **Questão** (em fundo branco): Informações da questão do respectivo bloco da avaliação.
   1. Tipo de questão
   2. Título da questão
   3. Tópico
   4. Dificuldade
   5. Pontuação obtida
   6. Cancelada

O relatório é composto pelos seguintes *datasets*:

* *assessmentAppQuestionDataset*: Dataset de questões aplicadas em uma avaliação
* *assessmentAppBlockDataset*: Dataset de blocos em uma avaliação
* *assessmentApplicationGenericDataset:*Dataset de execução de avaliações

### *AssessmentApplicationByTrackReport.rptdesign -*Relatório de execuções de avaliações por trilha

### *AssessmentApplicationByTrainingReport.rptdesign  -*Relatório de execuções de avaliações por treinamento

O objetivo destes relatórios é exibir as execuções de avaliações por Trilha/Treinamento.   
Na execução do relatório por Trilha, será necessário selecionar a Trilha, e no de treinamento, será necessário informar o Treinamento.  
Em ambos os relatórios, também será preciso selecionar o tipo de aplicação de avaliação (pré, pós, reação, todos)

A apresentação dos relatórios será definida em três níveis/tabelas:

1. **Execução** (cabeçalho em fundo amarelo, com separador em linha vermelha): Execução do Relatório com informações do executor e da avaliação:
   1. Executor (Nome do usuário ou email caso seja agendamento)
   2. Nome da Avaliação
   3. Tipo da Avaliação
   4. Data/Hora Início
   5. Data/Hora Fim
   6. Pontuação Mínima
   7. Pontuação Obtida
   8. Indicador de Aprovação
2. **Bloco** (cabeçalho em fundo azul claro):  Informações do bloco da respectiva avaliação:
   1. Nome do Bloco
   2. Peso
   3. Mínimo de Acertos
   4. Pontuação Obtida
3. **Questão** (em fundo branco): Informações da questão do respectivo bloco da avaliação.
   1. Tipo de Questão
   2. Título da Questão
   3. Tópico
   4. Dificuldade
   5. Pontuação Obtida
   6. Cancelada

### *AssessmentClassApplicationReport.rptdesign*- Relatório de execução de avaliações por turma

O objetivo deste relatório é exibir as execuções de avaliações por Turma. Na execução do relatório será necessário selecionar a turma.

A apresentação do relatório será definida em três níveis/tabelas:

1. **Execução** (cabeçalho em fundo amarelo, com separador em linha vermelha): Execução do Relatório com informações do executor e da avaliação:
   1. Executor (Nome do usuário ou email caso seja agendamento)
   2. Nome da avaliação
   3. Tópico
   4. Data/Hora início
   5. Data/Hora fim
   6. Pontuação mínima
   7. Pontuação obtida
   8. Indicador de aprovação
2. **Bloco** (cabeçalho em fundo azul claro):  Informações do bloco da respectiva avaliação:
   1. Nome do bloco
   2. Peso
   3. Mínimo de acertos
   4. Pontuação obtida
3. **Questão** (em fundo branco): Informações da questão do respectivo bloco da avaliação.
   1. Tipo de questão
   2. Título da questão
   3. Tópico
   4. Dificuldade
   5. Pontuação obtida
   6. Cancelada

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.

# Relatórios de Ambiente

---

### ***Colleague\_report.rptdesign*** **- Relatório de Usuários**

O objetivo deste relatório é listar os usuários que estão cadastrados na plataforma mostrando também seus status de cadastro (Ativo ou desativado). Este relatório fará consulta ao dataset  já disponível na plataforma, solicitando ao usuário filtrar por matrícula do colaborador e por status do cadastro (Ativo ou Desativado), além de permitir definir a ordem dos usuários cadastrados pelos campos: Matrícula, Nome, Login e E-mail.  Para fazer download do modelo de relatório [clique aqui](https://git.fluig.com/projects/SAMPLES/repos/relatorios/browse).

### *Accesslog-pt\_BR.rptdesign* - Relatório de Acesso dos Usuários

O objetivo deste relatório é listar os acessos dos usuários na plataforma mostrando também as datas e horários de acesso na plataforma. O usuário tem a opção de filtrar por login do colaborador, data inicial e data final de aceso, além de permitir definir a ordem de apresentação dos resultados pelos campos: Código do Usuário, Nome, Login e Data.  Para fazer download do modelo de relatório [clique aqui](https://git.fluig.com/projects/SAMPLES/repos/relatorios/browse). Ao extrair os arquivos, você pode escolher o relatório referente ao banco de dados que está utilizando em sua plataforma.
