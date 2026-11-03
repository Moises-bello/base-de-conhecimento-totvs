---
content_hash: c05ef7004789689c29f77e616cd6a12f3229e7a9d66ca6e24ed1c1256bcf9410
fetched_at: '2026-06-29T00:10:41.841742+00:00'
page_id: '546673221'
product: rm
source: tdn-rm
title: Solução Integradora - Telas do SGE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546673221
version: 33
---

Documentação para detalhar os critérios e regras aplicadas na ferramenta para extração de informações do SGE - Sistema de Gestão Escolar para importação no sistema Solução Integradora.

Abaixo apresentamos as telas para preenchimento das informações e execução das rotinas no SGE tendo como foco, a exportação das informações para o Solução Integradora. **Nível de Ensino:** **Profissional e** **Superior**.

**Curso**

**Serão extraídos do cadastro de Curso.**

**Dados Gerais do Curso:** As informações gerais relacionadas ao “Curso” apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela / Campo SGE** | **Dado Solução Integradora** |
| Nome do Curso (SCURSO.NOME) | Nome do Curso. |
| Modalidade - (SCURSO.CODMODALIDADECURSO) | Modalidade. |
| Área - (SAREA.CODAREA) | Área de Atuação. |
| Eixo Tecnológico - (SEIXOTECNOLOGICO.CODEIXOTECNOLOGICO) | Código do Eixo Tecnológico MEC. |
| Presencial/Distância - (SCURSO.CURPRESDIST) | Tipo de Ação. |
| CBO Solução Integradora - (SCURSOCOMPL.CBO\_SI) | Ocupação (CBO). |

**Cadastro de Curso - Aba Identificação l Aba Campos Complementares**

Importante

Os cursos ofertados nos formatos: "Presencial" e "A Distância" devem ter cadastros distintos no SGE, mesmo que as matrizes curriculares tenham conteúdos e cargas horárias equivalentes.

## **Matriz Curricular**

**Serão extraídos do cadastro da Matriz Curricular.**

**Dados Gerais da Matriz Curricular:** As informações gerais relacionadas à “Matriz Curricular” apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela / Campo SGE** | **Dado Solução Integradora** |
| Data Início - (SGRADE.DTINICIO) | Início da Oferta. |
| Carga Horária - À Distância (SGRADECOMPL.CHEAD) | Este campo foi criado para que o DR informe a carga horária A DISTÂNCIA prevista no Plano de Curso. |
| Carga Horária - Presencial (SGRADECOMPL.CHESCOLAR) | Este campo foi criado para que o DR informe a carga horária PRESENCIAL prevista no Plano de Curso.  Para cursos de Aprendizagem incluir as horas da Fase Escolar + a Carga Horária mínima de prática profissional. |
| Carga Horária - Estágio (SGRADECOMPL.CHESTAGIO) | Neste campo deverá ser informada somente a carga horária do ESTÁGIO, prevista no Plano de Curso. |
| Código do Curso - Enviado ao DN pelo Legado (SGRADECOMPL.CODCURSOSCOP) | Código do Curso. |
| Curso Técnico no MEC - (SGRADECOMPL.CURSOMEC) | Código do Curso MEC - SISTEC. |

**Cadastro da Matriz Curricular - Aba Identificação l Aba Campos Complementares**

## **Matriz Curricular**

## **Competência / Certificações Intermediárias**

O extrator trará apenas informações acerca das certificações intermediárias caso a modalidade do curso seja uma das listadas abaixo:

**15 - Aprendizagem Industrial Técnica**  
**31 - Habilitação Técnica**

|  |  |
| --- | --- |
| **Nome da Tabela /Campo SGE** | **Dado Solução Integradora** |
| Competência (SCOMPETENCIAGRADE.CODCOMPETENCIA) | Certificações Intermediárias. |

**Cadastro da Matriz Curricular - Anexos l Competência**

Certificações intermediarias

