---
content_hash: 070110326a3e3981b7011eaf2196e038cb1805951ac2378d97619e7d657cb5c4
fetched_at: '2026-06-29T00:06:03.390284+00:00'
page_id: '198953922'
product: rm
source: tdn-rm
title: TS9062_DT_Matriz_Curricular_Curriculo_Individual
type: documentation
url: https://tdn.totvs.com/display/LRM/TS9062_DT_Matriz_Curricular_Curriculo_Individual
version: 11
---

# MATRIZ CURRICULAR E CURRÍCULO INDIVIDUAL DO ALUNO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Matriz Curricular* | *Matriz Curricular* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Currículo individual** | *Currículo* *individual* | | **Assistente para cópia da matriz para o currículo individual** | **Assistente para cópia da matriz para o currículo individual** | | **Geração de arquivo Enade** | **Geração de arquivo Enade (Visão de seleção de alunos)** | | **Cadastro de Diplomação do Aluno** | **Cadastro de Diplomação do Aluno** | | **Processo de Inscrições em atividades ofertadas do Aluno** | **Processo de Inscrições em atividades ofertadas do Aluno** | | **Cadastro de Cursos / Habilitações de uma atividade ofertada** | **Cadastro de Cursos / Habilitações de uma atividade ofertada** | | **Inscrição de alunos na atividade ofertada** | **Inscrição de alunos na atividade ofertada** | | **Avaliação institucional do Aluno** | **Avaliação institucional do Aluno (Visão de seleção de candidatos)** | | **Matrícula de aluno em um período letivo** | **Matricula de aluno em um período letivo** | | **Matrícula de aluno em disciplinas sugestivas** | **Matrícula de aluno em disciplinas sugestivas** | | **Transferência Interna** | **Transferência Interna** | | **Transferência entre coligadas** | **Transferência entre coligadas** | | **Assistente para cadastro de equivalência de alunos** | **Assistente para cadastro de equivalência de alunos** | | **Confirmação de matrícula por pagamento** | **Confirmação de matrícula por pagamento** | | **Enturmação** | **Enturmação** | | **Matrícula por prioridade** | **Matrícula por prioridade (Visão turma / disciplina)** | | **Cadastro de matriz aplicada a uma linha de pesquisa** | **Cadastro de matriz aplicada a uma linha de pesquisa** | | **Digitação de notas e faltas de etapas** | **Digitação de notas e faltas de etapas** | | **Digitação de notas de avaliação por aluno** | **Digitação de notas de avaliação por aluno** | | **Cadastro de turma** | **Cadastro de turma** | | **Concessão de bolsa para aluno** | **Concessão de bolsa para aluno** | | **Cadastro de contrato** | **Cadastro de contrato** | | **Cadastro de faixa de crédito** | **Cadastro de faixa de crédito** | | **Assistente de Geração de lançamento** | **Assistente de Geração de lançamento** | | **Cadastro de plano de pagamento de uma habilitação** | **Cadastro de plano de pagamento de uma habilitação** | | **Análise curricular** | **Análise curricular** | | **Geração de histórico no ensino básico** | **Geração de histórico no ensino básico** | |
| **Cadastros Iniciais:** | *1) Período letivo cadastrado;*  *2) Aluno cadastrado com um curso/habilitação;*  *3) Curso cadastrado com uma habilitação e matriz curricular com a descrição contendo 255 caracteres;*  *4) Para o ensino básico: aluno cadastrado e matriculado em um curso, onde o mesmo já foi aprovado;*  *5) Linha de pesquisa cadastrada para a rotina Cadastro de matriz aplicada a uma linha de pesquisa;*  *6) Para a rotina **Transferência entre coligadas, deverá possuir outra coligada cadastrada com uma Filial, Nível de Ensino, Período Letivo, Curso, Habilitação, Matriz Curricular.*** |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas utilizadas:** | *SGRADE, SGRADEALUNO e SHISTHABILITACAOALUNO.* |
| **Sistema(s) operacional(is):** | *Windows 7* |
| **Versões/Release:** | *12.1.7* |

## Descrição

Ajuste no tamanho máximo do campo DESCRICAO da tabela SGRADE e SGRADEALUNO, e NOMEGRADE da tabela SHISTHABILITACAOALUNO de 60 caracteres para 255 caracteres.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(12.1.7)* deste chamado.

## Procedimento para Utilização

Para a rotina Matriz Curricular:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Cursos | Efetuar o cadastro de um curso;
3. Acessar Currículo e Oferta | Matriz Curricular | Efetuar o cadastro da matriz curricular do curso cadastrado.

Para a rotina Currículo Individual:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Aluno | Anexos | Cursos / Habilitações | Editar um curso / habilitação | Anexos | Matriz Curricular do Aluno | Currículo Individual | Efetuar o cadastro de um currículo individual.

