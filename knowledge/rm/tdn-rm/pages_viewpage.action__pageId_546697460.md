---
content_hash: d3e822492eb2fb1670a499b13207c645dae970e0c406f076580cfcd9e64e9169
fetched_at: '2026-06-29T00:10:42.197269+00:00'
page_id: '546697460'
product: rm
source: tdn-rm
title: MIT021 - Solução Integradora
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546697460
version: 80
---

Documentação para detalhar os critérios e regras aplicadas na ferramenta para extração de informações do SGE – Sistema de Gestão Escolar para importação no sistema SOLUÇÃO INTEGRADORA.

# **Extração dos Dados:**

* Os dados serão gerados mensalmente. O usuário irá informar o mês e ano para extração da produção.
* Após selecionar o mês e ano, o usuário poderá filtrar as matriculas que serão incluídas no arquivo por:
  + **Filial**
  + **Modalidade**
  + **Turma**
  + **Tipo de Ação (Presencial ou à Distância)**

Importante

Sempre que o filtro é deixado em branco, com exceção do mês e ano que são obrigatórios, o extrator irá entender que todas as informações deverão ser inseridas no arquivo.   
Ex: Se a Modalidade for preenchida como '11' (Aprendizagem Industrial Básica); serão inseridas no arquivo, respeitando as regras descritas neste documento, matriculas de todas as filiais, turmas, tipo de ação, porém, apenas aquelas associadas a cursos de Aprendizagem Básica.

* As informações serão extraídas conforme o mês e filtros selecionados pelo DR no momento da geração do arquivo:
  + Os dados correspondentes a situação da matrícula do aluno e carga horária serão exportados de acordo com o mês selecionado.

* + As informações básicas do aluno: Nome, endereço, documentos... serão exportadas de acordo com o dado atual informado na base.

* Seleção de alunos que serão extraídos do SGE:
  + Os dados serão filtrados conforme a data de início e fim da turma, ou seja, o extrator localiza no SGE as turmas que estão ativas no mês de referência e a partir desta identificação busca as demais informações: Dados do curso, alunos matriculados e carga horária associada.
  + Após filtrar alunos / matrículas a partir das datas inicial e final da turma é feita uma verificação de todas as matrículas reportadas no mês anterior como 'em andamento' e as mesmas são incluídas no arquivo para que sejam enviadas para a Solução Integradora.
  + As matrículas que foram reportadas no mês anterior ao de referência como 'em andamento' e por algum motivo vieram a ser 'canceladas', serão reportadas a Solução Integradora como operação do tipo 'exclusão'.
  + Para a identificação destas matrículas em andamento foi criada uma tabela que armazena os dados gerados pelo extrator. Após gerar o arquivo para um determinado mês de referência a tabela é alimentada com as matrículas correspondentes ao mês informado no momento da geração.
Importante

Para que esta tabela seja alimentada, no primeiro mês após a entrada em produção no SGE foi criado um campo na Matrícula do Aluno no Curso/Habilitação com a descrição: Encerrar Matricula na Solução Integradora (ENCALUNO). O objetivo do campo é permitir que o regional alimente a tabela com as matriculas que ainda estão em andamento na Solução Integradora, mas, as turmas associadas foram finalizadas no sistema legado.   
Quando o campo é preenchido como 'sim' a matricula é exibida no arquivo para exportação com o status em que se encontra no momento da geração, mesmo a turma não estando mais vigente.   
Após o primeiro envio de produção as matriculas sinalizadas com o 'sim' já estarão na tabela 'que armazena as matriculas' e estas permaneceram sendo enviadas para a Solução Integradora até que sejam finalizadas no SGE.   
O Campo deve ficar marcado como 'SIM' na matricula do aluno apenas no primeiro mês de utilização do SGE para envio de produção. Após este primeiro mês o SIM deve ser retirado das matriculas e o campo desabilitado.

Existe uma restrição para não trazer produção dos alunos que possuem a modalidade 150 – Certificação de Pessoas, alunos com situação de matrícula igual a Pré-Matriculado e aluno com situação de matrícula igual a Cancelado.

Os alunos com situação de matrículas Cancelada serão enviados apenas nos casos onde a matrícula foi reportada no mês anterior ao de referência como 'em andamento'.

Matrículas que não atendam as regras do item ***2.3 Movimentações do Aluno***, são retiradas do arquivo de extração para evitar a crítica 27 - Campo: Situação da Matrícula - Campo obrigatório não preenchido ao subir a produção para Solução Integradora. O regional deve consultar o Cubo da Solução Integradora e filtrar o campo Situação de Matrícula igual a vazio para identificação dessas matrículas.

* Controle de Versão do Extrator:

Foi criado a tabela ZVERSAOSI que irá registrar a versão e data de atualização do Extrator da Solução Integradora.

# **Campos e Tabelas criados Para Atender a Solução:**

Importante

Os campos complementares cuja origem dos dados não é proveniente de uma ***tabela referencial disponibilizada pelo Departamento Nacional*** estarão no SGE em branco para que o usuário no regional preencha a informação solicitada

| Tabela | Campo | Descrição |
| --- | --- | --- |
| **SCURSOCOMPL** | **CBO\_SI** | Tabela dinâmica  Campo para preenchimento da ocupação segundo a Classificação Brasileira de Ocupações. A tabela é disponibilizada pelo Departamento Nacional e segue os padrões definidos pelo Ministério do Trabalho e Emprego. |
| **ZPARAMNSTABREFCURSO** | **CODCURSOCATALAGO** | Cód. Curso Catálogo é um campo customizado no anexo do cadastro de curso. Nele estará vinculado uma tabela com os cursos do Catálogo Nacional, disponibilizada pelo Departamento Nacional. As regras para preenchimento deste campo estão descritas na customização “Tabela Referencial de Cursos – Solução Integradora”. |
| **SGRADECOMPL** | **CODCURSOSCOP** | Este campo foi criado para identificar os cursos que já haviam sido reportados pelo DR antes do primeiro reporte de produção utilizando o SGE para o SCOP / Solução Integradora. Para estes cursos anteriormente enviados. O Código do Curso enviado ao DN pelo Legado deve ser preenchido com o mesmo código reportado anteriormente através do sistema legado para o SCOP e/ou Solução Integradora. |
| **CURSOMEC** | Tabela dinâmica  Campo utilizado para cursos técnicos, bem como para aprendizagem técnica. O campo possui uma tabela para seleção de cursos técnicos constantes da tabela disponibilizada pelo Departamento Nacional dos cursos cadastrados na base do MEC/SISTEC. |
| **CHESCOLAR** | Este campo foi criado para que o DR informe a carga horária PRESENCIAL prevista em Plano de Curso. Para cursos de Aprendizagem incluir as horas da Fase Escolar + a Carga Horaria mínima de Pratica Profissional. |
| **CHESTAGIO** | Neste campo deverá ser informada somente a carga horária do ESTÁGIO, prevista em Plano de Curso. |
| **CHEAD** | Este campo foi criado para que o DR informe a carga horária A DISTÂNCIA prevista em Plano de Curso. |
| **STURMACOMPL** | **DRPARCEIRO** | Este campo “DR Parceiro” na turma foi criado para que o DR informe o DR Parceiro do atendimento, de acordo com a tabela referencial disponibilizada pelo Departamento Nacional.  Quando o curso for "modular" será preciso preencher o campo somente na primeira turma da matricula no período letivo do aluno para que a informação seja apresentada no arquivo gerado pelo extrator. |
| **SALUNOCOMPL** | **CODALUNOSCOP** | Este campo foi criado para identificar os alunos que já haviam sido reportados pelo DR antes do primeiro reporte de produção utilizando o SGE para o SCOP / Solução Integradora. Para estes alunos anteriormente enviados, o código do Aluno no legado deve ser preenchido com o mesmo código reportado anteriormente através do sistema legado para o SCOP e/ou Solução Integradora. Para os alunos reportados pela primeira vez via SGE o campo deve estar vazio. |
| **MOTIVOCPF** | Tabela Dinâmica  Este campo foi criado para que o DR possa justificar a falta de CPF do aluno. Tabela referencial disponibilizada pelo Departamento Nacional. |
| **SITUACAOOCUP** | Tabela Dinâmica  Este campo identifica a situação ocupacional do aluno. Tabela referencial disponibilizada pelo Departamento Nacional. |
| **TIPOESCOLA** | Tabela Dinâmica  Este campo é utilizado para identificar o tipo de escola de origem. Tabela referencial disponibilizada pelo Departamento Nacional. |
| **SALUNOCOMPL.DDI** | Este campo é utilizado para informar o código DDI (Discagem Direta Internacional) do telefone do aluno. |
| **SALUNOCOMPL.DDICELULAR** | Este campo é utilizado para informar o código DDI (Discagem Direta Internacional) do telefone celular do aluno. |
| **SALUNOCOMPL.TIPOPF** | Tabela Dinâmica  Este campo é utilizado para identificar a nacionalidade do aluno. Tabela referencial disponibilizada pelo Departamento Nacional. |
| **SHABILITACAOALUNOCOMPL** | **CODMATRICULASCOP** | Este campo foi criado para identificar as matriculas que já haviam sido reportados pelo DR antes do primeiro reporte de produção utilizando o SGE para o SCOP / Solução Integradora. Para estas matriculas anteriormente enviados, o código da Matricula no legado deve ser preenchido com o mesmo código reportado anteriormente através do sistema legado para o SCOP e/ou Solução Integradora. Para as matriculas iniciadas no SGE o campo não deverá ser preenchido. |
| **TIPODOCA** | Este campo foi criado para identificar o Tipo de documento da empresa que é responsável pelo contrato da Aprendizagem do aluno.  Para as Matrizes da Aprendizagem 4.0 não deverá preencher este campo. |
| **EMPRESACOMP** | Este campo foi criado para identificar o número do documento referente ao CNPJ ou CEI ou Inscrição Estadual da empresa que é responsável pelo contrato da Aprendizagem do aluno.  Para as Matrizes da Aprendizagem 4.0 não deverá preencher este campo. |
| **DATAINICIALA** | Este campo é usado para identificar a data inicial do Contrato de Aprendizagem.  Para as Matrizes da Aprendizagem 4.0 não deverá preencher este campo. |
| **DATAFINALA** | Este campo é utilizado para identificar a data final do Contrato de Aprendizagem.  Para as Matrizes da Aprendizagem 4.0 não deverá preencher este campo. |
| **CHCONTRATADAA** | Este campo é utilizado para identificar a Carga Horaria Contratada do contrato da Prática Profissional.  Para as Matrizes da Aprendizagem 4.0 não deverá preencher este campo. |
| **DATAPREVISTASAIDA** | Neste campo deve ser informada a data de previsão de saída da conclusão do curso pelo aluno. |
| **CNPJEMPATENDIDA** | Neste campo deve ser informado o CNPJ da empresa atendida. O campo só permite informar números, sem espaço, ponto, barra ou traço. |
| **SMATRICPLCOMPL** | **ARTICULACAO** | Tabela Dinâmica  Neste campo deve ser indicado se é um curso articulado entre SESI e SENAI ou entre SENAI e outras instituições. |
| **TIPOGRAT** | Tabela Dinâmica  Este campo é utilizado para informar a "Condição do aluno" em relação a Gratuidade Regimental. Tabela referencial disponibilizada pelo Departamento Nacional. |