O extrator busca as seis primeiras saídas intermediárias identificadas.

## **Disciplina Optativa/Eletiva - Aplicada ao** **Registro de Estágio e Fase Empresa (****Anterior à Fase Empresa 4.0)**

**Dados Gerais da Disciplina Optativa/Eletiva:** As informações gerais relacionadas à “Disciplina Estágio” para registro da Fase Empresa ou Estágio apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela /Campo SGE** | **Dado Solução Integradora** |
| Disciplina para a Prática Profissional.   Carga Horária Fase Empresa da Aprendizagem - (SDISCIPLINA.CHESTAGIO) | Prática Profissional Contratada (Formato de Registro Anterior à Fase Empresa 4.0)  ou Registro de Estágio. |

**Cadastro da Disciplina - Aba Identificação**

## **Registro da Fase Empresa (Anterior à Fase Empresa 4.0)**

**Serão extraídos do cadastro de Turma e Turma/Disciplina da Fase Empresa.**

## **Turma Fase Empresa**

**Dados Gerais da Turma:** As informações gerais relacionadas à “Fase Empresa” apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela /Campo SGE** | **Dado Solução Integradora** |
| Data Inicial - (STURMA.DATAINICIAL) | Data de Entrada da Matrícula. |

**Cadastro da Turma Fase Empresa - Aba Identificação**

## **Turma/Disciplina Fase Empresa**

**Dados Gerais da  Turma/Disciplina:** A carga horária de "Prática Profissional" será identificada a partir das "Turmas/Disciplinas" associadas às disciplinas optativas/eletivas exclusivas de estágio.

|  |  |
| --- | --- |
| **Nome da Tabela /Campo SGE** | **Dado Solução Integradora** |
| Tipo da Turma (STURMADISC.TIPO) | Tipo da Turma no Cadastro da Turma / Disciplina. |
| Plano de Aula | Carga Horária Executada. |

**Cadastro da Turma/Disciplina Fase Empresa - Aba Identificação l Anexos: Planos de Aula**

* **Geração e Contabilização de Matrículas**
* **Informações Gerais da Matrícula e Dados Básicos do Aluno**
* **Cadastro do Aluno**

**Serão extraídos do cadastro de Aluno.**

