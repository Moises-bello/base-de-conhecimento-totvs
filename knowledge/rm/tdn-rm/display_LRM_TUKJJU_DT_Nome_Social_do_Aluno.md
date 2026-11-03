---
content_hash: 582bb66707c17c18c37aa585745ac8e56f7c1100883a9167b635daaee38354d9
fetched_at: '2026-06-29T00:08:11.535694+00:00'
page_id: '243011682'
product: rm
source: tdn-rm
title: TUKJJU_DT_Nome_Social_do_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKJJU_DT_Nome_Social_do_Aluno
version: 117
---

# NOME SOCIAL DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Gestão Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Dados pessoais do Aluno* | *N/A* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | ***Frequência Diária***  **Notas e faltas de etapa**  **Notas de Avaliações**  **Aprovação de frequência**  ****Ocorrências****  **Aprovação de Ocorrências**  **Relatório fixo notas de etapas**  **Relatório fixo notas de avaliações** | *N/A* | |  |  | |
| **Cadastros Iniciais:** | - |
| **Parâmetro(s):** | - |
| **Ponto de Entrada:** | *Sistema:*  *Matrícula e Avaliação | Notas e Faltas | Notas e faltas de etapas*  **Matrícula e Avaliação | Notas e Faltas | Notas de avaliação**  ***Matrícula e Avaliação | Notas e Faltas |Frequência diária***  ***Matrícula e Avaliação | Notas e Faltas | Mais... | Digitação por aluno | Notas e faltas de etapas***  ***Matrícula e Avaliação | Notas e Faltas | Mais... | Digitação por aluno | Notas de avaliação***  ***Matrícula e Avaliação | Notas e Faltas | Mais... | Digitação de faltas por dia***  ******Matrícula e Avaliação | Notas e Faltas | Mais... | Relatório fixo | Notas por etapa******  ******Matrícula e Avaliação | Notas e Faltas | Mais... | Relatório fixo | Notas por avaliação******  ******Matrícula e Avaliação | Notas e Faltas | Mais... | Aprovação de frequência******  *Portal:*  *Início | Educacional | Professor | Diário de Classe | Alunos*  **Início | Educacional | Professor | Diário de Classe |Frequência**  **Início | Educacional | Professor | Diário de Classe | Notas avaliação**  **Início | Educacional | Professor | Diário de Classe | Notas etapa**  ***Início | Educacional | Professor | Diário de Classe | Ocorrências***  ***Início | Educacional | Professor | Aprovar ocorrências***  ***Início | Educacional | Professor | Aprovar frequência***  *Educa Mobile:*  *Professor | Avaliações | Detalhes do aluno*  *Professor | Chamada | Detalhes do aluno*  *Professor | Notas/Faltas | Detalhes do aluno* |
| **Chamados Relacionados** | *TUZKAE,  TVE481,  TVEYUA* |
| **Requisito (ISSUE):** | - |
| **País(es):** | - |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *SPARAM* |
| **Sistema(s) Operacional(is):** | - |

## Descrição

Implementação da legislação sobre o nome social do aluno que poderá ser exibido no lugar do seu nome civil em algumas funcionalidades do Sistema.

## Procedimento para Implantação

```
O sistema é atualizado logo após a aplicação do release 12.1.12 ou superior.
```

```
Porém, para habilitar a exibição do nome social, é necessário executar também o script ExecSQL_TUKJJU ou ExecORA_TUKJJU.
```

## Procedimento para Utilização

## Sistema

       1.           No módulo Educacional, acesse Matrícula e Avaliação | Notas e Faltas | Frequência diária.

       2.           Preencha os filtros e clique em Selecionar Alunos

                    O sistema apresenta os alunos da turma/disciplina selecionada. Observe que se o nome social estiver preenchido, é este campo que é apresentado como nome do aluno.

       3.           Posicione o cursor no nome de um aluno que possui nome social

       4.           Observe que o nome civil do aluno é exibido logo abaixo do cursor.

       5.           Depois, acesse Matrícula e Avaliação | Notas e Faltas | Mais... | Digitação de faltas por dia.

       6.           Observe que agora existe a opção de pesquisar pelo nome social de um aluno logo abaixo do filtro RA.

                     Com esta opção marcada, a pesquisa pelo nome digitado neste campo será feita pelo nome social.

                     Com a opção desmarcada, a pesquisa será pelo campo nome.

## Portal

       1.           No Portal, acesse Educacional | Professor | Diário de classe.

       2.           Selecione a turma/disciplina e clique em Frequência.

      3.            Preencha os filtros e clique em Selecionar.

                    O sistema apresenta os alunos da turma/disciplina selecionada. Observe que se o nome social estiver preenchido, é este campo que é apresentado como nome do aluno.

       3.           Posicione o cursor no nome de um aluno que possui nome social

       4.           Observe que o nome civil do aluno é exibido logo abaixo do cursor.

## Educa Mobile

       1.           No Educa Mobile, acesse Professor | Chamada.

       2.           Preencha o contexto.

      3.            Preencha os filtros e clique em Selecionar.

                    O sistema apresenta os alunos da turma/disciplina selecionada. Observe que se o nome social estiver preenchido, é este campo que é apresentado como nome do aluno.

       3.           Clique no nome de um aluno que possui nome social

                     São exibidos os dados do aluno, incluindo seu nome civil.

divs