## **REGRAS PARA EXTRAÇÃO DOS DADOS**

**Baseado nas regras de importação e análise dos dados da Solução Integradora foram definidas regras para extração dos dados dentro do SGE**   
**Abaixo segue as regras que impactam na extração dos dados pelo SGE para a Solução Integradora.**

# **TIPO DE REGISTRO - CURSO**

### **Código do curso**

**Cursos iniciados no SGE:** Código gerado pelo extrator: IDFT do Curso + IDFT da Matriz Curricular   
**Cursos migrados do Sistema Legado para o SGE:** Para os cursos já enviados pelo DR para o SCOP e/ou Solução Integradora via sistema legado, o campo complementar Código do Curso no SCOP deve ser preenchido com o mesmo código reportado anteriormente para o SCOP e/ou Solução Integradora.

### **Dados gerais do Curso**

**Título, modalidade, ocupação, área, eixo tecnológico MEC:** Serão extraídos do cadastro de Curso.   
**Linha de ação:** O extrator irá enviar um valor fixo igual a '11'**;**   
**Nível MEC:** O extrator irá enviar um valor fixo 'Vazio'

### **Dados gerais da Matriz Curricular**

Os campos: Curso MEC, início de oferta e carga horária: fases escolar e estágio, serão extraídos da Matriz Curricular.

### **Certificações intermediarias**

* O extrator busca as seis primeiras saídas intermediarias identificadas
* O extrator trará apenas informações acerca das certificações intermediárias caso a modalidade do curso seja uma das listadas abaixo:

15 - Aprendizagem Industrial Técnica  
31 - Habilitação Técnica

# **TIPO DE RESGISTRO - MATRÍCULA**

## **G****eração / contabilização de matriculas**

### **Código da matricula**

**Matrículas iniciadas no SGE:** Código gerado pelo extrator: RA + IDFT da Primeira Turma   
**Matrículas migradas do Sistema Legado para o SGE:** Para as matriculas já enviados pelo DR para o SCOP e/ou Solução Integradora via sistema legado, o campo complementar Código da matricula no SCOP deve ser preenchido com o mesmo código reportado anteriormente para o SCOP e/ou Solução Integradora. Os alunos com as situações de matricula trancado e pendente de estágio, ao retornarem, serão reportados a Solução Integradora com o mesmo código de matricula já enviado.

### **Matrículas geradas**

* + - Para cada matricula gerada no SGE em um Curso (Curso + Matriz Curricular + Matriz Aplicada) distinto é gerado um Código de Matricula.
    - Quando o aluno faz um curso/habilitação, assume uma situação de saída (Matricula Encerrada) e retorna posteriormente para fazer o mesmo curso, matriz curricular e matriz aplicada, o extrator contabiliza este retorno como uma nova matricula. Esta verificação é feita quando o aluno retorna no mesmo período letivo ou quando ele retorna em um período letivo distinto.

**Retorno Cursos Modulares**

1. Alunos com situação de matrícula: “Aguardando Estágio”, “Pendente Estágio”, “Cancelado”, “Transferência de Curso”, “Transferência de Escola”, “Transferência Externa”,  “Desistente”, “Evadido” e “Trancado” no período letivo e que retornam com situação de "Matriculado" em outro período letivo, sendo que a data de matrícula do retorno seja maior que a data de matrícula do período letivo onde ocorreu a saída.
2. Alunos com situação de resultado: “Reprovado” no período letivo e situação de matrícula “Reprovado” no curso/habilitação, que retornam com situação de "Matriculado" em outro período letivo e situação de "Matriculado" no curso/habilitação, sendo que a data de matrícula do retorno seja maior que a data de matrícula do período letivo onde ocorreu a saída.

## **Informações gerais da matrícula**

### **Dados Básicos do Aluno -****Código do Aluno**

**Alunos migrados para o SGE de um Sistema Legado:** Para estes alunos o campo complementar 'Código do Aluno no legado' deve estar preenchido com o código do aluno no sistema legado. O extrator irá buscar o dado do campo e enviar como 'Código do Aluno'   
**Alunos cadastrados inicialmente no SGE:** Para os alunos onde o campo 'Código do Aluno no legado' estiver em branco, o extrator irá enviar o código como: SGE+UF+RA, ex: SGEPE00000125

### **Dados pessoais**

**Alunos cadastrados inicialmente no SGE:** Para os alunos onde o campo 'Código do Aluno no legado' estiver em branco, o extrator irá enviar o código como: SGE+UF+RA, ex: SGEPE00000125  
Os dados pessoais do aluno tais como: Nome, CPF, endereço, se possui ou não deficiência, dentre outros, são extraídos da tela de cadastro do aluno no SGE.

### **Responsável financeiro**

A informação será extraída do responsável financeiro do contrato vinculado a matricula do aluno. Se não tiver preenchido será enviado vazio.

### **Nome da mãe**

O extrator, para envio do registro verificará primeiro se o campo complementar do aluno Nome Mãe está preenchido com a informação:   
***Se sim***, envia o dado informado no campo  
***Se não,*** verifica se existe um registro de mãe 'pessoa' associado ao aluno   
Sempre que houver no nome da mãe a palavra 'Desconhecida' ou 'Mãe Desconhecida' será enviado para a Solução Integradora o registro como "Desconhecida"; seja no campo complementar ou no nome da pessoa.

### **Dados da Matricula do Aluno**

**Curso:** A informação referente ao Curso em que o aluno está matriculado é extraída da matricula no Curso/Habilitação

**Modalidade:** A modalidade é identificada a partir do curso que está vinculado na matricula no Curso/Habilitação do aluno.   
Se o curso estiver vinculado a modalidade 57 ou 67 será gerado como modalidade 58.

**Unidade de Atendimento:** Através do registro de habilitação filial (Filial + Matriz Aplicada) que está vinculado a matrícula do aluno é identificada a UO. Para a identificação da Unidade Operacional pela Solução Integradora é necessário que o campo 'Campo Livre 1' esteja preenchido dentro do cadastro da Filial no SGE, anexo 'Dados Fiscais'. Este código informado deve ser o mesmo cadastrado na base de ativos pelo regional. ***'Filial | Dados Fiscais | Dados Adicionais | Campo Livre 1'***

### **Tipo de Ação**

O Tipo de ação será identificado a partir do campo localizado no cadastro do curso: Presencial / Distância. Se um mesmo curso for ofertado presencial e a distância pelo DR terão que ser criados dois cadastros de cursos distintos dentro do SGE sendo um Tipo Presencial e outro A Distância.

### **Condição do Aluno em Relação ao Contrato de Aprendizagem**

**Para identificar a condição do aluno o extrator faz as seguintes verificações:**   
**1º**  Alunos pertencem a uma das modalidades 11 - Aprendizagem Industrial Básica ou 15 Aprendizagem Industrial Técnica, o extrator envia 1 - ‘Com Contrato’ quando atender as seguintes condições.

Matrizes de Aprendizagem atuais:

* Se existir matrícula no período letivo FE e aluno possuir Termo de Compromisso. A disciplina estiver com situação de “Matriculado ou “Aprovado/Reprovado” no mês de referência, os campos do Termo de Compromisso **CNPJ** ou **IE** da empresa preenchido e a **Data Início** e **Data Término** vigente no mês de referência.
* Se existir matrícula no período letivo FE e aluno não possuir termo de compromisso. A disciplina estiver com situação de “Matriculado ou “Aprovado/Reprovado” no mês de referência, os campos complementares do Curso/Habilitação **CNPJ, IE ou CEI da Empresa** preenchido**, Data Inicial do Contrato** e **Data Final do Contrato** vigente no mês de referência.
* Se não existir matrícula no período letivo FE.  Os campos complementares do Curso/Habilitação **CNPJ, IE ou CEI da Empresa** estiver preenchido**, Data Inicial do Contrato** e **Data Final do Contrato** vigente no mês de referência.

Matrizes de Aprendizagem 4.0 criadas a partir de 01/10/2020

* Se na Matriz Aplicada estiver vinculado o componente curricular “100 – Fase Empresa da Aprendizagem”;
* Se existir alunos inscritos em uma Atividade Ofertada do Componente “Fase Empresa da Aprendizagem”, com Empresa vinculada na Atividade que tenha **CNPJ, IE ou CEI da Empresa** preenchido e **Data Início e Data Fim da Inscrição na Atividade** vigente no mês de referência;
* Se o aluno não cumpriu a atividade ou se a data de conclusão da atividade for no mês de referência.

**2º**  Para os alunos que não estão matriculados no período letivo FE, não possuem no campo complementar do curso/habilitação o 'CNPJ da Empresa'  e também não estão inscritos em uma Atividade Ofertada do tipo “Fase Empresa da Aprendizagem” mas pertencem a uma das modalidades: 11 - Aprendizagem Industrial Básica ou 15 Aprendizagem Industrial Técnica, o extrator envia a condição com valor Fixo 2 - 'Sem Contrato'   
**3º -** Se não atender a nenhuma das condições acima envia Fixo 9 – 'Não se Aplica'

### **Tipo de Gratuidade / Fonte de Financiamento**

O extrator busca está informação do campo complementar 'Condição do Aluno'. Inicialmente a primeira verificação é feita no campo 'Condição do Aluno' presente na Matricula no Período Letivo, caso este campo esteja vazio o extrator verifica a informação preenchida no campo 'Condição do Aluno' na tela de cadastro da matricula no Curso/Habilitação.   
**Se valor igual a Zero (Não Gratuita),** o extrator vai enviar o valor igual a 9 (Não Gratuita segundo tabela referencial da Solução Integradora).   
**Se** **valor diferente de zero** o extrator busca o primeiro digito do código identificado no valor selecionado:

|  |  |  |
| --- | --- | --- |
| **Tipo de Financiamento** | | |
| **Código** | **Descrição** | **Código no SGE** |
| 1 | Gratuidade Regimental | 1 |
| 101 | Programa Emprega Mais (Desempregado) | 101 |
| 102 | Programa Emprega Mais (Empregado) | 102 |
| 103 | Programa Brasil Mais Produtivo | 103 |
| 2 | Gratuidade Não Regimental | 2 |
| 3 | Convênio | 3 |
| 4 | PRONATEC | 4 |
| 9 | Pago por Pessoa Física ou Empresa | 0 |
| 901 | Pago pelo SESI | 001 |
| 902 | Pago pela Rede Pública de Educação | 002 |
| 903 | Pago pela Rede Privada de Educação | 003 |
| 904 | Programa Ministério da Cidadania (SESI) | 004 |

# **MOVIMENTAÇÃO DO ALUNO**

### **Situação de matrícula do aluno**

O extrator faz a verificação da situação de matrícula do aluno no SGE, para que esta seja enviada a Solução Integradora seguindo a ordem e os critérios abaixo:

***Verifica se a Data Final da Turma é menor ou igual a mês de referência e se não existe log de movimentação para o aluno no curso/habilitação ou período letivo maior ou igual ao mês de referência.***

Cursos Modulares

Verifica se a situação de matrícula no curso/habilitação do aluno (SHABILITACAOALUNO) encontra-se como *Concluinte, Reprovado, Reconduzido - Legislação PcD ou Aluno com Pendência.*

*Verifica se a situação de matrícula na última matrícula do período letivo do aluno (SMATRICPL) encontra-se como Matriculado, Cancelado, Evadido, Transferência de Curso, Transferência de Escola, Trancado, Pendente Estágio, Desistente, Falecido, Reprovado, Reconduzido - Legislação PcD ou Transferência Externa.*

Cursos com apenas um Módulo

Verifica se a situação de matrícula no curso/habilitação do aluno (SHABILITACAOALUNO) encontra-se como *Concluinte, Reprovado, Reconduzido - Legislação PcD ou Aluno com Pendência.*

Verifica se a situação de resultado final na matrícula do período letivo do aluno (SMATRICPL) encontra-se como *Aprovado, Reprovado, Reprovado por Frequência ou Reconduzido - Legislação PcD.*

Verifica se a situação de matrícula do período letivo do aluno (SMATRICPL) encontra-se como *Matriculado, Cancelado, Evadido, Transferência de Curso, Transferência de Escola, Trancado, Pendente Estágio, Desistente, Falecido, Reprovado, Reconduzido - Legislação PcD ou Transferência Externa.*

***Se a Data Final da Turma é maior do que o mês de referência ou existe log de movimentação para o aluno no curso/habilitação ou período letivo maior ou igual ao mês de referência.***

Cursos Modulares

Verifica se a situação de matrícula no log de movimentações do curso/habilitação do aluno (SLOGHABILITACAOALUNO) encontra-se como *Concluinte, Reprovado, Reconduzido - Legislação PcD ou Aluno com Pendência.*

Verifica se a situação de matrícula no log de movimentações do período letivo do aluno (SLOGPLETIVO) encontra-se como *Matriculado, Cancelado, Evadido, Transferência de Curso, Transferência de Escola, Trancado, Pendente Estágio, Desistente, Falecido, Reprovado, Reconduzido - Legislação PcD ou Transferência Externa.*

Cursos com apenas um Módulo

Verifica se a situação de matrícula no log de movimentações do curso/habilitação do aluno (SLOGHABILITACAOALUNO) encontra-se como *Concluinte, Reprovado, Reconduzido - Legislação PcD ou Aluno com Pendência.*

***Novo!*** Verifica se a situação de resultado final no log de movimentações da matrícula do período letivo do aluno (SLOGPLETIVO) encontra-se como *Aprovado, Reprovado, Reprovado por Frequência ou Reconduzido - Legislação PcD e a situação de matrícula no curso/habilitação é diferente de Matriculado.*

Verifica se a situação de matrícula no log de movimentações do período letivo do aluno (SLOGPLETIVO) encontra-se como *Matriculado, Cancelado, Evadido, Transferência de Curso, Transferência de Escola, Trancado, Pendente Estágio, Desistente, Falecido, Reprovado, Reconduzido - Legislação PcD ou Transferência Externa.*

***Alunos que retornam para fazer o mesmo Curso/Matriz curricular***

Cursos com apenas um Módulo

Verifica se a situação de matrícula no log de movimentações da matricula na disciplina encontra-se como *Matriculado, Cancelado, Aprovado, Reprovado, Reprovado por Frequência, Reconduzido - Legislação PcD, Evadido, Transferência de Curso, Transferência de Escola, Trancado, Pendente Estágio, Desistente, Falecido ou Transferência Externa.*

Para enviar a situação o extrator identifica todas as disciplinas em que o aluno está matriculado e utiliza a regra de prioridade abaixo.

*Matriculado*

*Evadido, Transferência de Curso, Transferência de Escola, Trancado, Pendente Estágio, Desistente, Falecido ou Transferência Externa.*

*Reprovado e Reprovado por Frequência*

*Aprovado e Reconduzido - Legislação PcD*

*Cancelado*

***Novo!* Para alunos com contrato de aprendizagem e situação de matrícula Concluinte ou Reprovado.**

* SE a data de término da matrícula(regras do item ) for MENOR que a data fim do contrato de aprendizagem vigente, a situação de saída será enviada no arquivo somente no ano/mês da data fim do contrato de aprendizagem vigente.

### **Regra para aplicação dos status de matrícula** **do aluno no SGE**

**Matricula Em Andamento**   
***Matriculado:*** Este status deve ser aplicado para alunos cuja matrícula está em andamento no SGE.

**Interrupção da Matricula**   
**Cancelado:** A Matricula do aluno deve ser colocada como cancelada se a formalização da saída for feita antes de o aluno ter frequentado a primeira aula. Após o primeiro dia de aula registrado no SGE para o aluno, em caso de o aluno formalizar a interrupção do curso este, deve ser colocado como desistente.  
Aplicação no SGE***:*** A situação deverá ser aplicada manualmente na matricula do aluno.   
***Desistente:*** O Aluno deve ser colocado no SGE como desistente quando a saída dele durante o andamento do curso for formalizada.  
Aplicação no SGE***:*** A situação deverá ser aplicada manualmente na matricula do aluno.   
***Evadido:*** A situação de evadido deve ser aplicada quando os responsáveis (Professores, Coordenadores...) identificarem que o aluno não está frequentando o curso, tentaram entrar em contato e não obtiveram sucesso. A evasão é uma saída não formalizada.   
*Aplicação no SGE**:*** A situação deverá ser aplicada manualmente na matricula do aluno.   
**Falecido:** Esta situação de matricula deve ser aplicada diante do comprovante de falecimento de um aluno.   
*Aplicação no SGE**:*** A situação deverá ser aplicada manualmente na matricula do aluno.   
***Trancado:*** A situação de trancado deve ser aplicada quando o aluno formaliza uma paralização temporária da matricula em um determinado curso/matriz.   
*Aplicação no SGE:* A situação deverá ser aplicada manualmente na matricula do aluno.   
***Pendente Estágio:*** A situação de Pendente de Estágio deve ser aplicada quando o aluno finaliza toda a fase escolar, porém, para conclusão do curso, precisa fazer o estágio e este ainda não foi iniciado.   
*Aplicação no SGE:* A situação deverá ser aplicada manualmente na matrícula do aluno.

**Encerramento da Matricula**   
***Concluinte:*** O Status de concluinte deve ser aplicado quando o aluno é aprovado em todas as Disciplinas do curso e está apto a receber o certificado/diploma de conclusão.  
*Aplicação no SGE**:*** A situação deverá ser aplicada via fórmula de apuração de resultados a não ser em casos e exceção.   
***Reprovado:*** O status de Reprovado é colocado no SGE quando o aluno finaliza o curso com alguma pendência.  
*Aplicação no SGE**:*** A situação deverá ser aplicada via fórmula de apuração de resultados a não ser em casos e exceção.   
***Reconduzido Legislação PCD:*** O status de Reconduzido Legislação PCD deve ser aplicado em casos onde o aluno portador de deficiência, não consegue atingir as competências necessárias para sua aprovação em um determinado curso.   
Aplicação no SGE: A situação deverá ser aplicada na matricula do aluno na disciplina que ele não conseguiu concluir, no resultado final da matrícula no período letivo e no curso/habilitação.

**Transferências**   
***Transferência de Curso:*** A transferência de curso deve ser aplicada quando o aluno muda de Curso ou Matriz Curricular.   
Aplicação no SGE: Esta alteração deve ser feita manualmente na matrícula do aluno (criar um curso habilitação novo e matricular o aluno no período letivo); não deve ser executado nenhum processo. Na matrícula de origem o status deverá ficar como Transferência de Curso e na de destino como matriculado.   
***Transferência de Escola:*** A transferência de Escola deve ser aplicada quando o aluno muda de uma Unidade/Filial para outra:   
Aplicação no SGE: A transferência deve ser executada pelo processo de Transferência Interna indicando o status do aluno na matrícula / unidade de origem como Transferência de Escola e na Matrícula / Unidade de destino como matriculado.   
***Transferência Externa:*** Esta situação de matrícula deve ser aplicada quando o aluno formaliza a saída, informando que dará continuidade ao curso em outra instituição de ensino ou no SENAI, porém, em outro Departamento Regional.   
Aplicação no SGE: Esta alteração deve ser feita manualmente na matrícula do aluno, apenas alterando o status de matriculado para transferência externa. Não deve ser gerado um novo registro de matrícula para o aluno no SGE.   
***Transferência de Turma:*** A transferência de turma deve ser aplicada quando o aluno muda de turma ou de turno no SGE.  
*Aplicação no SGE:* A Transferência de Turma deve ser realizado no SGE pelo processo de Mudança de Turma indicando na turma de origem o status Transferência de Turma e na turma de destino o status Matriculado. Na matrícula do aluno no Período Letivo/Modulo apenas a turma irá mudar, o status permanecera como matriculado.   
***Importante: A Transferência de turma não é entendida pela solução integradora com um status de movimentação do aluno (saída). Para a Solução Integradora permanece sendo enviada uma única matricula com status 'em andamento'.***   
\*As situações de matrícula aplicados exclusivamente a matriculas em disciplinas não foram listadas.

### **Tipo de Entrada**