**Dados Gerais do Cadastro de Aluno:** As informações gerais relacionadas ao cadastro de “Aluno” apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela / Campo SGE** | **Dado Solução Integradora** |
| RA | Código do Aluno.  Alunos migrados para o SGE de um Sistema Legado: Para estes alunos o campo complementar “Código do Aluno no legado” deve estar preenchido com o código do aluno no sistema legado. O extrator irá buscar o dado do campo e enviar como “Código do Aluno”.  Alunos cadastrados inicialmente no SGE: Para os alunos onde o campo “Código do Aluno no legado” estiver em branco, o extrator irá enviar o código como: SGE+UF+RA, ex: SGEPE00000125 |
| Nome - (PPESSOA.NOME) | Nome |
| Estado Natal |  |
| Naturalidade |  |
| Data de Nascimento - (PPESSOA.DTNASCIMENTO) | Data de Nascimento |
| Sexo - (PPESSOA.SEXO) | Sexo |
| Email - (PPESSOA.EMAIL) | E-mail |
| País de Nacionalidade do Aluno | Baseado no cod. do País será realizado um de/para buscando informação na tabela ZSIPAIS.CODIGO, que está de acordo com a tabela disponibilizada pelo DN. |
| Estado Civil do Aluno (PPESSOA.ESTADOCIVIL ) | Estado Civil |
| Cor / Raça - (PPESSOA.CORRACA) | Raça. |
| Grau de Instrução (PPESSOA.GRAUINSTRUCAO) | Nível de Escolaridade. |
| CEP - (PPESSOA.CEP) | CEP. |
| Logradouro (Rua) - (PPESSOA.RUA) | Endereço do aluno. |
| Número - (PPESSOA.NUMERO) | Número do Endereço. |
| Complemento do Endereço - (PPESSOA.COMPLEMENTO) | Complemento do Endereço. |
| Bairro - (PPESSOA.BAIRRO) | Bairro/Distrito. |
| Estado - (PPESSOA.ESTADO) | Unidade da Federação. |
| Cidade |  |
| País |  |
| Telefone Residencial - (PPESSOA.TELEFONE1) | Telefone do Aluno. |
| Telefone Celular - (PPESSOA.TELEFONE2) | Telefone Celular do Aluno. |
| CPF - (PPESSOA.CPF) | CPF. |
| Passaporte do Aluno - (PPESSOA.NPASSAPORTE) ***Novo!*** | Número do Passaporte. |
| Registro Nacional de Migratório - (PPESSOA.NROREGGERAL) ***Novo!*** | Será enviada a informação sempre houver preenchimento do campo  SALUNOCOMPL.TIPOPF igual a “E - Estrangeiro”. |
| Nome da Mãe (SPESSOA.CODPESSOAMAE) | Sempre que houver no nome da mãe a palavra "Desconhecida" será enviado para a Solução Integradora o registro como "Desconhecida". |
| Situação Ocupacional - (SALUNOCOMPL.SITUACAOOCUP) | Situação Ocupacional. |
| Tipo de Escola de Origem - (SALUNOCOMPL.TIPOESCOLA) | Tipo de Escola de Origem do Aluno. |
| Código do Aluno no Legado - (SALUNOCOMPL.CODALUNOSCOP) | Código do Aluno. |
| Grupos Vulneráveis - (SALUNOCOMPL.MOTIVOCPF) | Motivo de Falta de CPF. |
| Nome da Mãe (SPESSOA.CODPESSOAMAE) | Sempre que houver no nome da mãe a palavra "Desconhecida" será enviado para a Solução Integradora o registro como "Desconhecida". |
| DDI do Telefone do Aluno - (SALUNOCOMPL.DDI) ***Novo!*** | DDI do Telefone do Aluno Estrangeiro. |
| DDI do Telefone Celular do Aluno - (SALUNOCOMPL.DDICELULAR) ***Novo!*** | DDI do Telefone Celular do Aluno Estrangeiro. |
| Tipo Pessoa Física - (SALUNOCOMPL.TIPOPF) ***Novo!*** | Tipo de Pessoa Física (Estrangeiro ou Nacional). |

**Cadastro do Aluno - Aba Identificação l Dados Básicos**

**Cadastro do Aluno - Aba Identificação l Informações Adicionais**

**Cadastro do Aluno - Aba Identificação l Pessoas com Necessidades Especiais**

**Cadastro do Aluno - Aba Endereço l Residencial**

**Cadastro do Aluno - Aba Documentos l Pessoais I**

**Cadastro do Aluno - Aba Documentos l Complementares**

**Cadastro do Aluno - Aba Responsáveis l Filiação**

Responsáveis

*Nome da Mãe - (SPESSOA.CODPESSOAMAE) -* *Sempre que houver no nome da mãe a palavra "Desconhecida" será enviado para a Solução Integradora o registro como "Desconhecida"*

**Cadastro do Aluno - Aba Campos Complementares**

Novo!!!

*Novos campos complementares implementados a partir de Ago/2022* com a finalidade de informar o código de discagem internacional e relacionar o tipo da pessoa física.

* **DDI do telefone do aluno;**
* **DDI do telefone celular do aluno;**
* **Tipo Pessoa Física (Tabela dinâmica nacionalidade de acordo com a tabela referencial da SI).**

## **Registro de Matrícula**

## **Curso/ Habilitação**

**Serão extraídos do cadastro do Curso/Habilitação.**

