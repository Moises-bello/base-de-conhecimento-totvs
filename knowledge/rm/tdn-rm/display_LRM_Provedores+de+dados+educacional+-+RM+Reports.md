---
content_hash: 7948f642d118057dd3515a09aa9ea6fd4c5e0db86eb8b698a9695c9b50b84407
fetched_at: '2026-06-29T00:10:32.767782+00:00'
page_id: '527853139'
product: rm
source: tdn-rm
title: Provedores de dados educacional - RM Reports
type: documentation
url: https://tdn.totvs.com/display/LRM/Provedores+de+dados+educacional+-+RM+Reports
version: 19
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Definições**

## **01. VISÃO GERAL**

O TOTVS Educacional disponibiliza uma série de provedores de dados para auxiliar na montagem de relatórios pois estes trazem dados específicos alinhados com as regras educacionais.

* Análise Curricular- EduAnaliseCurricularProvider  
  + Carrega o histórico do aluno do ensino superior.
* Documentos pendentes do aluno - EduDocExigidoProvider  
  + Carrega os documentos pendentes do aluno.
* Ficha de resultado final - EduFichaResultadoFinalProvider  
  + Carrega a ficha de resultado final para alunos de uma determinada turma.
* Histórico Ensino Fundamental - EduHistoricoFundamentalProvider  
  + Carrega o histórico do aluno do ensino fundamental.
* Histórico Ensino Médio - EduHistoricoMedioProvider  
  + Carrega o histórico do aluno do ensino médio.
* Nota etapa do aluno - EduNotaEtapaAlunoProvider  
  + Carrega a nota etapa do aluno.
* Quadro de horário do aluno - EduQuadroHorarioAlunoProvider  
  + Carrega o quandro de horários do aluno.
* Quadro de horário do professor - EduQuadroHorarioProfessorProvider  
  + Carrega o quadro de horários do professor.
* Resumo do Histórico Ensino Fundamental - EduResumoHistoricoProvider
  + Carrega o resumo do histórico do aluno do ensino fundamental.

* Declaração Mensal de Serviços Educacionais - EduDeclaracaoMensalServicoProvider
  + Carrega os dados do contrato do aluno para o curso.

## **02. Definições**

Para os provedores carregarem os dados corretamente, existem parâmetros obrigatórios para cada provedor, abaixo está detalhado quais os parâmetros necessários para utilizar cada provedor e quais regras mínimas devem existir.

Análise Curricular

### Análise Curricular - EduAnaliseCurricularProvider

Este provedor executa o mesmo processo utilizado na tela de análise curricular para um ou mais alunos.

Parâmetros obrigatórios:

| Campo | Descrição | Tipo | Observação |
| --- | --- | --- | --- |
| CODCOLIGADA | Código da coligada | inteiro |  |
| IDHABILITACAOFILIAL | Id. habilitação filial | inteiro |  |
| RADE | R.A. de: | texto |  |
| RAATE | R.A. até: | texto |  |

Para utilizar um único R.A. informe o mesmo nos dois parâmetros de R.A de e R.A. até.

Para mais informações sobre as regras do provedor acesse a documentação:

Documentos pendentes do aluno

### Documentos pendentes do aluno - EduDocExigidoProvider

Este provedor carrega a lista de documentos exigidos de um ou mais alunos, sendo documentos de ingresso ou do período letivo, quantidade entregue pelo aluno e data da entrega.

Parâmetros obrigatórios:

| Campo | Descrição | Tipo | Observação |
| --- | --- | --- | --- |
| CODCOLIGADA | Código da coligada | inteiro |  |
| CODFILIAL | Código da filial | inteiro |  |
| CODTIPOCURSO | Nível de ensino | inteiro |  |
| DTENTREGA | Data da entrega | data |  |
| RADE | R.A. de: | texto |  |
| RAATE | R.A. até: | texto |  |

Para utilizar um único R.A. informe o mesmo nos dois parâmetros de R.A de e R.A. até.

Para mais informações sobre as regras do provedor acesse as documentações:

Ficha de resultado final

### Ficha de resultado final - EduFichaResultadoFinalProvider

Este provedor carrega a ficha de resultado final dos alunos das turmas/disciplinas de uma determinada turma.

Parâmetros obrigatórios:

| Campo | Descrição | Tipo | Observação |
| --- | --- | --- | --- |
| CODCOLIGADA | Código da coligada | inteiro |  |
| CODFILIAL | Id. habilitação filial | inteiro |  |
| IDPERLET | Id. período letivo | inteiro |  |
| CODTURMA | Código da turma | texto |  |

As turmas/disciplinas devem possuir uma etapa do tipo "nota" e que seja a etapa final.

Para mais informações sobre as regras do provedor acesse a documentação:

Histórico Ensino Fundamental e Histórico Ensino Médio

### Histórico Ensino Fundamental - EduHistoricoFundamentalProvider

### Histórico Ensino Médio - EduHistoricoMedioProvider

Este provedor carrega o histórico que foi cadastrado ou gerado para o aluno.

Parâmetros obrigatórios:

| Campo | Descrição | Tipo | Observação |
| --- | --- | --- | --- |
| CODCOLIGADA | Código da coligada | inteiro |  |
| CODCURSOHIST | Código do Curso do Histórico | inteiro |  |
| RA | Registro acadêmico | texto |  |