1. **Nova:** As matriculas do aluno quando enviadas para a Solução Integradora serão identificadas com Tipo de Entrada igual a 'Nova' com exceção do aluno que retorna à instituição após ter trancado o curso e aqueles que entram por meio de transferência.
2. **Por Transferência:** Quando o aluno solicita transferência de escola ao ingressar no curso em uma nova Unidade Operacional, o mesmo é enviado para a Solução Integradora com Tipo de Entrada igual a Por Transferência. O tipo de ingresso do aluno no novo Curso/Habilitação deve ser igual a 'Transferência'.
3. **Por Destrancamento:** O aluno solicita o trancamento do curso e retorna após um período. Ao retornar o aluno é enviado para a Solução Integradora com Tipo de Entrada igual a Por Destrancamento e a situação da matricula como 'em andamento'. No SGE o motivo de alteração da situação de matricula quando o aluno retorna deve ser igual a 'Destrancamento' e situação alterada de 'trancado' para 'matriculado'
4. **Reconduzido PCD:** Quando o aluno for PCD e ingressar no curso buscando uma certificação compatível com suas competências.
5. **Marketplace DN:** Preenchimento automático quando utilizar a customização MarketPlace e estiver definido nos parâmetros da customização o Tipo de Ingresso igual a ‘Marketplace DN’.

### **Data de início da matrícula**

No SGE existem quatro cenários distintos avaliados pelo extrator para determinar de qual campo irá buscar a 'Data de Início da Matrícula:   
A matricula da primeira turma com ingresso anterior a 31/12/2019 será enviado a data de início da primeira turma e matriculas posteriores a 01/01/2020 serão seguidas as regras abaixo:   
**Cursos com mais de um Módulo*:***

* Se a data de matricula for anterior a de início da turma –> Considerar a data de início da turma
* Se a data de matricula for igual ou posterior a data de início da turma – > Considerar a data de matricula do aluno da 'primeira matricula no período letivo'.

**Cursos com Apenas um Modulo:**

* Se a data de matricula for anterior a de início da turma –> Considerar a data de início da turma
* Se a data de matricula for igual ou posterior a data de início da turma – Considerar a data de matricula do aluno da matricula no período letivo.

**Matriculas de retorno para o mesmo curso:**

* Se a data de matricula na disciplina for anterior a de início da turma –> Considerar a data de início da turma
* Se a data de matricula na disciplina for igual ou posterior a data de início da turma – > Considerar a menor data de matricula na disciplina.

**Matriculas com origem no sistema legado:** Para as matriculas trazidas do sistema legado para o SGE ***com** **Aproveitamento de Estudos das disciplinas cursadas na primeira turma*** a 'Data de Início da Matricula' será extraída do campo 'Data de Ingresso' do Curso/Habilitação do aluno. Para a identificação destas matriculas é obrigatório o preenchimento do campo Tipo de Ingresso localizado na matricula no curso/habilitação. O tipo informado deve ser 'Legado'   
**Matrículas por Transferência:** Para matrículas geradas a partir de uma transferência de curso ou de escola a 'Data de Início da Matricula' será extraída do campo 'Data de Ingresso' do Curso/Habilitação do aluno. Para identificação destas matrículas é obrigatório o preenchimento do campo Tipo de Ingresso localizado na matrícula no curso/habilitação. O tipo informado deve ser 'Transferência'.

### **Data de término previsto**

**Término previsto:** Este dado será extraído do campo 'Data de Previsão de Saída' localizado no cadastro da matricula de Curso/Habilitação do aluno.

### **DataTerminoData de saída da matrícula / Atualização da Situação**

Com relação ao envio da data de saída temos as seguintes tratativas:  
   
**Data de saída enviada em branco (vazia):**

* + Alunos no SGE com situação de matrícula no SGE igual a Matriculado.

**Data de Saída igual a data fim da última turma/disciplina do aluno no curso.**

* ***Cursos com mais de um módulo (Presencial):***
  + Aluno com Situação de Matrícula no Curso Habilitação igual a **Concluinte**.
  + Aluno com Situação de Matrícula no Curso Habilitação igual a **Reprovado**.
  + Aluno com Situação de Matrícula no Curso Habilitação igual a **Reconduzido Legislação PCD**

* ***Novo! Cursos com apenas um módulo (Presencial) e a situação de matrícula no curso/habilitação é diferente de Matriculado:***
  + Aluno com Resultado Final na Matricula no período letivo igual a **Aprovado**
  + Aluno com Resultado Final na Matrícula no período letivo igual a **Reprovado**.
  + Aluno com Resultado Final na Matrícula no período letivo igual a **Reconduzido Legislação PCD**

* ***Alunos que retornam para fazer o mesmo Curso/Matriz curricular – Curso com apenas um módulo (Presencial):***
  + Aluno com Resultado Final na Matrícula na Disciplina igual a **Aprovado**
  + Aluno com Resultado Final na Matrícula na Disciplina igual a **Reprovado**.
  + Aluno com Resultado Final na Matrícula na Disciplina igual a **Reconduzido Legislação PCD**

**Data de Saída igual a data em que a operação (atualização de status) foi executada no sistema.**

* ***Cursos com mais de um módulo (A Distância):***
  + Aluno com Situação de Matrícula no Curso Habilitação igual a **Concluinte**.
  + Aluno com Situação de Matrícula no Curso Habilitação igual a **Reprovado**.
  + Aluno com Situação de Matrícula no Curso Habilitação igual a **Reconduzido Legislação PCD**

* ***Novo! Cursos com apenas um módulo (A Distância) e a situação de matrícula no curso/habilitação é diferente de Matriculado:***
  + Aluno com Resultado Final na Matrícula no período letivo igual a **Aprovado**
  + Aluno com Resultado Final na Matrícula no período letivo igual a **Reprovado**.
  + Aluno com Resultado Final na Matrícula no período letivo igual a **Reconduzido Legislação PCD**

* ***Alunos que retornam para fazer o mesmo Curso/Matriz curricular – Curso com apenas um módulo*** ***(A Distância):***
  + Aluno com Resultado Final na Matrícula na Disciplina igual a **Aprovado**
  + Aluno com Resultado Final na Matrícula na Disciplina igual a **Reprovado**
  + Aluno com Resultado Final na Matrícula na Disciplina igual a **Reconduzido Legislação PCD**

* ***Cursos com mais de um módulo (Presencial e a distância):***
  + Aluno com Situação de Matrícula no Curso Habilitação igual a **Aluno com Pendência**

* ***Cursos com um ou mais módulos (Presencial e a distância):***
  + Alunos com Situação de Matrícula no período letivo igual a **Desistente**,
  + Alunos com Situação de Matrícula no período letivo igual a **Evadido**
  + Alunos com Situação de Matrícula no período letivo igual a **Falecido**
  + Alunos com Situação de Matrícula no período letivo igual a **Pendente de Estágio**
  + Alunos com Situação de Matrícula no período letivo igual a **Trancado**
  + Alunos com Situação de Matrícula no período letivo igual a **Transferência de Curso**
  + Alunos com Situação de Matrícula no período letivo igual a **Transferência de Escola**
  + Alunos com Situação de Matrícula no período letivo igual a **Transferência Externa.**

* ***Alunos que retornam para fazer o mesmo Curso/Matriz curricular – Curso com apenas um módulo*** ***(Presencia e a distância):***
  + Alunos com Situação de Matrícula na Disciplina igual a **Desistente**,
  + Alunos com Situação de Matrícula na Disciplina igual a **Evadido**
  + Alunos com Situação de Matrícula na Disciplina igual a **Falecido**
  + Alunos com Situação de Matrícula na Disciplina igual a **Pendente de Estágio**
  + Alunos com Situação de Matrícula na Disciplina igual a **Trancado**
  + Alunos com Situação de Matrícula na Disciplina igual a **Transferência de Curso**
  + Alunos com Situação de Matrícula na Disciplina igual a **Transferência de Escola**
  + Alunos com Situação de Matrícula na Disciplina igual a **Transferência Externa.**

\*As regras citadas, referentes a alunos que retornam para fazer o mesmo curso/matriz curricular fazem referência a alunos que retornam no mesmo período letivo ou em um período letivo diferente do primeiro cursado pelo aluno.

***Novo!* Data de Saída igual a data de término do contrato de aprendizagem.**

Para alunos com contrato de aprendizagem e situação de matrícula Concluinte ou Reprovado.

* SE a data de término da matrícula(regras do item )  for MAIOR OU IGUAL que a data fim do contrato de aprendizagem vigente no ano/mês informado na execução do extrator, envia como data de término da matrícula conforme as regras do item .
* SE a data de término da matrícula (regras do item ) for MENOR que a data fim do contrato de aprendizagem vigente, envia a data fim do contrato de aprendizagem vigente no ano/mês informado na execução do extrator. A data de saída será enviada no arquivo somente no ano/mês da data fim do contrato de aprendizagem vigente.

# **TIPO DE REGISTRO - CARGA HORÁRIA**

### **Carga horária escolar cursada:**

**Para turmas/disciplinas com data anterior a 01/08/2018**

* A carga horária cursada pelo aluno dentro do SGE é extraída a partir dos planos de aula gerados para as turmas/disciplinas que o aluno está matriculado. É feita a soma dos planos de aula gerados até o último dia do mês de referência. As faltas são abatidas do valor total de horas.

**Para turmas/disciplinas com data igual ou posterior a 01/08/2018**

* O extrator irá verificar se a turma/disciplina é presencial, a distância ou semipresencial (STURMADISC.TIPO)

**Tipo Presencial:**   
O extrator soma as horas executadas (plano de aula) e subtrai as faltas lançadas para o aluno   
**Tipo Semipresencial**:   
**Aluno/Hora, carga horária presencial:** O extrator soma as horas executadas (plano de aula) e subtrai as faltas lançadas para o aluno**.**   
**Aluno/Hora, carga horária à distância:** O extrator identifica a quantidade de horas a distância da disciplina, a partir do percentual informado no campo 'Percentual de aulas não presenciais' que fica na tela de Disciplinas da Matriz Curricular.   
O envio do aluno/hora correspondente a carga horária EAD (% a distância) será dividido entre no 1º mês e o último mês de execução da turma/disciplina. Metade da carga horária a distância da disciplina será enviada no primeiro mês e a outra metade no último mês da turma/disciplina.   
Se o mês da matricula do aluno na turma/disciplina for maior que o mês de início da turma/disciplina, enviar a "primeira metade" da Carga Horária à distância no mês da matricula do aluno na turma/disciplina.   
Se a matricula do aluno for em um mês anterior ou igual ao do início da Turma/Disciplinas enviar a 'primeira metade' da carga horária no primeiro mês da turma/disciplina   
**Tipo A distância (100% EAD):**   
O extrator enviará a carga horária total da disciplina sendo metade no primeiro mês de execução da turma/disciplina e o restante no mês correspondente a conclusão da matrícula do aluno na DISCIPLINA. Esta data corresponde ao dia/mês em que a situação de matrícula no aluno na disciplina foi alterada para um status de conclusão.   
Se o mês da matricula do aluno na turma/disciplina for maior que o mês de início da turma/disciplina, enviar a "primeira metade" da Carga Horária à distância no mês da matricula do aluno na turma/disciplina.  
Se a matricula do aluno for em um mês anterior ou igual ao do início da Turma/Disciplinas enviar a 'primeira metade' da carga horária no primeiro mês da turma/disciplina   
***Importante: Se o campo 'Tipo de Turma' não estiver preenchido no cadastro da turma/disciplina o extrator irá considerar a informação preenchida no campo 'Presencial/Distância' do cadastro do curso.***

* Para os alunos sem carga horária no período deverá ser enviado o valor igual a Zero.

### **Carga horária Estágio**

* Carga Horária Estágio: O valor da carga horária de estágio executada corresponde ao somatório dos planos de aula associados a turma/disciplina cuja disciplina está marcada como 'exclusiva de estágio'.

# **TIPO DE REGISTRO - CONTRATO DE APRENDIZAGEM**

Este registro somente será preenchido para alunos dos cursos da Modalidade Aprendizagem e que atenderem a umas das situações abaixo:

Matrizes de Aprendizagem Atuais

* Se existir matrícula no período letivo FE e aluno possuir Termo de Compromisso. A disciplina deve estar com situação de “Matriculado ou “Aprovado/Reprovado” no mês de referência, os campos do Termo de Compromisso **CNPJ** ou **IE** da empresa preenchido e a **Data Início** e **Data Término** vigente no mês de referência.
* Se existir matrícula no período letivo FE e aluno não possuir termo de compromisso. A disciplina deve estar com situação de “Matriculado ou “Aprovado/Reprovado” no mês de referência, os campos complementares do Curso/Habilitação **CNPJ, IE ou CEI da Empresa** preenchido**, Data Inicial do Contrato** e **Data Final do Contrato** vigente no mês de referência.
* Se não existir matrícula no período letivo FE. Os campos complementares do Curso/Habilitação **CNPJ, IE ou CEI da Empresa** preenchido**, Data Inicial do Contrato** e **Data Final do Contrato** vigente no mês de referência.

Nesta situação é necessário informar a Carga Horária Contratada no campo complementar do Curso/Habilitação para não gerar crítica na importação do arquivo na Solução Integradora.

Matrizes de Aprendizagem 4.0 criadas a partir de 01/10/2020

* Se na Matriz Aplicada estiver vinculado o componente curricular “100 – Fase Empresa da Aprendizagem”;
* Se existir alunos inscritos em uma Atividade Ofertada do Componente “Fase Empresa da Aprendizagem”, com Empresa vinculada na Atividade que tenha **CNPJ, IE ou CEI da Empresa** preenchido e **Data Início e Data Fim da Inscrição na Atividade** vigente no mês de referência;
* Se o aluno não cumpriu a atividade ou se a data de conclusão da atividade for no mês de referência.

### **Empresa Contratante:**

Para os alunos com "Contrato de Aprendizagem" a informação será extraída de 2 formas, de acordo com a Matriz Curricular:

Matrizes de Aprendizagem Atuais:

A informação será extraída do termo de compromisso de estágio ou do campo complementar “CNPJ, Inscrição Estadual ou CEI da Empresa” localizado na matricula no curso/habilitação.

A verificação no SGE seguirá os seguintes critérios:

**1º** Ao identificar a matricula do aluno no período letivo \_\_FE o extrator irá verificar se existe ‘termo de compromisso de estágio’ vinculado a turma/disciplina em que o aluno está matriculado. Ao identificar o ‘Termo de Compromisso de Estágio’ o extrator irá buscar o CNPJ ou Inscrição Estadual da empresa vinculada e enviar a Solução Integradora.   
**2º** Caso o termo de compromisso de estágio não seja identificado o extrator irá verificar se o campo CNPJ, Inscrição Estadual ou CEI da empresa possui alguma informação. Se o dado for identificado no campo, o mesmo é enviado como CNPJ, Inscrição Estadual ou CEI da empresa responsável pelo contrato de aprendizagem.

Importante

1. Caso preencham o Termo de Compromisso não podem preencher os Campos Complementares do curso/habilitação referente ao Contrato de Aprendizagem, e vice-versa.
2. O campo UF da Inscrição Estadual somente existe na Empresa do Termo de Compromisso, mas quando for preenchido o campo complementar da empresa como Inscrição Estadual será extraído a UF da Filial que o aluno está matriculado.
3. A informação de CEI da empresa está presente apenas nos campos complementares.
4. Caso o aluno tenha 2(dois) contratos de empresas diferentes no mesmo mês será enviado 2 linhas do registro 4, desde que a data inicial do último contrato seja posterior a data fim do contrato anterior. Esta situação somente será possível pelo Termo de Compromisso de Estágio e as disciplinas de pratica profissional vinculadas ao Termo terão que compreender o período dos contratos. Nos campos complementares de Empresa será sempre enviado um único registro.

Matrizes de Aprendizagem 4.0 criadas a partir de 01/10/2020

A informação será extraída do CNPJ, Inscrição Estadual ou CEI da Empresa vinculada na Atividade Ofertada que o aluno estiver inscrito.

Caso o aluno tenha 2(dois) contratos de empresas diferentes no mesmo mês será enviado 2 linhas do registro 4, desde que a data inicial do último contrato seja posterior a data fim do contrato anterior. Esta situação somente será possível ocorrer quando o 1º contrato for rescindo e o aluno fizer contrato com outra empresa para as horas restantes da Fase Empresa da Aprendizagem.

Caso os 2(dois) contratos de empresas diferentes sejam de duração de meses diferentes, será enviado o contrato que estiver vigente assim que o primeiro contrato finalizar, passará a ser enviado o próximo contrato vigente.

A rescisão do contrato deve ser registrada no mês que ocorreu a rescisão para que tenha o reflexo correto na Solução Integrada.

### **Carga horária Fase Empresa de Aprendizagem**

* **Carga Horária executada:** **Somente para as Matrizes da Aprendizagem Atuais -** O valor da carga horária executada corresponde ao somatório dos planos de aula considerando a turma/disciplina que está vinculada ao período letivo FE. O primeiro plano de aula gerada para a Turma/Disciplina do aluno no mês de referência até o plano de aula com data menor ou igual ao último dia do mês de referência para envio da produção.

Para as Matrizes de Aprendizagem 4.0 criadas a partir de 01/10/2020 não será enviado Carga Horaria executada.

* **Carga Horária Contratada:**

**Para as Matrizes da Aprendizagem Atuais:**

O valor da carga horária contratada corresponde a quantidade de horas informadas no campo 'Carga horaria de estágio' na tela de cadastro de disciplina do tipo Exclusiva de Estágio da turma/disciplina que está vinculada na matricula do período letivo FE **OU** quando o curso não possuir a disciplina de pratica profissional irá enviar a "Carga Horaria Contratada" do campo complementar do curso/habilitação do aluno desde que tenha o campo complementar CNPJ, CEI ou Inscrição Estadual da Empresa Atendida preenchido.

Para os alunos com matrícula no período letivo FE e sem termo de compromisso, caso a carga horária da fase empresa seja dividida em várias disciplinas na matriz curricular é necessário preencher o campo "**Total**" com as horas reais da disciplina e o campo "**Estágio**" com as horas totais da fase empresa, desta forma o campo "**Estágio**" deve ser igual em todas as disciplinas da matriz.

**Para as Matrizes de Aprendizagem 4.0 criadas a partir de 01/10/2020:**

O valor da carga horária contratada será extraído da inscrição do aluno na Atividade Ofertada “Fase Empresa da Aprendizagem do campo “Carga Horaria aproveitada”.

A apuração de resultados e certificação do aluno, deve ser executada obrigatoriamente até o último dia do mês posterior ao mês de encerramento da turma.   
De acordo com a crítica 2807 a data de saída do aluno (data final da turma) deve pertencer ao mês de referência da carga ou ao mês imediatamente anterior e a data de saída poderá ser enviada apenas quando a situação do aluno for diferente de 'em andamento' (Matriculado)

# **ORIGEM DOS DADOS**

Abaixo segue o detalhamento dos campos / tabelas do SGE dos quais os dados serão extraídos.   
Em caso de necessidade de alteração dos campos/tabelas de onde a informação é extraída do SGE por motivo de correção, o ajuste do extrator será feito pela TOTVS e a documentação atualizada.   
Para os casos onde a necessidade de ajuste for em decorrência de alteração na regra de negócio, a demanda será considerada como alteração de escopo.

1horizontal1Cursoshorizontal

### **Registro Cursos**

1. **Nome do Campo:** Tipo do Registro  
**Campo Fixo:** 1  
**Numérico**

2. **Nome do Campo:** Operação de Transação  
**Campo Registro:** “”

3. **Nome do Campo:** Código do Curso  
**Campo Registro:** SGRADECOMPL.CODCURSOSCOP. Se não tiver preenchido: SCURSO.IDFT + SGRADE.IDFT  
**Tamanho:** 20

4. **Nome do Campo:** Nome do Curso  
**Campo Registro:** Verifica SCURSO.COMPLEMENTO, se vazio, busca informação do campo SCURSO.NOME  
**Tamanho:** 100

5. **Nome do Campo:** Linha de Ação  
**Numérico**  
VALOR FIXO = 11

6. **Nome do Campo:** Modalidade  
**Tabela:** SCURSO.CODMODALIDADECURSO  
**Numérico**

7. **Nome do Campo:** Área de Atuação  
**Tabela:** SAREA.CODAREA  
**Numérico**

8. **Nome do Campo:** Código do Eixo Tecnológico MEC  
**Tabela:** SEIXOTECNOLOGICO.CODEIXOTECNOLOGICO  
**Numérico**

9. **Nome do Campo:** Código do Curso MEC – SISTEC  
**Tabela:** SGRADECOMPL.CURSOMEC \*\*Tabela Dinâmica \*\*  
**Numérico**

10. **Nome do Campo:** Nível do Curso MEC  
**Numérico**  
VALOR FIXO - VAZIO

11. **Nome do Campo:** Ocupação (CBO)  
**Tabela:** SCURSOCOMPL.CBO\_SI \*\*Tabela Dinâmica \*\*  
**Numérico**

