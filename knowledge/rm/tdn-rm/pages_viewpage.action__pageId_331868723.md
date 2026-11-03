---
content_hash: 948c02094844bbfd8679fe9549df8c396eb94fbe085492e8105d2e799ccb5e30
fetched_at: '2026-06-29T00:08:50.178146+00:00'
page_id: '331868723'
product: rm
source: tdn-rm
title: DT Função de fórmula para o cálculo da quantidade de disciplinas em curso para
  validação de correquisito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331868723
version: 7
---

# FUNÇÃO DE FÓRMULA PARA O CÁLCULO DA QUANTIDADE DE DISCIPLINAS EM CURSO PARA VALIDAÇÃO DE CORREQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Matricula em disciplinas*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Matrícula em disciplina pelo portal* | *Matrícula Online.* | | *Matrícula em disciplina presencial* | *Matrícula em disciplinas* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Funções de fórmula** | *Funções de fórmula* | |
| **Parâmetro(s):** | *Fórmula de correquisito - Cadastro de disciplinas da Matriz Curricular* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [EDUCACIONAL01-3692](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-3692) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL/Oracle* |
| **Tabelas Utilizadas:** | *SDISCGRADE* |
| **Sistema(s) Operacional(is):** | *Windows* |
| **Issue relacionada:** | EDUCACIONAL01-4947 / EDUCACIONAL01-5105 |

## Descrição

Criação de uma função de fórmula capaz de calcular a quantidade de disciplinas que um aluno está matriculado e matriculando no momento da execução do processo de matrícula.

## Importante

Foi criada a função de fórmula, ***QTDCOEMCURSO***, para que seja utilizada, exclusivamente, na validação de correquisito do processo de matrícula. A sua utilização em um teste de fórmula, através do editor, terá um retorno padrão com valor zerado.

## Procedimento para Utilização

Função de fórmula:

***QtdCoEmCurso*** - Retorna o nº de créditos ou de disciplinas em curso pelo aluno até um determinado período, ou de um período específico, de acordo com o operador, considerando as disciplinas que estão sendo matriculadas no processo de matrícula.

Parâmetros necessários:

* + **Número do período**: Número do período que será calculada a quantidade de disciplinas que estão em curso.
  + **Operador**: Caractere de operação que será utilizado no filtro dos períodos considerados no cálculo das disciplinas matriculadas. Os caracteres permitidos e que serão utilizados: **"="**, **"<="**, **">="**, **">"**, **"<"**
  + **Tipo de retorno:**De acordo com o tipo passado como parâmetro a função terá um retorno diferente. Poderão ser utilizados os tipos: **"C"**, **"D"**, **"CH" *(Créditos, Disciplinas, Carga horária)***

Exemplo de fórmula:

c#Fórmula para a validação de co-requisitotrue

***Importante:***

falseDisciplinas Optativas/Eletivas

Caso o parâmetro com o número do período seja informado o valor 0, o retorno considerará no cálculo apenas as disciplinas Optativas/Eletivas.

Exemplo:

```
DECL RESULT; 

SETVAR (RESULT,'É NECESSÁRIO QUE SE TENHA 48 HORAS EM DISCIPLINAS OPTATIVAS/ELETIVAS');

SE QTDCOEMCURSO (0,'=','CH') = 48
    ENTAO SETVAR (RESULT,'S')
FIMSE;

RESULT
```

A fórmula será utilizada no parâmetro ***"Fórmula de correquisito"*** no cadastro de disciplinas da matriz curricular:

**Educacional | Currículo e Oferta | Matrizes curriculares | Anexos: Período | Anexos: Disciplinas da matriz curricular |** ***"Fórmula de correquisito"***

Ao selecionar as disciplinas para matrícula, seja no portal ou pelo RM, o sistema irá executar a fórmula configurada para validação de correquisito e o resultado da função ***QtdCoEmCurso***, contida na fórmula, será o total das disciplinas já matriculadas e as selecionadas para matrícula do período informado.