Para mais informações sobre as regras do provedor acesse a documentação:



A partir da versão 12.1.25 o provedor de dados de histórico do ensino médio (EduHistoricoMedioProvider) foi alterado de 25 para até 60 posições de disciplinas entre base comum e base diversificada, assim será possível ter até 60 disciplinas no relatório conforme definição disponível nas partes do histórico, porém o relatório do book "EDUREL0002 - Histórico Escolar - Ensino Médio" disponível para o TOTVS Educacional continuará com 25 posições fixas no relatório. 

As disciplinas estão sendo ordenadas por:

* Ordem da Série do histórico
* Código da Parte do histórico
* Posição da Disciplina do histórico
Nota etapa do aluno

### Nota etapa do aluno - EduNotaEtapaAlunoProvider

Este provedor carrega as notas e faltas das etapas do aluno.

Parâmetros obrigatórios:

| Campo | Descrição | Tipo | Observação |
| --- | --- | --- | --- |
| CODCOLIGADA | Código da coligada | inteiro |  |
| IDHABILITACAOFILIAL | Id. habilitação filial | inteiro |  |
| IDPERLET | Id. período letivo | inteiro |  |
| RA | Registro acadêmico | texto |  |

Para mais informações sobre as regras do provedor acesse a documentação:

Quadro de horário do aluno

### Quadro de horário do aluno - EduQuadroHorarioAlunoProvider

Este provedor carrega o quadro de horários das disciplinas que o aluno está matriculado no período letivo.

Parâmetros obrigatórios:

| Campo | Descrição | Tipo | Observação |
| --- | --- | --- | --- |
| CODCOLIGADA | Código da coligada | inteiro |  |
| CODFILIAL | Código da filial | inteiro |  |
| IDPERLET | Id. período letivo | inteiro |  |
| IDHABILITACAOFILIAL | Id. habilitação filial | inteiro |  |
| RA | Registro acadêmico | texto |  |
| CODTIPOCURSO | Código do nível de ensino | inteiro |  |

O sistema não irá carregar os horários de turmas/disciplinas que estiverem desativadas.

Os campos "data inicial (DATAINICIAL) e final (DATAFINAL) que o provedor retorna são buscados do horário da turma/disciplina, porém se estiver vazio o sistema busca da turma/disciplina, se este também estiver vazio o sistema busca da turma e caso este também esteja vazio o sistema irá buscar o do período letivo.

Os campos código da sala (CODSALA), código do bloco (CODBLOCO) e código do prédio (CODPREDIO) que o provedor retorna são buscados do horário da turma/disciplina, se um deles estiver vazio o sistema irá buscar da turma/disciplina e se também estiver vazio o sistema irá buscar da turma.

Quadro de horário do professor

### Quadro de horário do professor - EduQuadroHorarioProfessorProvider

Este provedor carrega o quadro de horários das disciplinas que o professor está definido.

Parâmetros obrigatórios:

| Campo | Descrição | Tipo | Observação |
| --- | --- | --- | --- |
| CODCOLIGADA | Código da coligada | inteiro |  |
| CODFILIAL | Código da filial | inteiro |  |
| CODPERLET | Código do período letivo | texto |  |
| CODPROF | Código do professor | texto |  |
| CODTIPOCURSO | Código do nível de ensino | inteiro |  |
| DATAATUAL | Data atual | inteiro | Não é obrigatório |

O sistema não irá carregar os horários de turmas/disciplinas que estiverem desativadas.

Os campos "data inicial (DATAINICIAL) e final (DATAFINAL) que o provedor retorna são buscados do horário da turma/disciplina, porém se estiver vazio o sistema busca da turma/disciplina, se este também estiver vazio o sistema busca da turma e caso este também esteja vazio o sistema irá buscar o do período letivo.

Os campos código da sala (CODSALA), código do bloco (CODBLOCO) e código do prédio (CODPREDIO) que o provedor retorna são buscados horário da turma/disciplina, se um deles estiver vazio o sistema irá buscar da turma/disciplina e se também estiver vazio o sistema irá buscar da turma.

Resumo do Histórico Ensino Fundamental

### Resumo do Histórico Ensino Fundamental - EduResumoHistoricoProvider

Este provedor carrega um resumo do histórico do ensino básico.

Parâmetros obrigatórios:

| Campo | Descrição | Tipo | Observação |
| --- | --- | --- | --- |
| CODCOLIGADA | Código da coligada | inteiro |  |
| CODCURSOHIST | Código do curso no histórico | texto |  |
| RA | Registro acadêmico | texto |  |

Para mais informações sobre as regras do provedor acesse a documentação:

Declaração Mensal de Serviços Educacionais

### Declaração Mensal de Serviços Educacionais - EduDeclaracaoMensalServicoProvider

Este provedor carrega os dados do contrato do aluno para um curso

Parâmetros obrigatórios:

| Campo | Descrição | Tipo | Observação |
| --- | --- | --- | --- |
| CODCOLIGADA | Código da coligada | inteiro |  |
| CODFILIAL | Código da filial | inteiro |  |
| CODTIPOCURSO | Código do nível de ensino | inteiro |  |
| DATACOMPETENCIADMS | Competência da DMS | texto | A competência da DMS deve ser informada no formatado **MM/yyyy**. Exemplos: 11/2023, 01/2024 |

Para mais informações sobre as regras do provedor acesse a documentação:
