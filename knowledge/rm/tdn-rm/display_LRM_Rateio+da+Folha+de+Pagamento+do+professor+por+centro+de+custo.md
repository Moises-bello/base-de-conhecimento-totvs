---
content_hash: 325a176b0a505a2db376174b8e941fab076202aaed211ec412f74b8482c02df9
fetched_at: '2026-06-29T00:08:35.650209+00:00'
page_id: '283377821'
product: rm
source: tdn-rm
title: Rateio da Folha de Pagamento do professor por centro de custo
type: documentation
url: https://tdn.totvs.com/display/LRM/Rateio+da+Folha+de+Pagamento+do+professor+por+centro+de+custo
version: 1
---

# Rateio da folha de pagamento do professor por alunos considerando o centro de custo onde o aluno foi matriculado

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | Informe o módulo. |
| **Função:** | Folha Educacional |
| **Situação/Requisito:** | Informe a Situação que levou a manutenção ou o requisito quando se tratar de inovação.  A informação a ser inclusa aqui pode ter origem na Story ou Issue. |
| **Solução/Implementação:** | Informe a solução/implementação. |
| **Conversores e Parâmetros:** | Informe os conversores/parâmetros. |
| **Tickets relacionados:** | Informe o(s) chamado(s) relacionado(s). |
| **Requisito:** | Informe o requisito relacionado. |

**RATEIO DA FOLHA DE PAGAMENTO DO PROFESSOR POR ALUNOS CONSIDERANDO O CENTRO DE CUSTO O CURSO ONDE O ALUNO FOI MATRICULADO**

**VISÃO GERAL**

Através deste rateio será possível calcular o rateio da folha de pagamento do professor que está ministrando aulas em determinada TurmaDisciplina de acordo com os alunos matriculados na própria TurmaDisciplina e também os alunos de outros cursos que matricularam nesta TurmaDisciplina.

Exemplo:

 Digamos que o professor deveria receber no mês 645,00 para esta TurmaDisciplina.

Como ficaria o rateio por centro de custo

CC1 – (645,00 / 38 )  \* 1 aluno = 16,98

CC2 – (645,00 / 38 )  \* 37 alunos =  628,02

Será lançado na tabela de rateio por centro de custo da folha (PFSALCMPCC) os valores acima.

**REGRA DE NEGÓCIO**

Ao executar a reprogramação salarial deverá verificar se o parâmetro ‘Reprogramação detalhada por CC está marcado’ e o parâmetro do Classis Net ‘ Ratear pagamento do professor por centro de custo da turma disciplina’ está marcado.

1– Caso afirmativo, deverá:   
 1.1 - Selecionar movimento de ensino do professor obtendo os centros de custos dos alunos retornado pelo sistema educacional (serviço do RM Classis)   
 1.1.1 – A regra para retornar os centros de custos será feita pelo RM Classis , funciona conforme abaixo :

Um professor ministra aulas em uma TurmaDisciplina que está associada a determinada turma, esta turma está associada a uma grade curricular (curso/turma /turno/centro de custo). Caso tenha alunos matriculados nesta TurmaDisciplina que não seja desta grade (curso/turno/centro de custo) , ou seja, o aluno é de outra grade curricular (Curso/turma/turno/centro de custo) cursando esta disciplina. Neste caso o rateio do valor a pagar ao professor deverá ser conforme total de alunos de cada grade curricular , ou seja , para os alunos da turma que o professor está vinculado e para os alunos de outras turma/curso deverá ser feito uma proporção conforme exemplo abaixo :

Total de alunos da turma/curso onde o professor está alocado : 55 alunos

 Alunos matriculados na turma/curso onde o professor está alocado : 50 alunos (cc 01.1) Alunos de outro curso matricula na turma onde o professor está alocado : 5 alunos (cc 01.2)

1.1.2 - Cálculo valor mensal: Exemplo :   
 Valor Mensal que o professor receberá pelas aulas dadas na disciplina = 1000,00   
 Centro de custo

CC 01.1 = 1000,00/55 \* 50 = 909,09 CC 01.2 = 1000,00/55 \* 5 = 90,90 Total = 999,99

A diferença de 0,01 deverá ser creditada ao 1º centro de custo, no caso acima 0,01 centavos.

1.1.3 - Cálculo jornada mensal:   
 Valor Mensal que o professor receberá pelas aulas dadas na disciplina = 1000,00   
 CC 01.1 = 200/55 \* 50 =181,81 CC 01.2 = 200/55 \* 5 = 18,18   
 Total = 199,99

A diferença de 0,01 deverá ser creditada ao 1º centro de custo, no caso acima 0,01