12. **Nome do Campo:** Carga Horária – Presencial  
**Tabela:** SGRADECOMPL.CHESCOLAR  
**Numérico**

13. **Nome do Campo:** Carga Horária – Estágio  
**Tabela:** SGRADECOMPL.CHESTAGIO  
**Numérico**

14. **Nome do Campo:** Inicio da Oferta  
**Tabela:** SGRADE.DTINICIO  
**Data**

15. **Nome do Campo:** Término da Oferta  
Fixo campo vazio: “”  
**Data**

16. **Nome do Campo:** Certificação Intermediária 1  
**Tabela:** SCOMPETENCIAGRADE.CODCOMPETENCIA  
(Descrito na regra: Certificações Intermediárias, pág. 6)

17. **Nome do Campo:** Certificação Intermediária 2  
**Tabela:** SCOMPETENCIAGRADE.CODCOMPETENCIA  
(Descrito na regra: Certificações Intermediárias, pág. 6)

18. **Nome do Campo:** Certificação Intermediária 3  
**Tabela:** SCOMPETENCIAGRADE.CODCOMPETENCIA  
(Descrito na regra: Certificações Intermediárias, pág. 6)

19. **Nome do Campo:** Certificação Intermediária 4  
**Tabela:** SCOMPETENCIAGRADE.CODCOMPETENCIA  
(Descrito na regra: Certificações Intermediárias, pág. 6)

20. **Nome do Campo:** Certificação Intermediária 5  
**Tabela:** SCOMPETENCIAGRADE.CODCOMPETENCIA  
(Descrito na regra: Certificações Intermediárias, pág. 6)

21. **Nome do Campo:** Certificação Intermediária 6  
**Tabela:** SCOMPETENCIAGRADE.CODCOMPETENCIA  
(Descrito na regra: Certificações Intermediárias, pág. 6)

22. **Nome do Campo:** Carga Horária – À Distância  
**Tabela:** SGRADECOMPL.CHEAD  
**Numérico**

23. **Nome do Campo:** Código Curso Catálogo  
**Tabela:** ZPARAMNSTABREFCURSO.CODCURSOCATALAGO  
**Numérico**

2Matrículashorizontal

### **Registro Matrículas**

1. **Nome do Campo:** Tipo do Registro  
**Campo Fixo:** 2  
**Numérico**

2. **Nome do Campo:** Operação de Transação  
**Campo:** “”

3. **Nome do Campo:** Código da Matrícula  
**Campo:** SHABILITACAOALUNOCOMPL.CODMATRICULASCOP. Se não preenchido envia: SHABILITACAOALUNO.RA + STURMA.IDFT  
**Texto(20)**

4. **Nome do Campo:** Código da Unidade Atendimento  
**Campo:** DFILIAL.CAMPOLIVRE1  
**Numérico**

5. **Nome do Campo:** Código do Curso  
**Campo:** SGRADECOMPL.CODCURSOSCOP. Se não preenchido envia: SCURSO.IDFT + SGRADE.IDFT  
**Tamanho:** Texto (20)

6. **Nome do Campo:** Tipo de Ação  
**Campo:** Se SCURSO.CURPRESDIST = ‘D’ ENTÃO “2” senão “1”

7. **Nome do Campo:** Tipo de Ambiente  
**Campo:** SCAMPUS.CODCAMPUS (Vinculado ao Curso/Habilitação)

8. **Nome do Campo:** Data de entrada da matrícula  
**Tabela:** STURMA.DATAINICIAL (Primeira Turma), se matricula migrada do legado SHABILITACAOALUNO.DTINGRESSO  
**Tamanho:** 08

9. **Nome do Campo:** Data de Saída Prevista da Matricula  
**Tabela:** SHABILITACAOALUNOCOMPL.DATAPREVISTASAIDA  
**Tamanho:** 08

10. **Nome do Campo:** Data de Término Real da Matrícula  
(Descrito na regra: Data de Saída da Matrícula, pág.12)

11. **Nome do Campo:** Código do Município de Execução da Ação  
**Tabela:** ZSIMUNICIPIO.SCOP\_COD\_MUNICIPIO  
**Tamanho:** 06

12. **Nome do Campo:** Código do Aluno  
**Tabela:** SALUNOCOMPL.CODALUNOSCOP. Se não tiver preenchido envia: SGE+GFILIAL.ESTADO+SALUNO.RA  
**Texto(20)**

13. **Nome do Campo:** Situação de Matrícula  
(Descrito na regra: Situação de Matrícula do aluno, pág. 11)  
Tabela:

**Nível de Ensino: Educação Profissional**

|  |  |  |  |
| --- | --- | --- | --- |
| **CÓDIGO SGE** | **DESCRICAO SGE** | **CÓDIGO SI** | **DESCRIÇÃO SI** |
| 2 | Matriculado | 1 | Em Andamento |
| 4 | Concluinte | 2 | Concluída |
| 7 | Aprovado | 2 | Concluída |
| 16 | Evadido | 4 | Evadido |
| 11 | Transferência de Curso | 5 | Transferida - Interna |
| 12 | Transferência de Escola | 5 | Transferida - Interna |
| 14 | Trancado | 6 | Trancada |
| 18 | Pendente Estágio | 7 | Pendente de Estágio |
| 15 | Desistente | 8 | Aluno Desistente |
| 40 | Falecido | 9 | Aluno Falecido |
| 10 | Reprovado | 10 | Aluno Reprovado |
| 38 | Transferência Externa | 11 | Transferida - Externa |
| 70 | Aluno com Pendência | 6 | Trancado |
| 45 | Reconduzido Legislação PCD | 31 | Reconduzido Legislação PCD |

**Nível de Ensino: Ensino Superior**

|  |  |  |  |
| --- | --- | --- | --- |
| **CÓDIGO SGE** | **DESCRICAO SGE** | **CÓDIGO SI** | **DESCRIÇÃO SI** |
| 20 | Matriculado | 1 | Em Andamento |
| 22 | Concluinte | 2 | Concluída |
| 25 | Aprovado | 2 | Concluída |
| 34 | Evadido | 4 | Evadido |
| 29 | Transferência de Curso | 5 | Transferida - Interna |
| 30 | Transferência de Escola | 5 | Transferida - Interna |
| 32 | Trancado | 6 | Trancada |
| 36 | Pendente Estágio | 7 | Pendente de Estágio |
| 33 | Desistente | 8 | Aluno Desistente |
| 44 | Falecido | 9 | Aluno Falecido |
| 28 | Reprovado | 10 | Aluno Reprovado |
| 42 | Transferência Externa | 11 | Transferida – Externa |
| 71 | Aluno com Pendência | 6 | Trancado |

**Numérico**

14. **Nome do Campo:** Tipo de Entrada da Matrícula  
**Tabela:** CASE WHEN SMOTIVOALTMAT.DESCRICAO LIKE '%DESTRANCAMENTO%' THEN 3  
WHEN STIPOINGRESSO.DESCRICAO LIKE '%TRANSFERENCIA%' THEN 2  
ELSE 1  
**Obs:** Criar de-para conforme no layout. 1 para nova, 2 para transferência, 3 destrancamento  
Numérico

15.**Nome do Campo:** Condição do Aluno no Ato da Matrícula  
(Descrito na regra: Condição do aluno em relação ao contrato de aprendizagem, pág. 9)

16. **Nome do Campo:** Articulação SENAI/SESI  
**Tabela:** SMATRICPLCOMPL.ARTICULACAO \*\*Tabela Dinâmica\*\*  
**SE 1 = S SE 2 = N Caso seja ARTICULACAO = 3 ENVIA N**

17. **Nome do Campo:** Tipo de Gratuidade / Fonte de Financiamento  
**Tabela:** SMATRICPLCOMPL.TIPOGRAT \*\*Tabela Dinâmica\*\*  
(Descrito na regra: Tipo de Gratuidade / Fonte de Financiamento, pág. 9)

18. **Nome do Campo:** Tipo de Escola de Origem do Aluno  
**Tabela:** SALUNOCOMPL.TIPOESCOLA \*\*Tabela Dinâmica \*\*

19. **Nome do Campo:** Tipo de vínculo com o Pronatec  
**Tabela:** SMATRICPLCOMPL.TIPOGRAT  
**Regra:** Buscar os dois últimos caracteres da Condição do aluno em relação ao tipo de gratuidade / fonte de financiamento  
Numérico

20. **Nome do Campo:** Certificação Intermediária 1  
**Tabela:** SCOMPETENCIA.CODCOMPETENCIA  
**Numérico**  
(Descrito na regra: Certificações Intermediárias, pág. 6)

21. **Nome do Campo:** Certificação Intermediária 2  
**Tabela:** SCOMPETENCIA.CODCOMPETENCIA  
**Numérico**  
(Descrito na regra: Certificações Intermediárias, pág. 6)

22. **Nome do Campo:** Certificação Intermediária 3  
**Tabela:** SCOMPETENCIA.CODCOMPETENCIA  
**Numérico**  
(Descrito na regra: Certificações Intermediárias, pág. 6)

23. **Nome do Campo:** Certificação Intermediária 4  
**Tabela:** SCOMPETENCIA.CODCOMPETENCIA  
**Numérico**  
(Descrito na regra: Certificações Intermediárias, pág. 6)

24. **Nome do Campo:** Certificação Intermediária 5  
**Tabela:** SCOMPETENCIA.CODCOMPETENCIA  
**Numérico**  
(Descrito na regra: Certificações Intermediárias, pág. 6)

25. **Nome do Campo:** Certificação Intermediária 6  
**Tabela:** SCOMPETENCIA.CODCOMPETENCIA  
**Numérico**  
(Descrito na regra: Certificações Intermediárias, pág. 6)

26. **Nome do Campo:** Grupos Vulneráveis (Motivo de Falta de CPF)  
**Tabela:** SALUNOCOMPL.MOTIVOCPF \*\* Tabela Dinâmica \*\*  
**Tamanho:** 02

27. **Nome do Campo:** CPF  
**Tabela:** PPESSOA.CPF

28. **Nome do Campo:** Nome do aluno  
**Tabela:** PPESSOA.NOME  
**Texto (80)**

29. **Nome do Campo:** Data de Nascimento  
**Tabela:** PPESSOA.DTNASCIMENTO  
**Data**

30. **Nome do Campo:** Nome da Mãe  
Tabela: Busca do campo SALUNOCOMPL.NOMEMAE, se estiver vazio busca do campo PPESSOA.NOME (SPESSOA.CODPESSOAMAE)  
**Texto (80)**