Para a rotina Assistente para cópia da matriz para o currículo individual:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Grupo Estrutura Curricular | Mais | Assistente para cópia da matriz para o currículo individual | Avançar | Selecionar e adicionar um aluno | Avançar | Selecionar aluno da visão | Avançar | Confirmar | Avançar | Executar.

Para a rotina Geração de arquivo Enade, apenas exibição da visão Seleção de Alunos:

1. Acessar o TOTVS Educacional;
2. Acessar Atividades Acadêmicas | Assistentes | Geração de arquivo Enade.

Para a rotina Cadastro de Diplomação do Aluno:

1. Acessar o TOTVS Educacional;
2. Acessar Atividades acadêmicas | Certificados / Diplomas.

Para a rotina Processo de Inscrições em atividades ofertadas do Aluno:

1. Acessar o TOTVS Educacional;
2. Acessar Atividades acadêmicas | Atividades Ofertadas | Processo | Inscrições em atividades ofertadas.

Para a rotina Cadastro de Cursos / Habilitações de uma atividade ofertada:

1. Acessar o TOTVS Educacional;
2. Acessar Atividades acadêmicas | Atividades Ofertadas | Anexos | Cursos / Habilitações.

Para a rotina Inscrição de alunos na atividade ofertada:

1. Acessar o TOTVS Educacional;
2. Acessar Atividades acadêmicas | Atividades Ofertadas | Anexos | Alunos Inscritos.

Para a rotina Avaliação institucional do Aluno, apenas a visão de seleção de candidatos:

1. Acessar o TOTVS Educacional;
2. Acessar Atividades acadêmicas | Avaliação Institucional.

Para a rotina Matricular aluno em um período letivo:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Aluno | Anexos | Cursos / Habilitações | Processos | Matricular Aluno.

Para a rotina Matricular aluno em disciplinas sugestivas:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Aluno | Anexos | Matrículas no período letivo | Processos | Matricular aluno nas disciplinas.

Para a rotina Transferência Interna:

1. Acessar o TOTVS Educacional;
2. Acessar Atividades acadêmicas | Transferência Interna | Transferência Interna.

Para a rotina Transferência entre coligadas:

1. Acessar o TOTVS Educacional;
2. Acessar Atividades acadêmicas | Transferência Interna | Transferência entre coligadas.

Para a rotina Assistente para cadastro de equivalência de alunos:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Grupo Estrutura Curricular | Mais | Assistente para cadastro de equivalência de alunos.

Para a rotina Confirmação de matrícula por pagamento:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Aluno | Anexos | Matrículas no período letivo | Processos | Confirmação de matrícula por pagamento.

Para a rotina Enturmação:

1. Acessar o TOTVS Educacional;
2. Acessar Matrícula e Avaliação | Enturmação.

Para a rotina Matrícula por prioridade, apenas exibição da visão Turma / Disciplina:

1. Acessar o TOTVS Educacional;
2. Acessar Matrícula e Avaliação | Grupo Matrícula | Mais | Matrícula por prioridade.

Para a rotina Cadastro de matriz aplicada a uma linha de pesquisa:

1. Acessar o TOTVS Educacional;
2. Acessar Atividades acadêmicas | TCC | Linhas de pesquisa | Anexos | Matrizes aplicadas da linha de pesquisa.

Para a rotina Acesso da tela de Digitação de notas e faltas de etapas:

1. Acessar o TOTVS Educacional;
2. Acessar Matrícula e Avaliação | Grupo Notas e Faltas | Mais | Digitação por aluno | Notas e faltas de etapas.

Para a rotina Acesso da tela de Digitação de notas de avaliação por aluno:

1. Acessar o TOTVS Educacional;
2. Acessar Matrícula e Avaliação | Grupo Notas e Faltas | Mais | Digitação por aluno | Notas de avaliação.

Para a rotina Cadastro de turma:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Turmas.

Para a rotina Concessão de bolsa para aluno:

1. Acessar o TOTVS Educacional;
2. Acessar Financeiro / Contábil | Bolsas | Concessão de bolsas futuras | Anexos | Habilitação da concessão de bolsas futuras.

Para a rotina Cadastro de contrato:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Auno | Anexos | Contrato.

Para a rotina Cadastro de faixa de crédito:

1. Acessar o TOTVS Educacional;
2. Acessar Financeiro / Contábil | Faixas de crédito.

Para a rotina Geração de lançamento pelo assistente:

1. Acessar o TOTVS Educacional;
2. Acessar Financeiro / Contábil | Financeiro.

Para a rotina Cadastro de plano de pagamento de uma habilitação:

1. Acessar o TOTVS Educacional;
2. Acessar Financeiro / Contábil | Plano de pagamento | Anexos | Habilitações do plano de pagamento.

Para a rotina Análise curricular:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Aluno | Anexos | Cursos / Habilitações | Editar | Análise Curricular.

Para a rotina Execução da Geração de histórico no ensino básico:

1. Acessar o TOTVS Educacional;
2. Acessar Matrícula e Avaliação | Geração Histórico.