**Dados Gerais do Curso/Habilitação:** As informações gerais relacionadas ao cadastro do “Curso/Habilitação" apropriados pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela / Campo SGE** | **Dado Solução Integradora** |
| Situação de Matrícula - (SHABILITACAOALUNO-CODSTATUS) | Situação de Matrícula. |
| Código do Campus - (SCAMPUS.CODCAMPUS) | Tipo de Ambiente. |
| Código da Matrícula no SCOP - (SHABILITACAOALUNOCOMPL.CODMATRICULASCOP) | Código da Matrícula. |
| Data Previsão de Saída - (SHABILITACAOALUNOCOMPL.DATAPREVISTASAIDA) | Data de Saída Prevista da Matrícula. |
| CNPJ / Inscrição Estadual - (SEMPRESA.CNPJ / ) OU | CNPJ / Inscrição Estadual da Empresa Responsável pelo Contrato do Aluno. |
| Tipo de Documento da Empresa (SHABILITACAOALUNOCOMPL.TIPODOCA) | Tipo de Documento da Empresa Responsável pelo Contrato do Aluno. |
| Número do documento da empresa (SHABILITACAOALUNOCOMPL.EMPRESACOMP ) | CNPJ ou CEI ou Inscrição Estadual da Empresa Responsável pelo Contrato do Aluno. |
| Carga Horária Contratada (SHABILITACAOALUNOCOMPL.CHCONTRATADAA) | Este campo é utilizado para identificar a Carga Horária Contratada do Contrato da Prática Profissional. |

**Cadastro do Curso/Habilitação - Aba Identificação l Aba Campos Complementares**

Para matriculas da Fase Empresa se o cadastro do Termo de Compromisso não for realizado em Gestão de Estágio, os mesmos podem ser preenchidos através dos campos complementares do Curso/Habilitação (CNPJ/CEI/Insc. Est), Data Inicial do Contrato, Data Final do Contrato e Carga Horaria Contratada.

## **Matrícula no Período Letivo**

**Serão extraídos do cadastro da Matrícula no Período Letivo**

**Dados Gerais da Matrícula no Período Letivo:** As informações gerais relacionadas ao cadastro da "Matrícula no Período Letivo" apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela /Campo SGE** | **Dado Solução Integradora** |
| Situação de Matricula - (SMATRICPL.CODSTATUS) | Situação de Matrícula. |
| Articulação - (SMATRICPLCOMPL.ARTICULACAO) | Articulação SENAI/SESI. |
| Condição do Aluno - (SMATRICPLCOMPL.TIPOGRAT) | Tipo de Gratuidade / Indicador PRONATEC. |

**Cadastro da Matrícula no Período Letivo - Aba identificação l Aba Campos Complementares**

Na Matrícula do Período Letivo, o campo: Contrato de Aprendizagem não precisa ser mais preenchido, portanto, poderá ser desabilitado, uma vez que a Solução Integradora extrai a informação a partir de outros campos.

## **Cadastro da Empresa (Contrato de Aprendizagem)**

**Serão extraídos do cadastro da Empresa**

**Dados Gerais da Empresa:** As informações gerais relacionadas ao cadastro da "Empresa" apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela /Campo SGE** | **Dado Solução Integradora** |
| CNPJ - (SEMPRESA.CNPJ) | CNPJ da Empresa Responsável pela Matrícula. |
| Data Início - (SESTAGIOCONTRATO.DTINICIOESTAGIO) | Data Início do Contrato de Aprendizagem. |
| Data Fim - (SESTAGIOCONTRATO.DTFINALESTAGIO) | Data Fim do Contrato de Aprendizagem. |

**Cadastro da Empresa l Aba - Identificação**

## **Termo de Compromisso** **(****Anterior à Fase Empresa 4.0)**

**Serão extraídos do cadastro do Termo de Compromisso**

**Dados Gerais do Termo de Compromisso:** As informações gerais relacionadas ao cadastro do "Termo de Compromisso" apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela /Campo SGE** | **Dado Solução Integradora** |
| Data Início - (SESTAGIOCONTRATO.DTINICIOESTAGIO) | Data Início do Contrato de Aprendizagem. |
| Data Fim - (SESTAGIOCONTRATO.DTFINALESTAGIO) | Data Fim do Contrato de Aprendizagem. |