31. **Nome do Campo:** Nome do Responsável  
**Tabela:** PPESSOA.NOME (Responsável Acadêmico)  
**VALOR FIXO** - VAZIO

32. **Nome do Campo:** Nome do Pai  
**Tabela:** \*\*  
**VALOR FIXO** - VAZIO

33. **Nome do Campo:** Identidade Número  
**Tabela:** \*\*  
**VALOR FIXO** - VAZIO

34. **Nome do Campo:** Identidade Órgão Emissor  
**Tabela:** \*\*  
**VALOR FIXO** - VAZIO

35. **Nome do Campo:** Identidade Data de emissão  
**Tabela:** \*\*  
**VALOR FIXO** - VAZIO

36. **Nome do Campo:** PIS/PASEP  
**Tabela:** \*\*  
**VALOR FIXO** - VAZIO

37. **Nome do Campo:** Sexo  
**Tabela:** PPESSOA.SEXO De-Para (M=1, F=2)

38. **Nome do Campo:** Raça  
**Tabela:** PPESSOA.CORRACA De-Para (0=5, 2=1, 4=2, 6=4, 8=3)  
**Numérico**  
CASE  
WHEN PPESSOA.CORRACA = 2 THEN '1'  
WHEN PPESSOA.CORRACA = 4 THEN '2'  
WHEN PPESSOA.CORRACA = 8 THEN '3'  
WHEN PPESSOA.CORRACA = 6 THEN '4'  
WHEN PPESSOA.CORRACA = 0 THEN '5'  
WHEN PPESSOA.CORRACA = 10 THEN '6'  
ELSE '6'

39. **Nome do Campo:** País de Nacionalidade do aluno  
**Tabela:** ZSIPAIS.CODIGO  
**Texto(02)**

40. **Nome do Campo:** Código do Município  
**VALOR FIXO** - zero

41. **Nome do Campo:** Estado Civil do Aluno  
**Tabela:** PPESSOA.ESTADOCIVIL  
**VALOR FIXO** - ZERO

42. **Nome do Campo:** Nível de escolaridade  
**Tabela:** PPESSOA.GRAUINSTRUCAO  
**Numérico**

43. **Nome do Campo:** Situação Ocupacional  
**Tabela:** SALUNOCOMPL.SITUACAOOCUP \*\*Tabela Dinâmica \*\*  
**Tamanho:** 01

44. **Nome do Campo:** Necessidade Especial  
**Tabela:** Buscar deficiência do cadastro do Aluno

45. **Nome do Campo:** Endereço do aluno  
**Tabela:** PPESSOA.RUA  
**Texto(120)**

46. **Nome do Campo:** Número do Endereço  
**Tabela:** PPESSOA.NUMERO  
**Texto(20)**

47. **Nome do Campo:** Complemento do Endereço  
**Tabela:** PPESSOA.COMPLEMENTO  
**Texto(100)**

48. **Nome do Campo:** Bairro/Distrito  
**Tabela:** PPESSOA.BAIRRO  
**Texto(20)**

49. **Nome do Campo:** Município  
**Tabela:** PPESSOA.CIDADE  
**Texto(32)**

50. **Nome do Campo:** Unidade da Federação  
**Tabela:** PPESSOA.ESTADO  
**Texto(2)**

51. **Nome do Campo:** CEP  
**Tabela:** PPESSOA.CEP  
**Texto(8)**

52. **Nome do Campo:** DDD do Tel  
**Tabela:** LEFT(PPESSOA.TELEFONE1,2)  
**Numérico**

53. **Nome do Campo:** Telefone do Aluno  
**Tabela:** PPESSOA.TELEFONE1  
**Numérico**

54. **Nome do Campo:** DDD do Celular  
**Tabela:** LEFT(PPESSOA.TELEFONE2,2)  
**Numérico**

55. **Nome do Campo:** Telefone Celular do Aluno  
**Tabela:** PPESSOAL.TELEFONE2  
**Numérico**

56. **Nome do Campo:** Email  
**Tabela:** PPESSOA.EMAIL  
**Texto(100)**

57. **Nome do Campo:** Tipo do responsável financeiro  
**Tabela:** FCFO.PESSOAFISOUJUR – J = ‘PJ’, F = ‘PF’  
**Tamanho:** 1  
**Regra:** Verifica se existe Contrato Corporativo para enviar o tipo de responsável, caso não exista, é enviado o tipo de responsável vinculado no contrato educacional.  
Caso a matrícula não atenda as regras acima, é verificado se o campo complementar SHABILITACAOALUNOCOMPL.CNPJEMPATENDIDA está preenchido e neste caso é enviado o valor fixo ‘PJ’.

58. **Nome do Campo:** CNPJ do responsável financeiro  
**Tabela:** FCFO.CGCCFO ou SHABILITACAOALUNOCOMPL.CNPJEMPATENDIDA  
**Regra:** Verifica se existe Contrato Corporativo para enviar o CNPJ do responsável, caso não exista, é enviado o CNPJ do responsável vinculado no contrato educacional.  
Caso a matrícula não atenda as regras acima, é enviado o CNPJ informado no campo SHABILITACAOALUNOCOMPL.CNPJEMPATENDIDA.

59. **Nome do Campo:** CPF  
**Tabela:** FCFO.CGCCFO – se físico

60. **Nome do Campo:** Nome da PF Responsável  
**Tabela:** FCFO.NOME  
**Texto(80)**  
**VALOR FIXO** - VAZIO

61. **Nome do Campo:** Endereço da PF Responsável  
**Tabela:** FCFO.RUA  
**Tamanho:** 60  
**VALOR FIXO** - VAZIO

62. **Nome do Campo:** Número do responsável  
**Tabela:** FCFO.NUMERO  
**Tamanho:** 20  
**VALOR FIXO** - VAZIO

63. **Nome do Campo:** Complemento do responsável  
**Tabela:** FCFO.COMPLEMENTO  
**Tamanho:** 100  
**VALOR FIXO** - VAZIO

64. **Nome do Campo:** Bairro  
**Tabela:** FCFO.BAIRRO  
**Tamanho:**20  
**VALOR FIXO** - VAZIO

65. **Nome do Campo:** Município  
**Tabela:** FCFO.CIDADE  
**VALOR FIXO** - VAZIO

66. **N****ome do Campo:** Unidade Federação  
**Tabela:** FCFO.CODETD  
**Texto(2)**  
**VALOR FIXO** - VAZIO

67.**Nome do Campo:** Cep  
**Tabela:** FCFO.CEP  
**Texto(8)**  
**VALOR FIXO** - VAZIO

68. **Nome do Campo:** Telefone Residencial  
**Tabela:** FCFO.TELEFONE  
**Texto(20)**  
**VALOR FIXO** - VAZIO

69. **Nome do Campo:** FAX  
**Tabela:** FCFO.FAX  
**Texto(20)**  
**VALOR FIXO** - VAZIO

70. **Nome do Campo:** Email  
**Tabela:** FCFO.EMAIL  
**Texto(100)**  
**VALOR FIXO** - VAZIO

71. **Nome do Campo:** Contato  
**Tabela:** FCFO.CONTATO  
**Texto(100)**  
**VALOR FIXO** - VAZIO

72. **Nome do Campo:** DR Parceiro  
**Tabela:** STURMACOMPL.DRPARCEIRO  
**Texto(50)**

73. **Nome do Campo:** DDI do Telefone do Aluno  
**Tabela:** SALUNOCOMPL.DDI  
**Numérico**

74. **Nome do Campo:** DDI do Telefone Celular do Aluno  
**Tabela:** SALUNOCOMPL.DDICELULAR  
**Numérico**

75. **Nome do Campo:** Tipo Pessoa Física (Aluno)  
**Tabela:** SALUNOCOMPL.TIPOPF \*\*Tabela Dinâmica \*\*   
**Texto(1)**

76. **Nome do Campo:** Passaporte do Aluno  
**Tabela:** PPESSOA.NPASSAPORTE  
**Texto(45)**

77. **Nome do Campo:** Registro Nacional de Migratório  
**Tabela:** PPESSOA.NROREGGERAL  
**Texto(45)**  
**Regra:** Será enviado essa informação se o campo SALUNOCOMPL.TIPOPF igual a “E - Estrangeiro”.

4Cargas Horárias Mensaishorizontal

### **Registro de Cargas Horárias Mensais**

1. **Nome do Campo:** Tipo de Registro  
Fixo: “3”

2. **Nome do Campo:** Operação de Transação  
**Campo:** “”

3. **Nome do Campo:** Código da Matrícula  
**Campo:** SHABILITACAOALUNOCOMPL.CODMATRICULASCOP. Se não preenchido envia: SHABILITACAOALUNO.RA + STURMA.IDFT  
**Texto(20)**

4. **Nome do Campo:** Referência  
**Tabela:** Mês e Ano do Parâmetro.  
**Formato:** 01/MM/AAAA

5. **Nome do Campo:** Carga Horária na Fase Escolar  
Para turmas/disciplinas com data anterior a 01/08/2018  
**Tabela:** SHORARIO.HORAFINAL – SHORARIO.HORAINICIAL  
**Regra:** Somatória da Horafim – Horainicio do plano de aula de todas as disciplinas que o aluno está matriculado do mês informado no parâmetro, descontando as faltas.  
Para turmas/disciplinas com data igual ou posterior a 01/08/2018  
**O extrator verifica o campo:** STURMADISC.TIPO

**Presencial:** O extrator verifica se o campo STURMADISC.TIPO é igual a “P – Presencial” e envia as horas executadas do aluno de acordo com o plano de aula no mês e ano de referência que foi gerado o arquivo da Solução Integradora, descontando as faltas.  
Caso o campo STURMADISC.TIPO não esteja preenchido será verificado o campo SCURSO.CURPRESDIST.

Quando houver uma subturma associada a matrícula do aluno, as horas serão extraídas do plano de aula da subturma e não da turma/disciplina, levando em consideração o mês e ano de referência que foi gerado o arquivo da Solução Integradora.

**Semipresencial**