**Configurações no RM Classis**

Parametrização necessária para incluir uma disciplina de outro curso quando matricular o aluno.

Parametrizar para buscar o centro de custo da matriz aplicada.

Marcar o parâmetro ratear pagamento de professores da turma/disciplina por centro de custo.

Abaixo uma memória de cálculo demonstrando o rateio por aluno por centro de custo.

A turma/disciplina  07 5LOZI-NT1/5LOZI  consta em dois cursos

Administração = cc 02.01.01.01.001 total de 37 alunos matriculados

Direito  = 02.01.01.01.012  1 aluno matriculado.

Abaixo uma conferencia na base de dados referente alunos matriculados.

Aluno matriculado na turmaD isciplina 07 5LOGZI-NT1 (curso origem Administração)  , mas o aluno é do curso Direito.

**Abaixo os comandos SQL para conferencia.**

--Matriz aplicada da turma '07 5LOZI-NT1' =  idhabilitafilial = 22

select IDPERLET,CODTURMA,IDHABILITACAOFILIAL

from STURMA

where CODTURMA = '07 5LOZI-NT1' and IDPERLET = 45

-- Disciplina da turma '07 5LOZI-NT1'  vinculada a matriz aplicada 22 do curso 1 = Administração

select codturma,SDISCIPLINA.CODDISC,SDISCIPLINA.NOME,IDPERLET,codcurso,codhabilitacao,codgrade,sturmadisc.IDHABILITACAOFILIAL,shabilitacaofilial.CODCCUSTO

from STURMADISC,SHABILITACAOFILIAL,SDISCIPLINA

where SHABILITACAOFILIAL.CODCOLIGADA = STURMADISC.CODCOLIGADA AND

      SHABILITACAOFILIAL.IDHABILITACAOFILIAL = STURMADISC.IDHABILITACAOFILIAL AND

      SDISCIPLINA.CODCOLIGADA = STURMADISC.CODCOLIGADA AND

      SDISCIPLINA.CODDISC = STURMADISC.CODDISC AND

      IDTURMADISC = 7436

--Relação de alunos matriculados nos cursos

select IDPERLET,RA,CODCURSO,CODHABILITACAO,CODGRADE,SMATRICULA.IDHABILITACAOFILIAL,codturno,CODCCUSTO from smatricula , SHABILITACAOFILIAL

WHERE SHABILITACAOFILIAL.CODCOLIGADA = SMATRICULA.CODCOLIGADA AND

      SHABILITACAOFILIAL.IDHABILITACAOFILIAL = SMATRICULA.IDHABILITACAOFILIAL AND

      IDTURMADISC = 7436 AND IDPERLET = 45 AND CODFILIAL = 1

ORDER BY 1

-- total de alunos matriculados em cursos diferentes

select SGRADE.DESCRICAO,tbb.\* from

(

      select CODCURSO,CODHABILITACAO,CODGRADE,SHABILITACAOFILIAL.idhabilitacaofilial,codturno,CODCCUSTO,COUNT(\*) TotAlunos

      from smatricula , SHABILITACAOFILIAL

      WHERE SHABILITACAOFILIAL.CODCOLIGADA = SMATRICULA.CODCOLIGADA AND

              SHABILITACAOFILIAL.IDHABILITACAOFILIAL = SMATRICULA.IDHABILITACAOFILIAL AND

              IDTURMADISC = 7436 AND IDPERLET = 45 AND CODFILIAL = 1

      group by CODCURSO,CODHABILITACAO,CODGRADE,SHABILITACAOFILIAL.idhabilitacaofilial,codturno,CODCCUSTO

) tbb inner join SGRADE on SGRADE.CODCURSO = tbb.CODCURSO

and SGRADE.CODHABILITACAO = tbb.CODHABILITACAO and SGRADE.CODGRADE = tbb.CODGRADE

-- Total de alunos por curso na turmadisciplina '07 5LOZI-NT1' conforme calculado pela reprogramação salarial

--  1 = Administração

-- 24 = Direito

      select CODCURSO,CODHABILITACAO,CODCCUSTO,COUNT(\*) TotAlunos

      from smatricula , SHABILITACAOFILIAL

      WHERE SHABILITACAOFILIAL.CODCOLIGADA = SMATRICULA.CODCOLIGADA AND

              SHABILITACAOFILIAL.IDHABILITACAOFILIAL = SMATRICULA.IDHABILITACAOFILIAL AND

              IDTURMADISC = 7436 AND IDPERLET = 45 AND CODFILIAL = 1

      group by CODCURSO,CODHABILITACAO,CODCCUSTO
