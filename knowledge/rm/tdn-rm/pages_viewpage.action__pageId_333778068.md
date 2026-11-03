---
content_hash: f2b294871d97cf7a93d9a1d894dc03cfd68daf64596e8b2a558edafbb7165a96
fetched_at: '2026-06-29T00:08:50.228182+00:00'
page_id: '333778068'
product: rm
source: tdn-rm
title: DT Preparação e Geração do Arquivo do Censo Ensino Superior 2017
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=333778068
version: 88
---

# PREPARAÇÃO E GERAÇÃO DO ARQUIVO DO CENSO ENSINO SUPERIOR 2017

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Preparação do Arquivo do Censo do Ensino Superior* | **Preparação do Arquivo do Censo do Ensino Superior** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Gerador de Saída - Censup - Censo da Educação Superior - Aluno** | ***Gerador de Saída - Censup - Censo da Educação Superior - Aluno*** | | **Gerador de Saída - Censup - Censo da Educação Superior - Docente** | ****Gerador de Saída - Censup - Censo da Educação Superior - Docente**** | | **Cadastro de Campus/Polo** | **Cadastro de Campus/Polo** | | **Cadastro de Deficiências da Pessoa/Aluno** | **Cadastro de Deficiências da Pessoa/Aluno** | | ****Preparação do arquivo para o Censo do Ensino Superior**** | ****Preparação do arquivo para o Censo do Ensino Superior**** | | **Preparação do arquivo para o Educacenso** | **Preparação do arquivo para o Educacenso** | | **Gerador de Saída - Educacenso** | **Gerador de Saída - Educacenso** | |
| **Cadastros Iniciais:** | * ***Consultas Importadas:*** * ****Possuir as configurações do Censo corretamente informadas no sistema (alunos, curso, professores e etc.).**** |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *[EDUCACIONAL01-3717](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-3717)*  *[EDUCACIONAL01-2657](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-2657)*  *[EDUCACIONAL01-3730](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-3730)* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *SCAMPUS,* *SCURSOMEC, SPROFESSORMEC, SINSTITUICAOMEC, SALUNOMEC* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

Foram feitos diversos ajustes no seguintes registros da geração do censo superior:

* No registro 42 do aluno as posições 42, 43 e 45 referente aos financiamentos não reembolsáveis estavam invertidas. E o campo 4 passa a pegar o valor do campo Cod. do Campus no MEC no cadastro de Campus/Polo da matriz aplicada do curso do aluno que está matriculado;
* No registro 31 do docente foram ajustadas as posições 5, 9, 12 e 30 que não respeitavam as regras do MEC;
* No registro 32 do docente foi ajustado para trazer o Cod Inep do Curso do Curso do Mec informado na matriz aplicada da turma do professor.
* No registro 41 do aluno, as posições de 14 a 27 referente às deficiências do aluno foram alteradas para buscar as deficiências da pessoa.

Foram feitos diversos ajustes no seguintes registros da geração do censo básico:

* No registro 60 do aluno, as posições de 17 a 29 referente às deficiências do aluno foram alteradas para buscar as deficiências da pessoa.

## Procedimento para Implantação

Censo Básico: O sistema é atualizado logo após a aplicação do pacote de atualizações do patch 12.1.17. e importar a nova consulta MEC.ES.SQL.60 / MEC.ES.ORA.60.

Censo Superior: O sistema é atualizado logo após a aplicação do pacote de atualizações do patch 12.1.17. e importar as novas consultas MEC.ES.SQL.31 / MEC.ES.ORA.31, MEC.ES.SQL.32 / MEC.ES.ORA.32, MEC.ES.SQL.41 / MEC.ES.ORA.41 e MEC.ES.SQL.42 / MEC.ES.ORA.42.

Além disso, rodar o script de marcação código CN.2018.01\_09 para criar o novo campo Cod. do Campus no MEC no cadastro de Campus/Polo.

## Procedimento para Utilização

O procedimento de utilização toma por base o seguinte documento: <http://tdn.totvs.com/x/F9slE>

divs