**Cadastro do Termo de Compromisso l Aba - Identificação**

## **Registro da Fase Empresa 4.0**

A partir de 01/10/2020, os registros das informações referentes à Contração - Fase Empesa de Aprendizagem (Matrizes 4.0) estão associados ao cadastro da Empresa e Atividade Ofertada.

Conforme o novo formato de Gestão da Fase Empresa da Aprendizagem 4.0, não será mais necessário vincular o aluno ao período letivo exclusivo para registros da fase empresa (AAAA/FE) e, da mesma forma, a uma turma e disciplina exclusiva da fase empresa.  
Desta forma, a vivência profissional do aluno passa a ser realizada  por meio de uma Atividade ofertada, vinculada à empresa na qual o aluno possui um contrato.

Assim, através do componente curricular vinculado a esta atividade ofertada, é possível realizar a análise curricular do aluno mediante a conclusão do mesmo, além das informações associadas à Matriz Curricular e Curso/Habilitação.

As informações relacionadas à Matriz Curricular e Curso/Habilitação não sofreram alterações e, portanto, devem ser registradas.

## **Cadastro do Componente Curricular - Fase Empresa da Aprendizagem 4.0**

**Serão extraídos do cadastro da Matriz Aplicada o Componente: 100 - Fase Empresa da Aprendizagem**

**Dados Gerais do Componente da Matriz Curricular:** A informação geral relacionada ao cadastro do "Componente" apropriado pelo extrator da Solução Integradora são:

**Cadastro da Matriz Aplicada l Anexos: Componentes l 100 - Fase Empresa da Aprendizagem**

## **Inscrição na Atividade Ofertada - Fase Empresa da Aprendizagem 4.0**

**Serão extraídos da Inscrição na Atividade Ofertada (Fase Empresa da Aprendizagem 4.0)**

**Dados Gerais da Inscrição na Atividade Ofertada:** As informações gerais relacionadas ao cadastro da "Inscrição na Atividade Ofertada" apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela /Campo SGE** | **Dado Solução Integradora** |
| Data Início (SATIVIDADEALUNO.DATAINICIO) | Carga Horária Executada. |
| Data Fim (SATIVIDADEALUNO.DATAFIM) | Tipo da Turma no Cadastro da Turma / Disciplina. |
| CH Aproveitada (SATIVIDADEALUNO.CARGAHORARIAATV) | Carga Horária correspondente à Contratação |
| Seleção do Parâmetro Inscrição Confirmada | Quando da Contratação do Aprendiz, conforme a Data de Início do Contrato. |
| Seleção do Parâmetro Cumpriu Atividade | Quando do Encerramento/Conclusão da Contratação do Aprendiz, conforme a Data de Início do Contrato. |

**Cadastro da Inscrição na Atividade Ofertada - Aba Identificação**

## **Contrato Financeiro do Aluno**

**Serão extraídos do Contrato Financeiro do Aluno**

**Dados Gerais do Contrato Financeiro do Aluno:** As informações gerais relacionadas ao cadastro do "Contrato Financeiro do Aluno" apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela /Campo SGE** | **Dado Solução Integradora** |
| CNPJ - (FCFO.CGCCFO ) | CNPJ da Empresa Responsável pela Matrícula (Somente de Pessoa Jurídica). |
| Tipo de Cliente Fornecedor - (FCFO.PESSOAFISOUJUR) | Tipo do Responsável Financeiro. |

**Cadastro do Contrato Financeiro do Aluno - Aba Responsável Financeiro l Cadastro Cliente/Fornecedor**

## **BackOffice | Gestão Fiscal**

**Serão extraídos do Cadastro da Filial**