**Presencial:** O extrator verifica se o campo STURMADISC.TIPO é igual a “S - Semipresencial” e envia as horas executadas do aluno de acordo com o plano de aula no mês e ano de referência que foi gerado o arquivo da Solução Integradora, descontando as faltas. Caso o campo STURMADISC.TIPO não esteja preenchido será verificado o campo SCURSO.CURPRESDIST.  
**Á Distância:** O extrator verifica se o campo STURMADISC.TIPO é igual a “S - Semipresencial” e STURMADISC.DTINICIAL é maior ou igual a data de corte, em seguida executa o cálculo ((SDISCIPLINA.CH \* SDISCGRADE.PERCAULASNAOPRES) / 2), onde o campo STURMADISC.DTINICIAL(1ª) ou STURMADISC.DTFINAL(2ª) seja o mês e ano de referência que foi gerado o arquivo da Solução Integradora. Caso o mês e ano de referência seja igual a STURMADISC.DTINICIAL e STURMADISC.DTFINAL será executado o cálculo (SDISCIPLINA.CH \* SDISCGRADE.PERCAULASNAOPRES).  
Se o mês da matricula do aluno na turma/disciplina for maior que o mês de início da turma/disciplina, enviar a “primeira metade” da Carga Horária à distância no mês da matricula do aluno na turma/disciplina.  
Se a matricula do aluno for em um mês anterior ou igual ao do início da Turma/Disciplinas enviar a ‘primeira metade’ da carga horária no primeiro mês da turma/disciplina

**A distância:**

Data de início da Turma/Disciplina (50% da carga horária)  
O extrator verifica se o campo STURMADISC.TIPO é igual a “D – A distância” e STURMADISC.DTINICIAL é maior ou igual a data de corte, em seguida executa o cálculo SDISCIPLINA.CH / 2, onde o campo STURMADISC.DTINICIAL seja o mês e ano de referência que foi gerado o arquivo da Solução Integradora. Caso o campo STURMADISC.TIPO não esteja preenchido será verificado o campo SCURSO.CURPRESDIST.  
Se o mês da matricula do aluno na turma/disciplina for maior que o mês de início da turma/disciplina, enviar a “primeira metade” da Carga Horária à distância no mês da matricula do aluno na turma/disciplina.  
Se a matricula do aluno for em um mês anterior ou igual ao do início da Turma/Disciplinas enviar a ‘primeira metade’ da carga horária no primeiro mês da turma/disciplina  
Data de saída do Aluno (50% da carga horária)  
O extrator verifica se o campo STURMADISC.TIPO é igual a “D – A distância” e STURMADISC.DTINICIAL é maior ou igual a data de corte, em seguida executa o cálculo SDISCIPLINA.CH / 2, onde o campo SLOGMATRICULA.DTALTERACAO seja o mês e ano de referência que foi gerado o arquivo da Solução Integradora e o último status do aluno no campo SLOGMATRICULA.CODSTATUS seja igual (Aprovado, Reprovado, Reprovado por Frequência ou Reconduzido - Legislação PcD). Caso o campo STURMADISC.TIPO não esteja preenchido será verificado o campo SCURSO.CURPRESDIST.  
Tamanho: 03

6. **Nome do Campo:** Carga Horária no Estágio  
**Tabela:** SHORARIO.HORAFINAL – SHORARIO.HORAINICIAL  
**Regra:** Somatória da Horafim – Horainicio do plano de aula de todas as disciplinas que o aluno está matriculado do mês informado no parâmetro, descontando as faltas. São consideradas apenas as turmas/disciplinas de “Estágio” que por sua vês não estão vinculadas a um período letivo FE  
**Tamanho:** 03

Quando houver uma subturma associada a matrícula do aluno, as horas serão extraídas do plano de aula da subturma e não da turma/disciplina, levando em consideração o mês e ano de referência que foi gerado o arquivo da Solução Integradora.

7. **Nome do Campo:** Hora Aluno na Fase Escolar Presencial  
**Tabela:** SHORARIO.HORAFINAL – SHORARIO.HORAINICIAL  
**Regra:** Somatória da Horafim – Horainicio do plano de aula de todas as disciplinas que o aluno está  
matriculado do mês informado no parâmetro sem descontar as faltas.  
**Tamanho:** 03

Quando houver uma subturma associada a matrícula do aluno, as horas serão extraídas do plano de aula da subturma e não da turma/disciplina, levando em consideração o mês e ano de referência que foi gerado o arquivo da Solução Integradora.

8. **Nome do Campo:** Hora Aluno na Fase Escolar a Distância  
**Tabela:** SDISCGRADE.PERCAULASNAOPRES  
**Regra:** Verificar o tipo da turma/disciplina – STURMADISC.TIPO  
**Semi-Presencial:** O extrator verifica se o campo STURMADISC.TIPO é igual a “S – Semi-Presencial” e realiza o cálculo (SDISCIPLINA.CH \* SDISCGRADE.PERCAULASNAOPRES)/2)) dividindo entre no 1º mês e o último mês de execução da turma/disciplina. Metade da carga horária a distância da disciplina será enviada no primeiro mês e a outra metade no último mês da turma/disciplina.

* Se o mês da matricula do aluno na turma/disciplina for maior que o mês de início da turma/disciplina, enviar a “primeira metade” da Carga Horária à distância no mês da matricula do aluno na turma/disciplina.
* Se a matricula do aluno for em um mês anterior ou igual ao do início da Turma/Disciplinas enviar a ‘primeira metade’ da carga horária no primeiro mês da turma/disciplina. Caso o mês e ano de referência seja igual a STURMADISC.DTINICIAL e STURMADISC.DTFINAL será executado o cálculo (SDISCIPLINA.CH \* SDISCGRADE.PERCAULASNAOPRES).

**À Distância:** O extrator verifica se o campo STURMADISC.TIPO é igual a “D – A distância” e em seguida  
executa o cálculo SDISCIPLINA.CH / 2, onde o campo STURMADISC.DTINICIAL seja o mês e ano de referência que foi gerado o arquivo da Solução Integradora. Sendo que a metade no primeiro mês de execução da turma/disciplina e o restante no mês correspondente a conclusão da matrícula do aluno na DISCIPLINA. Caso o campo STURMADISC.TIPO não esteja preenchido será verificado o campo SCURSO.CURPRESDIST.

* Se o mês da matricula do aluno na turma/disciplina for maior que o mês de início da turma/disciplina, enviar a “primeira metade” da Carga Horária à distância no mês da matricula do aluno na turma/disciplina.
* Se a matricula do aluno for em um mês anterior ou igual ao do início da Turma/Disciplinas enviar a ‘primeira metade’ da carga horária no primeiro mês da turma/disciplina.

**Tamanho:** 03  
**Posição:** 8

5Contrato de Aprendizagemhorizontal

### **Registro de Contrato de Aprendizagem**

1. **Nome do Campo:** Tipo de Registro  
**Fixo:** “4”

2. **Nome do Campo:** Operação de Transação  
**Campo:** “”

3. **Nome do Campo:** Código da Matrícula  
**Campo:** SHABILITACAOALUNOCOMPL.CODMATRICULASCOP. Se não preenchido envia: SHABILITACAOALUNO.RA + STURMA.IDFT  
**Texto(20)**

4. **Nome do Campo:** CNPJ da Empresa Atendida  
**Tabela:** SEMPRESA.CNPJ ou SHABILITACAOALUNOCOMPL.EMPRESACOMP (CNPJ da empresa contratante do aluno).  
**Tamanho:** 14

5. **Nome do Campo:** Inscrição Estadual da Empresa Atendida  
**Tabela:** SEMPRESA.CNPJ ou SHABILITACAOALUNOCOMPL.EMPRESACOMP (Inscrição Estadual da empresa contratante do aluno).  
**Tamanho:** 14

6. **Nome do Campo:** UF da Inscrição Estadual  
**Tabela:** SEMPRESA.ESTADO ou GFILIAL.CODMUNICIPIO (Inscrição Estadual da empresa contratante do aluno).  
**Tamanho:** 14

7. **Nome do Campo:** Matricula CEI da Empresa Atendida  
**Tabela:** SEMPRESA.CNPJ ou SHABILITACAOALUNOCOMPL.EMPRESACOMP (CEI da empresa contratante do aluno).   
**Tamanho:** 14

8. **Nome do Campo:** Referência  
**Tabela:** Mês e Ano do Parâmetro.  
**Formato:** 01/MM/AAAA

9. **Nome do Campo:** Data Inicio Vigência Contrato  
**Tabela:** SHABILITACAOALUNOCOMPL.DATAINICIALA ou SESTAGIOCONTRATO.DTINICIOESTAGIO ou SATIVIDADEALUNO.DATAINICIO  
**Regra:** Essa data só será apresentada caso o DOCUMENTO da empresa atendida esteja preenchido

10. **Nome do Campo:** Data Final Vigência Contrato  
**Tabela:** SHABILITACAOALUNOCOMPL.DATAFINALA OU SESTAGIOCONTRATO.DTFINALESTAGIO OU SATIVIDADEALUNO.DATAFIM  
**Regra:** Essa data só será apresentada caso o DOCUMENTO da empresa atendida esteja preenchido

11. **Nome do Campo:** Horas de Prática Profissional Contratada  
**Tabela:** SUM(SDISCIPLINA.CHESTAGIO) ou SHABILITACAOALUNOCOMPL.CHCONTRATADAA ou SATIVIDADEALUNO.CARGAHORARIAATV

Para as Matrizes Atuais, se o aluno não tiver matriculado na “Disciplina de Pratica Profissional” será enviado as horas do campo complementar “Carga Horária Contratada” do curso/habilitação do aluno.

12. **Nome do Campo:** Horas de Prática Profissional Realizada  
**Tabela:** SHORARIO.HORAFINAL – SHORARIO.HORAINICIAL  
**Regra:** Somatória da Horafim – Horainicio do plano de aula da disciplina de “prática profissional” que o aluno está matriculado do mês informado no parâmetro, descontando as faltas.  
Se o aluno não tiver matriculado na “Disciplina de Pratica Profissional” será enviado 0(zero) horas.

Para as Matrizes da Aprendizagem 4.0 a partir de 01/10/2020 não será gerado horas de prática realizadas.

**Tamanho:** 03

13. **Nome do Campo:** Código do Contrato de Aprendizagem no DR  
Para turmas/disciplinas com data anterior a 01/08/2018  
**Tabela:** SALUNO.RA + CNPJ ou IE ou CEI  
**Regra:** Será enviado o SALUNO.RA concatenado com os dados do CNPJ ou IE ou CEI que podem estar no cadastro de Atividade Ofertada ou Termo de Compromisso ou Campos Complementares do Curso/Habilitação conforme as regras definidas no item “ 4 Tipo de Registro – Contrato de Aprendizagem”  
**Tamanho:** 35

RESTRIÇÕES 

**Filtros:**   
Coligada Senai  
Turmas que a data inicio e fim estejam compreendidas no mês e ano passado pelo parâmetro.  
Alunos enviados no mês anterior ao que está sendo passado no parâmetro com status: Em andamento.

**Menu que chama o relatório**

Gerador de saídas (Arquivo TXT)