**Dados Gerais do Cadastro da Filial:** As informações gerais relacionadas ao cadastro da "Filial" apropriadas pelo extrator da Solução Integradora são:

|  |  |
| --- | --- |
| **Nome da Tabela /Campo SGE** | **Dado Solução Integradora** |
| Código da Unidade Atendimento (DFILIAL.CAMPOLIVRE1) | Código da Unidade Atendimento. |
| Munícipio | Código do Município da Unidade Atendimento. |

**Cadastro da Filial - Aba Endereço l Anexos: Dados Adicionais l Anexos: Dados Fiscais l Campo Livre 1**

## **Registro da Carga Horária Cursada**

**Serão extraídos os registros das cargas Horárias Cursadas conforme as situações apresentadas a seguir.**

**Situação I: Turmas/Disciplinas com data anterior a 01/08/2018**

A carga horária cursada pelo aluno dentro do SGE é extraída a partir dos planos de aula gerados para as turmas/disciplinas que o aluno está matriculado. É feita a soma dos planos de aula gerados até o último dia do mês de referência. As faltas são abatidas do valor total de horas.

**Situação II: Turmas/Disciplinas com data igual ou posterior a 01/08/2018**

O extrator irá verificar se a turma/disciplina é presencial, a distância ou semipresencial (STURMADISC.TIPO)

* **Tipo Presencial:** O extrator soma as horas executadas (plano de aula) e subtrai as faltas lançadas para o aluno.
* **Tipo Semipresencial - Aluno/Hora, carga horária presencial:** O extrator soma as horas executadas (plano de aula) e subtrai as faltas lançadas para o aluno

* **Tipo Semipresencial - Aluno/Hora, carga horária à distância:** O extrator identifica a quantidade de horas a distância da disciplina, a partir do percentual informado no campo “Percentual de Aulas não Presenciais” que fica na tela de “Disciplinas da Matriz Curricular”.

* O envio do aluno/hora correspondente a carga horária EAD (% a distância) será dividido entre o primeiro mês e o último mês de execução da turma/disciplina. Metade da carga horária a distância da disciplina será enviada no primeiro mês e a outra metade no último mês da turma/disciplina, independente do período de execução.
* Para as disciplinas de curta duração, ou seja, que são desenvolvidas totalmente em um mesmo mês, será portanto realizado o envio total da carga horária a distância.

Se o mês de matrícula do aluno na Turma/Disciplina for maior que o mês de início da Turma/Disciplina, enviar a "primeira metade" da Carga Horária à distância no mês da matrícula do aluno na Turma/Disciplina.

Se a matrícula do aluno for em um mês anterior ou igual ao do início da Turma/Disciplina enviar a “primeira metade” da carga horária no primeiro mês da Turma/Disciplina.

* **Tipo À Distância:** O extrator enviará a carga horária total da disciplina sendo metade no primeiro mês de execução da Turma/Disciplina e o restante no mês correspondente a conclusão da matrícula do aluno na disciplina. Esta data corresponde ao Dia/Mês em que a situação de matrícula do aluno na disciplina foi alterada para um status de conclusão.

Se o mês de matrícula do aluno na turma/disciplina for maior que o mês de início da turma/disciplina, enviar a "primeira metade" da Carga Horária à distância no mês da matrícula do aluno na turma/disciplina.

Se a matrícula do aluno for em um mês anterior ou igual ao do início da Turma/Disciplinas enviar a “primeira metade” da carga horária no primeiro mês da turma/disciplina.

Se o campo “Tipo de Turma” não estiver preenchido no cadastro da turma/disciplina o extrator irá considerar a informação preenchida no campo “Presencial/Distância” do cadastro do curso.

Para os alunos sem carga horária no período deverá ser enviado o valor igual a 0 (Zero).

**Situação III - Carga Horária Estágio** 

O valor da carga horária de estágio executada corresponde ao somatório dos planos de aula associados a turma/disciplina cuja disciplina está marcada como: Exclusiva de Estágio.
